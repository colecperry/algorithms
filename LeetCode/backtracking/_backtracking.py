"""
=================================================================
BACKTRACKING COMPLETE GUIDE
=================================================================

WHAT IS BACKTRACKING?
---------------------
Backtracking is a systematic algorithm for finding all (or some) solutions to computational
problems by incrementally building candidates and abandoning a candidate ("backtracking")
as soon as it determines the candidate cannot lead to a valid solution.

Key characteristics:
- Explores all possibilities by making choices
- Makes a choice → Explores → Undoes choice (backtracks)
- Recursively builds solution tree
- Prunes invalid branches early (optimization)
- Typically exponential time complexity

Think of it as:
- Exploring a maze: try a path, if dead end, go back and try another
- Making decisions: choose option, if doesn't work, undo and try different option
- DFS with explicit undo step

Backtracking vs Other Approaches:
- Backtracking: Explores all possibilities, exponential time
- Greedy: Makes one choice, never backtracks, polynomial time
- Dynamic Programming: Memoizes overlapping subproblems, polynomial time
- Brute Force: Generates all solutions then filters (less efficient)

When to use Backtracking:
- Need to find ALL solutions (not just one optimal)
- Generate all permutations, combinations, or subsets
- Constraint satisfaction problems (N-Queens, Sudoku)
- Exhaustive search required
- No greedy or DP solution exists

When NOT to use Backtracking:
- Only need one optimal solution (try greedy or DP first)
- Problem has optimal substructure (use DP)
- Exponential time is unacceptable
- Simple iterative solution exists

Common backtracking problem types:
- Permutations and combinations
- Subsets and power sets
- Partition problems
- Grid exploration (word search, N-Queens)
- Constraint satisfaction
- Generating all valid structures

BACKTRACKING CORE TEMPLATES
============================
"""

from typing import List

# ================================================================
# BASIC BACKTRACKING TEMPLATE
# ================================================================
def backtrack_template(choices, path, result):
    """
    Basic backtracking template
    
    TC: O(b^d) where b = branching factor, d = depth
    SC: O(d) for recursion stack + path
    
    CORE PATTERN:
    1. Base case: if path is complete, save it
    2. For each choice:
       - Make choice (add to path)
       - Recurse (explore with this choice)
       - Unmake choice (backtrack - remove from path)
    
    KEY PRINCIPLE: Make → Explore → Undo
    """
    # Base case: complete solution
    if is_complete(path):
        result.append(path[:])  # Must copy path!
        return
    
    # Try each choice
    for choice in get_choices():
        # Make choice
        path.append(choice)
        
        # Explore with this choice
        backtrack_template(choices, path, result)
        
        # Undo choice (backtrack)
        path.pop()
    
    return result

# ================================================================
# PERMUTATIONS TEMPLATE (ORDER MATTERS, USE ALL)
# ================================================================
def permutations_template(nums):
    """
    Template for generating permutations
    
    TC: O(n! * n) - n! permutations, O(n) to copy each
    SC: O(n) - recursion depth + path storage
    
    WHEN TO USE:
    - Generate all arrangements
    - Order matters
    - Use each element exactly once
    
    KEY TECHNIQUE:
    - Track which elements already used
    - Skip used elements
    - All permutations have same length
    """
    result = []
    
    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue
            
            # Make choice
            path.append(nums[i])
            used[i] = True
            
            # Explore
            backtrack(path, used)
            
            # Undo
            path.pop()
            used[i] = False
    
    backtrack([], [False] * len(nums))
    return result

# ================================================================
# COMBINATIONS TEMPLATE (ORDER DOESN'T MATTER, CHOOSE K)
# ================================================================
def combinations_template(n, k):
    """
    Template for generating combinations
    
    TC: O(C(n,k) * k) - C(n,k) combinations, copy each takes k
    SC: O(k) - recursion depth + path
    
    WHEN TO USE:
    - Choose k elements from n
    - Order doesn't matter
    - No duplicates in result
    
    KEY TECHNIQUE:
    - Use start index to avoid duplicates
    - Only consider elements after current
    - Path length is fixed (k)
    """
    result = []
    
    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        
        for i in range(start, n + 1):
            # Make choice
            path.append(i)
            
            # Explore (start from i+1 to avoid reusing)
            backtrack(i + 1, path)
            
            # Undo
            path.pop()
    
    backtrack(1, [])
    return result

# ================================================================
# SUBSETS TEMPLATE (ALL POSSIBLE SUBSETS)
# ================================================================
def subsets_template(nums):
    """
    Template for generating subsets (power set)
    
    TC: O(2^n * n) - 2^n subsets, O(n) to copy each
    SC: O(n) - recursion depth
    
    WHEN TO USE:
    - Generate all possible subsets
    - Include all sizes (0 to n)
    - Order doesn't matter
    
    KEY TECHNIQUE:
    - Include/exclude decision for each element
    - Use start index
    - Save at every recursion level (not just leaves)
    """
    result = []
    
    def backtrack(start, path):
        # Save current subset (not just when complete)
        result.append(path[:])
        
        for i in range(start, len(nums)):
            # Include nums[i]
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(0, [])
    return result

"""
COMPLEXITY QUICK REFERENCE
==========================

Backtracking Time Complexity:
- Permutations: O(n!) - n choices, then n-1, then n-2, etc.
- Combinations: O(C(n,k)) = O(n!/(k!(n-k)!))
- Subsets: O(2^n) - include/exclude each element
- Combination Sum: O(2^n) to O(n^target) depending on constraints
- Partitioning: O(2^n) - try all ways to partition

Space Complexity:
- Recursion stack: O(depth) typically O(n)
- Path storage: O(depth) typically O(n)
- Result storage: depends on number of solutions
- Total auxiliary space: O(n) for recursion + result storage

Why Backtracking is Slow:
- Explores entire solution space
- Exponential growth: 2^n or n!
- Can't be avoided for "find all solutions" problems
- Pruning helps but doesn't change complexity class

Optimization Techniques:
1. Early termination: Stop when solution found (if only need one)
2. Pruning: Skip branches that can't lead to solution
3. Sort input: Enables duplicate skipping
4. Memoization: Cache results if subproblems overlap (becomes DP)

Common Time Complexities:
Pattern                  | Time Complexity  | Space Complexity
-------------------------|------------------|------------------
Permutations             | O(n!)           | O(n)
Combinations             | O(C(n,k))       | O(k)
Subsets                  | O(2^n)          | O(n)
Combination Sum          | O(2^n)          | O(target/min)
Partitioning             | O(2^n * n)      | O(n)
Grid Backtracking        | O(4^L)          | O(L)

Where:
- n = input size
- k = subset size
- L = word length or path length
- target = target sum value

Pattern Space Analysis:
- All patterns: O(n) recursion depth
- Permutations: need used array O(n)
- Result storage varies: O(n!) to O(2^n) solutions

When to Use Each Pattern:
1. Permutations: Arrange all elements, order matters
2. Combinations: Choose k from n, order doesn't matter
3. Subsets: All possible subsets, any size
4. Combination Sum: Find subsets that sum to target
5. Partitioning: Split into valid groups
6. Grid Backtracking: Explore 2D space with constraints
"""

"""
BACKTRACKING PATTERNS
=====================
"""

# ================================================================
# PATTERN 1: PERMUTATIONS (ARRANGE ALL ELEMENTS)
# PATTERN EXPLANATION: Generate all possible arrangements of elements where order matters.
# Use all elements exactly once. Track which elements are already used with boolean array
# or set. For each position, try all unused elements, recurse, then mark as unused (backtrack).
# Base case: when path length equals input length.
#
# TYPICAL STEPS:
# 1. Create used array to track which elements in current path
# 2. Base case: if len(path) == len(nums), save permutation
# 3. For each element in nums:
#    - If already used, skip
#    - Mark as used, add to path
#    - Recurse to fill next position
#    - Unmark as used, remove from path (backtrack)
# 4. Return all permutations
#
# Applications: Generate permutations, arrange elements, ordering problems.
# ================================================================

class PermutationsPattern:
    """
    Problem: Given array nums of distinct integers, return all possible permutations.
    Can return answer in any order.
    
    TC: O(n! * n) - n! permutations, each takes O(n) to build/copy
    SC: O(n) - recursion depth + path + used array
    
    How it works:
    1. For each position in permutation, try every unused element
    2. Track used elements with boolean array
    3. When permutation complete (length = n), save it
    4. Backtrack by unmarking element and removing from path
    5. Try next element for this position
    
    Why we need 'used' array:
    - Each element can only appear once in permutation
    - Must track what's already in current path
    - Can't use index-based approach (like combinations)
    """
    def permute(self, nums: List[int]) -> List[List[int]]: # LC 46
        result = []
        
        def backtrack(path, used):
            # Base case: permutation complete
            if len(path) == len(nums):
                result.append(path[:])  # Must copy!
                return
            
            # Try each element
            for i in range(len(nums)):
                if used[i]:  # Already in current path
                    continue
                
                # Make choice
                path.append(nums[i])
                used[i] = True
                
                # Explore with this choice
                backtrack(path, used)
                
                # Undo choice (backtrack)
                path.pop()
                used[i] = False
        
        backtrack([], [False] * len(nums))
        return result

# Example:
# nums = [1,2,3]
#
# Backtracking tree:
#                    []
#         /          |          \
#       [1]         [2]         [3]
#      /   \       /   \       /   \
#    [1,2][1,3] [2,1][2,3]  [3,1][3,2]
#      |    |     |    |      |    |
#   [1,2,3][1,3,2][2,1,3][2,3,1][3,1,2][3,2,1]
#
# All leaves are complete permutations (6 total = 3!)
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

sol = PermutationsPattern()
print("Permutations:", sol.permute([1,2,3]))
# [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


# ================================================================
# PATTERN 2: COMBINATIONS (CHOOSE K ELEMENTS)
# PATTERN EXPLANATION: Generate all ways to choose k elements from n elements where order
# doesn't matter. Use start index to avoid duplicates - only consider elements at or after
# current position. Unlike permutations, [1,2] and [2,1] are the same combination. Base case:
# when path length equals k.
#
# TYPICAL STEPS:
# 1. Define target size k
# 2. Base case: if len(path) == k, save combination
# 3. For each element from start index to end:
#    - Add element to path
#    - Recurse with start = i + 1 (avoid reusing same element)
#    - Remove element from path (backtrack)
# 4. Return all combinations
#
# Applications: Choose k from n, lottery numbers, team selection, subset of fixed size.
# ================================================================

class CombinationsPattern:
    """
    Problem: Given two integers n and k, return all possible combinations of k numbers
    chosen from range [1, n].
    
    TC: O(C(n,k) * k) where C(n,k) = n!/(k!(n-k)!)
        - Number of combinations: C(n,k)
        - Copy each combination: O(k)
    SC: O(k) - recursion depth + path storage
    
    How it works:
    1. Build combinations by choosing k elements from [1,n]
    2. Use start index to avoid duplicates
    3. Only consider elements >= start (no going backward)
    4. When path length = k, found valid combination
    5. Backtrack to try different choices
    
    Why start index prevents duplicates:
    - [1,2] and [2,1] are same combination
    - By only going forward (start+1), we build [1,2] but never [2,1]
    - Ensures each combination generated exactly once
    """
    def combine(self, n: int, k: int) -> List[List[int]]: # LC 77
        result = []
        
        def backtrack(start, path):
            # Base case: combination complete
            if len(path) == k:
                result.append(path[:])
                return
            
            # Try each element from start to n
            for i in range(start, n + 1):
                # Make choice
                path.append(i)
                
                # Explore (start from i+1 to avoid duplicates)
                backtrack(i + 1, path)
                
                # Undo choice
                path.pop()
        
        backtrack(1, [])
        return result

# Example:
# n = 4, k = 2 (choose 2 from [1,2,3,4])
#
# Backtracking tree:
#                    []
#         /      /      \      \
#       [1]    [2]     [3]    [4]
#      / | \    | \     |
#   [1,2][1,3][1,4][2,3][2,4][3,4]
#
# All paths to leaves are combinations
# Note: [2,1] never generated (start index prevents it)
#
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

sol = CombinationsPattern()
print("Combinations:", sol.combine(4, 2))
# [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]


# ================================================================
# PATTERN 3: SUBSETS (POWER SET)
# PATTERN EXPLANATION: Generate all possible subsets of a set, including empty set and
# full set. Unlike combinations (fixed size k), generate subsets of ALL sizes from 0 to n.
# Key difference: save path at EVERY recursion level, not just when complete. Each element
# has two choices: include or exclude.
#
# TYPICAL STEPS:
# 1. Base case: save current subset (at every level!)
# 2. For each element from start index to end:
#    - Include element in subset
#    - Recurse with start = i + 1
#    - Exclude element (backtrack by removing)
# 3. Return all subsets (2^n total)
#
# Applications: Power set, all subsets, subset generation, toggle combinations.
# ================================================================

class SubsetsPattern:
    """
    Problem: Given integer array nums of unique elements, return all possible subsets
    (the power set). Solution set must not contain duplicate subsets.
    
    TC: O(2^n * n) - 2^n subsets, each takes O(n) to copy
    SC: O(n) - recursion depth
    
    How it works:
    1. For each element, two choices: include or exclude
    2. Save subset at EVERY level (not just leaves)
    3. Use start index to maintain order and avoid duplicates
    4. Tree has 2^n leaf nodes (all possible include/exclude combinations)
    
    Key difference from combinations:
    - Combinations: save only when len(path) == k
    - Subsets: save at every level (all sizes from 0 to n)
    """
    def subsets(self, nums: List[int]) -> List[List[int]]: # LC 78
        result = []
        
        def backtrack(start, path):
            # Save current subset (at every level!)
            result.append(path[:])
            
            # Try adding each remaining element
            for i in range(start, len(nums)):
                # Include nums[i]
                path.append(nums[i])
                
                # Explore with nums[i] included
                backtrack(i + 1, path)
                
                # Exclude nums[i] (backtrack)
                path.pop()
        
        backtrack(0, [])
        return result

# Example:
# nums = [1,2,3]
#
# Backtracking tree (save at EVERY node):
#                      []
#              /        |        \
#           [1]        [2]       [3]
#          /   \        |
#       [1,2] [1,3]   [2,3]
#         |
#      [1,2,3]
#
# All nodes (including root) are saved:
# [], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]
#
# Total: 2^3 = 8 subsets
# Output: [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]

sol = SubsetsPattern()
print("Subsets:", sol.subsets([1,2,3]))
# [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]


# ================================================================
# PATTERN 4: COMBINATION SUM (TARGET WITH REUSE)
# PATTERN EXPLANATION: Find all combinations that sum to target. Can reuse elements
# unlimited times (unbounded knapsack). Use start index to avoid duplicate combinations.
# Prune branches early when sum exceeds target. Unlike standard combinations, same element
# can appear multiple times in one combination.
#
# TYPICAL STEPS:
# 1. Sort array (enables pruning and easier duplicate handling)
# 2. Base case: if sum == target, save combination
# 3. For each element from start index:
#    - If adding element exceeds target, prune (stop exploring)
#    - Add element to path, add to sum
#    - Recurse with same start index (can reuse element)
#    - Remove element, subtract from sum (backtrack)
# 4. Return all valid combinations
#
# Applications: Coin change variations, combination sum, target sum with reuse.
# ================================================================

class CombinationSumPattern:
    """
    Problem: Given array of distinct integers candidates and target integer, return list
    of all unique combinations of candidates where chosen numbers sum to target.
    Same number may be chosen unlimited times.
    
    TC: O(2^n) in worst case, but pruning helps significantly
    SC: O(target/min) - maximum recursion depth
    
    How it works:
    1. For each element, can include it multiple times
    2. Use start index to avoid duplicate combinations
    3. Pass same start to allow reusing current element
    4. Prune when sum exceeds target (no point continuing)
    5. Save when sum exactly equals target
    
    Why we can reuse elements:
    - Same element allowed multiple times in one combination
    - Recurse with i (not i+1) to allow picking same element again
    - Start index still prevents duplicates: [2,2,3] generated, not [2,3,2]
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]: # LC 39
        result = []
        candidates.sort()  # Sort for pruning optimization
        
        def backtrack(start, path, current_sum):
            # Base case: found valid combination
            if current_sum == target:
                result.append(path[:])
                return
            
            # Pruning: if sum exceeds target, stop
            if current_sum > target:
                return
            
            for i in range(start, len(candidates)):
                # Pruning: since sorted, all remaining will also exceed
                if current_sum + candidates[i] > target:
                    break
                
                # Make choice
                path.append(candidates[i])
                
                # Explore (can reuse same element, so pass i not i+1)
                backtrack(i, path, current_sum + candidates[i])
                
                # Undo choice
                path.pop()
        
        backtrack(0, [], 0)
        return result

# Example:
# candidates = [2,3,6,7], target = 7
#
# Backtracking tree (pruned):
#                    []
#         /      /      |      \
#       [2]    [3]    [6]    [7] ← sum=7, save!
#      / | \    |
#   [2,2][2,3][2,6] [3,3]
#    |    |          |
# [2,2,2][2,2,3]  [3,3,3] (exceeds 7, prune)
#    |      ↓
# [2,2,2,2] sum=7, save!
#   ...
#
# Valid combinations:
# [2,2,3] → 2+2+3=7 ✓
# [7] → 7=7 ✓
#
# Output: [[2,2,3],[7]]
# Note: Can reuse 2 multiple times in one combination

sol = CombinationSumPattern()
print("Combination sum:", sol.combinationSum([2,3,6,7], 7))
# [[2,2,3],[7]]
print("Combination sum:", sol.combinationSum([2,3,5], 8))
# [[2,2,2,2],[2,3,3],[3,5]]


# ================================================================
# PATTERN 5: PARTITIONING (SPLIT INTO VALID GROUPS)
# PATTERN EXPLANATION: Split string or array into groups where each group satisfies a
# condition. For each position, try all possible ways to partition from current position.
# Check if each partition is valid before recursing. Collect all valid complete partitionings.
#
# TYPICAL STEPS:
# 1. For current position, try all possible partition endpoints
# 2. Check if substring/subarray from start to end is valid
# 3. If valid:
#    - Add to current partition
#    - Recurse from end+1 position
#    - Remove from partition (backtrack)
# 4. Base case: when reach end of string/array, save partition
# 5. Return all valid partitionings
#
# Applications: Palindrome partitioning, word break, split array, decode ways.
# ================================================================

class PartitioningPattern:
    """
    Problem: Given string s, partition s such that every substring is a palindrome.
    Return all possible palindrome partitioning.
    
    TC: O(2^n * n) - 2^n possible partitions, O(n) to check palindrome and copy
    SC: O(n) - recursion depth + path storage
    
    How it works:
    1. At each position, try all possible partition cuts
    2. Check if substring from start to cut is palindrome
    3. If valid palindrome:
       - Add to current partition
       - Recurse from cut+1 position
       - Backtrack by removing substring
    4. When reach end, found valid complete partitioning
    
    Why backtracking:
    - Many ways to partition same string
    - Need to try all possibilities
    - Each partition decision affects future possibilities
    """
    def partition(self, s: str) -> List[List[str]]: # LC 131
        result = []
        
        def is_palindrome(string):
            """Helper to check if string is palindrome"""
            return string == string[::-1]
        
        def backtrack(start, path):
            # Base case: partitioned entire string
            if start == len(s):
                result.append(path[:])
                return
            
            # Try all possible partition endpoints
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                
                # Only proceed if this partition is valid (palindrome)
                if is_palindrome(substring):
                    # Make choice
                    path.append(substring)
                    
                    # Explore from end of this partition
                    backtrack(end, path)
                    
                    # Undo choice
                    path.pop()
        
        backtrack(0, [])
        return result

# Example:
# s = "aab"
#
# Backtracking tree:
#                    []
#              /      |      \
#           ["a"]   ["aa"]  ["aab"]✗ (not palindrome)
#          /   \      |
#      ["a","a"]["a","ab"]✗ ["aa","b"]
#         |
#    ["a","a","b"]
#
# Valid complete partitions:
# ["a","a","b"] - all palindromes ✓
# ["aa","b"] - all palindromes ✓
#
# Output: [["a","a","b"],["aa","b"]]

sol = PartitioningPattern()
print("Palindrome partitions:", sol.partition("aab"))
# [["a","a","b"],["aa","b"]]
print("Palindrome partitions:", sol.partition("a"))
# [["a"]]


# ================================================================
# PATTERN 6: GRID BACKTRACKING (2D EXPLORATION)
# PATTERN EXPLANATION: Explore 2D grid to find path or pattern. Mark cells as visited
# during exploration, unmark when backtracking. Try all 4 directions from each cell.
# Combines DFS with backtracking - explore path, if fails backtrack and try different path.
#
# TYPICAL STEPS:
# 1. For each cell in grid (or starting cell):
#    - Check boundary conditions and constraints
#    - Mark cell as visited
#    - Try all 4 directions recursively
#    - Unmark cell (backtrack) to try other paths
# 2. Base case: when target found or path complete
# 3. Return true if any path succeeds
#
# Applications: Word search, N-Queens, robot paths, sudoku, maze solving.
# ================================================================

class GridBacktrackingPattern:
    """
    Problem: Given m×n board and word, return true if word exists in grid. Word can be
    constructed from sequentially adjacent cells (horizontal or vertical). Same cell
    cannot be used twice.
    
    TC: O(m * n * 4^L) where L = word length
        - Try starting from each cell: O(m*n)
        - From each cell, explore 4 directions recursively
        - Maximum depth L, branching factor 4
        - Worst case: O(m*n*4^L)
    SC: O(L) - recursion depth equals word length
    
    How it works:
    1. Try starting word search from every cell
    2. For each cell, check if current character matches
    3. If match: mark visited, try all 4 directions for next character
    4. If found complete word: return true
    5. If dead end: unmark cell (backtrack) and try different direction
    
    Why backtracking:
    - Must try all possible paths
    - Same cell can't be used twice in same path
    - But same cell CAN be used in different paths
    - Mark/unmark enables trying all possibilities
    """
    def exist(self, board: List[List[str]], word: str) -> bool: # LC 79
        rows, cols = len(board), len(board[0])
        
        def backtrack(r, c, index):
            # Base case: matched entire word
            if index == len(word):
                return True
            
            # Boundary check and constraints
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                board[r][c] != word[index] or board[r][c] == '#'):
                return False
            
            # Mark as visited
            temp = board[r][c]
            board[r][c] = '#'
            
            # Try all 4 directions
            found = (backtrack(r + 1, c, index + 1) or
                    backtrack(r - 1, c, index + 1) or
                    backtrack(r, c + 1, index + 1) or
                    backtrack(r, c - 1, index + 1))
            
            # Unmark (backtrack) - restore original value
            board[r][c] = temp
            
            return found
        
        # Try starting from each cell
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        
        return False

# Example:
# board = [['A','B','C','E'],
#          ['S','F','C','S'],
#          ['A','D','E','E']]
# word = "ABCCED"
#
# Start at (0,0) 'A':
# Path: A → B → C → C → E → D
# (0,0)→(0,1)→(0,2)→(1,2)→(2,2)→(2,1)
#
# Mark visited as we go:
# ['#','#','#','E']
# ['S','F','#','S']  
# ['A','#','#','E']
#
# Found complete word!
# Backtrack and restore board
#
# Output: True

sol = GridBacktrackingPattern()
board = [['A','B','C','E'],
         ['S','F','C','S'],
         ['A','D','E','E']]
print("Word exists:", sol.exist(board, "ABCCED"))  # True
print("Word exists:", sol.exist(board, "SEE"))  # True
print("Word exists:", sol.exist(board, "ABCB"))  # False
