from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Problem , TestCase
import json
from .RunCode import execute_code
import base64


@csrf_exempt
def problem_list(request):
    """
    List all problems.
    """
    if request.method == "GET":
        problems = Problem.objects.all()
        data = [
            {
                "id": problem.id,
                "title": problem.title,
                "description": problem.description,
                "examples": problem.examples,
                "class_name": problem.class_name,
                "method_name": problem.method_name,
                "category": problem.category.name if problem.category else None,  # Accessing the category name directly
                "constraints": problem.constraints,
                "followup": problem.followup,
            }
            for problem in problems
        ]
        return JsonResponse(data, safe=False)

@csrf_exempt
def problem_detail(request, problem_id):
    """
    Retrieve details of a specific problem.
    """
    try:
        problem = Problem.objects.get(pk=problem_id)
    except Problem.DoesNotExist:
        return JsonResponse({"error": "Problem not found"}, status=404)

    if request.method == "GET":
        data = {
            "id": problem.id,
            "title": problem.title,
            "description": problem.description,
            "examples": problem.examples,
            "class_name": problem.class_name,
            "method_name": problem.method_name,
            "category": problem.category.name if problem.category else None,  # Accessing the category name directly
            "constraints": problem.constraints,
            "followup": problem.followup,
            "test_cases": [
                {"input_data": test_case.input_data, "expected_output": test_case.expected_output}
                for test_case in problem.testcase_set.all()
            ],
        }
        return JsonResponse(data)


@csrf_exempt
def run_code(request):
    if request.method == "POST":
        try:
            # Parse the incoming JSON data
            data = json.loads(request.body)
            language = data.get("language")
            user_code = data.get("user_code")
            class_name = data.get("class_name")
            method_name = data.get("method_name")
            test_cases = data.get("test_cases")

            # Validate required fields
            if not all([language, user_code, class_name, method_name, test_cases]):
                return JsonResponse({"error": "Missing required fields: language, user_code, class_name, method_name, or test_cases."}, status=400)

            # Execute the code using the `execute_code` function from Runcode.py
            result = execute_code(language, user_code, class_name, method_name, test_cases)

            # Extracting result details
            stdout_base64 = result.get("stdout")
            stderr_base64 = result.get("stderr")
            status = result.get("status", {}).get("description", "Unknown status")

            # Decode base64 outputs if present
            decoded_stdout = base64.b64decode(stdout_base64).decode('utf-8') if stdout_base64 else "No output generated."
            decoded_stderr = base64.b64decode(stderr_base64).decode('utf-8') if stderr_base64 else "No error output."

            # Prepare response data
            response_data = {
                "status": status,
                "stdout": decoded_stdout,
                "stderr": decoded_stderr,
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format in request body."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    # Return error for unsupported methods
    return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)
