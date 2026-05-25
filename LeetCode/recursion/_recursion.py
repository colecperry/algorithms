from typing import List, Optional

"""
=================================================================
RECURSION COMPLETE GUIDE
=================================================================

WHAT IS RECURSION?
------------------
Recursion is a programming technique where a function calls itself to solve smaller instances of the same problem. It breaks down complex problems into simpler subproblems until reaching a base case that can be solved directly. The solution is built by combining results from recursive calls as the call stack unwinds.

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

=================================================================
QUICK REFERENCE: RECURSION COMPLEXITY PATTERNS
=================================================================

1. BASIC LINEAR RECURSION
--------------------------
Pattern: Single recursive call, process one at a time
Example: factorial(n) = n x factorial(n-1)

TC: O(n) - n recursive calls
SC: O(n) - call stack depth of n

Examples: Factorial, Sum Array, Reverse Linked List


2. TREE RECURSION (BINARY TREE)
--------------------------------
Pattern: Two recursive calls (left & right children)
Example: maxDepth = 1 + max(left_depth, right_depth)

TC: O(n) - visit each node once
SC: O(h) - call stack depth = tree height
    - Balanced tree: O(log n)
    - Skewed tree: O(n)

Examples: Max Depth, Path Sum, Invert Tree, Same Tree

SPECIAL CASE - Naive Fibonacci:
TC: O(2^n) - exponential branching without memoization
SC: O(n) - max call stack depth


3. DIVIDE AND CONQUER
----------------------
Pattern: Split in half, solve recursively, combine

TC: O(n log n)
    - log n levels (halving each time)
    - O(n) work per level
    
SC: O(log n) for recursion stack
    - Add O(n) if using extra arrays (merge sort)

Examples:
- Merge Sort: O(n log n) time, O(n) space
- Quick Sort: O(n log n) time, O(log n) space
- Binary Search: O(log n) time, O(log n) space


4. BACKTRACKING
---------------
Pattern: Try all possibilities, backtrack when invalid

TC: O(2^n) or O(n!)
    - Subsets: O(2^n) - include/exclude each element
    - Permutations: O(n!) - n choices, then n-1, etc.
    
SC: O(n)
    - Call stack depth = max path length
    - Path storage = O(n)

Examples:
- Subsets: O(2^n) time, O(n) space
- Permutations: O(n!) time, O(n) space
- Combination Sum: O(2^n) time, O(n) space


5. MEMOIZATION (TOP-DOWN DP)
-----------------------------
Pattern: Cache results to avoid recomputation

TC: O(n) to O(n²)
    - Each unique subproblem solved once
    - 1D problems: O(n) subproblems
    - 2D problems: O(n²) subproblems
    
SC: O(n) to O(n²)
    - Memo dictionary size
    - Plus recursion stack

Examples:
- Fibonacci: O(n) time, O(n) space (vs O(2^n) naive)
- Climbing Stairs: O(n) time, O(n) space
- Coin Change: O(n × amount) time, O(n × amount) space


6. HELPER FUNCTION RECURSION
-----------------------------
Pattern: Pass accumulated state through recursion

TC: Same as underlying pattern
    - Usually O(n) for trees or lists
    
SC: Same as underlying + state storage
    - Usually O(h) for trees, O(n) for lists
    - State variables don't usually add much

Examples:
- Reverse Linked List: O(n) time, O(n) space
- Sum Root to Leaf: O(n) time, O(h) space
- Range Sum BST: O(n) time, O(h) space

================================================================
PATTERN 1: BASIC RECURSION (LINEAR/SINGLE BRANCH)
PATTERN EXPLANATION: Single recursive call that progresses linearly toward base case. Each call processes current element and delegates rest to recursive call. Build solution as stack unwinds. Simplest form of recursion, often can be converted to iteration. Used for sequential processing, validation, and simple transformations.

#
Applications: Factorial, sum, reverse, string palindrome, power calculation.
================================================================
"""

class BasicRecursion:
    """
    Problem 1: Calculate n! (n factorial) = n x (n-1) x ... x 2 x 1
    
    Example:
        factorial(5) = 5 x 4 x 3 x 2 x 1 = 120
    
    Steps:
    1. Base case: if n <= 1, return 1 (0! and 1! both equal 1)
    2. Recursive case: return n * factorial(n - 1)
    3. Each call multiplies current n with the result returned by the next call
    4. Stack unwinds multiplying n * (n-1) * ... * 2 * 1 back up to the original call
    """
    def factorial(self, n: int) -> int:
        """
        - TC: O(n) - n recursive calls
        - SC: O(n) - call stack depth
        """
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

sol = BasicRecursion()
print(sol.factorial(5)) # 120

"""
================================================================
PATTERN 2: TREE RECURSION (MULTIPLE BRANCHES)
PATTERN EXPLANATION: Multiple recursive calls from each invocation, creating branching structure like a tree. Each branch explores different possibility or subproblem. Without memoization, can have exponential time complexity. Common in decision problems, tree traversal, and exploring all paths. Solutions combine results from all branches.

#
Applications: Fibonacci, tree traversal, counting paths, decision trees.
================================================================
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeRecursion:
    """
    Find maximum depth of binary tree. 
    
        3
       / \
      9  20
        /  \
       15   7

    Input: root = [3,9,20,null,null,15,7]
    Output: 3

    Steps:
    1. Base case: if root is None, return 0
    2. Recurse left: call maxDepth(root.left) to get left subtree depth
    3. Recurse right: call maxDepth(root.right) to get right subtree depth
    4. Return 1 + max(left_depth, right_depth) — current node adds 1 level
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:  # LC 104
        """
        - TC: O(n) - visit each node once
        - SC: O(h) - recursion depth = tree height
        """
        # Base case: null node has depth 0
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

sol = TreeRecursion()
tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print("Max Depth:", sol.maxDepth(tree))  # 3

"""
================================================================
PATTERN 3: DIVIDE AND CONQUER
PATTERN EXPLANATION: Break problem into independent subproblems, solve recursively, then combine results. Typically divides input in half (binary division). Each level does O(n) work across all subproblems, with O(log n) levels, giving O(n log n) complexity. Used in efficient sorting, searching, and optimization algorithms.

#
Applications: Merge sort, quick sort, binary search, closest pair, maximum subarray.
================================================================
"""

class DivideAndConquer:
    """
    Problem 1: Implement merge sort to sort an array.
    
    Example:
        Input: [38, 27, 43, 3, 9, 82, 10]
        Output: [3, 9, 10, 27, 38, 43, 82]
    
    Steps:
    1. Base case: if len(nums) <= 1, return nums (already sorted)
    2. Divide: find mid = len(nums) // 2, split into left = nums[:mid] and right = nums[mid:]
    3. Conquer: recursively call mergeSort(left) and mergeSort(right)
    4. Combine: call merge(left, right) — walk both sorted halves with two pointers, appending the smaller element each time
    5. Return the merged result up to the caller
    """
    def mergeSort(self, nums: List[int]) -> List[int]:  # LC 912 - Sort an Array
        """
        - TC: O(n log n) - log n levels, O(n) work per level
        - SC: O(n) - temporary arrays for merging
        """
        # Base case: single element is already sorted
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
            if left[i] <= right[j]: # Compare values
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

sol = DivideAndConquer()
print("Merge Sort:", sol.mergeSort([38, 27, 43, 3]))  # [3, 27, 38, 43]

"""
================================================================
PATTERN 4: BACKTRACKING
PATTERN EXPLANATION: Systematically explore all possible solutions by making choices, recursing with each choice, then undoing choice (backtracking) to try alternatives. Build solution incrementally, abandoning paths that violate constraints. Returns to previous state by removing last choice before trying next option. Essential for combinatorial problems and constraint satisfaction.

#
Applications: Permutations, combinations, subsets, N-Queens, Sudoku, word search.
================================================================
"""

class Backtracking:
    """
    Problem 1: Generate all subsets (power set) of given set.
    
    Example:
        Input: [1, 2, 3]
        Output: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
    
    Steps:
    1. Save a copy of the current path into result (every path is a valid subset)
    2. Loop over indices from start to end of nums:
       a. Make choice: append nums[i] to path
       b. Recurse: call backtrack(i + 1, path) to build subsets that include nums[i]
       c. Backtrack: pop nums[i] from path to restore state before trying next element
    3. Return result after all branches are explored
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:  # LC 78
        """
        - TC: O(2^n) - 2^n subsets to generate
        - SC: O(n) - recursion depth (max n levels deep)
        """
        result = []  # Stores all subsets we find
        
        def backtrack(start: int, path: List[int]):
            """
            - Build subsets starting from index 'start'
            - Args:
                start: index to start considering elements from
                path: current subset we're building
            """
            result.append(path[:])  # [:] creates a copy
            
            # Try adding each remaining element
            for i in range(start, len(nums)):
                path.append(nums[i])    # Choose: add nums[i]
                backtrack(i + 1, path)  # Explore: build subsets with nums[i]
                path.pop()              # Undo: remove nums[i] to try next
            backtrack(0, [])

        return result

# EXECUTION TRACE: nums = [1, 2]
# ═══════════════════════════════════════════════════════════

# ┌─ CALL 1: backtrack(start=0, path=[])
# │  ├─ Save [] → result = [[]]
# │  ├─ Loop i from 0 to 1
# │  │
# │  ├─ [i=0] Add nums[0]=1, path becomes [1]
# │  │  │
# │  │  ┌─ CALL 2: backtrack(start=1, path=[1])
# │  │  │  ├─ Save [1] → result = [[], [1]]
# │  │  │  ├─ Loop i from 1 to 1
# │  │  │  │
# │  │  │  ├─ [i=1] Add nums[1]=2, path becomes [1,2]
# │  │  │  │  │
# │  │  │  │  ┌─ CALL 3: backtrack(start=2, path=[1,2])
# │  │  │  │  │  ├─ Save [1,2] → result = [[], [1], [1,2]]
# │  │  │  │  │  ├─ Loop i from 2 to 1 (empty - base case!)
# │  │  │  │  │  └─ RETURN ↩
# │  │  │  │  └─────────────────────────────────────────
# │  │  │  │
# │  │  │  ├─ Pop 2, path becomes [1]
# │  │  │  └─ RETURN ↩
# │  │  └─────────────────────────────────────────────────
# │  │
# │  ├─ Pop 1, path becomes []
# │  │
# │  ├─ [i=1] Add nums[1]=2, path becomes [2]
# │  │  │
# │  │  ┌─ CALL 4: backtrack(start=2, path=[2])
# │  │  │  ├─ Save [2] → result = [[], [1], [1,2], [2]]
# │  │  │  ├─ Loop i from 2 to 1 (empty - base case!)
# │  │  │  └─ RETURN ↩
# │  │  └─────────────────────────────────────────────────
# │  │
# │  ├─ Pop 2, path becomes []
# │  └─ RETURN ↩
# └─────────────────────────────────────────────────────────

# FINAL RESULT: [[], [1], [1,2], [2]]

sol = Backtracking()
print("Subsets:", sol.subsets([1,2,3]))

"""
================================================================
PATTERN 5: RECURSION WITH MEMOIZATION (TOP-DOWN DP)
PATTERN EXPLANATION: Optimize recursive solutions by caching results of subproblems in memo dictionary. Check cache before computing, store result after computing. Converts exponential time to polynomial by ensuring each unique subproblem solved only once. Natural bridge between naive recursion and dynamic programming. Also called top-down DP.

#
Applications: Fibonacci, climbing stairs, coin change, longest common subsequence.
================================================================
"""

class RecursionWithMemo:
    """
    # You are climbing a staircase. It takes n steps to reach the top.

    # Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    # Example 1:
    # Input: n = 2
    # Output: 2
    # Explanation: There are two ways to climb to the top.
    # 1. 1 step + 1 step
    # 2. 2 steps

    # Example 2:
    # Input: n = 3
    # Output: 3
    # Explanation: There are three ways to climb to the top.
    # 1. 1 step + 1 step + 1 step
    # 2. 1 step + 2 steps
    # 3. 2 steps + 1 step
    
    Steps:
    1. Initialize an empty memo dictionary to cache results
    2. Base case: if n <= 2, return n directly (1 way for step 1, 2 ways for step 2)
    3. Cache check: if n is already in memo, return memo[n] immediately
    4. Recurse: compute climb(n - 1) + climb(n - 2) — the two ways to arrive at step n
    5. Store result in memo[n] before returning so future calls skip recomputation
    6. Return memo[n] as the total number of distinct ways to reach step n
    """
    def climbStairs(self, n: int) -> int:  # LC 70
        """
        - TC: O(n) with memo, O(2^n) without
        - SC: O(n) - memo dictionary + recursion stack
        """
        memo = {}  # Dictionary to store already computed results
        
        def climb(n: int) -> int:
            # BASE CASE: For steps 1 and 2, answer equals the step number
            # Step 1: only 1 way (take 1 step)
            # Step 2: only 2 ways (1+1 or 2)
            if n <= 2:
                return n
            
            if n in memo: # CACHE CHECK: Have we solved this subproblem before?
                return memo[n] # If yes, return the saved answer
            
            # RECURSIVE CALCULATION: Ways to reach step n =  
            ways_step_1 = climb(n - 1) # (ways to reach n-1) + 
            ways_step_2 = climb(n - 2) # (ways to reach n-2)
            result = ways_step_1 + ways_step_2 # Why? You can get to step n from either step n-1 or step n-2
            
            memo[n] = result # SAVE TO CACHE: Store result so we don't recalc
            
            return memo[n] # return # of ways to reach step n
        
        return climb(n)

# ═══════════════════════════════════════════════════════════════════
# TRACE: climbStairs(5) WITH MEMOIZATION
# ═══════════════════════════════════════════════════════════════════
# 
# 📝 memo = {} (empty at start)
# 
# ┌─ climb(5)                                    
# │  🔍 Check memo[5]? ❌ NOT FOUND
# │  ➡️  Must calculate: climb(4) + climb(3)
# │
# │  ┌─ climb(4)                                 
# │  │  🔍 Check memo[4]? ❌ NOT FOUND
# │  │  ➡️  Must calculate: climb(3) + climb(2)
# │  │
# │  │  ┌─ climb(3)                              
# │  │  │  🔍 Check memo[3]? ❌ NOT FOUND
# │  │  │  ➡️  Must calculate: climb(2) + climb(1)
# │  │  │
# │  │  │  ├─ climb(2) = 2 ⚡ BASE CASE (n <= 2, return n)
# │  │  │  └─ climb(1) = 1 ⚡ BASE CASE (n <= 2, return n)
# │  │  │
# │  │  │  🧮 Calculate: 2 + 1 = 3
# │  │  │  💾 Store: memo[3] = 3
# │  │  │  ✅ Return 3
# │  │  └─────────────────────────────────────────────────
# │  │                                             memo = {3: 3}
# │  │
# │  │  ├─ climb(2) = 2 ⚡ BASE CASE (n <= 2, return n)
# │  │
# │  │  🧮 Calculate: 3 + 2 = 5
# │  │  💾 Store: memo[4] = 5
# │  │  ✅ Return 5
# │  └─────────────────────────────────────────────────────
# │                                                memo = {3: 3, 4: 5}
# │
# │  ┌─ climb(3)
# │  │  🔍 Check memo[3]? ✨ YES! Found 3
# │  │  💡 No calculation needed - use cached value!
# │  │  ✅ Return 3 (from memo)
# │  └─────────────────────────────────────────────────────
# │                                                memo = {3: 3, 4: 5}
# │
# │  🧮 Calculate: 5 + 3 = 8
# │     └─ 5 from climb(4) (calculated)
# │     └─ 3 from climb(3) (FROM MEMO! ✨)
# │  💾 Store: memo[5] = 8
# │  ✅ Return 8
# └─────────────────────────────────────────────────────────
#                                                  memo = {3: 3, 4: 5, 5: 8}
# 
# 🎯 FINAL ANSWER: 8
# 
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 💡 THE MAGIC MOMENT:
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 
# climb(3) was called TWICE:
#   1st time: ❌ Not in memo → CALCULATED (2 + 1 = 3) → Stored
#   2nd time: ✨ In memo → RETRIEVED (instant return 3) → Saved work!
# 
# Without memoization, climb(3) would recalculate 2 + 1 every time.
# With memoization, we calculate once and reuse the answer.

sol = RecursionWithMemo()
print("Climbing Stairs(5):", sol.climbStairs(5))  # 8

"""
================================================================
PATTERN 6: HELPER FUNCTION RECURSION (ACCUMULATED STATE)
PATTERN EXPLANATION: Use helper function with extra parameters to accumulate state or track progress through recursion. Main function initializes state, helper carries it through recursive calls. Common for problems needing indices, accumulators, or context that main function doesn't have. Cleaner than modifying input or using global variables.

#
Applications: Reverse list, flatten nested list, path collection, range recursion.
================================================================
"""

class HelperRecursion:
    """
    Sum all root-to-leaf numbers.
    
    Example:
        Tree:    1
                / \
               2   3
        
        Paths: 12, 13
        Sum: 12 + 13 = 25
    
    Steps:
    1. Main function calls helper(root, 0) to start traversal with current_num = 0
    2. Base case: if node is None, return 0 (no contribution)
    3. Accumulate: compute current_num = current_num * 10 + node.val to append the digit
    4. Leaf check: if node has no children, return current_num (path is complete)
    5. Recurse: call helper(node.left, current_num) and helper(node.right, current_num)
    6. Return left_sum + right_sum to bubble the total up to the root
    """
    def sumNumbers(self, root):  # LC 129 - Sum Root to Leaf Numbers
        """
        - TC: O(n) - visit each node once
        - SC: O(h) - recursion stack depth = tree height
        """
        def helper(node, current_num):
            """
            Accumulate path number as we traverse.
            - node: current node being visited
            - current_num: accumulated number built so far (0 → 1 → 12)
            """
            # Base case: null node contributes nothing
            if not node:
                return 0
            
            # ACCUMULATE: Build number by appending current digit
            # Example: current_num=1, node.val=2 → 1*10 + 2 = 12
            current_num = current_num * 10 + node.val
            
            # BASE CASE: Leaf node? We've completed a path, return the number
            if not node.left and not node.right:
                return current_num
            
            # RECURSIVE CASE: Internal node? Sum both subtree paths
            # Pass accumulated number to children (they'll build on it)
            left_sum = helper(node.left, current_num)
            right_sum = helper(node.right, current_num)
            return left_sum + right_sum
        
        # Start recursion: root node, number starts at 0
        return helper(root, 0)

# ═══════════════════════════════════════════════════════════════════
# TRACE: sumNumbers(root) - Sum Root to Leaf Numbers
# ═══════════════════════════════════════════════════════════════════
# 
# Tree:       1
#            / \
#           2   3
# 
# Goal: Calculate 12 + 13 = 25
# 
# ┌─ helper(node=1, current_num=0)
# │  🧮 Build number: 0 * 10 + 1 = 1
# │  📍 Not a leaf, explore both children
# │
# │  ┌─ LEFT: helper(node=2, current_num=1)
# │  │  🧮 Build number: 1 * 10 + 2 = 12
# │  │  🍃 LEAF! Return 12
# │  └─ Returns: 12
# │
# │  ┌─ RIGHT: helper(node=3, current_num=1)
# │  │  🧮 Build number: 1 * 10 + 3 = 13
# │  │  🍃 LEAF! Return 13
# │  └─ Returns: 13
# │
# │  ➕ Sum children: 12 + 13 = 25
# │  ✅ Return 25
# └─────────────────────────────────────────────────────────────────
# 
# 🎯 FINAL ANSWER: 25

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

sol = HelperRecursion()

# Test sum numbers
tree = TreeNode(1, TreeNode(2), TreeNode(3))
print("Sum Root to Leaf:", sol.sumNumbers(tree))  # 25
