"""
=================================================================
RECURSION COMPLETE GUIDE
=================================================================

WHAT IS RECURSION?
------------------
Recursion is a programming technique where a function calls itself to solve smaller
instances of the same problem. It breaks down complex problems into simpler subproblems
until reaching a base case that can be solved directly. The solution is built by combining
results from recursive calls as the call stack unwinds.

Key characteristics:
- Base case: Termination condition that stops recursion
- Recursive case: Function calls itself with smaller/simpler input
- Call stack: Each call creates new stack frame (uses memory)
- Stack unwinding: Results combine as calls return
- Must progress toward base case to avoid infinite recursion

Basic concept:
```
function(n):
    if base_case:           # Stop recursion
        return simple_answer
    
    # Break into smaller problem
    result = function(n-1)  # Recursive call
    
    # Combine with current
    return process(result, n)
```

When to use Recursion:
- Problem can be divided into similar subproblems
- Tree or graph traversal
- Backtracking (exploring all possibilities)
- Divide and conquer algorithms
- Problems with recursive structure (factorial, fibonacci)
- When iterative solution is complex but recursive is clear

Common Recursion problem types:
- Mathematical sequences (fibonacci, factorial)
- Tree traversal (pre/in/post-order, path finding)
- Divide and conquer (merge sort, quick sort, binary search)
- Backtracking (permutations, combinations, N-queens)
- String manipulation (reverse, palindrome, substrings)
- Array problems (subsets, partition, max depth)

RECURSION CORE TEMPLATES
=========================
"""

from typing import List, Optional

# ================================================================
# BASIC LINEAR RECURSION TEMPLATE
# ================================================================
def linear_recursion_template(n):
    """
    Simple recursion with single recursive call
    TC: O(n) - n recursive calls
    SC: O(n) - call stack depth
    """
    # Base case - stops recursion
    if n <= 0:
        return 0
    
    # Recursive case - call with smaller input
    result = linear_recursion_template(n - 1)
    
    # Process current level
    return result + n

# ================================================================
# TREE RECURSION TEMPLATE
# ================================================================
def tree_recursion_template(n):
    """
    Recursion with multiple recursive calls (branches)
    TC: O(2^n) - exponential branching
    SC: O(n) - max depth of call stack
    """
    # Base case
    if n <= 1:
        return n
    
    # Multiple recursive calls (branches)
    left = tree_recursion_template(n - 1)
    right = tree_recursion_template(n - 2)
    
    # Combine results
    return left + right

# ================================================================
# DIVIDE AND CONQUER TEMPLATE
# ================================================================
def divide_conquer_template(arr, left, right):
    """
    Divide problem in half, solve subproblems, combine
    TC: O(n log n) typical for divide and conquer
    SC: O(log n) - recursion depth
    """
    # Base case - single element or empty
    if left >= right:
        return
    
    # Divide - split problem in half
    mid = left + (right - left) // 2
    
    # Conquer - solve subproblems
    divide_conquer_template(arr, left, mid)
    divide_conquer_template(arr, mid + 1, right)
    
    # Combine - merge results
    merge(arr, left, mid, right)

# ================================================================
# BACKTRACKING TEMPLATE
# ================================================================
def backtracking_template(nums, path, result):
    """
    Explore all possibilities, backtrack when invalid
    TC: O(2^n) or O(n!) depending on problem
    SC: O(n) - recursion depth + path storage
    """
    # Base case - found valid solution
    if is_valid_solution(path):
        result.append(path[:])  # Store copy
        return
    
    # Try all choices
    for choice in get_choices(nums):
        # Make choice
        path.append(choice)
        
        # Recurse with choice
        backtracking_template(nums, path, result)
        
        # Backtrack - undo choice
        path.pop()

# ================================================================
# MEMOIZATION TEMPLATE
# ================================================================
def memoization_template(n, memo=None):
    """
    Cache results to avoid recomputation
    TC: O(n) - each subproblem solved once
    SC: O(n) - memo cache + recursion stack
    """
    if memo is None:
        memo = {}
    
    # Base case
    if n <= 1:
        return n
    
    # Check cache
    if n in memo:
        return memo[n]
    
    # Compute and cache
    result = memoization_template(n-1, memo) + memoization_template(n-2, memo)
    memo[n] = result
    
    return result

"""
TIME & SPACE COMPLEXITY REFERENCE
==================================

RECURSION COMPLEXITY PATTERNS:
-------------------------------
+---------------------------+------------------+------------------+
| Pattern                   | Time Complexity  | Space Complexity |
+---------------------------+------------------+------------------+
| Linear Recursion          | O(n)             | O(n)             |
| Binary Tree Recursion     | O(2^n)           | O(n)             |
| Divide and Conquer        | O(n log n)       | O(log n)         |
| Backtracking (subset)     | O(2^n)           | O(n)             |
| Backtracking (permute)    | O(n!)            | O(n)             |
| Memoized Recursion        | O(n) to O(n²)    | O(n) to O(n²)    |
+---------------------------+------------------+------------------+

COMMON RECURSION PATTERNS COMPLEXITY:
--------------------------------------
+---------------------------+------------------+------------------+
| Pattern                   | Time Complexity  | Space Complexity |
+---------------------------+------------------+------------------+
| Factorial                 | O(n)             | O(n)             |
| Fibonacci (naive)         | O(2^n)           | O(n)             |
| Fibonacci (memo)          | O(n)             | O(n)             |
| Tree Traversal            | O(n)             | O(h)             |
| Merge Sort                | O(n log n)       | O(n)             |
| Quick Sort                | O(n log n) avg   | O(log n)         |
| Binary Search             | O(log n)         | O(log n)         |
| Power (a^n)               | O(log n)         | O(log n)         |
| Generate Subsets          | O(2^n)           | O(n)             |
| Generate Permutations     | O(n!)            | O(n)             |
| N-Queens                  | O(n!)            | O(n²)            |
| Combination Sum           | O(2^n)           | O(target/min)    |
+---------------------------+------------------+------------------+

WHERE:
- n = input size (array length, tree nodes, etc.)
- h = height of tree
- target = target sum in combination problems
- min = minimum element in array

COMPLEXITY NOTES:
-----------------
1. Linear Recursion: O(n) time, O(n) space
   - Single recursive call per level: O(n) calls
   - Each call adds to stack: O(n) space
   - Examples: Factorial, sum of array, reverse list
   
   Recurrence: T(n) = T(n-1) + O(1)
   Common pattern: Process current, recurse on rest

2. Binary Tree Recursion: O(2^n) time, O(n) space
   - Two recursive calls per level: 2^n total calls
   - Max depth of recursion: O(n)
   - Examples: Fibonacci (naive), count ways, decision trees
   
   Recurrence: T(n) = 2T(n-1) + O(1)
   Exponential without memoization!
   Common pattern: Split into two subproblems

3. Divide and Conquer: O(n log n) time, O(log n) or O(n) space
   - Divide: Split into halves (log n levels)
   - Conquer: Solve recursively
   - Combine: Merge results (O(n) per level)
   - Total: O(n) work at each of O(log n) levels = O(n log n)
   
   Space: O(log n) for recursion, O(n) if additional array needed
   Examples: Merge sort, quick sort, binary search tree operations
   
   Recurrence: T(n) = 2T(n/2) + O(n)
   Master theorem: T(n) = O(n log n)

4. Backtracking - Subsets: O(2^n) time, O(n) space
   - For each element: include or exclude (2 choices)
   - Total combinations: 2^n
   - Space: O(n) for recursion depth + current path
   
   Examples: Power set, subset sum, combination sum
   At each step: make choice, recurse, undo choice
   
   Generate all: O(2^n) solutions × O(n) per solution = O(n * 2^n) output

5. Backtracking - Permutations: O(n!) time, O(n) space
   - First position: n choices
   - Second position: n-1 choices
   - Total: n! permutations
   
   Space: O(n) for recursion + current permutation
   Examples: All permutations, N-queens, Sudoku
   
   Output size: O(n!) permutations × O(n) per permutation

6. Memoization: O(n) to O(n²) time, O(n) to O(n²) space
   - Each unique subproblem solved once
   - Cache results in memo dictionary/array
   - Reduces exponential to polynomial
   
   Fibonacci: O(2^n) → O(n) with memoization
   Common pattern: Check cache, compute if missing, store result
   
   Trade-off: Use memory to save time

7. Tree Traversal: O(n) time, O(h) space
   - Visit each node once: O(n)
   - Stack depth = tree height: O(h)
   - Balanced tree: O(log n) space
   - Skewed tree: O(n) space
   
   Examples: Pre/in/post-order, path finding
   Each node processed once

8. Binary Search: O(log n) time, O(log n) space
   - Halve search space each step: log n steps
   - Recursion depth: O(log n)
   - Can be optimized to O(1) space with iteration
   
   Recurrence: T(n) = T(n/2) + O(1)
   Solution: T(n) = O(log n)

GENERAL RECURSION OPTIMIZATION:
--------------------------------
Time optimization:
- Use memoization to cache results
- Convert to iteration if tail recursion
- Use divide and conquer to reduce branching

Space optimization:
- Convert tail recursion to iteration
- Use iterative deepening for DFS
- Pass by reference instead of copying

Choosing approach:
- Recursive: Natural for tree/graph, backtracking
- Iterative: Better for simple loops, space-critical
- Memoized: When subproblems overlap

WHEN TO USE EACH PATTERN:
--------------------------
Linear Recursion:
  - Process sequence one element at a time
  - Sum, reverse, validate structure
  - Can often convert to iteration

Tree Recursion:
  - Multiple branches from each call
  - Decision trees, Fibonacci
  - Use memoization if subproblems overlap

Divide and Conquer:
  - Problem divisible into independent halves
  - Sorting, searching in sorted data
  - Merge/combine step needed

Backtracking:
  - Generate all possibilities
  - Constraint satisfaction problems
  - Undo choices to try alternatives

Memoization:
  - Overlapping subproblems
  - Optimize exponential to polynomial
  - Convert to DP for bottom-up
"""

"""
RECURSION PATTERNS
==================
"""

# ================================================================
# PATTERN 1: BASIC RECURSION (LINEAR/SINGLE BRANCH)
# PATTERN EXPLANATION: Single recursive call that progresses linearly toward base case.
# Each call processes current element and delegates rest to recursive call. Build solution
# as stack unwinds. Simplest form of recursion, often can be converted to iteration. Used
# for sequential processing, validation, and simple transformations.
#
# TYPICAL STEPS:
# 1. Define base case (empty, single element, or zero)
# 2. Process current element
# 3. Make recursive call with smaller input (n-1, rest of list)
# 4. Combine current with recursive result
# 5. Return combined result
#
# Applications: Factorial, sum, reverse, string palindrome, power calculation.
# ================================================================

class BasicRecursion:
    """
    Problem 1: Calculate n! (n factorial) = n × (n-1) × ... × 2 × 1
    
    Example:
        factorial(5) = 5 × 4 × 3 × 2 × 1 = 120
    
    TC: O(n) - n recursive calls
    SC: O(n) - call stack depth
    
    How it works:
    1. Base case: 0! = 1 or 1! = 1
    2. Recursive case: n! = n × (n-1)!
    3. Each call multiplies current n with result of (n-1)!
    4. Stack unwinds multiplying results together
    """
    def factorial(self, n: int) -> int:
        # Base case
        if n <= 1:
            return 1
        
        # Recursive case: n! = n × (n-1)!
        return n * self.factorial(n - 1)

# Example trace:
# factorial(5)
#   = 5 * factorial(4)
#   = 5 * (4 * factorial(3))
#   = 5 * (4 * (3 * factorial(2)))
#   = 5 * (4 * (3 * (2 * factorial(1))))
#   = 5 * (4 * (3 * (2 * 1)))         # Base case reached
#   = 5 * (4 * (3 * 2))               # Stack unwinds
#   = 5 * (4 * 6)
#   = 5 * 24
#   = 120

    def power(self, x: float, n: int) -> float:  # LC 50 - Pow(x, n)
        """
        Problem 2: Calculate x^n efficiently using recursion.
        
        Optimized with divide and conquer:
        - x^n = (x^(n/2))^2 if n is even
        - x^n = x × (x^(n/2))^2 if n is odd
        
        TC: O(log n) - halve n each time
        SC: O(log n) - recursion depth
        
        How it works:
        1. Base case: x^0 = 1
        2. Handle negative exponents: x^(-n) = 1/(x^n)
        3. Divide: Calculate half = x^(n/2)
        4. Conquer: Square half, multiply by x if odd
        """
        # Base case
        if n == 0:
            return 1.0
        
        # Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n
        
        # Divide and conquer
        half = self.power(x, n // 2)
        
        # Even exponent: x^n = (x^(n/2))^2
        if n % 2 == 0:
            return half * half
        # Odd exponent: x^n = x × (x^(n/2))^2
        else:
            return x * half * half

# Example trace:
# power(2, 10)
#   n=10 (even): half = power(2, 5)
#     n=5 (odd): half = power(2, 2)
#       n=2 (even): half = power(2, 1)
#         n=1 (odd): half = power(2, 0)
#           n=0: return 1         # Base case
#         return 2 * 1 * 1 = 2    # 2^1
#       return 2 * 2 = 4          # 2^2
#     return 2 * 4 * 4 = 32       # 2^5
#   return 32 * 32 = 1024         # 2^10

    def isPalindrome(self, s: str) -> bool:
        """
        Problem 3: Check if string is palindrome using recursion.
        
        TC: O(n) - process each character once
        SC: O(n) - recursion depth
        
        How it works:
        1. Base case: Empty or single character is palindrome
        2. Check if first and last characters match
        3. Recursively check middle substring
        """
        # Remove non-alphanumeric and convert to lowercase
        s = ''.join(c.lower() for c in s if c.isalnum())
        
        def helper(left: int, right: int) -> bool:
            # Base case: Pointers met or crossed
            if left >= right:
                return True
            
            # Check ends match and recurse on middle
            if s[left] != s[right]:
                return False
            
            return helper(left + 1, right - 1)
        
        return helper(0, len(s) - 1)

# Example trace:
# isPalindrome("A man, a plan, a canal: Panama")
# Clean: "amanaplanacanalpanama"
# helper(0, 20):  'a' == 'a'? Yes → helper(1, 19)
# helper(1, 19):  'm' == 'm'? Yes → helper(2, 18)
# helper(2, 18):  'a' == 'a'? Yes → helper(3, 17)
# ... continues until left >= right
# All characters matched → True

sol = BasicRecursion()
print("Factorial(5):", sol.factorial(5))  # 120
print("Power(2, 10):", sol.power(2, 10))  # 1024
print("Is Palindrome:", sol.isPalindrome("A man, a plan, a canal: Panama"))  # True


# ================================================================
# PATTERN 2: TREE RECURSION (MULTIPLE BRANCHES)
# PATTERN EXPLANATION: Multiple recursive calls from each invocation, creating branching
# structure like a tree. Each branch explores different possibility or subproblem. Without
# memoization, can have exponential time complexity. Common in decision problems, tree
# traversal, and exploring all paths. Solutions combine results from all branches.
#
# TYPICAL STEPS:
# 1. Define base case(s)
# 2. Make multiple recursive calls (typically 2+ branches)
# 3. Process/combine results from all branches
# 4. Return combined result
# 5. Consider memoization if subproblems overlap
#
# Applications: Fibonacci, tree traversal, counting paths, decision trees.
# ================================================================

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeRecursion:
    """
    Problem 1: Calculate nth Fibonacci number.
    F(n) = F(n-1) + F(n-2), where F(0)=0, F(1)=1
    
    Example:
        F(5) = 0, 1, 1, 2, 3, 5
        Output: 5
    
    TC: O(2^n) naive, O(n) with memoization
    SC: O(n) - recursion depth
    
    How it works:
    1. Base cases: F(0)=0, F(1)=1
    2. Two recursive branches: F(n-1) and F(n-2)
    3. Add results from both branches
    4. Many repeated calculations without memoization
    """
    def fib(self, n: int) -> int:  # LC 509 - Fibonacci Number
        # Base cases
        if n <= 1:
            return n
        
        # Two recursive calls (tree branching)
        return self.fib(n - 1) + self.fib(n - 2)
    
    def fib_memo(self, n: int, memo=None) -> int:
        """Optimized with memoization"""
        if memo is None:
            memo = {}
        
        # Base cases
        if n <= 1:
            return n
        
        # Check cache
        if n in memo:
            return memo[n]
        
        # Calculate and cache
        memo[n] = self.fib_memo(n-1, memo) + self.fib_memo(n-2, memo)
        return memo[n]

# Example trace (naive):
# fib(5)
#   = fib(4) + fib(3)
#   = (fib(3) + fib(2)) + (fib(2) + fib(1))
#   = ((fib(2) + fib(1)) + (fib(1) + fib(0))) + ((fib(1) + fib(0)) + 1)
#   = (((fib(1) + fib(0)) + 1) + (1 + 0)) + ((1 + 0) + 1)
#   = (((1 + 0) + 1) + 1) + (1 + 1)
#   = ((1 + 1) + 1) + 2
#   = (2 + 1) + 2
#   = 3 + 2
#   = 5
#
# Note: Many repeated calculations! fib(3) called twice, fib(2) called 3 times

    def maxDepth(self, root: Optional[TreeNode]) -> int:  # LC 104
        """
        Problem 2: Find maximum depth of binary tree.
        
        TC: O(n) - visit each node once
        SC: O(h) - recursion depth = tree height
        
        How it works:
        1. Base case: null node has depth 0
        2. Recursively get depth of left and right subtrees
        3. Current depth = 1 + max(left_depth, right_depth)
        """
        # Base case: empty tree
        if not root:
            return 0
        
        # Get depth from both subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # Current depth = 1 + max of children
        return 1 + max(left_depth, right_depth)

# Example trace:
# Tree:     3
#          / \
#         9  20
#           /  \
#          15   7
#
# maxDepth(3):
#   left = maxDepth(9):
#     left = maxDepth(None) = 0
#     right = maxDepth(None) = 0
#     return 1 + max(0, 0) = 1
#   right = maxDepth(20):
#     left = maxDepth(15):
#       return 1 + max(0, 0) = 1
#     right = maxDepth(7):
#       return 1 + max(0, 0) = 1
#     return 1 + max(1, 1) = 2
#   return 1 + max(1, 2) = 3

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:  # LC 112
        """
        Problem 3: Check if tree has root-to-leaf path with given sum.
        
        TC: O(n) - visit each node once
        SC: O(h) - recursion depth
        
        How it works:
        1. Base case: null node → False
        2. Leaf node: check if value equals remaining sum
        3. Internal node: check if either subtree has path
        4. Pass down remaining sum (targetSum - current value)
        """
        # Base case: empty tree
        if not root:
            return False
        
        # Leaf node: check if this completes the path
        if not root.left and not root.right:
            return root.val == targetSum
        
        # Check both subtrees with updated sum
        remaining = targetSum - root.val
        return (self.hasPathSum(root.left, remaining) or 
                self.hasPathSum(root.right, remaining))

# Example trace:
# Tree:      5
#           / \
#          4   8
#         /   / \
#        11  13  4
#       /  \      \
#      7    2      1
# targetSum = 22
#
# hasPathSum(5, 22):
#   Not leaf, remaining = 22 - 5 = 17
#   Check left: hasPathSum(4, 17)
#     Not leaf, remaining = 17 - 4 = 13
#     Check left: hasPathSum(11, 13)
#       Not leaf, remaining = 13 - 11 = 2
#       Check left: hasPathSum(7, 2)
#         Leaf, 7 == 2? No, return False
#       Check right: hasPathSum(2, 2)
#         Leaf, 2 == 2? Yes, return True  # Found path!
#       return False or True = True
#     return True
#   return True
# Path found: 5 → 4 → 11 → 2 = 22

sol = TreeRecursion()
print("Fibonacci(10):", sol.fib(10))  # 55
print("Fibonacci with Memo(10):", sol.fib_memo(10))  # 55

tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print("Max Depth:", sol.maxDepth(tree))  # 3

tree2 = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), 
                 TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
print("Has Path Sum:", sol.hasPathSum(tree2, 22))  # True


# ================================================================
# PATTERN 3: DIVIDE AND CONQUER
# PATTERN EXPLANATION: Break problem into independent subproblems, solve recursively, then
# combine results. Typically divides input in half (binary division). Each level does O(n)
# work across all subproblems, with O(log n) levels, giving O(n log n) complexity. Used in
# efficient sorting, searching, and optimization algorithms.
#
# TYPICAL STEPS:
# 1. Base case: Handle small input (single element, empty)
# 2. Divide: Split problem into subproblems (usually halves)
# 3. Conquer: Recursively solve each subproblem
# 4. Combine: Merge results from subproblems
# 5. Return combined result
#
# Applications: Merge sort, quick sort, binary search, closest pair, maximum subarray.
# ================================================================

class DivideAndConquer:
    """
    Problem 1: Implement merge sort to sort an array.
    
    Example:
        Input: [38, 27, 43, 3, 9, 82, 10]
        Output: [3, 9, 10, 27, 38, 43, 82]
    
    TC: O(n log n) - log n levels, O(n) work per level
    SC: O(n) - temporary arrays for merging
    
    How it works:
    1. Divide: Split array into two halves
    2. Conquer: Recursively sort each half
    3. Combine: Merge two sorted halves
    4. Recursion tree has log n height, O(n) work per level
    """
    def mergeSort(self, nums: List[int]) -> List[int]:  # LC 912 - Sort an Array
        # Base case: single element or empty
        if len(nums) <= 1:
            return nums
        
        # Divide: Split in half
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        
        # Conquer: Recursively sort both halves
        left = self.mergeSort(left)
        right = self.mergeSort(right)
        
        # Combine: Merge sorted halves
        return self.merge(left, right)
    
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        """Merge two sorted arrays"""
        result = []
        i = j = 0
        
        # Merge while both have elements
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        # Append remaining elements
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result

# Example trace:
# mergeSort([38, 27, 43, 3])
#   Divide: left=[38,27], right=[43,3]
#   
#   mergeSort([38, 27]):
#     Divide: left=[38], right=[27]
#     mergeSort([38]) = [38]  # Base case
#     mergeSort([27]) = [27]  # Base case
#     merge([38], [27]) = [27, 38]
#   
#   mergeSort([43, 3]):
#     Divide: left=[43], right=[3]
#     mergeSort([43]) = [43]  # Base case
#     mergeSort([3]) = [3]    # Base case
#     merge([43], [3]) = [3, 43]
#   
#   merge([27,38], [3,43]) = [3, 27, 38, 43]

    def search(self, nums: List[int], target: int) -> int:  # LC 704 - Binary Search
        """
        Problem 2: Binary search in sorted array.
        
        TC: O(log n) - halve search space each time
        SC: O(log n) - recursion depth (O(1) if iterative)
        
        How it works:
        1. Base case: left > right → not found
        2. Check middle element
        3. If target < mid: search left half
        4. If target > mid: search right half
        5. Otherwise: found at mid
        """
        def helper(left: int, right: int) -> int:
            # Base case: search space exhausted
            if left > right:
                return -1
            
            # Find middle
            mid = left + (right - left) // 2
            
            # Check middle element
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                # Search left half
                return helper(left, mid - 1)
            else:
                # Search right half
                return helper(mid + 1, right)
        
        return helper(0, len(nums) - 1)

# Example trace:
# search([1, 3, 5, 7, 9, 11], 7)
# helper(0, 5):
#   mid = 2, nums[2] = 5
#   5 < 7, search right: helper(3, 5)
#     mid = 4, nums[4] = 9
#     9 > 7, search left: helper(3, 3)
#       mid = 3, nums[3] = 7
#       7 == 7, return 3  # Found!

    def sortArray(self, nums: List[int]) -> List[int]:  # Quick Sort variation
        """
        Problem 3: Quick sort (divide and conquer with pivot).
        
        TC: O(n log n) average, O(n²) worst case
        SC: O(log n) - recursion depth
        
        How it works:
        1. Choose pivot element
        2. Partition: elements < pivot left, > pivot right
        3. Recursively sort left and right partitions
        4. Concatenate: left + [pivot] + right
        """
        # Base case
        if len(nums) <= 1:
            return nums
        
        # Choose pivot (middle element)
        pivot = nums[len(nums) // 2]
        
        # Partition into three groups
        left = [x for x in nums if x < pivot]
        middle = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]
        
        # Recursively sort and combine
        return self.sortArray(left) + middle + self.sortArray(right)

sol = DivideAndConquer()
print("Merge Sort:", sol.mergeSort([38, 27, 43, 3, 9, 82, 10]))  # [3,9,10,27,38,43,82]
print("Binary Search:", sol.search([-1,0,3,5,9,12], 9))  # 4
print("Quick Sort:", sol.sortArray([5,2,3,1]))  # [1,2,3,5]


# ================================================================
# PATTERN 4: BACKTRACKING
# PATTERN EXPLANATION: Systematically explore all possible solutions by making choices,
# recursing with each choice, then undoing choice (backtracking) to try alternatives. Build
# solution incrementally, abandoning paths that violate constraints. Returns to previous
# state by removing last choice before trying next option. Essential for combinatorial
# problems and constraint satisfaction.
#
# TYPICAL STEPS:
# 1. Check if current path is valid solution (base case)
# 2. If valid, store/count solution
# 3. For each possible choice:
#    a. Make choice (add to path)
#    b. Recurse with updated path
#    c. Backtrack (remove choice from path)
# 4. Return after exploring all branches
#
# Applications: Permutations, combinations, subsets, N-Queens, Sudoku, word search.
# ================================================================

class Backtracking:
    """
    Problem 1: Generate all subsets (power set) of given set.
    
    Example:
        Input: [1, 2, 3]
        Output: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
    
    TC: O(2^n) - 2^n subsets
    SC: O(n) - recursion depth
    
    How it works:
    1. For each element: choose to include or exclude
    2. Two recursive calls: with element and without
    3. Base case: processed all elements
    4. Collect all valid subsets
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:  # LC 78
        result = []
        
        def backtrack(start: int, path: List[int]):
            # Every path is a valid subset
            result.append(path[:])  # Store copy
            
            # Try adding each remaining element
            for i in range(start, len(nums)):
                # Make choice: include nums[i]
                path.append(nums[i])
                
                # Recurse with next elements
                backtrack(i + 1, path)
                
                # Backtrack: remove nums[i]
                path.pop()
        
        backtrack(0, [])
        return result

# Example trace:
# subsets([1, 2, 3])
# backtrack(0, []):
#   Add [] to result
#   i=0: path=[1]
#     backtrack(1, [1]):
#       Add [1] to result
#       i=1: path=[1,2]
#         backtrack(2, [1,2]):
#           Add [1,2] to result
#           i=2: path=[1,2,3]
#             backtrack(3, [1,2,3]):
#               Add [1,2,3] to result
#             path=[1,2] (backtrack)
#         path=[1] (backtrack)
#       i=2: path=[1,3]
#         backtrack(3, [1,3]):
#           Add [1,3] to result
#         path=[1] (backtrack)
#     path=[] (backtrack)
#   i=1: path=[2]
#     ... similar for [2], [2,3]
#   i=2: path=[3]
#     ... [3]
# Result: [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]

    def permute(self, nums: List[int]) -> List[List[int]]:  # LC 46
        """
        Problem 2: Generate all permutations of array.
        
        Example:
            Input: [1, 2, 3]
            Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
        
        TC: O(n!) - n! permutations
        SC: O(n) - recursion depth + path
        
        How it works:
        1. For each position, try all unused elements
        2. Mark element as used, recurse, then unmark
        3. Base case: path length equals array length
        """
        result = []
        
        def backtrack(path: List[int], used: set):
            # Base case: complete permutation
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            # Try each unused element
            for i in range(len(nums)):
                if i in used:
                    continue
                
                # Make choice
                path.append(nums[i])
                used.add(i)
                
                # Recurse
                backtrack(path, used)
                
                # Backtrack
                path.pop()
                used.remove(i)
        
        backtrack([], set())
        return result

# Example trace (partial):
# permute([1, 2, 3])
# backtrack([], {}):
#   Try i=0: path=[1], used={0}
#     backtrack([1], {0}):
#       Try i=1: path=[1,2], used={0,1}
#         backtrack([1,2], {0,1}):
#           Try i=2: path=[1,2,3], used={0,1,2}
#             Complete! Add [1,2,3]
#           path=[1,2] (backtrack)
#       path=[1] (backtrack)
#       Try i=2: path=[1,3], used={0,2}
#         backtrack([1,3], {0,2}):
#           Try i=1: path=[1,3,2], used={0,1,2}
#             Complete! Add [1,3,2]
#   ... continues for all permutations

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:  # LC 39
        """
        Problem 3: Find all unique combinations that sum to target.
        Elements can be reused unlimited times.
        
        Example:
            Input: candidates = [2,3,6,7], target = 7
            Output: [[2,2,3], [7]]
        
        TC: O(2^target) - exponential exploration
        SC: O(target/min) - recursion depth
        
        How it works:
        1. Try including current candidate (can reuse)
        2. Try excluding current candidate (move to next)
        3. Base case: sum equals target (valid) or exceeds (invalid)
        4. Prune branches that exceed target
        """
        result = []
        
        def backtrack(start: int, path: List[int], remaining: int):
            # Base case: found valid combination
            if remaining == 0:
                result.append(path[:])
                return
            
            # Base case: exceeded target
            if remaining < 0:
                return
            
            # Try each candidate starting from 'start'
            for i in range(start, len(candidates)):
                # Make choice
                path.append(candidates[i])
                
                # Recurse: can reuse same element (start=i, not i+1)
                backtrack(i, path, remaining - candidates[i])
                
                # Backtrack
                path.pop()
        
        backtrack(0, [], target)
        return result

# Example trace (partial):
# combinationSum([2,3,6,7], 7)
# backtrack(0, [], 7):
#   i=0: path=[2], remaining=5
#     backtrack(0, [2], 5):
#       i=0: path=[2,2], remaining=3
#         backtrack(0, [2,2], 3):
#           i=0: path=[2,2,2], remaining=1
#             backtrack(0, [2,2,2], 1):
#               i=0: remaining=-1 (exceeded)
#               i=1: remaining=-2 (exceeded)
#           i=1: path=[2,2,3], remaining=0
#             Found! Add [2,2,3]
#   i=3: path=[7], remaining=0
#     Found! Add [7]
# Result: [[2,2,3], [7]]

sol = Backtracking()
print("Subsets:", sol.subsets([1,2,3]))
print("Permutations:", sol.permute([1,2,3]))
print("Combination Sum:", sol.combinationSum([2,3,6,7], 7))


# ================================================================
# PATTERN 5: RECURSION WITH MEMOIZATION (TOP-DOWN DP)
# PATTERN EXPLANATION: Optimize recursive solutions by caching results of subproblems in
# memo dictionary. Check cache before computing, store result after computing. Converts
# exponential time to polynomial by ensuring each unique subproblem solved only once.
# Natural bridge between naive recursion and dynamic programming. Also called top-down DP.
#
# TYPICAL STEPS:
# 1. Create memo dictionary (or pass as parameter)
# 2. Check if result already in memo (base case)
# 3. If yes, return cached result immediately
# 4. If no, compute recursively
# 5. Store result in memo before returning
# 6. Return result
#
# Applications: Fibonacci, climbing stairs, coin change, longest common subsequence.
# ================================================================

class RecursionWithMemo:
    """
    Problem 1: Climbing stairs - count ways to climb n steps.
    Can take 1 or 2 steps at a time.
    
    Example:
        n = 5
        Ways: 1+1+1+1+1, 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1,
              1+2+2, 2+1+2, 2+2+1
        Output: 8
    
    TC: O(n) with memo, O(2^n) without
    SC: O(n) - memo dictionary + recursion stack
    
    How it works:
    1. Ways to reach step n = ways to reach (n-1) + ways to reach (n-2)
    2. Same as Fibonacci sequence
    3. Memoization prevents recalculating same steps
    """
    def climbStairs(self, n: int) -> int:  # LC 70
        memo = {}
        
        def climb(n: int) -> int:
            # Base cases
            if n <= 2:
                return n
            
            # Check cache
            if n in memo:
                return memo[n]
            
            # Calculate and cache
            memo[n] = climb(n - 1) + climb(n - 2)
            return memo[n]
        
        return climb(n)

# Example trace with memo:
# climbStairs(5)
# climb(5):
#   Not in memo, compute: climb(4) + climb(3)
#   climb(4):
#     Not in memo, compute: climb(3) + climb(2)
#     climb(3):
#       Not in memo, compute: climb(2) + climb(1)
#       climb(2) = 2 (base case)
#       climb(1) = 1 (base case)
#       memo[3] = 2 + 1 = 3
#     climb(2) = 2 (base case)
#     memo[4] = 3 + 2 = 5
#   climb(3):
#     In memo! return 3 (no recalculation!)
#   memo[5] = 5 + 3 = 8
# Return: 8
#
# Without memo, climb(3) would be recalculated many times

    def minCostClimbingStairs(self, cost: List[int]) -> int:  # LC 746
        """
        Problem 2: Find minimum cost to reach top of stairs.
        Can start from step 0 or 1, can climb 1 or 2 steps.
        
        Example:
            cost = [10, 15, 20]
            Start at 15, climb to top: cost = 15
            Output: 15
        
        TC: O(n) with memo
        SC: O(n) - memo + recursion
        
        How it works:
        1. Min cost to reach step i = min(cost from i-1, cost from i-2) + cost[i]
        2. Can start from step 0 or 1 (both cost 0)
        3. Memoize to avoid recalculating same steps
        """
        memo = {}
        
        def minCost(i: int) -> int:
            # Base cases: can start from 0 or 1 for free
            if i < 0:
                return 0
            if i <= 1:
                return cost[i]
            
            # Check cache
            if i in memo:
                return memo[i]
            
            # Min cost = current step cost + min of (previous two steps)
            memo[i] = cost[i] + min(minCost(i - 1), minCost(i - 2))
            return memo[i]
        
        # Top is one step beyond last
        n = len(cost)
        return min(minCost(n - 1), minCost(n - 2))

    def rob(self, nums: List[int]) -> int:  # LC 198 - House Robber
        """
        Problem 3: Rob houses, can't rob adjacent houses.
        Maximize total money robbed.
        
        Example:
            nums = [2, 7, 9, 3, 1]
            Rob houses 0, 2, 4: 2 + 9 + 1 = 12
            Output: 12
        
        TC: O(n) with memo
        SC: O(n)
        
        How it works:
        1. At each house: rob it (skip previous) or skip it (take previous max)
        2. rob(i) = max(nums[i] + rob(i-2), rob(i-1))
        3. Memoize to avoid recalculating
        """
        memo = {}
        
        def robFrom(i: int) -> int:
            # Base cases
            if i >= len(nums):
                return 0
            
            # Check cache
            if i in memo:
                return memo[i]
            
            # Choice: rob current house or skip it
            rob_current = nums[i] + robFrom(i + 2)
            skip_current = robFrom(i + 1)
            
            memo[i] = max(rob_current, skip_current)
            return memo[i]
        
        return robFrom(0)

# Example trace:
# rob([2, 7, 9, 3, 1])
# robFrom(0):
#   rob_current = 2 + robFrom(2)
#     robFrom(2):
#       rob_current = 9 + robFrom(4)
#         robFrom(4):
#           rob_current = 1 + robFrom(6) = 1 + 0 = 1
#           skip_current = robFrom(5) = 0
#           memo[4] = max(1, 0) = 1
#       skip_current = robFrom(3)
#         robFrom(3):
#           rob_current = 3 + robFrom(5) = 3 + 0 = 3
#           skip_current = robFrom(4) = 1 (from memo!)
#           memo[3] = max(3, 1) = 3
#       memo[2] = max(9+1, 3) = 10
#   skip_current = robFrom(1)
#     robFrom(1):
#       rob_current = 7 + robFrom(3) = 7 + 3 (from memo!) = 10
#       skip_current = robFrom(2) = 10 (from memo!)
#       memo[1] = max(10, 10) = 10
#   memo[0] = max(2+10, 10) = 12
# Return: 12

sol = RecursionWithMemo()
print("Climbing Stairs(5):", sol.climbStairs(5))  # 8
print("Min Cost Climbing:", sol.minCostClimbingStairs([10,15,20]))  # 15
print("House Robber:", sol.rob([2,7,9,3,1]))  # 12


# ================================================================
# PATTERN 6: HELPER FUNCTION RECURSION (ACCUMULATED STATE)
# PATTERN EXPLANATION: Use helper function with extra parameters to accumulate state or
# track progress through recursion. Main function initializes state, helper carries it
# through recursive calls. Common for problems needing indices, accumulators, or context
# that main function doesn't have. Cleaner than modifying input or using global variables.
#
# TYPICAL STEPS:
# 1. Main function: Set up initial state, call helper
# 2. Helper function: Takes original params + accumulated state
# 3. Base case: Check termination condition
# 4. Recursive case: Update state, pass to next call
# 5. Return or modify accumulated result
# 6. Main function returns final accumulated state
#
# Applications: Reverse list, flatten nested list, path collection, range recursion.
# ================================================================

class HelperRecursion:
    """
    Problem 1: Reverse a linked list using recursion.
    
    Example:
        Input: 1 -> 2 -> 3 -> 4 -> 5
        Output: 5 -> 4 -> 3 -> 2 -> 1
    
    TC: O(n) - visit each node once
    SC: O(n) - recursion stack
    
    How it works:
    1. Helper carries prev node through recursion
    2. Reverse link at each node
    3. Base case: reached end, return new head
    """
    def reverseList(self, head):  # LC 206
        """Using helper function with accumulated state"""
        def helper(node, prev):
            # Base case: reached end
            if not node:
                return prev
            
            # Save next node
            next_node = node.next
            
            # Reverse link
            node.next = prev
            
            # Recurse with updated prev
            return helper(next_node, node)
        
        return helper(head, None)

# Example trace:
# List: 1 -> 2 -> 3 -> None
# reverseList(1):
#   helper(1, None):
#     next = 2, reverse: 1.next = None
#     helper(2, 1):
#       next = 3, reverse: 2.next = 1
#       helper(3, 2):
#         next = None, reverse: 3.next = 2
#         helper(None, 3):
#           return 3 (new head)
# Result: 3 -> 2 -> 1 -> None

    def rangeSumBST(self, root, low, high):  # LC 938
        """
        Problem 2: Sum of values in BST within range [low, high].
        
        Example:
            Tree:     10
                     /  \
                    5    15
                   / \     \
                  3   7    18
            Range: [7, 15]
            Sum: 7 + 10 + 15 = 32
        
        TC: O(n) - visit nodes in range
        SC: O(h) - recursion depth
        
        How it works:
        1. Helper accumulates sum through recursion
        2. Use BST property to prune branches
        3. If node < low: only check right
        4. If node > high: only check left
        """
        def helper(node, accumulated_sum):
            if not node:
                return accumulated_sum
            
            # Add current if in range
            if low <= node.val <= high:
                accumulated_sum += node.val
            
            # Use BST property for pruning
            if node.val > low:
                accumulated_sum = helper(node.left, accumulated_sum)
            if node.val < high:
                accumulated_sum = helper(node.right, accumulated_sum)
            
            return accumulated_sum
        
        return helper(root, 0)

    def flatten(self, root):  # LC 114 - Flatten Binary Tree to Linked List
        """
        Problem 3: Flatten binary tree to linked list in-place (pre-order).
        
        Example:
            Tree:    1
                    / \
                   2   5
                  / \   \
                 3   4   6
            
            Flatten: 1 -> 2 -> 3 -> 4 -> 5 -> 6
        
        TC: O(n) - visit each node once
        SC: O(h) - recursion depth
        
        How it works:
        1. Helper returns tail of flattened subtree
        2. Flatten left, then right
        3. Connect: root -> left_tail -> right
        4. Return rightmost node
        """
        def helper(node):
            # Base case: null node
            if not node:
                return None
            
            # Leaf node
            if not node.left and not node.right:
                return node
            
            # Flatten left and right subtrees
            left_tail = helper(node.left)
            right_tail = helper(node.right)
            
            # If left subtree exists, connect it
            if left_tail:
                # Insert left subtree between root and right
                left_tail.right = node.right
                node.right = node.left
                node.left = None
            
            # Return rightmost node
            return right_tail if right_tail else left_tail
        
        helper(root)

# Example trace:
# Tree:    1
#         / \
#        2   3
#
# flatten(1):
#   helper(1):
#     left_tail = helper(2):
#       return 2 (leaf)
#     right_tail = helper(3):
#       return 3 (leaf)
#     
#     Connect: 2.right = 3, 1.right = 2, 1.left = None
#     Result: 1 -> 2 -> 3
#     return 3

    def sumNumbers(self, root):  # LC 129 - Sum Root to Leaf Numbers
        """
        Problem 4: Sum all root-to-leaf numbers.
        
        Example:
            Tree:   1
                   / \
                  2   3
            
            Paths: 12, 13
            Sum: 12 + 13 = 25
        
        TC: O(n), SC: O(h)
        
        How it works:
        1. Helper accumulates number as we traverse
        2. At each node: current_num = prev * 10 + node.val
        3. At leaf: add to total sum
        """
        def helper(node, current_num):
            if not node:
                return 0
            
            # Build number: shift previous left, add current digit
            current_num = current_num * 10 + node.val
            
            # Leaf node: return this number
            if not node.left and not node.right:
                return current_num
            
            # Internal node: sum of both subtrees
            return (helper(node.left, current_num) + 
                    helper(node.right, current_num))
        
        return helper(root, 0)

# Example trace:
# Tree:   1
#        / \
#       2   3
# sumNumbers(1):
#   helper(1, 0):
#     current_num = 0*10 + 1 = 1
#     left = helper(2, 1):
#       current_num = 1*10 + 2 = 12
#       Leaf, return 12
#     right = helper(3, 1):
#       current_num = 1*10 + 3 = 13
#       Leaf, return 13
#     return 12 + 13 = 25

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

sol = HelperRecursion()

# Test reverse list
head = ListNode(1, ListNode(2, ListNode(3)))
reversed_head = sol.reverseList(head)
print("Reversed List: ", end="")
while reversed_head:
    print(reversed_head.val, end=" -> " if reversed_head.next else "\n")
    reversed_head = reversed_head.next

# Test sum numbers
tree = TreeNode(1, TreeNode(2), TreeNode(3))
print("Sum Root to Leaf:", sol.sumNumbers(tree))  # 25


# ================================================================
# SUMMARY OF RECURSION PATTERNS
# ================================================================
"""
Pattern 1 - Basic Recursion (Linear):
  - Single recursive call, process linearly
  - Simple problems with sequential processing
  - Use for: Factorial, sum, reverse, power
  - Example: LC 50 (Pow(x, n))

Pattern 2 - Tree Recursion (Multiple Branches):
  - Multiple recursive calls from each invocation
  - Exponential without memoization
  - Use for: Fibonacci, tree traversal, decision problems
  - Example: LC 104 (Maximum Depth), LC 112 (Path Sum)

Pattern 3 - Divide and Conquer:
  - Divide problem in half, solve, combine
  - O(n log n) typical complexity
  - Use for: Sorting, binary search, optimization
  - Example: LC 912 (Sort Array - Merge Sort), LC 704 (Binary Search)

Pattern 4 - Backtracking:
  - Explore all possibilities, undo choices
  - Generate combinations, permutations
  - Use for: Constraint satisfaction, generate all solutions
  - Example: LC 78 (Subsets), LC 46 (Permutations), LC 39 (Combination Sum)

Pattern 5 - Recursion with Memoization:
  - Cache results to avoid recomputation
  - Convert exponential to polynomial
  - Use for: DP problems, overlapping subproblems
  - Example: LC 70 (Climbing Stairs), LC 198 (House Robber)

Pattern 6 - Helper Function Recursion:
  - Use helper with accumulated state
  - Track progress through parameters
  - Use for: Reverse, range problems, path accumulation
  - Example: LC 206 (Reverse List), LC 129 (Sum Root to Leaf)

Master these 6 patterns and you'll handle 80-90% of recursion problems on LeetCode!

KEY TAKEAWAYS:
--------------
1. Always define clear base case(s) to stop recursion
2. Ensure progress toward base case (smaller input, updated state)
3. Each recursive call should solve simpler subproblem
4. Use memoization for overlapping subproblems
5. Stack space = O(recursion depth)
6. Backtracking = make choice, recurse, undo choice
7. Helper functions for carrying accumulated state
8. Divide and conquer for problems divisible into halves
9. Tree recursion can be exponential - consider memoization
10. Some recursive solutions more elegant than iterative

WHEN TO CONVERT TO ITERATION:
------------------------------
- Tail recursion (last operation is recursive call)
- Simple linear recursion (factorial, sum)
- Space-critical applications
- Stack overflow concerns with deep recursion

WHEN TO KEEP RECURSIVE:
-----------------------
- Tree/graph traversal
- Backtracking problems
- Divide and conquer
- Natural recursive structure
- Code clarity more important than performance
"""