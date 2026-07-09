"""
=================================================================
RECURSION COMPLETE GUIDE
=================================================================

WHAT IS RECURSION?
------------------
Recursion is a technique where a function calls itself on a smaller version of the same
problem. Every recursive solution needs a base case (the stopping condition) and a
recursive case (the self-referencing call that makes progress toward the base case).

Key characteristics:
- Base case: terminates recursion and returns a known value
- Recursive case: breaks the problem into a smaller subproblem
- Call stack: each call uses memory; deep recursion can cause stack overflow
- Stack unwinding: results are combined as calls return in reverse order

Basic concept:
    solve(problem):
        if base_case:                       # Stop recursion
            return simple_answer
        smaller = solve(shrink(problem))    # Recurse on smaller input
        return combine(smaller, current)    # Combine on the way back up

When to use Recursion:
- Tree or graph traversal (every node leads to subtree of same shape)
- Backtracking (try a choice, recurse, undo)
- Problems with natural self-similar structure (factorial, Fibonacci)
- Dynamic programming top-down (recurse + cache subproblems)

Common Recursion problem types:
- Tree traversal (max depth, path sum, invert tree, same tree)
- Backtracking (subsets, permutations, combinations, N-Queens)
- Memoized recursion (Fibonacci, climbing stairs, coin change)
- Linked list and string recursion

RECURSION CORE PATTERNS
========================
"""

from typing import List, Optional

"""
RECURSION COMPLEXITY REFERENCE
================================

+---------------------------+------------------+------------------+
| Pattern                   | Time             | Space            |
+---------------------------+------------------+------------------+
| Linear Recursion          | O(n)             | O(n) call stack  |
| Tree DFS Recursion        | O(n)             | O(h) call stack  |
| Backtracking (subsets)    | O(2^n)           | O(n) call stack  |
| Backtracking (perms)      | O(n!)            | O(n) call stack  |
| Memoization 1D            | O(n)             | O(n) memo+stack  |
+---------------------------+------------------+------------------+

n = input size, h = tree height (O(log n) balanced, O(n) skewed)

NOTES:
- Linear: one recursive call per invocation -> depth equals input size
- Tree DFS: two calls per node but each node visited once -> O(n) total work
- Backtracking: exponential because we explore all paths (pruning reduces practical cost)
- Memoization: each unique subproblem solved once, transforms O(2^n) -> O(n)
"""

"""
==================
RECURSION PATTERNS
==================
"""

"""
================================================================
PATTERN 1: LINEAR RECURSION (SINGLE CALL, ACCUMULATE ON RETURN)
PATTERN EXPLANATION: Make one recursive call on a strictly smaller input. The result
is built by combining the returned value with the current element as the stack unwinds.
Simplest form of recursion: solve(n-1) + current element = solve(n). The call stack
grows to depth n, then collapses back multiplying at each level.

Applications: Factorial, power, sum array, reverse string, recursive search.
================================================================
"""

class LinearRecursion:
    """
    Problem: Compute n! = n x (n-1) x ... x 2 x 1.

    Example:
        factorial(5) = 120
        factorial(0) = 1

    Steps:
    1. Base case: if n <= 1, return 1  (0! = 1! = 1)
    2. Recursive case: return n * factorial(n - 1)
    3. Each call multiplies its n with the result returned from below
    """
    def factorial(self, n: int) -> int:
        """
        TC: O(n) - n recursive calls
        SC: O(n) - call stack depth
        """
        if n <= 1:
            return 1
        return n * self.factorial(n - 1)

    # Trace: factorial(4)
    # factorial(4) -> 4 * factorial(3)
    #   factorial(3) -> 3 * factorial(2)
    #     factorial(2) -> 2 * factorial(1)
    #       factorial(1) -> 1  (base case)
    #     returns 2 * 1 = 2
    #   returns 3 * 2 = 6
    # returns 4 * 6 = 24

sol = LinearRecursion()
print("Factorial(5):", sol.factorial(5))  # 120


"""
================================================================
PATTERN 2: TREE DFS RECURSION (BINARY BRANCHING)
PATTERN EXPLANATION: Make two recursive calls — one for each subtree. The answer for
the current node is computed by combining the results from both children. Every node
is visited exactly once. Call stack depth equals the tree height (O(log n) balanced,
O(n) skewed). This is the fundamental pattern for all binary tree problems.

Applications: Max depth, path sum, invert tree, same tree, symmetric tree, diameter.
================================================================
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeDFSRecursion:
    """
    Problem: Find the maximum depth of a binary tree (number of nodes along
    the longest path from root to a leaf node).

    Example:
        Tree:    3
                / \\
               9  20
                 /  \\
                15   7

        Output: 3

    Steps:
    1. Base case: if node is None, return 0 (null contributes 0 depth)
    2. Recurse on both subtrees to get their depths
    3. Return 1 + max(left_depth, right_depth) — current node adds 1 level
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:  # LC 104
        """
        TC: O(n) - visit each node once
        SC: O(h) - call stack depth equals tree height
        """
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)

    # Trace: tree = [3, 9, 20, null, null, 15, 7]
    # maxDepth(3):
    #   left = maxDepth(9):
    #     left = maxDepth(None) = 0
    #     right = maxDepth(None) = 0
    #     return 1 + max(0, 0) = 1
    #   right = maxDepth(20):
    #     left = maxDepth(15) = 1
    #     right = maxDepth(7)  = 1
    #     return 1 + max(1, 1) = 2
    #   return 1 + max(1, 2) = 3 ✓

sol = TreeDFSRecursion()
tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print("Max Depth:", sol.maxDepth(tree))  # 3


"""
================================================================
PATTERN 3: BACKTRACKING (TRY -> RECURSE -> UNDO)
PATTERN EXPLANATION: Systematically explore all possibilities by making a choice,
recursing with that choice, then undoing it (backtracking) before trying the next.
The key operations are: choose (append), explore (recurse), unchoose (pop).
Every valid state is captured by appending a copy to results before recursing further.

Applications: Subsets, permutations, combinations, N-Queens, word search, Sudoku.
================================================================
"""

class Backtracking:
    """
    Problem: Given an integer array nums of unique elements, return all possible subsets
    (the power set). The solution set must not contain duplicate subsets.

    Example:
        Input: [1, 2, 3]
        Output: [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]

    Steps:
    1. At each call, snapshot the current path as a valid subset (every prefix is valid)
    2. Loop from `start` to end — each iteration picks the next element to include
    3. Choose: append nums[i] to path
    4. Explore: recurse with start=i+1 (no reuse, no duplicate subsets)
    5. Unchoose: pop nums[i] from path (restore state before next iteration)
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:  # LC 78
        """
        TC: O(2^n) - 2^n subsets, each costs O(n) to copy
        SC: O(n) - recursion depth at most n levels
        """
        result = []

        def backtrack(start: int, path: List[int]):
            result.append(path[:])         # Snapshot current subset
            for i in range(start, len(nums)):
                path.append(nums[i])       # Choose
                backtrack(i + 1, path)     # Explore
                path.pop()                 # Unchoose

        backtrack(0, [])
        return result

    # Trace: nums = [1, 2]
    # backtrack(0, []):
    #   save [] -> result=[[]]
    #   i=0: path=[1] -> backtrack(1,[1]):
    #     save [1] -> result=[[],[1]]
    #     i=1: path=[1,2] -> backtrack(2,[1,2]):
    #       save [1,2] -> result=[[],[1],[1,2]]
    #     path=[1] (pop 2)
    #   path=[] (pop 1)
    #   i=1: path=[2] -> backtrack(2,[2]):
    #     save [2] -> result=[[],[1],[1,2],[2]]
    #   path=[] (pop 2)
    # Output: [[],[1],[1,2],[2]] ✓

sol = Backtracking()
print("Subsets:", sol.subsets([1, 2, 3]))


"""
================================================================
PATTERN 4: MEMOIZATION (TOP-DOWN DYNAMIC PROGRAMMING)
PATTERN EXPLANATION: Cache recursive results to avoid recomputing the same subproblem.
Before computing, check the cache (memo dict). After computing, store the result.
This transforms exponential recursion (where subproblems overlap) into linear time —
each unique subproblem is solved exactly once. The key question: "have I solved this
exact subproblem before?"

Applications: Fibonacci, climbing stairs, coin change, longest common subsequence.
================================================================
"""

class MemoRecursion:
    """
    Problem: You are climbing a staircase with n steps. Each time you can climb
    1 or 2 steps. In how many distinct ways can you reach the top?

    Example:
        climbStairs(3) = 3
        Paths: [1,1,1], [1,2], [2,1]

    Steps:
    1. Base case: n <= 2 -> return n  (1 way for 1 step, 2 ways for 2 steps)
    2. Cache check: if n already in memo, return immediately
    3. Compute: ways(n) = ways(n-1) + ways(n-2) — arrive from step below or 2 below
    4. Store result in memo before returning
    """
    def climbStairs(self, n: int) -> int:  # LC 70
        """
        TC: O(n) - each of n subproblems solved once (vs O(2^n) naive)
        SC: O(n) - memo dict + call stack
        """
        memo = {}

        def climb(n: int) -> int:
            if n <= 2:
                return n
            if n in memo:
                return memo[n]
            memo[n] = climb(n - 1) + climb(n - 2)
            return memo[n]

        return climb(n)

    # Trace: climbStairs(5), memo={}
    # climb(5): not in memo -> climb(4) + climb(3)
    #   climb(4): not in memo -> climb(3) + climb(2)
    #     climb(3): not in memo -> climb(2)+climb(1) = 2+1 = 3 -> memo[3]=3
    #     climb(2): base case -> 2
    #   memo[4] = 3+2 = 5
    #   climb(3): IN MEMO -> return 3 instantly ✓
    # memo[5] = 5+3 = 8
    # Output: 8

sol = MemoRecursion()
print("Climb Stairs(5):", sol.climbStairs(5))  # 8
print("Climb Stairs(3):", sol.climbStairs(3))  # 3
