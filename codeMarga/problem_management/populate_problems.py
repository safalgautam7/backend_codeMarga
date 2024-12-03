import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codeMarga.settings')
django.setup()

from problem_management.models import Problem, TestCase, Category  # Absolute import

# Create categories using get_or_create to avoid duplicates
categories = {
    "Array": Category.objects.get_or_create(name="Array")[0],
    "String": Category.objects.get_or_create(name="String")[0],
    "Hash Table": Category.objects.get_or_create(name="Hash Table")[0],
    "Dynamic Programming": Category.objects.get_or_create(name="Dynamic Programming")[0],
    "Math": Category.objects.get_or_create(name="Math")[0],
    "Sorting": Category.objects.get_or_create(name="Sorting")[0],
    "Greedy": Category.objects.get_or_create(name="Greedy")[0],
    "Algorithms": Category.objects.get_or_create(name="Algorithms")[0],
    "Database": Category.objects.get_or_create(name="Database")[0],
    "Shell": Category.objects.get_or_create(name="Shell")[0],
    "Concurrency": Category.objects.get_or_create(name="Concurrency")[0],
    "JavaScript": Category.objects.get_or_create(name="JavaScript")[0],
    "Binary Tree": Category.objects.get_or_create(name="Binary Tree")[0],
    "Stack": Category.objects.get_or_create(name="Stack")[0],
}

# Helper function to create problems and test cases
def create_problem(title, description, examples, class_name, method_name, default_code, constraints, followup, categories_list, test_cases):
    problem = Problem.objects.create(
        title=title,
        description=description,
        examples=examples,
        class_name=class_name,
        method_name=method_name,
        default_code=default_code,
        constraints=constraints,
        followup=followup,
    )
    # Add categories to the problem using the correct Many-to-Many relationship
    for category in categories_list:
        categories[category].problems.add(problem)  # Adding categories using the Many-to-Many relationship
    # Create test cases for the problem
    for test_case in test_cases:
        TestCase.objects.create(
            problem=problem,
            input_data=test_case["input_data"],
            expected_output=test_case["expected_output"],
        )

# Problem definitions (just a few examples, you can add more problems)
problems_data = [
     {
        "title": "Merge Sorted Array",
        "description": (
            "You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, "
            "and two integers m and n, representing the number of elements in nums1 and nums2 respectively.\n\n"
            "Merge nums2 into nums1 as one sorted array."
        ),
        "examples": [
            {"input": "nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3", "output": "[1,2,2,3,5,6]"},
        ],
        "class_name": "Solution",
        "method_name": "merge",
        "default_code": {"python": "class Solution:\n    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:"},
        "constraints": "0 <= m, n <= 200\n1 <= len(nums1), len(nums2) <= 200\n-10^9 <= nums1[i], nums2[i] <= 10^9",
        "followup": "Could you optimize the space complexity?",
        "categories_list": ["Array", "Sorting"],
        "test_cases": [
            {"input_data": {"nums1": [1, 2, 3, 0, 0, 0], "m": 3, "nums2": [2, 5, 6], "n": 3}, "expected_output": [1, 2, 2, 3, 5, 6]},
            {"input_data": {"nums1": [1], "m": 1, "nums2": [], "n": 0}, "expected_output": [1]},
        ],
    },
    {
        "title": "Trapping Rain Water",
        "description": (
            "Given n non-negative integers representing an elevation map where the width of each bar is 1, "
            "compute how much water it can trap after raining."
        ),
        "examples": [
            {"input": "height = [0,1,0,2,1,0,1,3,2,1,2,1]", "output": "6"},
        ],
        "class_name": "Solution",
        "method_name": "trap",
        "default_code": {"python": "class Solution:\n    def trap(self, height: List[int]) -> int:"},
        "constraints": "0 <= n <= 2 * 10^4\n0 <= height[i] <= 10^5",
        "followup": "Could you solve it in O(n) time?",
        "categories_list": ["Array", "Dynamic Programming", "Greedy"],
        "test_cases": [
            {"input_data": {"height": [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]}, "expected_output": 6},
            {"input_data": {"height": [4, 2, 0, 3, 2, 5]}, "expected_output": 9},
        ],
    },
    {
        "title": "Roman to Integer",
        "description": (
            "Given a Roman numeral, convert it to an integer.\n\n"
            "Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M."
        ),
        "examples": [
            {"input": "s = 'III'", "output": "3"},
            {"input": "s = 'LVIII'", "output": "58"},
        ],
        "class_name": "Solution",
        "method_name": "romanToInt",
        "default_code": {"python": "class Solution:\n    def romanToInt(self, s: str) -> int:"},
        "constraints": "1 <= s.length <= 15\ns contains only Roman numeral characters.",
        "followup": "Could you optimize for multiple conversions?",
        "categories_list": ["String", "Algorithms"],
        "test_cases": [
            {"input_data": {"s": "III"}, "expected_output": 3},
            {"input_data": {"s": "LVIII"}, "expected_output": 58},
            {"input_data": {"s": "MCMXCIV"}, "expected_output": 1994},
        ],
    },
    {
        "title": "Container With Most Water",
        "description": (
            "You are given an integer array height of length n. There are n vertical lines drawn such that "
            "the two endpoints of the i-th line are (i, 0) and (i, height[i]).\n\n"
            "Find two lines that together with the x-axis form a container, such that the container holds the most water."
        ),
        "examples": [
            {"input": "height = [1,8,6,2,5,4,8,3,7]", "output": "49"},
        ],
        "class_name": "Solution",
        "method_name": "maxArea",
        "default_code": {"python": "class Solution:\n    def maxArea(self, height: List[int]) -> int:"},
        "constraints": "2 <= height.length <= 10^5\n0 <= height[i] <= 10^4",
        "followup": "Can you solve it in O(n) time?",
        "categories_list": ["Array", "Greedy"],
        "test_cases": [
            {"input_data": {"height": [1, 8, 6, 2, 5, 4, 8, 3, 7]}, "expected_output": 49},
            {"input_data": {"height": [1, 1]}, "expected_output": 1},
        ],
    },
    {
        "title": "Binary Tree Maximum Path Sum",
        "description": (
            "Given a non-empty binary tree, find the maximum path sum.\n\n"
            "The path may start and end at any node in the tree."
        ),
        "examples": [
            {"input": "root = [-10,9,20,null,null,15,7]", "output": "42"},
        ],
        "class_name": "Solution",
        "method_name": "maxPathSum",
        "default_code": {"python": "class Solution:\n    def maxPathSum(self, root: Optional[TreeNode]) -> int:"},
        "constraints": "-10^4 <= Node.val <= 10^4\nThe tree contains at least one node.",
        "followup": "Could you solve it with bottom-up recursion?",
        "categories_list": ["Binary Tree", "Dynamic Programming"],
        "test_cases": [
            {"input_data": {"root": [-10, 9, 20, None, None, 15, 7]}, "expected_output": 42},
            {"input_data": {"root": [1, 2, 3]}, "expected_output": 6},
        ],
    },
    {
        "title": "Word Search",
        "description": (
            "Given an m x n grid of characters board and a string word, return true if word exists in the grid.\n\n"
            "The word can be constructed from letters of sequentially adjacent cells."
        ),
        "examples": [
            {"input": "board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = 'ABCCED'", "output": "True"},
        ],
        "class_name": "Solution",
        "method_name": "exist",
        "default_code": {"python": "class Solution:\n    def exist(self, board: List[List[str]], word: str) -> bool:"},
        "constraints": "1 <= m, n <= 200\n1 <= word.length <= 10^3",
        "followup": "Could you solve it using backtracking?",
        "categories_list": ["Algorithms", "Dynamic Programming"],
        "test_cases": [
            {"input_data": {"board": [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "word": "ABCCED"}, "expected_output": True},
            {"input_data": {"board": [["A", "B"], ["C", "D"]], "word": "ABCD"}, "expected_output": False},
        ],
    },
    {
        "title": "Evaluate Reverse Polish Notation",
        "description": (
            "Evaluate the value of an arithmetic expression in Reverse Polish Notation."
        ),
        "examples": [
            {"input": "tokens = ['2','1','+','3','*']", "output": "9"},
        ],
        "class_name": "Solution",
        "method_name": "evalRPN",
        "default_code": {"python": "class Solution:\n    def evalRPN(self, tokens: List[str]) -> int:"},
        "constraints": "1 <= tokens.length <= 10^4\nTokens are either operators or integers.",
        "followup": "Can you handle division properly with Python's integer division?",
        "categories_list": ["Math", "Stack"],
        "test_cases": [
            {"input_data": {"tokens": ["2", "1", "+", "3", "*"]}, "expected_output": 9},
            {"input_data": {"tokens": ["4", "13", "5", "/", "+"]}, "expected_output": 6},
        ],
    },
]

# Create problems
for problem_data in problems_data:
    create_problem(**problem_data)
