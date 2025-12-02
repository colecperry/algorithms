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
    Find maximum sum of any contiguous subarray (Kadane's Algorithm). A contiguous subarray is a sequence of ele's that appear consecutively in the original array - no skipping or reordering allowed.
    
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
========================================================================
2D DP TEMPLATE (GRID/TABLE)
    - Use for: Grid traversal problems, comparing two sequences (LCS, edit distance), or problems where the state depends on two variables (i, j).
    - Pattern: Build a table where each cell dp[i][j] depends on prev cells (typically from above dp[i-1][j], from left dp[i][j-1], or diagonal dp[i-1][j-1]).
    - Common problems: Unique paths, minimum path sum, longest common subsequence, edit distance, matrix chain multiplication.
========================================================================
"""

def min_path_sum(grid):
    """
    Find minimum sum path from top-left to bottom-right in a grid of numbers. Can only move right or down. Each cell stores the minimum cost to reach it.
    
    Example: [[1,3,1],
              [1,5,1],
              [4,2,1]] → 7 (path: 1→3→1→1→1)
    
    TC: O(m * n) - process each cell once
    SC: O(m * n) - dp table same size as grid
    """
    if not grid or not grid[0]: # Edge cases - empty matrix/first row
        return 0
    
    m, n = len(grid), len(grid[0])

    # Build DP matrix - create single row with "n" zero's and repeat 
    # this "m" times -> results in "m" rows with "n" columns
    dp = [[0] * n for _ in range(m)] 
    
    # Base case: top-left corner
    dp[0][0] = grid[0][0]
    
    # Fill first row (can only get to curr grid cell coming from left)
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    # Fill first col (can only get to curr grid cell coming from above)
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    # Fill rest of table: take minimum of top or left path + curr
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[m-1][n-1] # Bottom right of DP table = min sum path


# Test
grid = [[1,3,1],
        [1,5,1],
        [4,2,1]]
print(min_path_sum(grid))  # Output: 7

"""
=========================================================================
TOP-DOWN DP TEMPLATE (MEMOIZATION)
    - Use for: When recursion feels natural for the problem (break into smaller subproblems), you don't need to compute all subproblems (memo only computes what it needs), and when the base cases are clear but the iteration order isn't obvious
    - Pattern: Write recursive solution first, then add memoization to avoid recomputing. Start from the main problem and work down to base cases, caching results along the way.
    - Common problems: Fibonacci, climbing stairs, coin change, longest increasing subsequence,tree DP problems, any problem where you naturally think "solve for n using n-1, n-2...".
=========================================================================
"""
def dp_topdown_template(n):
    """
    Calculate the nth Fibonacci number using top-down DP with memoization. Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
    
    Example: fibonacci(6) → 8 (sequence: 0,1,1,2,3,5,8)
    
    TC: O(n) - each subproblem solved once
    SC: O(n) - memo cache + recursion stack
    """
    memo = {} # memo is a dict that maps the nth position to it's fib val
    
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

# Test
print(dp_topdown_template(6))   # Output: 8

"""
=========================================================================
BOTTOM-UP DP TEMPLATE (TABULATION)
    - Use for: When you need to compute all or most subproblems anyways, when the iteration order is clear, and when you want to avoid recursion stack overflow for large inputs
    - Pattern: Start from base cases and build up to the final answer using a table/array. Fill dp array in order so each state uses only previously computed states.
    - Common problems: Fibonacci, climbing stairs, house robber, coin change, knapsack, maximum subarray. Generally more space-efficient than top-down (can optimize to O(1)).
=========================================================================
"""
def fibonacci_bottomup(n):
    """
    Calculate the nth Fibonacci number using bottom-up DP with tabulation. Build from base cases (fib(0)=0, fib(1)=1) up to fib(n) iteratively.
    
    Example: fibonacci_bottomup(6) → 8 (sequence: 0,1,1,2,3,5,8)
    
    TC: O(n) - iterate through all states
    SC: O(n) - dp array
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


# Test
print(fibonacci_bottomup(6))   # Output: 8
print(fibonacci_bottomup(10))  # Output: 55

# =========================================================================
# SPACE-OPTIMIZED DP TEMPLATE
# =========================================================================
def fib_space_optimized(n):
    """
    Space-optimized DP when only need previous few states
    TC: O(n) - same time complexity
    SC: O(1) - constant space (only store last 2 values)
    """
    if n <= 1:
        return n
    
    # Only keep last 2 values instead of entire array
    prev2 = 0
    prev1 = 1
    
    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1  # Move pointers forward
        prev1 = current
    
    return prev1

# Test
print(fib_space_optimized(6))   # Output: 8
print(fib_space_optimized(10))  # Output: 55

"""
TIME & SPACE COMPLEXITY REFERENCE
==================================

COMMON DP PATTERNS COMPLEXITY:
-----------------------------
+---------------------+-----------------+------------------+------------------+
| Pattern             | Time Complexity | Space Complexity | Space Optimized  |
+---------------------+-----------------+------------------+------------------+
| 1D Linear DP        | O(n)            | O(n)             | O(1)             |
| 2D Grid DP          | O(m * n)        | O(m * n)         | O(min(m,n))      |
| 0/1 Knapsack        | O(n * W)        | O(n * W)         | O(W)             |
| Unbounded Knapsack  | O(n * W)        | O(W)             | O(W)             |
| LIS (DP solution)   | O(n²)           | O(n)             | O(n)             |
| LIS (Binary Search) | O(n log n)      | O(n)             | O(n)             |
| LCS (Two sequences) | O(m * n)        | O(m * n)         | O(min(m,n))      |
| Edit Distance       | O(m * n)        | O(m * n)         | O(min(m,n))      |
| State Machine DP    | O(n * k)        | O(n * k)         | O(k)             |
| Partition Problems  | O(n * sum)      | O(n * sum)       | O(sum)           |
+---------------------+-----------------+------------------+------------------+

WHERE:
- n, m = input array/string lengths
- W = knapsack capacity or target sum
- k = number of states in state machine
- sum = target sum or array sum

COMPLEXITY NOTES:
----------------
1. 1D Linear DP: O(n) time, O(n) space
   - Process each element once: O(n)
   - Store solution for each position: O(n)
   
   Space optimization:
   - If dp[i] only depends on dp[i-1] and dp[i-2], keep only last 2 vals
   - Reduces from O(n) to O(1) space
   - Examples: Fibonacci, House Robber, Climbing Stairs
   
   Common pattern: dp[i] = f(dp[i-1], dp[i-2], ..., nums[i])

2. 2D Grid DP: O(m * n) time, O(m * n) space
   - Fill entire m x n table: O(m * n)
   - Store solution for each cell: O(m * n)
   
   Space optimization:
   - If dp[i][j] only depends on current and previous row, keep only 2 rows
   - Reduces from O(m * n) to O(min(m, n)) space
   - Examples: Unique Paths, Minimum Path Sum
   
   Common pattern: dp[i][j] = f(dp[i-1][j], dp[i][j-1], grid[i][j])

3. Knapsack Problems: O(n * W) time
   - n items, W = capacity or target sum
   - For each item, try all possible capacities: O(n * W)
   
   0/1 Knapsack (each item once):
   - 2D: O(n * W) space - dp[i][w] = include/exclude item i at capacity w
   - 1D optimized: O(W) space - process backwards to avoid using same item twice
   
   Unbounded Knapsack (items unlimited):
   - 1D: O(W) space - process forwards, items can be reused
   
   Common pattern: dp[w] = max(dp[w], dp[w-weight] + value)

4. Longest Increasing Subsequence (LIS): Two approaches
   
   DP approach: O(n²) time, O(n) space
   - For each element, check all previous elements: O(n²)
   - dp[i] = length of LIS ending at index i
   
   Binary Search approach: O(n log n) time, O(n) space
   - Maintain array of smallest tail elements
   - Binary search for insertion position: O(log n) per element
   - More efficient but less intuitive
   
   Common pattern: dp[i] = max(dp[j] + 1) for all j < i where nums[j] < nums[i]

5. Longest Common Subsequence (LCS): O(m * n) time
   - Compare every character of both strings: O(m * n)
   - dp[i][j] = LCS length of first i chars of s1 and first j chars of s2
   
   Space optimization:
   - Only need previous row, reduce to O(min(m, n))
   
   Common pattern:
   - If s1[i] == s2[j]: dp[i][j] = dp[i-1][j-1] + 1
   - Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

6. State Machine DP: O(n * k) time, O(n * k) space
   - n positions/days, k possible states at each position
   - For each position, process each state: O(n * k)
   
   Space optimization:
   - If states only depend on previous position, keep only last position
   - Reduces from O(n * k) to O(k) space
   
   Common in: Stock trading (buy/sell/cooldown), game states
   Pattern: dp[i][state] = best result at position i in given state

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
    
    TC: O(n) - process each house once
    SC: 
        - O(n) - with DP array, store n values in the 
        - O(1) - space optimized - only keep track of last 2 values 
    
    How it works:
    1. At each house, decide: rob it or skip it
    2. If rob current: can't rob prev, so add to max from 2 houses ago
    3. If skip current: take max from previous house
    4. Pattern: dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    """
    # 1D DP with explicit DP array -> LC 198
    def rob_with_dp_array(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)  # Max money we can rob up to each house
        dp[0] = 0  # No houses robbed = $0
        dp[1] = nums[0]  # Rob first house only

        for i in range(2, n + 1):
            # Either skip current house (take prev max) OR rob current house + take max from 2 houses back
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])

        return dp[-1] # Max money after considering all houses
    
    # 1D DP with space optimization -> O(1) space
    def rob_with_space_op(self, nums: List[int]) -> int: 
        if len(nums) == 1: # Edge case -> can only rob one house
            return nums[0]
        
        prev2 = 0         # Max money 2 houses back
        prev1 = nums[0]   # Max money 1 house back
        
        for i in range(1, len(nums)):
            # Either skip current (keep prev1) OR rob current + prev2
            curr = max(prev1, prev2 + nums[i])
            prev2 = prev1  # Shift window forward
            prev1 = curr
        
        return prev1  # Max money after all houses

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

print("House Robber:", sol.rob_with_space_op([2,7,9,3,1]))  # 12
print("House Robber:", sol.rob_with_space_op([1,2,3,1]))  # 4

"""
=========================================================================
PATTERN 2: 2D GRID DP (PATH PROBLEMS)

PATTERN EXPLANATION: Navigate a 2D grid where each cell's value depends on cells above and/or to the left. Build solution by filling grid from top-left to bottom-right. Each cell represents optimal solution to reach that position. Common in counting paths, finding minimum/maximum path sums, or grid traversal with constraints.

TYPICAL STEPS:
1. Define dp[i][j] = solution for cell (i, j)
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
    
    TC: O(m * n) - fill entire grid once
    SC: O(m * n) - 2D dp table (can optimize to O(min(m,n)))
    
    How it works:
    1. To reach any cell, robot must come from top or left
    2. Number of paths to cell = paths from top + paths from left
    3. Base case: first row and column have only 1 path each
    4. Pattern: dp[i][j] = dp[i-1][j] + dp[i][j-1]
    """
    def uniquePaths(self, m: int, n: int) -> int: # LC 62
        # Initialize dp table -> m = rows, n = cols
        dp = [[0] * n for _ in range(m)]
        
        # Base case: first col - only one way to reach (go down)
        for i in range(m):  # Iterate through all m rows
            dp[i][0] = 1  # Set first col (col 0) in each row
        
        # Base case: first row - only one way to reach (go right)
        for j in range(n):  # Iterate through all n cols
            dp[0][j] = 1  # Set first row (row 0) in each col
        
        # Fill the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                # Paths to current = paths from above + paths from l
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
    
    # Space-optimized version: O(n) space
    def uniquePaths_optimized(self, m: int, n: int) -> int:
        # Only keep current row, previous row is implicit
        dp = [1] * n  # First row all 1s
        
        for i in range(1, m):
            for j in range(1, n):
                # dp[j] currently holds value from prev row (above)
                # dp[j-1] holds value from current row (left)
                dp[j] = dp[j] + dp[j-1]
        
        return dp[n-1]

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
print("Unique Paths optimized (3x3):", sol.uniquePaths_optimized(3, 3))  # 6

"""
=========================================================================
PATTERN 3: 0/1 KNAPSACK (SUBSET SELECTION)

PATTERN EXPLANATION: Choose items to include or exclude to meet a target constraint (sum, weight, capacity). Each item can be used at most once. 

Build solution by considering each item and deciding whether to include it. Often involves checking if a specific target sum or capacity is achievable using a subset of items.

TYPICAL STEPS:
1. Define dp[i][sum] = can we achieve sum using first i items
2. Base case: dp[0][0] = True (empty set has sum 0)
3. For each item, for each possible sum:
   - Option 1: exclude item -> dp[i][sum] = dp[i-1][sum]
   - Option 2: include item -> dp[i][sum] = dp[i-1][sum-item]
4. Return dp[n][target]
5. (Optional) Space optimize to O(target) by using 1D array

Applications: Partition equal subset, target sum, subset sum, coin change 
(count ways).
=========================================================================
"""

class KnapsackDP:
    """
    Problem: Given an integer array nums, return true if you can 
    partition the array into two subsets such that the sum of elements in both subsets is equal.
    
    TC: O(n * sum) where sum = total sum / 2
    SC: O(sum) - 1D dp array (space optimized)
    
    How it works:
    1. If total sum is odd, can't partition equally
    2. Problem becomes: can we find subset with sum = total/2
    3. This is 0/1 knapsack: for each number, include or exclude
    4. dp[s] = can we achieve sum s using available numbers
    5. Pattern: dp[s] = dp[s] OR dp[s-num] (exclude or include current num)
    """
    # 2D version (easier to understand but more space)
    def canPartition(self, nums: List[int]) -> bool: # LC 416
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        n = len(nums)
        
        # dp[i][s] = can we achieve sum s using first i numbers
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        
        # Base case: sum 0 is always achievable (empty subset)
        for i in range(n + 1):
            dp[i][0] = True
        
        for i in range(1, n + 1):
            for s in range(1, target + 1):
                # Option 1: don't include current number
                dp[i][s] = dp[i-1][s]
                
                # Option 2: include current number (if it fits)
                if s >= nums[i-1]:
                    dp[i][s] = dp[i][s] or dp[i-1][s - nums[i-1]]
        
        return dp[n][target]

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
    
    TC: O(n²) - for each element, check all previous elements
    SC: O(n) - dp array
    
    Note: There's an O(n log n) solution using binary search, but DP is 
    more intuitive.
    
    How it works:
    1. dp[i] = length of longest increasing subsequence ending at index i
    2. For each position, look at all previous positions
    3. If previous element is smaller, we can extend its subsequence
    4. Pattern: dp[i] = max(dp[j] + 1) for all j < i where nums[j] < nums[i]
    """
    def lengthOfLIS(self, nums: List[int]) -> int: # LC 300
        if not nums:
            return 0
        
        n = len(nums)
        # dp[i] = length of LIS ending at index i
        dp = [1] * n  # Each element by itself is a subsequence of length 1
        
        # For each position
        for i in range(1, n):
            # Check all previous positions
            for j in range(i):
                # If previous element is smaller, can extend its subsequence
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # Return the longest subsequence found at any position
        return max(dp)

# Example:
# nums = [10, 9, 2, 5, 3, 7, 101, 18]
#
# DP progression:
# Index:  0   1  2  3  4  5   6    7
# nums:  10   9  2  5  3  7  101  18
# dp:    [1]  1  1  1  1  1   1    1   (initial)
# 
# i=1 (9): 9 < 10? No. dp[1] = 1
# i=2 (2): 2 < 10? Yes, 2 < 9? Yes. dp[2] = 1 (no extension)
# i=3 (5): 5 < 2? No, but 5 > 2. dp[3] = dp[2] + 1 = 2 [2,5]
# i=4 (3): 3 > 2. dp[4] = dp[2] + 1 = 2 [2,3]
# i=5 (7): 7 > 5. dp[5] = dp[3] + 1 = 3 [2,5,7]
# i=6 (101): 101 > 7. dp[6] = dp[5] + 1 = 4 [2,5,7,101]
# i=7 (18): 18 > 7. dp[7] = dp[5] + 1 = 4 [2,5,7,18]
#
# Final dp: [1, 1, 1, 2, 2, 3, 4, 4]
# LIS: [2, 5, 7, 101] or [2, 5, 7, 18]
# Output: 4

sol = LISDP()
print("LIS length:", sol.lengthOfLIS([10,9,2,5,3,7,101,18]))  # 4
print("LIS length:", sol.lengthOfLIS([0,1,0,3,2,3]))  # 4

"""
=========================================================================
PATTERN 5: LONGEST COMMON SUBSEQUENCE (TWO SEQUENCES)

PATTERN EXPLANATION: Find the longest subsequence common to two sequences 
while maintaining relative order in both. Compare characters from both 
strings and build solution in a 2D table. When characters match, extend 
the common subsequence. When they don't match, take the best result from 
either excluding current character from first string or second string.

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
    Problem: Given two strings text1 and text2, return the length of 
    their longest common subsequence. If there is no common subsequence, 
    return 0.
    
    A subsequence is a string generated from the original string by 
    deleting some (or no) characters without changing the relative order 
    of the remaining characters.
    
    TC: O(m * n) - fill entire 2D table
    SC: O(m * n) - 2D dp table (can optimize to O(min(m,n)))
    
    How it works:
    1. Build 2D table where dp[i][j] = LCS of first i chars of text1 and 
    first j chars of text2
    2. If characters match, add 1 to LCS of previous characters
    3. If they don't match, take best from excluding either character
    4. Pattern: if match: dp[i][j] = dp[i-1][j-1] + 1
               else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    """
    def longestCommonSubsequence(self, text1: str, text2: str) -> int: # LC 1143
        m, n = len(text1), len(text2)
        
        # dp[i][j] = LCS length of text1[0:i] and text2[0:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    # Characters match - extend LCS from previous chars
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # Characters don't match - take best of two options:
                    # - exclude current char from text1 (dp[i-1][j])
                    # - exclude current char from text2 (dp[i][j-1])
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]
    
    # Space-optimized version: O(min(m,n))
    def longestCommonSubsequence_optimized(self, text1: str, text2: str) -> int:
        # Make text1 the shorter string for space optimization
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        
        m, n = len(text1), len(text2)
        
        # Only keep current and previous row
        prev = [0] * (n + 1)
        curr = [0] * (n + 1)
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    curr[j] = prev[j-1] + 1
                else:
                    curr[j] = max(prev[j], curr[j-1])
            
            prev, curr = curr, prev
        
        return prev[n]

# Example:
# text1 = "abcde"
# text2 = "ace"
#
# DP table:
#     ""  a  c  e
# ""  0   0  0  0
# a   0   1  1  1    'a' matches: dp[1][1] = dp[0][0] + 1 = 1
# b   0   1  1  1    'b' no match: max(dp[0][1], dp[1][0]) = 1
# c   0   1  2  2    'c' matches: dp[2][2] = dp[1][1] + 1 = 2
# d   0   1  2  2    'd' no match: max(dp[2][2], dp[3][1]) = 2
# e   0   1  2  3    'e' matches: dp[4][3] = dp[3][2] + 1 = 3
#
# LCS: "ace"
# Output: 3

sol = LCSDP()
print("LCS length:", sol.longestCommonSubsequence("abcde", "ace"))  # 3
print("LCS length:", sol.longestCommonSubsequence("abc", "abc"))  # 3
print("LCS length:", sol.longestCommonSubsequence("abc", "def"))  # 0

"""
=========================================================================
PATTERN 6: STATE MACHINE DP (MULTIPLE STATES)

PATTERN EXPLANATION: Track multiple distinct states at each position with 
transitions between states. Each state represents a different condition 
or situation (holding stock, cooldown, sold, etc). At each step, can 
transition from one state to another with associated costs or profits. 
Must track optimal value for each state and compute transitions based on
allowed moves.

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
    Problem: You are given an array prices where prices[i] is the price of 
    a stock on day i.

    You can complete as many transactions as you like with the following 
    restrictions: After you sell your stock, you cannot buy stock on the 
    next day (cooldown 1 day)
    
    Return the maximum profit you can achieve.
    
    TC: O(n) - process each day once, update all states
    SC: O(1) - only keep track of 3 states (space optimized)
    
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
       - hold = max(hold, rest - price)
       - sold = hold + price
       - rest = max(rest, sold)
    """
    def maxProfit(self, prices: List[int]) -> int: # LC 309
        if not prices:
            return 0
        
        # States: hold = holding stock, sold = just sold, rest = resting/cooldown
        hold = float('-inf')  # Initially can't be holding (no stock bought yet)
        sold = float('-inf')  # Initially can't have sold
        rest = 0  # Initially resting with 0 profit
        
        for price in prices:
            # Save previous values (needed for transitions)
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest
            
            # Update states based on transitions
            # Hold: either already holding, or buy today from rest state
            hold = max(prev_hold, prev_rest - price)
            
            # Sold: must have been holding, sell today
            sold = prev_hold + price
            
            # Rest: either already resting, or cooldown from just sold
            rest = max(prev_rest, prev_sold)
        
        # Return max profit from non-holding states (sold or rest)
        return max(sold, rest)
    
    # Alternative: explicit 2D DP (easier to visualize)
    def maxProfit_2d(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        # dp[i][state] where state: 0=hold, 1=sold, 2=rest
        dp = [[0] * 3 for _ in range(n)]
        
        # Base case: day 0
        dp[0][0] = -prices[0]  # Buy on day 0
        dp[0][1] = 0  # Can't sell on day 0 (nothing to sell)
        dp[0][2] = 0  # Rest on day 0
        
        for i in range(1, n):
            # Hold: either already holding, or buy today from rest
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            
            # Sold: must have been holding, sell today
            dp[i][1] = dp[i-1][0] + prices[i]
            
            # Rest: either already resting, or cooldown from sold
            dp[i][2] = max(dp[i-1][2], dp[i-1][1])
        
        # Return max of sold or rest on last day
        return max(dp[n-1][1], dp[n-1][2])

# Example:
# prices = [1, 2, 3, 0, 2]
#
# Day 0 (price=1):
#   hold = -1 (buy at 1)
#   sold = -inf (can't sell nothing)
#   rest = 0
#
# Day 1 (price=2):
#   hold = max(-1, 0-2) = -1 (keep holding)
#   sold = -1 + 2 = 1 (sell, profit 1)
#   rest = max(0, -inf) = 0
#
# Day 2 (price=3):
#   hold = max(-1, 0-3) = -1 (keep holding)
#   sold = -1 + 3 = 2 (sell, profit 2)
#   rest = max(0, 1) = 1 (cooldown from previous sell)
#
# Day 3 (price=0):
#   hold = max(-1, 1-0) = 1 (buy at 0 from rest state, overall profit 1)
#   sold = -1 + 0 = -1
#   rest = max(1, 2) = 2
#
# Day 4 (price=2):
#   hold = max(1, 2-2) = 1
#   sold = 1 + 2 = 3 (sell, total profit 3)
#   rest = max(2, -1) = 2
#
# Best strategy: buy at 1, sell at 2, cooldown, buy at 0, sell at 2
# Profit: (2-1) + (2-0) = 3
# Output: 3

sol = StateMachineDP()
print("Max profit with cooldown:", sol.maxProfit([1,2,3,0,2]))  # 3
print("Max profit with cooldown:", sol.maxProfit([1]))  # 0