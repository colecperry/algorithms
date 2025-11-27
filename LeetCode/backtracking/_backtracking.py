"""
=================================================================
BACKTRACKING COMPLETE GUIDE
=================================================================

WHAT IS BACKTRACKING?
---------------------
Backtracking is a systematic algorithm for finding all (or some) solutions to computational 
problems by incrementally building candidates and abandoning a candidate ("backtracking") as 
soon as it determines the candidate cannot lead to a valid solution.

Key characteristics:
- Explores all possibilities by making choices
- Makes a choice → Explores → Undoes choice (backtracks)
- Recursively builds solution tree
- Prunes invalid branches early (optimization)
- Typically exponential time complexity

When to use Backtracking:
- Need to find ALL solutions (not just one optimal)
- Generate all permutations, combinations, or subsets
- Constraint satisfaction problems (N-Queens, Sudoku)
- Exhaustive search required
- No greedy or DP solution exists

Common backtracking problem types:
- Permutations and combinations
- Subsets and power sets
- Partition problems
- Grid exploration (word search, N-Queens)
- Constraint satisfaction
- Generating all valid structures

BACKTRACKING CORE TEMPLATE
============================
"""

def backtracking_template(n):
    """
    Universal backtracking template demonstrated with a simple problem:
    Generate all binary strings of length n.
    
    Example: n=3 → ["000", "001", "010", "011", "100", "101", "110", "111"]
    
    CORE PRINCIPLE: Make → Explore → Undo
    
    TC: O(2^n) - 2 choices per position, n positions
    SC: O(n) - recursion depth
    """
    result = []  # Stores all complete solutions
    path = []    # Current solution being built
    
    def backtrack(position):
        """
        position: current index we're filling (0 to n-1)
        """
        # BASE CASE: Check if solution is complete
        if position == n:
            result.append(''.join(path))  # Save solution
            return
        
        # RECURSIVE CASE: Try all possible choices at current position
        for choice in ['0', '1']:  # At each position, can choose 0 or 1
            # 1. MAKE CHOICE: Add to current solution
            path.append(choice)
            
            # 2. EXPLORE: Recurse to fill next position
            backtrack(position + 1)
            
            # 3. UNDO CHOICE (BACKTRACK): Remove to try other options
            path.pop()
    
    backtrack(0)  # Start at position 0
    return result

# Test the template
print("Binary strings of length 3:")
print(backtracking_template(3))
# Output: ['000', '001', '010', '011', '100', '101', '110', '111']

print("\nBinary strings of length 2:")
print(backtracking_template(2))
# Output: ['00', '01', '10', '11']

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
- Total auxiliary space: O(n) for recursion + result storage

Why Backtracking is Exponential:
- Explores entire solution space
- Each level adds more branches
- Can't be avoided for "find all solutions" problems
- Pruning helps but doesn't change complexity class

Optimization Techniques:
1. Early termination: Stop when solution found (if only need one)
2. Pruning: Skip branches that can't lead to solution
3. Sort input: Enables duplicate skipping and better pruning
4. Memoization: Cache results if subproblems overlap (becomes DP)
"""

"""
=================================================================
BACKTRACKING PATTERNS
=================================================================
"""

from typing import List

# ================================================================
# PATTERN 1: PERMUTATIONS (ARRANGE ALL ELEMENTS)
# ================================================================
# Use when: Need all arrangements where order matters, use all elements
# Key technique: Track used elements with boolean array
# Time: O(n! * n), Space: O(n)
# ================================================================

class PermutationsPattern:
    """
    Problem: Given array nums of distinct integers, return all possible permutations.
    
    LC 46: Permutations
    
    TC: O(n! * n) - n! permutations, each takes O(n) to build/copy
    SC: O(n) - recursion depth + path + used array
    
    Key insight: Each element can only appear once. Track which elements are 
    already in current path with boolean array.
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(path, used):
            # Base case: permutation complete
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            # Try each element
            for i in range(len(nums)):
                if used[i]:  # Already in current path
                    continue
                
                # Make choice
                path.append(nums[i])
                used[i] = True
                
                # Explore
                backtrack(path, used)
                
                # Undo (backtrack)
                path.pop()
                used[i] = False
        
        backtrack([], [False] * len(nums))
        return result

# Example: [1,2,3] → [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


# ================================================================
# PATTERN 2: COMBINATIONS (CHOOSE K ELEMENTS)
# ================================================================
# Use when: Choose k from n, order doesn't matter
# Key technique: Use start index to avoid duplicates
# Time: O(C(n,k) * k), Space: O(k)
# ================================================================

class CombinationsPattern:
    """
    Problem: Given two integers n and k, return all possible combinations of 
    k numbers chosen from range [1, n].
    
    LC 77: Combinations
    
    TC: O(C(n,k) * k) where C(n,k) = n!/(k!(n-k)!)
    SC: O(k) - recursion depth + path storage
    
    Key insight: Use start index to prevent duplicates. [1,2] and [2,1] are 
    the same combination, so only build [1,2] by always moving forward.
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def backtrack(start, path):
            # Base case: combination complete
            if len(path) == k:
                result.append(path[:])
                return
            
            # Try each element from start to n
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)  # i+1 prevents reuse
                path.pop()
        
        backtrack(1, [])
        return result

# Example: n=4, k=2 → [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]


# ================================================================
# PATTERN 3: SUBSETS (POWER SET)
# ================================================================
# Use when: Need all possible subsets of any size
# Key technique: Save path at EVERY level, not just when complete
# Time: O(2^n * n), Space: O(n)
# ================================================================

class SubsetsPattern:
    """
    Problem: Given integer array nums of unique elements, return all possible 
    subsets (the power set).
    
    LC 78: Subsets
    
    TC: O(2^n * n) - 2^n subsets, each takes O(n) to copy
    SC: O(n) - recursion depth
    
    Key insight: Unlike combinations (save when len=k), save subset at EVERY 
    recursion level. Each element has two choices: include or exclude.
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(start, path):
            # Save current subset (at every level!)
            result.append(path[:])
            
            # Try adding each remaining element
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(0, [])
        return result

# Example: [1,2,3] → [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]


# ================================================================
# PATTERN 4: COMBINATION SUM (TARGET WITH REUSE)
# ================================================================
# Use when: Find combinations that sum to target, can reuse elements
# Key technique: Recurse with same index (not i+1) to allow reuse
# Time: O(2^n), Space: O(target/min)
# ================================================================

class CombinationSumPattern:
    """
    Problem: Given array of distinct integers candidates and target integer, 
    return all unique combinations where chosen numbers sum to target. 
    Same number may be chosen unlimited times.
    
    LC 39: Combination Sum
    
    TC: O(2^n) worst case, pruning helps significantly
    SC: O(target/min) - maximum recursion depth
    
    Key insight: Recurse with i (not i+1) to allow reusing same element. 
    Start index still prevents duplicates: [2,2,3] generated, not [2,3,2].
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()  # Enables pruning
        
        def backtrack(start, path, current_sum):
            # Base case: found valid combination
            if current_sum == target:
                result.append(path[:])
                return
            
            # Pruning: stop if exceeded
            if current_sum > target:
                return
            
            for i in range(start, len(candidates)):
                # Pruning: since sorted, rest will also exceed
                if current_sum + candidates[i] > target:
                    break
                
                path.append(candidates[i])
                # Pass i (not i+1) to allow reuse
                backtrack(i, path, current_sum + candidates[i])
                path.pop()
        
        backtrack(0, [], 0)
        return result

# Example: candidates=[2,3,6,7], target=7 → [[2,2,3],[7]]


# ================================================================
# PATTERN 5: PARTITIONING (SPLIT INTO VALID GROUPS)
# ================================================================
# Use when: Split string/array into groups satisfying constraints
# Key technique: Try all partition endpoints, validate each partition
# Time: O(2^n * n), Space: O(n)
# ================================================================

class PartitioningPattern:
    """
    Problem: Given string s, partition s such that every substring is a 
    palindrome. Return all possible palindrome partitionings.
    
    LC 131: Palindrome Partitioning
    
    TC: O(2^n * n) - 2^n possible partitions, O(n) to check/copy
    SC: O(n) - recursion depth + path storage
    
    Key insight: At each position, try all possible partition cuts. Only 
    proceed if substring is valid (palindrome). Backtrack to try different cuts.
    """
    def partition(self, s: str) -> List[List[str]]:
        result = []
        
        def is_palindrome(string):
            return string == string[::-1]
        
        def backtrack(start, path):
            # Base case: partitioned entire string
            if start == len(s):
                result.append(path[:])
                return
            
            # Try all possible partition endpoints
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                
                # Only proceed if valid palindrome
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end, path)
                    path.pop()
        
        backtrack(0, [])
        return result

# Example: "aab" → [["a","a","b"],["aa","b"]]


# ================================================================
# PATTERN 6: GRID BACKTRACKING (2D EXPLORATION)
# ================================================================
# Use when: Explore 2D grid to find path or pattern
# Key technique: Mark visited, try 4 directions, unmark when backtracking
# Time: O(m*n*4^L), Space: O(L)
# ================================================================

class GridBacktrackingPattern:
    """
    Problem: Given m×n board and word, return true if word exists in grid. 
    Word constructed from sequentially adjacent cells. Same cell can't be used twice.
    
    LC 79: Word Search
    
    TC: O(m*n*4^L) where L=word length
        - Try each cell as start: O(m*n)
        - Explore 4 directions, depth L: O(4^L)
    SC: O(L) - recursion depth
    
    Key insight: Mark cell as visited during exploration, unmark when 
    backtracking. Same cell can be used in different paths, just not same path.
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
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
            
            # Unmark (backtrack)
            board[r][c] = temp
            
            return found
        
        # Try starting from each cell
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False

# Example: board=[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], 
#          word="ABCCED" → True