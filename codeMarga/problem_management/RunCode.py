import requests
import time
import base64


JUDGE0_API_URL = "https://judge0-ce.p.rapidapi.com"
LANGUAGE_MAP = {
    "python": 71,  
    "cpp": 54,     
    "java": 62,   
}

def generate_driver_script(language, user_code, class_name, method_name, test_cases):
    if language == "python":
        test_code = "\n".join([
            f"from {class_name} import {class_name}",
            "",
            f"instance = {class_name}()",
            "results = []",
            "test_cases = [",
            *[
                f"    {{'input': {test_case['input']}, 'expected_output': {test_case['expected_output']}}},"
                for test_case in test_cases
            ],
            "]",
            "",
            "for test in test_cases:",
            "    try:",
            f"        output = instance.{method_name}(*test['input'])",
            "        results.append(output == test['expected_output'])",
            "    except Exception as e:",
            "        results.append(False)",
            "",
            "print(results)"
        ])

    elif language == "java":
        test_code = "\n".join([
            "import java.util.*;",
            f"public class Main {{",
            f"    public static void main(String[] args) {{",
            f"        {class_name} instance = new {class_name}();",
            "        boolean[] results = new boolean[] {",
            *[
                f"            instance.{method_name}({', '.join(map(str, test_case['input']))}) == {test_case['expected_output']}," 
                for test_case in test_cases
            ],
            "        };",
            "        System.out.println(Arrays.toString(results));",
            "    }",
            "}"
        ])

    elif language == "cpp":
        test_code = "\n".join([ 
            "#include <iostream>",
            "#include <vector>",
            "using namespace std;",
            "",
            user_code,  
            "",
            f"int main() {{",
            f"    {class_name} instance;",
            "    vector<pair<vector<int>, int>> test_cases = {",  
            *[
                f"        {{vector<int>{{{', '.join(map(str, test_case['input']))}}}, {test_case['expected_output']}}},"
                for test_case in test_cases
            ],
            "    };",
            "",
            f"    for (auto& test : test_cases) {{",
            f"        int output = instance.{method_name}(test.first[0], test.first[1]);", 
            "        cout << \"Input: \" << test.first[0] << \", \" << test.first[1] << \" => Output: \" << output",
            "             << \", Expected: \" << test.second << \" => \" << (output == test.second ? \"PASS\" : \"FAIL\") << endl;",
            "    }",
            "    return 0;",
            "}"
        ])

    else:
        raise ValueError(f"Unsupported language: {language}")

    return test_code



def execute_code(language, user_code, class_name, method_name, test_cases):

    driver_code = generate_driver_script(language,user_code, class_name, method_name, test_cases)
    print("Driver Code:", driver_code)
    full_code = driver_code 

    encoded_code = base64.b64encode(full_code.encode('utf-8')).decode('utf-8')
    encoded_stdin = base64.b64encode("".encode('utf-8')).decode('utf-8')

    data = {
        "language_id": LANGUAGE_MAP[language],
        "source_code": encoded_code,
        "stdin": encoded_stdin,
    }

    headers = {
        "Content-Type": "application/json",
        "x-rapidapi-host": "judge0-ce.p.rapidapi.com",
        "x-rapidapi-key": "9aaae2f2c2msh8185224faa9703ap14444fjsnec62096e3953"
    }

    response = requests.post(f"{JUDGE0_API_URL}/submissions?base64_encoded=true", json=data, headers=headers)
    if response.status_code != 201:
        raise Exception("Error submitting code to Judge0. Response: " + response.text)

    token = response.json().get("token")
    if not token:
        raise Exception("No token received from Judge0.")

    result_url = f"{JUDGE0_API_URL}/submissions/{token}?base64_encoded=true"
    while True:
        result_response = requests.get(result_url, headers=headers)
        result_data = result_response.json()

        status_id = result_data.get("status", {}).get("id", 2) 
        status_description = result_data.get("status", {}).get("description", "Processing")

        if status_id not in [1, 2]:  
            stdout_base64 = result_data.get('stdout')
            if stdout_base64:
                decoded_stdout = base64.b64decode(stdout_base64).decode('utf-8')
                print("Decoded stdout:\n", decoded_stdout)
            return result_data

        print(f"Status: {status_description}. Waiting...")
        time.sleep(1) 

#example
if __name__ == "__main__":
    user_code = """
class ExampleClass {
public:
    int exampleMethod(int x, int y) {
        return x + y;
    }
};
"""

    class_name = "ExampleClass"
    method_name = "exampleMethod"
    test_cases = [
        {"input": [2, 3], "expected_output": 5},
        {"input": [10, 20], "expected_output": 30},
        {"input": [0, 0], "expected_output": 0},
    ]

    try:
        result = execute_code("cpp", user_code, class_name, method_name, test_cases)
        print("Execution Result:", result)
    except Exception as e:
        print("Error:", str(e))
