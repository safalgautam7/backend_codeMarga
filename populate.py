import os
import django
from django.core.exceptions import ObjectDoesNotExist


# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "codeMarga.settings")

# Initialize Django
django.setup()

from problem_management.models import Problem, Category, TestCase


def populate():
    # Predefined categories
    categories = [
        "Array", "String", "Hash Table", "Dynamic Programming", "Math", "Sorting",
        "Greedy", "Two Pointers", "Binary Search", "Divide and Conquer", 
        "Backtracking", "Stack", "Heap", "Graph", "Tree", "Breadth-First Search",
        "Depth-First Search", "Union Find", "Binary Tree", "Recursion", "Linked List"
    ]
    
    # Create or retrieve categories
    category_objects = {}
    for cat_name in categories:
        category, created = Category.objects.get_or_create(name=cat_name)
        category_objects[cat_name] = category

    print("Categories populated.")

    # Sample problems
    problems = [
        {
            "title": "Two Sum",
            "description": "Find two numbers that add up to a target sum.",
            "examples": [
                {"input": "[2, 7, 11, 15], target=9", "output": "[0, 1]", "explanation": "2+7=9."}
            ],
            "class_name": "Solution",
            "method_name": "two_sum",
            "default_code": {
                "python": "def two_sum(nums, target):\n    pass",
                "cpp": "vector<int> two_sum(vector<int>& nums, int target) {\n    return {};\n}",
                "java": "int[] twoSum(int[] nums, int target) {\n    return new int[] {};\n}"
            },
            "constraints": "1 <= nums.length <= 10^4",
            "followup": "Can you do it in O(n) time?",
            "category": "Array",
            "test_cases": [
                {"input_data": {"nums": [2, 7, 11, 15], "target": 9}, "expected_output": [0, 1]},
                {"input_data": {"nums": [3, 2, 4], "target": 6}, "expected_output": [1, 2]},
                {"input_data": {"nums": [3, 3], "target": 6}, "expected_output": [0, 1]},
            ]
        },
        {
            "title": "Longest Palindromic Substring",
            "description": "Find the longest palindromic substring.",
            "examples": [
                {"input": "'babad'", "output": "'bab'", "explanation": "'aba' is also valid."}
            ],
            "class_name": "Solution",
            "method_name": "longest_palindrome",
            "default_code": {
                "python": "def longest_palindrome(s):\n    pass",
                "cpp": "string longest_palindrome(string s) {\n    return \"\";\n}",
                "java": "String longestPalindrome(String s) {\n    return \"\";\n}"
            },
            "constraints": "1 <= s.length <= 10^3",
            "followup": "Can you do it in O(n) time?",
            "category": "String",
            "test_cases": [
                {"input_data": {"s": "babad"}, "expected_output": "bab"},
                {"input_data": {"s": "cbbd"}, "expected_output": "bb"},
                {"input_data": {"s": "a"}, "expected_output": "a"},
            ]
        },
        # Add more problems here
    ]

    for prob_data in problems:
        category = category_objects[prob_data["category"]]
        problem = Problem.objects.create(
            title=prob_data["title"],
            description=prob_data["description"],
            examples=prob_data["examples"],
            class_name=prob_data["class_name"],
            method_name=prob_data["method_name"],
            default_code=prob_data["default_code"],
            constraints=prob_data.get("constraints", ""),
            followup=prob_data.get("followup", ""),
            category=category,
        )
        print(f"Created problem: {problem.title}")

        for test_case_data in prob_data["test_cases"]:
            TestCase.objects.create(
                problem=problem,
                input_data=test_case_data["input_data"],
                expected_output=test_case_data["expected_output"],
            )
        print(f"Test cases added for problem: {problem.title}")


if __name__ == "__main__":
    populate()
