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

TYPICAL STEPS:
1. Define dp[i] = optimal solution up to position i
2. Identify base case (dp[0], dp[1])
3. Find recurrence relation: how dp[i] relates to previous values
4. Fill dp array from left to right
5. Return dp[n-1] or final computed value
6. (Optional) Optimize space by keeping only needed previous values

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
    
    How it works:
    1. At each house, decide: rob it or skip it
    2. If rob current: can't rob prev, so add to max from 2 houses ago
    3. If skip current: take max from previous house
    4. Pattern: dp[i] = max(dp[i-1], dp[i-2] + nums[i])
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

TYPICAL STEPS:
1. Define dp[i][j] = optimal solution for cell (i, j)
2. Initialize first row and/or first column (base cases)
3. Fill grid row by row or column by column
4. Recurrence: dp[i][j] = f(dp[i-1][j], dp[i][j-1], grid[i][j])
5. Return dp[m-1][n-1] (bottom-right corner)
6. (Optional) Space optimize to O(min(m,n)) by keeping only current row

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
    
    How it works:
    1. To reach any cell, robot must come from top or left
    2. Number of paths to cell = paths from top + paths from left
    3. Base case: first row and column's cells can only come from one direction (1 unique path each)
    4. Pattern: dp[i][j] = dp[i-1][j] + dp[i][j-1]
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

TYPICAL STEPS (BOTTOM-UP):
1. Check if problem is solvable (e.g., if sum is odd, can't partition equally)
2. Define target value (e.g., total_sum / 2 for equal partition)
3. Create dp array: dp[j] = "Can we make sum j?"
4. Initialize base case: dp[0] = True (can always make sum 0)
5. For each item:
   - Iterate BACKWARDS from target to item value
   - If dp[j - item] is True, then dp[j] = True
6. Return dp[target]

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
    
    How it works (Bottom-Up):
    1. If total sum is odd, can't partition equally -> return False
    2. Problem becomes: can we find subset with sum = total/2?
    3. Create dp array where dp[j] = "Can we make sum j?"
    4. For each number, iterate backwards updating which sums are achievable
    5. Return dp[target] - can we make the target sum?
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

TYPICAL STEPS:
1. Define dp[i] = length of LIS ending at index i
2. Initialize all dp[i] = 1 (each element is subsequence of length 1)
3. For each position i, check all previous positions j < i:
   - If nums[j] < nums[i], can extend subsequence ending at j
   - dp[i] = max(dp[i], dp[j] + 1)
4. Return max(dp) (longest among all positions)

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
    
    How it works:
    1. dp[i] = length of longest increasing subsequence ending at index i
    2. For each position, look at all previous positions
    3. If previous element is smaller, we can extend its subsequence
    4. Pattern: dp[i] = max(dp[i], dp[j] + 1)
        - Keep current length OR take previous length + 1 (adding current number)
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

TYPICAL STEPS:
1. Define dp[i][j] = LCS length of text1[0:i] and text2[0:j]
2. Base case: dp[0][j] = dp[i][0] = 0 (empty string has LCS 0)
3. For each position (i, j):
   - If text1[i-1] == text2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
   - Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
4. Return dp[m][n]

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
    
    How it works:
    1. Build 2D table where dp[i][j] = LCS of first i chars of text1 and 
    first j chars of text2
    2. If characters match, add 1 to LCS of prev chars: dp[i][j] = dp[i-1][j-1] + 1
    3. If they don't match, take best LCS from excluding either char: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
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

TYPICAL STEPS:
1. Identify all possible states (e.g., hold, sold, cooldown)
2. Define dp[i][state] = optimal value at position i in given state
3. Initialize base cases for each state at position 0
4. For each position, compute transitions between states
5. Return best final state at last position
6. (Optional) Space optimize to keep only current and previous states

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
    
    How it works:
    1. Three states at each day: hold stock, just sold, or resting
    2. Track max profit for each state
    3. Transitions: can only buy from rest, must cooldown after sell
    4. Pattern: 
       - hold = Either I was holding yesterday and I'm still holding today, or I was resting yesterday and I bought today
       - sold = I was holding stock yesterday and sold today
       - rest = Either I was resting yesterday and I'm still resting today, or I sold yesterday so I must rest today
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