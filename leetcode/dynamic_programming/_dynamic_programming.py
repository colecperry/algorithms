"""
=========================================================================
DYNAMIC PROGRAMMING COMPLETE GUIDE
=========================================================================

WHAT IS DYNAMIC PROGRAMMING?
----------------------------
Dynamic Programming (DP) is an optimization technique that solves complex problems by breaking them down into simpler overlapping subproblems. It stores solutions to subproblems to avoid redundant computation, trading space for time.

Key characteristics:
- Optimal Substructure: Optimal solution contains optimal solutions to subproblems
- Overlapping Subproblems: Same subproblems are solved multiple times
- Memoization (Top-Down): Cache recursive results
- Tabulation (Bottom-Up): Build solution iteratively from base cases

When to use DP:
- Problem asks for optimal value (max/min)
- Problem asks for number of ways to do something
- Problem asks if something is possible
- Current decision depends on previous decisions
- Can identify recursive pattern with overlapping subproblems

Common DP problem types:
- Linear sequences (1D array)
- Grid paths (2D array)
- Knapsack/subset selection
- Subsequence problems
- String matching
- State machines

DYNAMIC PROGRAMMING CORE TEMPLATES
===================================
"""

from typing import List

"""
DYNAMIC PROGRAMMING COMPLEXITY REFERENCE
==========================================

+-------------------------------------+---------------+-----------+
| Pattern                             | Time          | Space     |
+-------------------------------------+---------------+-----------+
| 1D Linear DP (Sequential Decisions) | O(n)          | O(n)      |
| 2D Grid DP (Path Problems)          | O(m * n)      | O(m * n)  |
| 0/1 Knapsack (Subset Selection)     | O(n * target) | O(target) |
| Longest Increasing Subsequence      | O(n^2)        | O(n)      |
| Longest Common Subsequence          | O(m * n)      | O(m * n)  |
| State Machine DP (Multiple States)  | O(n)          | O(n)      |
+-------------------------------------+---------------+-----------+

n = length of the array/string/number of days, m * n = grid dimensions or
lengths of the two strings being compared, target = target sum for 0/1
knapsack. Several of these can be space-optimized further (see NOTES).

WHAT EACH PATTERN IS:
- 1D Linear DP: walk through a list one item at a time, deciding the best move at each
  step using only what was decided at the previous step or two — like deciding
  house-by-house whether robbing it is worthwhile.
- 2D Grid DP: fill in a grid one cell at a time, where each cell's answer is built from
  the cell above it and/or to its left — like counting paths to each square starting
  from the top-left corner.
- 0/1 Knapsack: figure out which items from a group to pick, each only once, to hit
  some target total, by tracking every total that's achievable so far.
- Longest Increasing Subsequence: for every position in a list, look back at all
  earlier positions to find the best increasing run that can be extended up to here.
- Longest Common Subsequence: compare two sequences piece by piece, building a table
  of "best match so far" that grows by extending a match or carrying forward the
  better of two neighboring answers.
- State Machine DP: track several possible "modes" you could be in at each step (like
  holding stock vs. resting) and work out the best way to move between those modes.

NOTES:
- 1D Linear DP: each of n positions computed once with O(1) work -> O(n) time; dp
  array can shrink to O(1) since each state only depends on the last 1-2 values
- 2D Grid DP: each of m*n cells computed once with O(1) work -> O(m*n) time; space can
  shrink to O(n) by keeping only the previous row
- 0/1 Knapsack: n items x up to target capacities, O(1) work per cell, iterated
  backwards so an item is never reused -> O(n * target) time; dp array sized target
- LIS: n positions, each checking up to n earlier positions -> O(n^2) time; dp array
  itself is only O(n)
- LCS: fills an (m+1) x (n+1) table with O(1) work per cell -> O(m*n) time and space
  (space reducible to O(min(m,n)) by keeping only the previous row)
- State Machine DP: n steps, a constant number of states with O(1) transitions per
  step -> O(n) time; space is O(n) for the full table but reducible to O(1) by keeping
  only the previous step's states
"""

# ========================================================================
# 1D DP TEMPLATE (LINEAR)
# ========================================================================
def max_subarray_sum(nums):
    """
    Find maximum sum of any contiguous subarray (Kadane's Algorithm). A contiguous subarray is sequence of ele's that appear consecutively in the original array - no skipping or reordering allowed.
    
    Example: [-2,1,-3,4,-1,2,1,-5,4] → 6 (subarray [4,-1,2,1])
    
    TC: O(n) - process each element once
    SC: O(n) - dp array stores solution for each position
    """
    if not nums:
        return 0
    
    n = len(nums)
    dp = [0] * n  # dp[i] = max subarray sum so far ending at index i
    
    dp[0] = nums[0] # Base case: first element is the only option
    
    # Fill dp array
    for i in range(1, n):
        # Either extend previous subarray or start fresh from current ele
        dp[i] = max(dp[i-1] + nums[i], nums[i]) # <- Kadane's algo
    
    return max(dp) # Return maximum sum found at any position

print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # Expected : 6

"""
=========================================================================
DP APPROACH COMPARISON: TOP-DOWN VS BOTTOM-UP VS SPACE-OPTIMIZED

Problem: Calculate the nth Fibonacci number
Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

Example: fibonacci(6) → 8 (sequence: 0,1,1,2,3,5,8)

THREE APPROACHES:
1. Top-Down (Memoization): Recursive with caching
   - Use when: Recursion feels natural, don't need all subproblems, base cases clear
   - TC: O(n), SC: O(n) memo dict + O(n) recursion stack

2. Bottom-Up (Tabulation): Iterative with DP array
   - Use when: Need most/all subproblems, clear iteration order, avoid stack overflow
   - TC: O(n), SC: O(n) dp array

3. Space-Optimized: Iterative with only last few values
   - Use when: Only need previous k states (common in 1D DP)
   - TC: O(n), SC: O(1) constant space

General rule: Start with approach that feels most intuitive, then optimize if needed.
=========================================================================
"""

# ===== APPROACH 1: TOP-DOWN (MEMOIZATION) =====
def fibonacci_topdown(n):
    """
    TC: O(n)
        - n unique subproblems: fib(6), fib(5), fib(4), fib(3), fib(2), fib(1), fib(0)
        - Each computed once: first call computes it, future calls hit cache
        - O(1) work per subproblem: one addition + one dict store
    SC: O(n) 
        - Memo dict: O(n) - stores n key-value pairs
        - Recursion stack: O(n) - max depth is n (fib(n)→fib(n-1)→...→fib(1))
        - Total: O(n) + O(n) = O(n)
    """
    memo = {} # memo is a dict that maps the nth position to its fib val
    
    def fib(i):
        # Base case for fib(0) = 0 and fib(1) = 1
        if i <= 1:
            return i
        
        # Check memo -> see if we already calculated fib(i)
        if i in memo:
            return memo[i]
        
        # fib(n) = fib(n-1) + fib(n-2)
        previous_num = fib(i-1) # Get num 1 pos back
        two_back_num = fib(i-2) # Get num 2 pos back
        result = previous_num + two_back_num
        
        # Store in memo
        memo[i] = result

        return result
    
    return fib(n)

print("Top-Down:", fibonacci_topdown(6)) # Output: 8

# ===== APPROACH 2: BOTTOM-UP (TABULATION) =====
def fibonacci_bottomup(n):
    """
    TC: O(n)
        - Single loop from 2 to n
        - O(1) work per iteration (one addition, one assignment)
        - Total: n iterations x O(1) = O(n)
    SC: O(n)
        - dp array: O(n) - stores n+1 values
        - No recursion stack (iterative)
        - Total: O(n)
    """
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)  # dp array -> dp[i] = ith Fibonacci number
    
    # Base cases
    dp[0] = 0
    dp[1] = 1
    
    # Build up dp array from base cases
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

print("Bottom-Up:", fibonacci_bottomup(6)) # Output: 8, seq: 0,1,1,2,3,5,8

# ===== APPROACH 3: SPACE-OPTIMIZED =====
def fibonacci_space_optimized(n):
    """
    TC: O(n) - same time complexity -> single loop from 2 to n
    SC: O(1) - constant space (only store last 2 values)
    """
    if n <= 1:
        return n
    
    # Only keep last 2 values instead of entire array
    prev2 = 0  # fib(i-2)
    prev1 = 1  # fib(i-1)
    
    for _ in range(2, n + 1):
        current = prev1 + prev2  # fib(i)
        prev2 = prev1  # Shift window forward
        prev1 = current
    
    return prev1

print("Space-Optimized:", fibonacci_space_optimized(6))  # Output: 8, seq: 0,1,1,2,3,5,8

"""
=====================================================================
                    DP TIME & SPACE COMPLEXITY
=====================================================================

WHY DP BEATS BRUTE FORCE
------------------------
Brute force: Recomputes same subproblems over and over
DP: Computes each subproblem once, stores result

Example: Fibonacci(6)

BRUTE FORCE - O(2^n):
    fib(6) → calls fib(5) and fib(4)
           → fib(5) calls fib(4) and fib(3)
           → fib(4) computed TWICE, fib(3) computed THREE times...
    
    Total calls: 25 for fib(6), 21,891 for fib(20)

WITH DP - O(n):
    fib(6) → compute fib(2), store it
           → compute fib(3) using stored fib(2), store it
           → each value computed exactly once
    
    Total calls: 6 for fib(6), 20 for fib(20)

Speedup: 1,094x faster for n=20


HOW TO CALCULATE DP COMPLEXITY
------------------------------
TC = (number of subproblems) * (work per subproblem)
SC = (space for storing subproblems) + (recursion stack if top-down)


1D DP (House Robber):
    - Subproblems: n (one per house)
    - Work per subproblem: O(1) — just compare two values
    - TC: n * O(1) = O(n)
    - SC: O(n) array, or O(1) if you only keep last 2 values

2D DP (Grid Paths):
    - Subproblems: m * n (one per cell)
    - Work per subproblem: O(1) — add two neighbors
    - TC: m*n * O(1) = O(m*n)
    - SC: O(m*n) grid, or O(n) if you only keep current row

LIS (Longest Increasing Subsequence):
    - Subproblems: n (one per index)
    - Work per subproblem: O(n) — check ALL previous indices
    - TC: n * O(n) = O(n²)
    - SC: O(n) — just the dp array

0/1 Knapsack:
    - Subproblems: n * W (each item * each capacity)
    - Work per subproblem: O(1) — take or skip decision
    - TC: n*W * O(1) = O(n*W)
    - SC: O(n*W), or O(W) if you only keep current row


SPACE OPTIMIZATION INSIGHT
--------------------------
Look at what dp[i] depends on:

Only depends on dp[i-1] and dp[i-2]?
    → Keep 2 variables instead of array → O(1)
    → Example: Fibonacci, House Robber

Only depends on previous row?
    → Keep 1 row instead of grid → O(n)
    → Example: Grid paths, Knapsack

Depends on all previous values?
    → Can't optimize, need full array → O(n)
    → Example: LIS
"""
# =========================================================================
#                         DP COMMON PATTERNS
# =========================================================================

"""
=========================================================================
PATTERN 1: 1D LINEAR DP (SEQUENTIAL DECISIONS)

PATTERN EXPLANATION: Make optimal decisions at each position based on previous positions in a linear sequence. Each position's solution depends on solutions to previous positions.

Common in problems where you process elements left-to-right and current decision is affected by previous decisions. Often can be space-optimized to O(1) by keeping only last few values.

#
Applications: House robber, climbing stairs, min cost climbing, decode ways.
=========================================================================
"""

class LinearDP:
    """
    Problem: You are a robber planning to rob houses along a street. Each house has a certain amount of money. Adjacent houses have security systems connected - if two adjacent houses are robbed on the same night, the police are automatically called.

    Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob without alerting the police.

    # Example 1:
    # Input: nums = [1,2,3,1]
    # Output: 4
    # Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    # Total amount you can rob = 1 + 3 = 4.

    Giveaway: "adjacent houses... alerting the police" — a linear sequence where
    each decision (rob or skip) is constrained only by your immediate previous
    choice, and you want the max total, is the tell for 1D DP where dp[i]
    depends on just dp[i-1] and dp[i-2], rather than needing to look arbitrarily
    far back.

    Steps:
    1. Define dp[i] = max money robbing from first i houses; set dp[0] = 0, dp[1] = nums[0]
    2. For each house i from 2 to n, apply the recurrence:
       a. Option A — skip house i: carry forward dp[i-1]
       b. Option B — rob house i: add nums[i-1] to dp[i-2]
       c. dp[i] = max(option A, option B)
    3. Return dp[n] (max money after considering all houses)
    4. (Optional) Replace dp array with two variables to reduce space to O(1)
    """
    # 1D DP with explicit DP array -> LC 198
    def rob_with_dp_array(self, nums: List[int]) -> int:
        """
        TC: O(n) - process each house once
        SC: O(n)
        - O(n) - with DP array, store n values
        - O(1) - space optimized - only keep track of last 2 values
        """
        n = len(nums)
        dp = [0] * (n + 1)  # dp[i] = max money robbing from first i houses
        dp[0] = 0  # No houses robbed = $0 -> base case
        dp[1] = nums[0] # Rob first house only

        for i in range(2, n + 1):
            # Either skip current house (take prev max) OR rob current house + take max from 2 houses back
            dp[i] = max(dp[i-1], nums[i-1] + dp[i-2] )

        return dp[-1] # Max money after considering all houses

# Example:
# nums = [2, 7, 9, 3, 1]
#
# Decisions at each house:
# House 0: rob 2, total = 2
# House 1: rob 7 (better than 2), total = 7
# House 2: rob 9 + 2 = 11 (better than 7), total = 11
# House 3: skip (11 better than 3+7=10)
# House 4: rob 1 + 11 = 12 (better than 11), total = 12
#
# Output: 12

sol = LinearDP()
print("House Robber:", sol.rob_with_dp_array([2,7,9,3,1]))  # 12
print("House Robber:", sol.rob_with_dp_array([1,2,3,1]))  # 4

"""
=========================================================================
PATTERN 2: 2D GRID DP (PATH PROBLEMS)

PATTERN EXPLANATION: Navigate a 2D grid where each cell's value depends on cells above and/or to the left. Build solution by filling grid from top-left to bottom-right. Each cell represents optimal solution to reach that position. Common in counting paths, finding minimum/maximum path sums, or grid traversal with constraints.

#
Applications: Unique paths, minimum path sum, dungeon game, maximal
square.
=========================================================================
"""

class GridDP:
    """
    Problem: A robot is located at the top-left corner of an m x n grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner.

    How many possible unique paths are there?

    Ex. 1
    Input: m = 3, n = 7
    Output: 28

    Giveaway: "robot... can only move either down or right" on a grid, asking
    how many paths exist to a fixed destination — movement restricted to two
    directions on a 2D grid, where each cell's count is just the sum of the
    cell above and the cell to the left, is the tell for filling a 2D table
    top-left to bottom-right.

    Steps:
    1. Define dp[i][j] = number of unique paths to reach cell (i, j)
    2. Initialize base cases:
       a. Set every cell in the first column to 1 (only one way: go straight down)
       b. Set every cell in the first row to 1 (only one way: go straight right)
    3. For each remaining cell (i, j), apply the recurrence:
       a. dp[i][j] = dp[i-1][j] + dp[i][j-1] (paths from above + paths from left)
    4. Return dp[m-1][n-1] (total paths to bottom-right corner)
    """
    def uniquePaths(self, m: int, n: int) -> int: # LC 62
        """
        TC: O(m * n) - fill entire grid once 
        SC: O(m * n) - 2D dp table (can optimize to O(min(m,n)))
        """
        # Initialize dp table -> m = rows, n = cols
        dp = [[0] * n for _ in range(m)]
        
        # Base case: first col - only one way to reach (go down)
        for i in range(m): # Iterate through all m rows and col stays 0
            dp[i][0] = 1  
        
        # Base case: first row - only one way to reach (go right)
        for j in range(n):  # Iterate through all n cols and row stays 0
            dp[0][j] = 1  
        
        # Fill the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                # Total unique paths to current = paths from above + paths from left
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]

# Example: 3x3 grid
# Start at (0,0), end at (2,2)
#
# DP table visualization:
#   0   1   2
# 0 [1] [1] [1]    Base cases: first row all 1
# 1 [1] [2] [3]    dp[1][1] = 1+1=2, dp[1][2] = 2+1=3
# 2 [1] [3] [6]    dp[2][1] = 1+2=3, dp[2][2] = 3+3=6
#
# Output: 6 unique paths

sol = GridDP()
print("Unique Paths (3x3):", sol.uniquePaths(3, 3))  # 6

"""
=========================================================================
PATTERN 3: 0/1 KNAPSACK (SUBSET SELECTION) - BOTTOM-UP APPROACH

PATTERN EXPLANATION: Choose items to include or exclude to meet a target constraint (sum, weight, capacity). Each item can be used at most once.

Use dynamic programming with a 1D array to track which target values are achievable. Build up possible sums iteratively by processing each item once.

WHY BACKWARDS? 0/1 knapsack makes sure we only use Items ONCE by iterating backwards.

    Example: nums = [5], target = 10

    FORWARD (WRONG):
      i=5:  dp[5] = dp[0] = T
      i=10: dp[10] = dp[5] = T  ← uses the NEW dp[5] we just set!
      Result: dp[10] = True ✗ (used 5 twice!)

    BACKWARD (CORRECT):
      i=10: dp[10] = dp[5] = F  ← uses OLD dp[5]
      i=5:  dp[5] = dp[0] = T
      Result: dp[10] = False ✓ (can't make 10 with just 5)

VARIATION: Unbounded Knapsack (items reusable)

    When items CAN be reused, iterate FORWARD instead.
    Example: Coin Change (LC 322) - minimum coins to make amount

    for coin in coins:
        for i in range(coin, amount + 1):  # FORWARD allows reuse
            dp[i] = min(dp[i], dp[i - coin] + 1)

    Forward works because we WANT to reuse:
      coin=5, i=5:  dp[5] = dp[0]+1 = 1   (one coin)
      coin=5, i=10: dp[10] = dp[5]+1 = 2  (two coins) ✓

#
Applications: Partition equal subset, target sum, subset sum, coin change (count ways).
=========================================================================
"""

class KnapsackDP:
    """
    Problem: Given an integer array nums, return true if you can partition
    the array into two subsets such that the sum of elements in both subsets
    is equal.

    Example 1:
    Input: nums = [1,5,11,5]
    Output: true
    Explanation: The array can be partitioned as [1, 5, 5] and [11].

    Giveaway: "partition the array into two subsets such that the sum... is
    equal" — needing to know, for a fixed target total, which sums are
    reachable by picking a subset of numbers where EACH number is used at most
    once, is the tell for 0/1 knapsack (a boolean array over achievable sums,
    updated backwards per item) instead of trying every subset.

    Steps:
    1. If total sum is odd, return False immediately (can't partition equally)
    2. Set target = total // 2
    3. Create dp array of size target + 1; initialize dp[0] = True, rest False
    4. For each num in nums, iterate backwards from target down to num:
       a. If dp[j - num] is True, set dp[j] = True (num bridges the gap)
    5. Return dp[target]
    """
    def canPartition(self, nums: List[int]) -> bool: # LC 416
        """
        TC: O(n * target)
            - Outer loop: process each num in nums → n iterations
            - Inner loop: for each num, iterate from target down to num → up to target iterations
            - Total: n nums * target iterations = O(n * target)
        SC: O(target)
            - dp array: size target + 1
            - No recursion stack (iterative approach)
        """
        total = sum(nums)
        
        # If total is odd, impossible to split equally
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        # dp[i] = Can we make sum i using numbers we've processed so far?
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: can always make sum 0 by picking nothing
        
        # For each num, see what sums we can make
        for num in nums:
            # Iterate backwards to avoid using num twice in one iteration -> forwards would let dp[i] use the updated dp[i-num] from this same iteration
            for i in range(target, num - 1, -1):
                if dp[i - num]:  # If we could make (i - num) before
                    dp[i] = True  # Then we can make i now (by adding num)
        
        return dp[target]

# Example trace:
# nums = [1, 5, 11, 5], target = 11
#
# Initial: dp = [T, F, F, F, F, F, F, F, F, F, F, F]
#                0  1  2  3  4  5  6  7  8  9  10 11
#
# -> With no nums we can only make sum 0
#
# After num=1: dp = [T, T, F, F, F, F, F, F, F, F, F, F]
#                    0  1
#
# -> With num 1, we can now make sum 1
#
# After num=5: dp = [T, T, F, F, F, T, T, F, F, F, F, F]
#                    0  1           5  6
#
# -> With num 5, we can now make sum 5 and 6
#
# After num=11: dp = [T, T, F, F, F, T, T, F, F, F, F, T]
#                     0  1           5  6              11 ✓
#
# # -> With num 11, we can now make sum 11
#
# dp[11] = True -> Found subset [1, 5, 5] = 11, other subset [11] = 11
# Output: True


sol = KnapsackDP()
print("Can Partition:", sol.canPartition([1,5,11,5]))  # True
print("Can Partition:", sol.canPartition([1,2,3,5]))  # False

"""
=========================================================================
PATTERN 4: LONGEST INCREASING SUBSEQUENCE (SINGLE SEQUENCE)

PATTERN EXPLANATION: Find the longest subsequence from an array where elements are in increasing order (maintain relative positions from original array). For each position, look back at all previous positions and find the longest increasing subsequence ending at those positions. Current position extends the best valid previous subsequence.

#
Applications: LIS, Russian doll envelopes, maximum length of pair chain.
=========================================================================
"""

class LISDP:
    """
    Problem: Given an integer array nums, return the length of the
    longest strictly increasing subsequence.

    A subsequence is an array derived from another array by deleting some
    or no elements without changing the order of the remaining elements.

    Example 1:
    Input: nums = [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

    Giveaway: "longest strictly increasing subsequence" — elements may be
    skipped (subsequence, not subarray) but must stay in relative order and
    increase, which forces you to compare each position against every earlier
    position to see what it can extend, the tell for the O(n^2) "look back at
    all previous indices" DP rather than a single linear scan.

    Steps:
    1. Initialize dp array of size n with all 1s (each element is its own subsequence)
    2. For each position i from 1 to n-1, check all previous positions j < i:
       a. If nums[j] < nums[i], nums[i] can extend the subsequence ending at j
       b. dp[i] = max(dp[i], dp[j] + 1)
    3. Return max(dp) (longest subsequence ending at any position)
    """
    def lengthOfLIS(self, nums: List[int]) -> int: # LC 300
        """
        TC: O(n²)
            - Outer loop: process each num in nums → n iterations
            - Inner loop: for each num, check all previous elements → up to i iterations (worst case n)
            - Total: n elements * n comparisons = O(n²)
        SC: O(n)
            - dp array: size n (one entry per element)
            - No recursion stack (iterative approach)
        """
        if not nums:
            return 0
        
        n = len(nums)
        # dp[i] = length of LIS ending at index i
        dp = [1] * n  # Each ele itself is a subsequence of len 1
        
        # For each position
        for i in range(1, n):
            # Check all previous positions
            for j in range(i):
                # If curr num is greater, can extend its subsequence
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1) # see if extending it gets us a better result
        
        # Return the longest subsequence found at any position
        return max(dp)

# Example: nums = [2, 5, 3, 7]
#
# dp[i] = length of LIS ending at index i
# Initial: dp = [1, 1, 1, 1]
#
# i=1, num=5:
#   Check j=0 (num=2): 5 > 2? Yes → dp[1] = max(1, dp[0]+1) = 2
#   dp = [1, 2, 1, 1]
#
# i=2, num=3:
#   Check j=0 (num=2): 3 > 2? Yes → dp[2] = max(1, dp[0]+1) = 2
#   Check j=1 (num=5): 3 > 5? No (skip)
#   dp = [1, 2, 2, 1]
#
# i=3, num=7:
#   Check j=0 (num=2): 7 > 2? Yes → dp[3] = max(1, dp[0]+1) = 2
#   Check j=1 (num=5): 7 > 5? Yes → dp[3] = max(2, dp[1]+1) = 3
#   Check j=2 (num=3): 7 > 3? Yes → dp[3] = max(3, dp[2]+1) = 3 (no change)
#   dp = [1, 2, 2, 3]
#
# Answer: max(dp) = 3 → LIS is [2,5,7] or [2,3,7]
sol = LISDP()
print("LIS length:", sol.lengthOfLIS([10,9,2,5,3,7,101,18]))  # 4
print("LIS length:", sol.lengthOfLIS([0,1,0,3,2,3]))  # 4

"""
=========================================================================
PATTERN 5: LONGEST COMMON SUBSEQUENCE (TWO SEQUENCES)

PATTERN EXPLANATION: Find the longest subsequence common to two sequences while maintaining relative order in both. Compare characters from both strings and build solution in a 2D table. When characters match, extend the common subsequence. When they don't match, take the best result from either excluding current character from first string or second string.

#
Applications: LCS, edit distance, shortest common supersequence, diff tools.
=========================================================================
"""

class LCSDP:
    """
    Problem: Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

    A subsequence is a string generated from the original string by deleting some (or no) characters without changing the relative order of the remaining characters.

    Example 1:
    Input: text1 = "abcde", text2 = "ace"
    Output: 3
    Explanation: The longest common subsequence is "ace" and its length is 3.

    Giveaway: "given two strings... return the length of their longest common
    subsequence" — comparing TWO independent sequences (not one) for a shared
    subsequence, where characters can be skipped in either string, is the tell
    for a 2D dp[i][j] table built off matching current characters or carrying
    forward the better of the two neighbors, rather than the single-sequence
    LIS recurrence.

    Steps:
    1. Define dp[i][j] = LCS length of text1[0:i] and text2[0:j]; initialize all cells to 0
    2. For each character pair (i, j) starting at (1, 1):
       a. If text1[i-1] == text2[j-1], characters match: dp[i][j] = dp[i-1][j-1] + 1
       b. Otherwise, take the best from skipping one character: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    3. Return dp[m][n]
    """
    def longestCommonSubsequence(self, text1: str, text2: str) -> int: # LC 1143
        """ 
        TC: O(m * n)
            - Outer loop: iterate through text1 → m iterations
            - Inner loop: for each char in text1, iterate through text2 → n iterations
            - Total: m chars * n comparisons = O(m * n)
        SC: O(m * n)
            - 2D dp table: (m+1) x (n+1) grid
            - Can optimize to O(min(m,n)) by keeping only previous row
        """
        m, n = len(text1), len(text2)
        
        # dp[i][j] = LCS length of text1[0:i] and text2[0:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the table -> iterate through char of each word
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]: # index off by one
                    # Characters match - extend LCS from previous chars
                    dp[i][j] = dp[i-1][j-1] + 1
                else: # Characters don't match - take best of two options:
                    # - exclude current char from text1 (dp[i-1][j])
                    # - exclude current char from text2 (dp[i][j-1])
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]

# Example: text1 = "abcde", text2 = "ace"
#
# Building DP table step-by-step:
#
# Initial (all 0s):
#       ""  a  c  e
#   ""   0  0  0  0
#   a    0  
#   b    0  
#   c    0  
#   d    0  
#   e    0  
#
# i=1, char='a':
#   j=1, char='a': Match! dp[1][1] = dp[0][0] + 1 = 1
#   j=2, char='c': No match → dp[1][2] = max(dp[0][2]=0, dp[1][1]=1) = 1
#   j=3, char='e': No match → dp[1][3] = max(dp[0][3]=0, dp[1][2]=1) = 1
#       ""  a  c  e
#   ""   0  0  0  0
#   a    0  1  1  1
#
# i=2, char='b':
#   j=1, char='a': No match → dp[2][1] = max(dp[1][1]=1, dp[2][0]=0) = 1
#   j=2, char='c': No match → dp[2][2] = max(dp[1][2]=1, dp[2][1]=1) = 1
#   j=3, char='e': No match → dp[2][3] = max(dp[1][3]=1, dp[2][2]=1) = 1
#       ""  a  c  e
#   ""   0  0  0  0
#   a    0  1  1  1
#   b    0  1  1  1
#
# i=3, char='c':
#   j=1, char='a': No match → dp[3][1] = max(dp[2][1]=1, dp[3][0]=0) = 1
#   j=2, char='c': Match! dp[3][2] = dp[2][1] + 1 = 2
#   j=3, char='e': No match → dp[3][3] = max(dp[2][3]=1, dp[3][2]=2) = 2
#       ""  a  c  e
#   ""   0  0  0  0
#   a    0  1  1  1
#   b    0  1  1  1
#   c    0  1  2  2
#
# i=4, char='d':
#   j=1, char='a': No match → dp[4][1] = max(dp[3][1]=1, dp[4][0]=0) = 1
#   j=2, char='c': No match → dp[4][2] = max(dp[3][2]=2, dp[4][1]=1) = 2
#   j=3, char='e': No match → dp[4][3] = max(dp[3][3]=2, dp[4][2]=2) = 2
#       ""  a  c  e
#   ""   0  0  0  0
#   a    0  1  1  1
#   b    0  1  1  1
#   c    0  1  2  2
#   d    0  1  2  2
#
# i=5, char='e':
#   j=1, char='a': No match → dp[5][1] = max(dp[4][1]=1, dp[5][0]=0) = 1
#   j=2, char='c': No match → dp[5][2] = max(dp[4][2]=2, dp[5][1]=1) = 2
#   j=3, char='e': Match! dp[5][3] = dp[4][2] + 1 = 3
#       ""  a  c  e
#   ""   0  0  0  0
#   a    0  1  1  1
#   b    0  1  1  1
#   c    0  1  2  2
#   d    0  1  2  2
#   e    0  1  2  3
#
# Answer: dp[5][3] = 3 → LCS is "ace"

sol = LCSDP()
print("LCS length:", sol.longestCommonSubsequence("abcde", "ace"))  # 3
print("LCS length:", sol.longestCommonSubsequence("abc", "abc"))  # 3
print("LCS length:", sol.longestCommonSubsequence("abc", "def"))  # 0

"""
=========================================================================
PATTERN 6: STATE MACHINE DP (MULTIPLE STATES)

PATTERN EXPLANATION: Track multiple distinct states at each position with transitions between states. Each state represents a different condition or situation (holding stock, cooldown, sold, etc). At each step, can transition from one state to another with associated costs or profits. Must track optimal value for each state and compute transitions based on allowed moves.

#
Applications: Stock trading with constraints, game states, state-dependent
decisions.
=========================================================================

"""

class StateMachineDP:
    """
    Problem: You are given an array prices where prices[i] is the price of a stock on day i. You can complete as many transactions as you like with the following restrictions: After you sell your stock, you cannot buy stock on the next day (cooldown 1 day)

    Return the maximum profit you can achieve.

    Example 1:
    Input: prices = [1,2,3,0,2]
    Output: 3
    Explanation: transactions = [buy, sell, cooldown, buy, sell]

    States:
    - hold: currently holding stock
    - sold: just sold stock today
    - rest: not holding, not in cooldown

    Transitions:
    - hold: either already holding or buy today from rest
    - sold: must have been holding, sell today
    - rest: either already resting or cooldown from sold

    Giveaway: "after you sell... you cannot buy on the next day (cooldown)" — an
    extra rule that makes the profit on a given day depend on which of several
    distinct MODES you were in the day before (holding, just sold, resting),
    rather than just yesterday's best profit, is the tell for tracking parallel
    dp values per state with explicit transitions between them.

    Steps:
    1. Identify the three states: hold (own stock), sold (just sold today), rest (no stock, no cooldown)
    2. Initialize base cases for day 0:
       a. hold = -prices[0] (buy on day 0)
       b. sold = 0 (can't sell on day 0)
       c. rest = 0 (do nothing on day 0)
    3. For each subsequent day i, compute state transitions:
       a. hold = max(dp[i-1][hold], dp[i-1][rest] - prices[i])
       b. sold = dp[i-1][hold] + prices[i]
       c. rest = max(dp[i-1][rest], dp[i-1][sold])
    4. Return max(dp[n-1][sold], dp[n-1][rest])
    5. (Optional) Replace 2D array with three variables to reduce space to O(1)
    """
    def maxProfit_2d(self, prices: List[int]) -> int: # LC 309
        """
        TC: O(n)
            - Single loop: iterate through n days
            - Per day: constant time state transitions (3 states, each O(1))
            - Total: n days * O(1) = O(n)
        SC: O(n)
            - 2D dp array: n days * 3 states
            - Can optimize to O(1) by keeping only previous day's states
        """
        if not prices: # Edge case -> no array of prices -> cannot return profit
            return 0
        
        n = len(prices)
        # dp[i][state] where state: 0=hold, 1=sold, 2=rest
        dp = [[0] * 3 for _ in range(n)]
        
        # Base case: day 0
        dp[0][0] = -prices[0]  # Buy on day 0
        dp[0][1] = 0  # Can't sell on day 0 (nothing to sell)
        dp[0][2] = 0  # Rest on day 0
        
        for i in range(1, n):
            # Hold state: find most profitable way to hold stock
            dp[i][0] = max(dp[i-1][0], # Continue holding -> held stock yesterday
                           dp[i-1][2] - prices[i]) # Buy today-> rested yesterday
            
            # Sold state: only one way to be in sold state
            dp[i][1] = dp[i-1][0] + prices[i] # Held stock yesterday and sold today
            
            # Rest state: find most profitable way to be resting
            dp[i][2] = max(dp[i-1][2], # Continue resting -> Were resting yesterday
                           dp[i-1][1]) # Enter cooldown -> sold yesterday, must cooldown
        
        # Return max of sold or rest on last day
        return max(dp[n-1][1], dp[n-1][2])

# Example: prices = [1,2,3,0,2]
#
# Day 0 (price=1):
#   hold = -1 (buy stock)
#   sold = 0 (can't sell, nothing owned)
#   rest = 0 (do nothing)
#   dp = [[-1, 0, 0], ...]
#
# Day 1 (price=2):
#   hold = max(-1, 0-2) = -1 (keep holding from day 0)
#   sold = -1+2 = 1 (sell stock bought on day 0)
#   rest = max(0, 0) = 0 (continue resting)
#   dp = [[-1, 0, 0], [-1, 1, 0], ...]
#
# Day 2 (price=3):
#   hold = max(-1, 0-3) = -1 (keep holding from day 0)
#   sold = -1+3 = 2 (sell stock bought on day 0)
#   rest = max(0, 1) = 1 (cooldown from selling on day 1)
#   dp = [[-1, 0, 0], [-1, 1, 0], [-1, 2, 1], ...]
#
# Day 3 (price=0):
#   hold = max(-1, 1-0) = 1 (buy on day 3 after cooldown from day 1 sale)
#   sold = -1+0 = -1 (sell stock bought on day 0)
#   rest = max(1, 2) = 2 (cooldown from selling on day 2)
#   dp = [[-1, 0, 0], [-1, 1, 0], [-1, 2, 1], [1, -1, 2], ...]
#
# Day 4 (price=2):
#   hold = max(1, 2-2) = 1 (keep holding from day 3)
#   sold = 1+2 = 3 (sell stock bought on day 3)
#   rest = max(2, -1) = 2 (cooldown from selling on day 2)
#   dp = [[-1, 0, 0], [-1, 1, 0], [-1, 2, 1], [1, -1, 2], [1, 3, 2]]
#
# Answer: max(sold, rest) = max(3, 2) = 3
# Transactions: buy day 0, sell day 1, cooldown day 2, buy day 3, sell day 4

sol = StateMachineDP()
print("Max profit with cooldown:", sol.maxProfit_2d([1,2,3,0,2]))  # 3
print("Max profit with cooldown:", sol.maxProfit_2d([1]))  # 0