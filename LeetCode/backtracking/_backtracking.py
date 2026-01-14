"""
=========================================================================
BACKTRACKING COMPLETE GUIDE
=========================================================================

WHAT IS BACKTRACKING?
---------------------
Backtracking is a systematic algorithm for finding all (or some) solutions to computational problems by incrementally building candidates and abandoning a candidate ("backtracking") as soon as it determines the candidate cannot lead to a valid solution.

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

======================================================================
                   BACKTRACKING VS BRUTE FORCE
======================================================================
Backtracking is "intelligent brute force" - it explores all possibilities but prunes invalid branches early.

┌─────────────────────────────────────────────────────────────────────┐
│ BRUTE FORCE: Generate everything, then filter                       │
│ BACKTRACKING: Build incrementally, abandon invalid paths early      │
└─────────────────────────────────────────────────────────────────────┘

Example: Generate all 3-digit numbers where digits are in increasing order

BRUTE FORCE APPROACH:
- Generate all 1000 numbers (000-999) ← O(10^n) = O(1000) numbers
- For EACH number, check if digits increase ← O(n) = O(3) per number
- TC: O(10^n * n) = O(1000 * 3) to generate and check

BACKTRACKING APPROACH:
- At position 0: try digits 0-9 (10 choices)
- At position 1: try only digits >= previous (prunes invalid)
- At position 2: try only digits >= previous (prunes invalid)

For n=3, this generates roughly 220 valid candidates
(compared to brute force checking all 1000)

┌─────────────────────────────────────────────────────────────────────┐
│ KEY DIFFERENCES                                                     │
├─────────────────────────────────────────────────────────────────────┤
│ BRUTE FORCE          │ BACKTRACKING                                 │
├──────────────────────┼──────────────────────────────────────────────┤
│ Generate all         │ Build incrementally                          │
│ Check validity later │ Check validity during construction           │
│ Wastes memory        │ Memory efficient (reuse path)                │
│ No pruning           │ Abandons invalid paths early                 │
│ Often O(k^n) worse   │ Still exponential but prunes aggressively    │
└─────────────────────────────────────────────────────────────────────┘

CONCRETE EXAMPLES:

Example 1: Subsets of [1,2,3]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Brute Force:
  1. Generate ALL possible sequences: [1,1,1], [1,1,2], [1,1,3], ...
     → Creates 2^n x 2^n = 8 x 8 = 64 sequences
  2. Filter out invalid ones (duplicates, wrong order)
  TC: O(2^n x 2^n) = O(64) - wasteful!

Backtracking:
  1. Build subsets step-by-step: [], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]
     → Each decision: "include this element or skip it?"
     → Only creates valid subsets (no filtering needed)
  TC: O(2^n) = O(8) - each element has 2 choices
  
💡 Win: Backtracking is 8x more efficient (no wasted generation)


Example 2: N-Queens on 8x8 Board
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Brute Force:
  1. Choose 8 squares from 64 total squares
     → C(64,8) = 4,426,165,368 (~4.4 billion combinations)
  2. Check each: "Do any queens attack each other?"
  TC: O(billions) - checks almost everything

Backtracking:
  1. Place queens row-by-row (1 per row)
     → Row 1: try 8 columns
     → Row 2: only try columns that don't conflict with Row 1
     → Row 3: only try columns safe from Rows 1 & 2
     → Most branches die early!
  TC: O(n!) = O(40,320) - huge pruning effect
  
💡 Win: Backtracking is 100,000x faster by abandoning bad paths early


Example 3: Permutations of [1,2,3,4]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Brute Force:
  1. Generate all possible 4-digit sequences using digits 1-4
     → [1,1,1,1], [1,1,1,2], ..., [4,4,4,4]
     → 4^4 = 256 total sequences
  2. Filter for valid permutations (each digit used exactly once)
     → Only 24 are valid: [1,2,3,4], [1,2,4,3], ..., [4,3,2,1]
  TC: O(n^n) = O(256) - generates 232 invalid sequences

Backtracking:
  1. Build permutations one position at a time
     → Position 1: choose from [1,2,3,4] (4 choices)
     → Position 2: choose from remaining 3 numbers
     → Position 3: choose from remaining 2 numbers
     → Position 4: only 1 number left
  TC: O(n!) = O(24) - only builds valid permutations
  
💡 Win: Backtracking is 10x more efficient (no invalid sequences created)

COMPLEXITY SUMMARY:
┌─────────────────────────────────────────────────────────────────────┐
│ Problem          │ Brute Force TC    │ Backtracking TC              │
├──────────────────┼───────────────────┼──────────────────────────────┤
│ Subsets          │ O(2^n * 2^n)      │ O(2^n)                       │
│ Permutations     │ O(n^n)            │ O(n!)                        │
│ Combinations     │ O(2^n * n)        │ O(C(n,k))                    │
│ N-Queens         │ O(C(n^2,n) * n)   │ O(n!)                        │
│ Sudoku 9x9       │ O(9^81)           │ O(9^m) m=empty cells         │
└─────────────────────────────────────────────────────────────────────┘

Space Complexity:
- Brute Force: O(total_solutions) - stores everything before filtering
- Backtracking: O(depth) - only stores current path during exploration

WHEN BACKTRACKING DOESN'T HELP:
- If pruning opportunities are minimal (still explore most branches)
- If there are better algorithms (DP, Greedy) for the problem
- If only need one solution and it's early in search tree

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
            return # return to prev callstack
        
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

# ═══════════════════════════════════════════════════════════════════
# DECISION TREE: backtracking_template(n=2)
# ═══════════════════════════════════════════════════════════════════
#
#                            []
#                         (pos=0)
#                      /           \
#                   0 /             \ 1
#                    /               \
#                 [0]                 [1]
#               (pos=1)             (pos=1)
#              /     \               /    \
#           0 /       \ 1         0 /      \ 1
#            /         \           /        \
#         [0,0]      [0,1]      [1,0]      [1,1]
#        (pos=2)    (pos=2)    (pos=2)    (pos=2)
#           │          │          │          │
#           ▼          ▼          ▼          ▼
#         "00"       "01"       "10"       "11"
#           ✓          ✓         ✓          ✓
#

print("\nBinary strings of length 2:")
print(backtracking_template(2))
# Output: ['00', '01', '10', '11']

"""
=================================================================
BACKTRACKING PATTERNS
=================================================================
"""

from typing import List

"""
================================================================
PATTERN 1: PERMUTATIONS (ORDER MATTERS)
================================================================
PATTERN EXPLANATION: Generate all possible orderings of a collection where each element appears exactly once. Order matters means that [A,B] and [B,A] are both unique permutations. Uses backtracking to systematically explore all arrangements by making choices at each position, then undoing choices to try alternatives. Tracks used elements with boolean array to ensure no duplicates in a single permutation.

TYPICAL STEPS:
1. Initialize result list and helper function with path and used array
2. Base case: When path length equals input size, save permutation
3. Loop through all elements in input array
4. Skip if element already used (check used array)
5. Make choice: Add element to path, mark as used
6. Recursively build rest of permutation
7. Undo choice: Remove element from path, mark as unused
8. Return all collected permutations

Applications: Arranging elements, generating orderings, scheduling problems, TSP variants, password cracking, generating test cases, exploring all sequences.
================================================================
"""

class PermutationsPattern: # LC 46: Permutations
    """
    Problem: Given array nums of distinct integers, return all possible permutations.
    
    Example:
        Input: nums = [1,2,3]
        Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        Explanation: All 3! = 6 ways to arrange 3 distinct elements
    
    Key insight: 
    - Try ALL elements at each position (unlike combinations which only try remaining)
    - Track used elements with boolean array to stop you from using the same element twice 
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        TC: O(n! * n) 
        - n! permutations exist (n=3 → 6, n=4 → 24, n=5 → 120)
        - Each permutation takes O(n) to copy to result
        - Why n!? At each level: n choices, then n-1, ... → n*(n-1)*...*1 = n!
    
        SC: O(n)
        - Recursion depth: O(n) - build position by position, n levels deep
        - Path storage: O(n) - current permutation being built
        - Used array: O(n) - tracks which elements are in path
        - Result storage O(n! * n) not counted (output, not auxiliary space)
        """
        result = []  # Store all complete permutations
        
        def backtrack(path, used):
            """
            Build permutations one element at a time.
            - path: current permutation being built
            - used: boolean array tracking which elements are in path
            """
            # BASE CASE: Permutation complete when all n elements used
            if len(path) == len(nums):
                result.append(path[:])  # Save copy (not reference!)
                return
            
            # RECURSIVE CASE: Try adding each unused element
            for i in range(len(nums)):
                # PRUNING: Skip if element already in current permutation
                if used[i]:
                    continue
                
                # STEP 1: MAKE CHOICE - add element to permutation
                path.append(nums[i])
                used[i] = True  # Mark as used
                
                # STEP 2: EXPLORE - recursively build rest
                backtrack(path, used)
                
                # STEP 3: UNDO CHOICE (BACKTRACK) - restore state
                path.pop()       # Remove element
                used[i] = False  # Mark as unused
        
        # Start with empty path, nothing used
        backtrack([], [False] * len(nums))
        return result

# ============================================
# VISUALIZATION FOR PERMUTATIONS: nums=[1,2]
# ============================================
#
#                     backtrack(path=[], used=[F,F])
#                           /                \
#                      TRY 1                  TRY 2
#                        /                      \
#               path=[1]                      path=[2]
#             used=[T,F]                    used=[F,T]
#                  /    \                      /    \
#              TRY 1  TRY 2                TRY 1  TRY 2
#              (skip)   |                    |    (skip)
#                       |                    |
#                   path=[1,2]           path=[2,1]
#                   used=[T,T]           used=[T,T]
#                       ✓                     ✓
#                     SAVE                  SAVE
#
# Result: [[1,2], [2,1]]
#

# ================================================================================
# VISUALIZATION FOR PERMUTATIONS: nums=[1,2,3] -> at every level, try all elements
# ================================================================================ 
# 
#                         path = []
#                 /          |          \     
#                /           |           \
#               1            2            3    
#         path=[1]        path=[2]        path=[3]   
#        /      |        |       |        |       \
#       /       |        |       |        |        \
#      2        3        1       3        1         2
#   [1,2]     [1,3]    [2,1]   [2,3]    [3,1]      [3,2]
#     |         |        |       |        |          |
#     3         2        3       1        2          1
#  [1,2,3]   [1,3,2]  [2,1,3] [2,3,1]  [3,1,2]    [3,2,1]

sol = PermutationsPattern()
print(sol.permute([1,2])) # [[1,2],[2,1]]
print(sol.permute([1,2])) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


"""
===================================================================
PATTERN 2: COMBINATIONS (CHOOSE K ELEMENTS) - ORDER DOESN'T MATTER
==================================================================
PATTERN EXPLANATION: Select k elements from n elements where order doesn't matter. Order doesn't matter means that [A,B] and [B,A] are both not unique combinations -  we only count those two elements once. Uses backtracking with a start index to systematically build combinations by trying elements in forward order only. Prevents duplicates like [1,2] and [2,1] by ensuring we always move forward through candidates.

TYPICAL STEPS:
1. Initialize result list and helper function with start index and path
2. Base case: When path length equals k, save combination
3. Loop from start index to n (or end of array)
4. Make choice: Add current element to path
5. Recursively build rest with start=i+1 (move forward only)
6. Undo choice: Remove element from path
7. Return all collected combinations

Applications: Lottery combinations, team selection, choosing items from menu, subset of fixed size, card hands, committee formation.
================================================================
"""

class CombinationsPattern:
    """
    Problem: Given two integers n and k, return all possible combinations of 
    k numbers chosen from range [1, n].
    
    Example:
        Input: n=4, k=2
        Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
        Explanation: Choose 2 numbers from [1,2,3,4]
            [1,2] and [2,1] are the SAME combination (order doesn't matter)
            So we only generate [1,2] by always moving forward
    """
    def combine(self, n: int, k: int) -> List[List[int]]: # LC 77
        """
        TC: O(C(n,k) * k) 
            - C(n,k) = n!/(k!(n-k)!) number of combinations exist for "n choose k"
            - O(k) work per combination -> each combination takes O(k) to copy to result (each combination is exactly k elements)
            - Example: C(4,2) = 6, so O(6 * 2) = O(12)
    
        SC: O(k)
            - O(k) recursion depth - we add one element at a time until we have k elements
            - O(k) path storage - path only ever holds k elements max
        """
        result = []  # Store all complete combinations
        
        def backtrack(start, path):
            """
            Build combinations one element at a time.
            
            Args:
                start: First number to consider (prevents going backwards)
                path: Current combination being built (e.g., [1,2])
            """
            # BASE CASE: Combination complete when we have k elements
            if len(path) == k:
                result.append(path[:])  # Save copy
                return
            
            # RECURSIVE CASE: Try adding each number from start to n
            # Key: start from 'start', not from 1! This prevents duplicates
            for i in range(start, n + 1):
                # STEP 1: MAKE CHOICE - add number i
                path.append(i)
                
                # STEP 2: EXPLORE - build rest starting from i+1
                backtrack(i + 1, path)
                
                # STEP 3: UNDO CHOICE (BACKTRACK)
                path.pop()
        
        # Start at 1, empty path
        backtrack(1, [])
        return result

# ============================================
# VISUALIZATION FOR COMBINATIONS: n=4, k=2
# ============================================
#
#                           backtrack(start=1, path=[])
#                      /          |            |           \
#                  TRY 1        TRY 2         TRY 3       TRY 4
#                    /            |            |             \
#              path=[1]       path=[2]      path=[3]        path=[4]
#              start=2        start=3       start=4         start=5
#             /  |   \          /  \           |        (k not reached)
#         TRY   TRY   TRY     TRY   TRY      TRY 4
#          2     3     4       3     4         |
#          |     |     |       |     |         |
#       [1,2]  [1,3] [1,4]   [2,3] [2,4]     [3,4]
#         ✓      ✓     ✓       ✓     ✓         ✓
#       SAVE   SAVE  SAVE    SAVE   SAVE     SAVE
#
# Result: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
#
# Key: start index prevents going backwards
#   After choosing 1, can only try 2,3,4 (not 1 again)
#   After choosing 2, can only try 3,4 (not 1 or 2)
#   After choosing 3, can only try 4 (not 1,2, or 3)

sol = CombinationsPattern()
print("Combinations n=4, k=2:")
print(sol.combine(4, 2)) # [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

"""
================================================================
PATTERN 3: SUBSETS (POWER SET)
================================================================
PATTERN EXPLANATION: Generate all possible subsets of a set, including empty set and the set itself. Unlike combinations which saves only when size=k, subsets saves at EVERY level of recursion. Each element has binary choice: include or exclude, creating 2^n total subsets.

TYPICAL STEPS:
1. Initialize result list and helper function with start index and path
2. Save current path to result (at EVERY level, not just base case!)
3. Loop from start to end of array
4. Make choice: Add element to path
5. Recursively explore with start=i+1
6. Undo choice: Remove element from path
7. Return all collected subsets

Applications: Power set generation, finding all subsequences, feature selection, generating test cases, exploring possibilities, configuration options.
================================================================
"""

class SubsetsPattern: # LC 78: Subsets
    """
    Problem: Given integer array nums of unique elements, return all possible 
    subsets (the power set).
    
    Example:
        Input: nums=[1,2,3]
        Output: [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]
        Explanation: Power set has 2^3 = 8 subsets
            Each element: include (1) or exclude (0)
            000=[], 001=[3], 010=[2], 011=[2,3], 
            100=[1], 101=[1,3], 110=[1,2], 111=[1,2,3]
    
    Key insight:
    - CRITICAL difference from combinations: save at EVERY level!
    - Combinations: save only when len(path) == k
    - Subsets: save immediately on entering function
    - Empty subset [] is valid, as are all partial builds [1], [1,2], etc.
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        TC: O(2^n * n)
            - 2^n subsets - Each element has 2 choices: in or out, each subset can be up to n elements long
            - O(n) copy - It takes O(n) to copy each subset in worst case
    
        SC: O(n)
            - Recursion depth: O(n) - maximum n ele deep (including every element: []→[1]→[1,2]→[1,2,3])
            - Path storage: O(n) - current subset being built -> path never exceeds n elements
            - O(n) + O(n) = O(n)
        """
        result = []  # Store all subsets
        
        def backtrack(start, path):
            """
            Build subsets incrementally, saving at every step.
            
            Args:
                start: Index to start considering elements from
                path: Current subset being built (e.g., [1,2])
            """
            # KEY INSIGHT: Save current subset at EVERY level!
            # This is the main difference from combinations pattern
            # [] is a valid subset, [1] is valid, [1,2] is valid, etc.
            result.append(path[:])  # Save copy of current state
            
            # RECURSIVE CASE: Try adding each remaining element
            # Note: No explicit base case needed!
            # When start >= len(nums), loop doesn't run, function returns naturally
            for i in range(start, len(nums)):
                # STEP 1: MAKE CHOICE - include nums[i] in subset
                path.append(nums[i])
                
                # STEP 2: EXPLORE - build subsets with nums[i] included
                # Pass i+1 to avoid reusing same element
                backtrack(i + 1, path)
                
                # STEP 3: UNDO CHOICE (BACKTRACK) - exclude nums[i]
                # Remove to try subsets without this element
                path.pop()
        
        # Start at index 0, empty path
        backtrack(0, [])
        return result

# ============================================
# VISUALIZATION FOR SUBSETS: nums=[1,2,3]
# ============================================
#
#                              backtrack(start=0, path=[])
#                                💾 SAVE [] → result=[[]]
#                            /              |              \
#                        TRY 1            TRY 2           TRY 3
#                          /                |                \
#                   path=[1]             path=[2]            path=[3]
#                 start=1                start=2             start=3
#             💾 SAVE [1]                💾 SAVE [2]          💾 SAVE [3]
#              /       \                    |             (no more elements)
#         TRY 2       TRY 3               TRY 3
#           /            \                  |
#       path=[1,2]     path=[1,3]       path=[2,3]
#       start=2        start=3          start=3
#    💾 SAVE [1,2]   💾 SAVE [1,3]    💾 SAVE [2,3]
#         |            (no more)        (no more)
#       TRY 3
#         |
#    path=[1,2,3]
#    start=3
# 💾 SAVE [1,2,3]
# (no more elements)
#


sol = SubsetsPattern()
print("Subsets of [1,2,3]:")
print(sol.subsets([1,2,3]))
# [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]


"""
================================================================
PATTERN 4: COMBINATION SUM (TARGET WITH REUSE)
================================================================
PATTERN EXPLANATION: Find all combinations of numbers that sum to a target value, where each number can be reused unlimited times. Uses backtracking with pruning to efficiently explore solution space. Key difference from combinations: recurse with same index (i, not i+1) to allow element reuse.

TYPICAL STEPS:
1. Sort candidates array (enables early termination pruning)
2. Initialize result and helper with start, path, and current sum
3. Base case: If sum equals target, save combination
4. Pruning: If sum exceeds target, return early
5. Loop from start to end, trying each candidate
6. Pruning: Break if adding candidate would exceed target
7. Make choice: Add candidate, update sum
8. Recurse with SAME index (allows reuse)
9. Undo choice: Remove candidate
10. Return all valid combinations

Applications: Coin change variations, resource allocation, making change, filling capacity, decomposing numbers, knapsack variants.
================================================================
"""

class CombinationSumPattern:
    """
    Problem: Given array of distinct integers candidates and target integer, 
    return all unique combinations where chosen numbers sum to target. 
    Same number may be chosen unlimited times.
    
    LC 39: Combination Sum
    
    Example:
        Input: candidates=[2,3,6,7], target=7
        Output: [[2,2,3],[7]]
        Explanation: 
            2+2+3 = 7 (can reuse 2)
            7 = 7
            Not [3,2,2] because that's duplicate of [2,2,3]
    
    Key insight:
    - Allow element reuse: pass 'i' not 'i+1' to backtrack
    - Prevent duplicates: still use start index (no backwards)
    - [2,2,3] generated, but [2,3,2] not generated (would need to go backwards)
    - Pruning: sort array and break early when sum would exceed target
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]: # 39
        """
        TC: O(n^d) where n = len(candidates), d = target / min_candidate
            - Decision tree: up to n choices per node, d levels deep
            - d = longest possible combination (e.g., target=8, min=2 → [2,2,2,2] → d=4)
        
        SC: O(d)
            - O(d) recursion depth
            - O(d) path array (reused via backtracking)
        """
        result = []
        candidates.sort()  # Enable pruning optimization
        
        def backtrack(start, path, current_sum):
            """
            Build combinations that sum to target, allowing reuse.
            
            Args:
                start: Index to start considering candidates from
                path: Current combination being built (e.g., [2,2,3])
                current_sum: Sum of elements in path so far
            """
            # BASE CASE: Found valid combination!
            if current_sum == target:
                result.append(path[:])  # Save copy
                return
            
            # RECURSIVE CASE: Try adding each candidate
            for i in range(start, len(candidates)):
                # PRUNING OPTIMIZATION: Since array is sorted,
                # if adding candidates[i] exceeds target, all remaining will too
                # So we can break early instead of continuing loop
                if current_sum + candidates[i] > target:
                    break  # Not 'continue' - everything after is also too big!
                
                # STEP 1: MAKE CHOICE - add candidate if sum smaller than target
                path.append(candidates[i])
                
                # STEP 2: EXPLORE - recurse with SAME index i (not i+1!) & update curr sum
                # This allows reusing same element multiple times
                # [2,2,3] is built by: add 2 at i=0, recurse with i=0, add 2 again
                backtrack(i, path, current_sum + candidates[i])
                
                # STEP 3: UNDO CHOICE (BACKTRACK)
                path.pop()
        
        # Start at index 0, empty path, sum=0
        backtrack(0, [], 0)
        return result

# ═══════════════════════════════════════════════════════════════════
# DECISION TREE: combinationSum([2,3], target=5)
# ═══════════════════════════════════════════════════════════════════
#
#                                 [] 
#                               sum=0
#                              start=0
#                            /         \
#                        +2 /           \ +3
#                          /             \
#                       [2]               [3]
#                     sum=2               sum=3
#                    start=0             start=1
#                    /     \                |
#               +2 /        \ +3            | +3
#                 /          \              |
#             [2,2]         [2,3]           ✗
#             sum=4         sum=5         3+3=6>5
#            start=0       start=1        PRUNED
#              |              |
#              |              ▼
#         +2   ✗           ✓ SAVE
#        4+2=6>5         result=[[2,3]]
#        PRUNED

sol = CombinationSumPattern()
print("Combination Sum [2,3,6,7], target=7:")
print(sol.combinationSum([2,3,6,7], 7))
# [[2,2,3],[7]]


"""
================================================================
PATTERN 5: PARTITIONING (SPLIT INTO VALID GROUPS)
================================================================
PATTERN EXPLANATION: Partition a string or array into groups where each group satisfies certain constraints (e.g., palindrome, valid word). At each position, try all possible partition points and validate each partition before proceeding. Uses backtracking to explore all valid partition combinations.

TYPICAL STEPS:
1. Initialize result and helper function with start position and path
2. Base case: If start reaches end, entire string partitioned - save result
3. Loop through possible end positions from start+1 to len+1
4. Extract substring/subarray from start to end
5. Validate: Check if partition satisfies constraint (palindrome, etc.)
6. If valid: Make choice - add to path, recurse from end position
7. Undo choice: Remove partition from path
8. Return all valid partitionings

Applications: Palindrome partitioning, word break, splitting into valid chunks, sentence segmentation, domain splitting.
================================================================
"""

class PartitioningPattern:
    """
    Problem: Given string s, partition s such that every substring is a 
    palindrome. Return all possible palindrome partitionings.
    
    Example:
        Input: s="aab"
        Output: [["a","a","b"],["aa","b"]]
        Explanation: Two ways to partition into all palindromes:
            "aab" = "a" + "a" + "b" (each is palindrome)
            "aab" = "aa" + "b" (both are palindromes)
            NOT "a" + "ab" (since "ab" is not palindrome)
    
    Key insight:
    - At each position, try ALL possible cut points
    - Only proceed if substring before cut is valid (palindrome)
    - Unlike previous patterns (try elements), here we try partition endpoints
    - Start index tracks "what part of string is unpartitioned"
    """
    def partition(self, s: str) -> List[List[str]]: # LC 131
        """
        TC: O(2^n * n)
            - 2^n possible ways to partition string (at each pos: split or don't)
            - For each partition: O(n) to check palindrome and copy result
            - Example: "abc" → 4 partitionings: [a,b,c], [a,bc], [ab,c], [abc]
    
        SC: O(n)
            - Recursion depth: O(n) - worst case split into n single characters
            - Path storage: O(n) - current partitioning being built
        """
        result = []
        
        def is_palindrome(string):
            return string == string[::-1]
        
        def backtrack(i, path): # i = current index in string, # path = palindromes collected so far
            
            # Base case: reached end of string, found valid partition
            if i == len(s):
                result.append(path[:])
                return
            
            # Try all possible substrings starting at index i
            # j represents where we cut: s[i:j]
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                
                # Only proceed if it's a palindrome
                if is_palindrome(substring):
                    path.append(substring)   # Choose
                    backtrack(j, path)       # Explore from j (where we just cut)
                    path.pop()               # Undo
        
        backtrack(0, []) # start at index 0, empty path
        return result

# ============================ DECISION TREE FOR "aab" ============================
#
#                                    backtrack(i=0, [])
#                                       s = "a a b"
#                                            ↑
#                                            i=0
#                                             |
#                 ---------------------------------------------------------
#                 |                           |                           |
#            j=1: s[0:1]                 j=2: s[0:2]                 j=3: s[0:3]
#              "a" ✓                       "aa" ✓                      "aab" ✗
#                 |                           |                        PRUNED
#                 |                           |
#         backtrack(i=1, ["a"])       backtrack(i=2, ["aa"])
#            s = "a a b"                 s = "a a b"
#                 ↑                               ↑
#                 i=1                             i=2
#                 |                               |
#        -------------------                 j=3: s[2:3]
#        |                 |                   "b" ✓
#   j=2: s[1:2]       j=3: s[1:3]                 |
#     "a" ✓             "ab" ✗                    |
#        |              PRUNED           backtrack(i=3, ["aa","b"])
#        |                                        |
# backtrack(i=2, ["a","a"])                 i == len(s)
#    s = "a a b"                          ✅ FOUND: ["aa","b"]
#             ↑
#            i=2
#             |
#        j=3: s[2:3]
#          "b" ✓
#             |
#  backtrack(i=3, ["a","a","b"])
#             |
#        i == len(s)
#   ✅ FOUND: ["a","a","b"]
#

sol = PartitioningPattern()
print("Palindrome Partitioning 'aab':")
print(sol.partition("aab")) # [["a","a","b"],["aa","b"]]


"""
================================================================
PATTERN 6: GRID BACKTRACKING (2D EXPLORATION)
================================================================
PATTERN EXPLANATION: Explore 2D grid to find paths or patterns by trying all four directions (up, down, left, right) at each cell. Mark cells as visited during exploration to prevent reuse in same path, then unmark when backtracking. Different paths can reuse same cell, just not within single path.

TYPICAL STEPS:
1. Iterate through grid to find all possible starting positions
2. For each start, call backtrack helper with position and match index
3. Base case: If matched entire pattern, return success
4. Boundary/validity checks: out of bounds, already visited, or mismatch
5. Mark current cell as visited (temporarily modify grid or use visited set)
6. Try all 4 directions: up, down, left, right recursively
7. If any direction succeeds, propagate success
8. Unmark current cell (backtrack) to allow use in other paths
9. Return success/failure status

Applications: Word search, pathfinding, maze solving, island problems, connected components, pattern matching in grids.
================================================================
"""

class GridBacktrackingPattern:
    """
    Problem: Given m*n board and word, return true if word exists in grid. 
    Word constructed from sequentially adjacent cells (horizontal or vertical).
    Same cell cannot be used twice in same path.
    
    LC 79: Word Search
    
    Example:
        Input: 
            board = [["A","B","C","E"],
                     ["S","F","C","S"],
                     ["A","D","E","E"]]
            word = "ABCCED"
        Output: true
        Explanation: Path exists: A→B→C→C→E→D
            (0,0)→(0,1)→(0,2)→(1,2)→(2,2)→(2,1)
    
    Key insight:
    - Same cell can appear in DIFFERENT paths (different searches)
    - Same cell CANNOT appear TWICE in SAME path (mark visited temporarily)
    - Mark cell with special character during exploration (e.g., '#')
    - Unmark when backtracking so other paths can use it
    - Try all 4 directions: if ANY succeeds, entire search succeeds
    """
    def exist(self, board: List[List[str]], word: str) -> bool: # 79
        """
        TC: O(m * n * 4^L) where m = rows, n = cols, L = len(word)
            - Try each cell as starting point: O(m * n)
            - From each start, explore up to 4^L paths (4 directions, L levels deep)
        
        SC: O(L)
            - O(L) recursion depth (one call per character in word)
            - In-place marking on board (no extra visited structure)
        """
        rows, cols = len(board), len(board[0])
        
        def backtrack(r, c, index):
            """
            Search for word starting from board[r][c] matching word[index].
            
            Args:
                r: Current row position
                c: Current column position
                index: Current position in word we're trying to match
            
            Returns:
                True if word can be formed from this position, False otherwise
            """
            # BASE CASE: Matched entire word!
            if index == len(word):
                return True
            
            # BOUNDARY CHECKS: Invalid if any of these true
            if (r < 0 or r >= rows or          # Out of bounds vertically
                c < 0 or c >= cols or          # Out of bounds horizontally
                board[r][c] != word[index] or  # Character mismatch
                board[r][c] == '#'):           # Already visited in this path
                return False
            
            # STEP 1: MARK as visited in current path
            # Save original character and replace with '#' marker
            # This prevents using same cell twice in THIS path
            temp = board[r][c]
            board[r][c] = '#'
            
            # STEP 2: EXPLORE all 4 directions
            # Try moving: down, up, right, left
            # If ANY direction finds the word, return True
            # Use 'or' short-circuit: stops as soon as one succeeds
            found = (backtrack(r + 1, c, index + 1) or  # DOWN
                    backtrack(r - 1, c, index + 1) or   # UP
                    backtrack(r, c + 1, index + 1) or   # RIGHT
                    backtrack(r, c - 1, index + 1))     # LEFT
            
            # STEP 3: UNMARK (BACKTRACK)
            # Restore original character so other paths can use this cell
            # This is CRITICAL: same cell might be part of different valid path
            board[r][c] = temp
            
            return found
        
        # Try starting from EACH cell in grid
        # Word could start anywhere, so check all positions
        for r in range(rows):
            for c in range(cols):
                # If search from (r,c) succeeds, word exists
                if backtrack(r, c, 0):
                    return True
        
        # Tried all starting positions, word not found
        return False

# ═══════════════════════════════════════════════════════════════════
# DECISION TREE: exist(board, "AB")
# ═══════════════════════════════════════════════════════════════════
#
# Board: [["A","B"],        Word: "AB"
#         ["C","D"]]
#
# Starting from (0,0) = 'A':
#
#                              (0,0) 'A'
#                               idx=0
#                            'A'='A' ✓
#                         /    |    |    \
#                    ↓   /   ↑ |  → |   ← \
#                      /       |    |       \
#                 (1,0)    (-1,0)  (0,1)   (0,-1)
#                  'C'      OOB     'B'      OOB
#                 idx=1    idx=1   idx=1    idx=1
#                'C'≠'B'    ✗     'B'='B'    ✗
#                   ✗              ✓
#                                  |
#                               idx=2
#                            len(word)=2
#                                 ✓
#                            WORD FOUND!

# WHY UNMARK?
# Same cell may be needed in a different path from the same search.
#
# word = "ABFC"
# board = [["A","B","C"],
#          ["D","F","E"],
#          ["G","H","I"]]
#
# Path 1: A → B → F → ??? (no 'C' adjacent to F, fails)
# Path 2: A → B → C ← needs to try this, but if F still '#', board is corrupted
#
# Unmarking F lets us backtrack to B and explore other directions cleanly.

sol = GridBacktrackingPattern()
board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
print("Word Search 'ABCCED':", sol.exist(board, "ABCCED"))  # True
print("Word Search 'SEE':", sol.exist(board, "SEE"))        # True
print("Word Search 'ABCB':", sol.exist(board, "ABCB"))      # False