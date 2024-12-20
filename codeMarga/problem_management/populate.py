from coderun.models import Problem, TestCase, Category

# Create categories
categories = {
    "Array": Category.objects.create(name="Array"),
    "String": Category.objects.create(name="String"),
    "Hash Table": Category.objects.create(name="Hash Table"),
    "Dynamic Programming": Category.objects.create(name="Dynamic Programming"),
    "Math": Category.objects.create(name="Math"),
    "Sorting": Category.objects.create(name="Sorting"),
    "Greedy": Category.objects.create(name="Greedy"),
    "Two Pointers": Category.objects.create(name="Two Pointers"),
    "Binary Search": Category.objects.create(name="Binary Search"),
    "Divide and Conquer": Category.objects.create(name="Divide and Conquer"),
    "Backtracking": Category.objects.create(name="Backtracking"),
    "Stack": Category.objects.create(name="Stack"),
    "Heap": Category.objects.create(name="Heap"),
    "Graph": Category.objects.create(name="Graph"),
    "Tree": Category.objects.create(name="Tree"),
    "Depth-first Search": Category.objects.create(name="Depth-first Search"),
    "Breadth-first Search": Category.objects.create(name="Breadth-first Search"),
    "Union Find": Category.objects.create(name="Union Find"),
    "Binary Tree": Category.objects.create(name="Binary Tree"),
    "Recursion": Category.objects.create(name="Recursion"),
    "Linked List": Category.objects.create(name="Linked List"),
}

# Helper function to create problems and test cases
def create_problem(title, description, examples, class_name, method_name, default_code, constraints, followup, categories_list, test_cases):
    # Create the Problem instance
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

    # Add categories to the problem (ManyToManyField)
    for category_name in categories_list:
        category, created = Category.objects.get_or_create(name=category_name)
        problem.category.add(category)

    # Create TestCase instances
    for test_case in test_cases:
        TestCase.objects.create(
            problem=problem,
            input_data=test_case["input_data"],
            expected_output=test_case["expected_output"],
        )

    return problem


# Problem definitions
problems_data = [
    
    {
        "title": "Two Sum",
        "description": (
            "Given an array of integers nums and an integer target, "
            "return indices of the two numbers such that they add up to target.\n\n"
            "You may assume that each input would have exactly one solution, "
            "and you may not use the same element twice.\n\n"
            "You can return the answer in any order."
        ),
        "examples": [
            {
                "input": "nums = [2,7,11,15], target = 9",
                "output": "[0,1]",
                "explanation": "Because nums[0] + nums[1] == 9, we return [0, 1].",
            }
        ],
        "class_name": "Solution",
        "method_name": "twoSum",
"default_code": {
    "python": "class Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:",
    "cpp": (
        "class Solution {\n"
        "public:\n"
        "    vector<int> twoSum(vector<int>& nums, int target) {\n"
        "        // Implement your code here\n"
        "    }\n"
        "};"
    ),
    "java": (
        "class Solution {\n"
        "    public int[] twoSum(int[] nums, int target) {\n"
        "        // Implement your code here\n"
        "    }\n"
        "};"
    ),
},

        "constraints": "2 <= nums.length <= 10^4\n-10^9 <= nums[i] <= 10^9\n-10^9 <= target <= 10^9.",
        "followup": "Can you come up with an algorithm that is less than O(n^2) time complexity?",
        "categories_list": ["Array", "Hash Table"],
        "test_cases": [
            {"input_data": {"nums": [2, 7, 11, 15], "target": 9}, "expected_output": [0, 1]},
            {"input_data": {"nums": [3, 2, 4], "target": 6}, "expected_output": [1, 2]},
            {"input_data": {"nums": [3, 3], "target": 6}, "expected_output": [0, 1]},
        ],
    },
    {
        "title": "Palindrome Check",
        "description": "Determine if a given string is a palindrome.",
        "examples": [
            {"input": "s = 'racecar'", "output": "True"},
            {"input": "s = 'hello'", "output": "False"},
        ],
        "class_name": "Solution",
        "method_name": "isPalindrome",
        "default_code": {
            "python": "class Solution:\n    def isPalindrome(self, s: str) -> bool:",
        },
        "constraints": "1 <= len(s) <= 10^5\ns consists of only printable ASCII characters.",
        "followup": "Can you solve it using O(1) additional space?",
        "categories_list": ["String", "Algorithms"],
        "test_cases": [
            {"input_data": {"s": "racecar"}, "expected_output": True},
            {"input_data": {"s": "hello"}, "expected_output": False},
            {"input_data": {"s": "A man, a plan, a canal: Panama"}, "expected_output": True},
        ],
    },
    {
        "title": "Maximum Subarray",
        "description": "Find the contiguous subarray with the largest sum.",
        "examples": [
            {"input": "nums = [-2,1,-3,4,-1,2,1,-5,4]", "output": "6"},
        ],
        "class_name": "Solution",
        "method_name": "maxSubArray",
        "default_code": {
            "python": "class Solution:\n    def maxSubArray(self, nums: List[int]) -> int:",
        },
        "constraints": "1 <= nums.length <= 10^5\n-10^4 <= nums[i] <= 10^4.",
        "followup": "Can you implement this using O(n) time complexity?",
        "categories_list": ["Array", "Dynamic Programming"],
        "test_cases": [
            {"input_data": {"nums": [-2, 1, -3, 4, -1, 2, 1, -5, 4]}, "expected_output": 6},
            {"input_data": {"nums": [1]}, "expected_output": 1},
            {"input_data": {"nums": [5, 4, -1, 7, 8]}, "expected_output": 23},
        ],
    },
    {
        "title": "Reverse Integer",
        "description": "Given a signed 32-bit integer x, reverse its digits.",
        "examples": [
            {"input": "x = 123", "output": "321"},
        ],
        "class_name": "Solution",
        "method_name": "reverse",
        "default_code": {
            "python": "class Solution:\n    def reverse(self, x: int) -> int:",
        },
        "constraints": "-2^31 <= x <= 2^31 - 1.",
        "followup": "How would you handle overflow?",
        "categories_list": ["Math", "String"],
        "test_cases": [
            {"input_data": {"x": 123}, "expected_output": 321},
            {"input_data": {"x": -123}, "expected_output": -321},
            {"input_data": {"x": 120}, "expected_output": 21},
        ],
    },
    {
        "title": "Remove Duplicates from Sorted Array",
        "description": (
            "Given an integer array nums sorted in non-decreasing order, "
            "remove the duplicates in-place such that each unique element appears only once. "
            "The relative order of the elements should be kept the same.\n\n"
            "Then return the number of unique elements in nums."
        ),
        "examples": [
            {
                "input": "nums = [1,1,2]",
                "output": "2",
                "explanation": "After removing duplicates, nums becomes [1, 2, _] with unique count = 2."
            }
        ],
        "class_name": "Solution",
        "method_name": "removeDuplicates",
        "default_code": {
            "python": "class Solution:\n    def removeDuplicates(self, nums: List[int]) -> int:"
        },
        "constraints": "1 <= nums.length <= 3 * 10^4\n-100 <= nums[i] <= 100",
        "followup": "Can you come up with an algorithm that is less than O(n^2) time complexity?",
        "categories_list": ["Array", "Two Pointers"],
        "test_cases": [
            {"input_data": {"nums": [1, 1, 2]}, "expected_output": 2},
            {"input_data": {"nums": [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]}, "expected_output": 5},
            {"input_data": {"nums": [1, 2, 3]}, "expected_output": 3}
        ]
    },
    {
        "title": "Climbing Stairs",
        "description": (
            "You are climbing a staircase. It takes n steps to reach the top.\n\n"
            "Each time you can either climb 1 or 2 steps. "
            "In how many distinct ways can you climb to the top?"
        ),
        "examples": [
            {
                "input": "n = 2",
                "output": "2",
                "explanation": "There are two ways: (1 step + 1 step) or (2 steps)."
            },
            {
                "input": "n = 3",
                "output": "3",
                "explanation": "There are three ways: (1+1+1), (1+2), or (2+1)."
            }
        ],
        "class_name": "Solution",
        "method_name": "climbStairs",
        "default_code": {
            "python": "class Solution:\n    def climbStairs(self, n: int) -> int:"
        },
        "constraints": "1 <= n <= 45",
        "followup": "Can you come up with an algorithm that is less than O(n^2) time complexity?",
        "categories_list": ["Dynamic Programming"],
        "test_cases": [
            {"input_data": {"n": 2}, "expected_output": 2},
            {"input_data": {"n": 3}, "expected_output": 3},
            {"input_data": {"n": 4}, "expected_output": 5}
        ]
    },
    {
        "title": "Search Insert Position",
        "description": (
            "Given a sorted array of distinct integers and a target value, "
            "return the index if the target is found. "
            "If not, return the index where it would be if it were inserted in order."
        ),
        "examples": [
            {
                "input": "nums = [1,3,5,6], target = 5",
                "output": "2",
                "explanation": "The target is found at index 2."
            },
            {
                "input": "nums = [1,3,5,6], target = 2",
                "output": "1",
                "explanation": "The target would be inserted at index 1."
            }
        ],
        "class_name": "Solution",
        "method_name": "searchInsert",
        "default_code": {
            "python": "class Solution:\n    def searchInsert(self, nums: List[int], target: int) -> int:"
        },
        "constraints": "1 <= nums.length <= 10^4\n-10^4 <= nums[i], target <= 10^4\nnums contains distinct integers.",
        "followup": "Can you come up with an algorithm that is less than O(n^2) time complexity?",
        "categories_list": ["Array", "Binary Search"],
        "test_cases": [
            {"input_data": {"nums": [1, 3, 5, 6], "target": 5}, "expected_output": 2},
            {"input_data": {"nums": [1, 3, 5, 6], "target": 2}, "expected_output": 1},
            {"input_data": {"nums": [1, 3, 5, 6], "target": 7}, "expected_output": 4}
        ]
    },
    {
        "title": "Best Time to Buy and Sell Stock",
        "description": (
            "You are given an array prices where prices[i] is the price of a given stock on the ith day.\n\n"
            "You want to maximize your profit by choosing a single day to buy one stock "
            "and choosing a different day in the future to sell that stock.\n\n"
            "Return the maximum profit you can achieve from this transaction. "
            "If you cannot achieve any profit, return 0."
        ),
        "examples": [
            {
                "input": "prices = [7,1,5,3,6,4]",
                "output": "5",
                "explanation": "Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5."
            }
        ],
        "class_name": "Solution",
        "method_name": "maxProfit",
        "default_code": {
            "python": "class Solution:\n    def maxProfit(self, prices: List[int]) -> int:"
        },
        "constraints": "1 <= prices.length <= 10^5\n0 <= prices[i] <= 10^4",
        "followup": "Can you come up with an algorithm that is less than O(n^2) time complexity?",
        "categories_list": ["Array", "Dynamic Programming"],
        "test_cases": [
            {"input_data": {"prices": [7, 1, 5, 3, 6, 4]}, "expected_output": 5},
            {"input_data": {"prices": [7, 6, 4, 3, 1]}, "expected_output": 0},
            {"input_data": {"prices": [1, 2, 3, 4, 5]}, "expected_output": 4}
        ]
    },
    {
        "title": "Binary Search",
        "description": (
            "Given an array of integers nums which is sorted in ascending order, "
            "and an integer target, write a function to search target in nums.\n\n"
            "If target exists, return its index. Otherwise, return -1."
        ),
        "examples": [
            {
                "input": "nums = [-1,0,3,5,9,12], target = 9",
                "output": "4",
                "explanation": "Target 9 is found at index 4."
            }
        ],
        "class_name": "Solution",
        "method_name": "search",
        "default_code": {
            "python": "class Solution:\n    def search(self, nums: List[int], target: int) -> int:"
        },
        "constraints": "1 <= nums.length <= 10^4\n-10^4 <= nums[i], target <= 10^4",
        "followup": "Can you come up with an algorithm that is less than O(n^2) time complexity?",
        "categories_list": ["Binary Search"],
        "test_cases": [
            {"input_data": {"nums": [-1, 0, 3, 5, 9, 12], "target": 9}, "expected_output": 4},
            {"input_data": {"nums": [-1, 0, 3, 5, 9, 12], "target": 2}, "expected_output": -1},
            {"input_data": {"nums": [5], "target": 5}, "expected_output": 0}
        ]
    },
    {
        "title": "Find Peak Element",
        "description": (
            "A peak element is an element that is strictly greater than its neighbors.\n\n"
            "Given an integer array nums, find a peak element, and return its index. "
            "If the array contains multiple peaks, return the index to any of the peaks."
        ),
        "examples": [
            {
                "input": "nums = [1,2,3,1]",
                "output": "2",
                "explanation": "3 is a peak element and its index is 2."
            }
        ],
        "class_name": "Solution",
        "method_name": "findPeakElement",
        "default_code": {
            "python": "class Solution:\n    def findPeakElement(self, nums: List[int]) -> int:"
        },
        "constraints": "1 <= nums.length <= 10^3\n-2^31 <= nums[i] <= 2^31 - 1",
        "followup": "Can you come up with an algorithm that is less than O(n^2) time complexity?",
        "categories_list": ["Binary Search"],
        "test_cases": [
            {"input_data": {"nums": [1, 2, 3, 1]}, "expected_output": 2},
            {"input_data": {"nums": [1, 2, 1, 3, 5, 6, 4]}, "expected_output": 5},
            {"input_data": {"nums": [1]}, "expected_output": 0}
        ]
    }
]

for problem_data in problems_data:
    create_problem(**problem_data)

