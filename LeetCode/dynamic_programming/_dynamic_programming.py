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
    
    m, n = len(grid), len(grid[0]) # "m" = rows, "n" = cols

    # Build DP matrix - create single row with "n" ele's and repeat 
    # this "m" times -> results in "m" rows with "n" columns
    dp = [[0] * n for _ in range(m)] 
    
    # Base case: top-left corner
    dp[0][0] = grid[0][0]

    # Fill first col (can only get to curr cell coming from above)
    for i in range(1, m): # iterate through rows "m" and keep col = 0
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    # Fill first row (can only get to curr cell coming from left)
    for j in range(1, n): # iterate through cols "n" and keep row = 0
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
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
DP APPROACH COMPARISON: TOP-DOWN VS BOTTOM-UP VS SPACE-OPTIMIZED

Problem: Calculate the nth Fibonacci number
Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

Example: fibonacci(6) → 8 (sequence: 0,1,1,2,3,5,8)

THREE APPROACHES:
1. Top-Down (Memoization): Recursive with caching
   - Use when: Recursion feels natural, don't need all subproblems, base cases clear
   - TC: O(n), SC: O(n) memo + O(n) recursion stack

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
    TC: O(n) - each subproblem solved once
    SC: O(n) - memo cache + recursion stack
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

print("Top-Down:", fibonacci_topdown(6)) # Output: 8, 

# ===== APPROACH 2: BOTTOM-UP (TABULATION) =====
def fibonacci_bottomup(n):
    """
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

print("Bottom-Up:", fibonacci_bottomup(6)) # Output: 8, seq: 0,1,1,2,3,5,8

# ===== APPROACH 3: SPACE-OPTIMIZED =====
def fibonacci_space_optimized(n):
    """
    TC: O(n) - same time complexity
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

----------------------------------
WHY USE DP INSTEAD OF BRUTE FORCE?
----------------------------------
DP transforms exponential time into polynomial time by remembering solutions to subproblems.

KEY INSIGHT: Brute force solves the same subproblem thousands of times. 
DP solves each subproblem once and stores the result.

1. SIMPLE EXAMPLE: FIBONACCI
   
   Problem: Calculate fib(6) where fib(n) = fib(n-1) + fib(n-2)
   
   BRUTE FORCE - O(2^n):
   - fib(6) calls fib(5) and fib(4)
   - fib(5) calls fib(4) and fib(3)
   - fib(4) calls fib(3) and fib(2)
   - Notice: fib(4) computed twice, fib(3) computed 3 times, fib(2) computed 5 times!
   - Total calls for fib(6): 25 function calls
   - Total calls for fib(20): 21,891 function calls
   - TC: O(2^n) - grows exponentially
   
   WITH DP - O(n):
   - Store fib(2), fib(3), fib(4), etc. in a cache
   - When fib(4) is needed again, just look it up
   - Each fib(i) computed exactly once
   - Total calls for fib(6): 6 function calls
   - Total calls for fib(20): 20 function calls
   - TC: O(n) - linear time
   - For n=20: 21,891 → 20 operations (1,094x faster!)

2. ORDERING EXAMPLE: SHORTEST PATH THROUGH CITIES
   
   Problem: Visit cities A, B, C, D and return to start. What's the shortest total distance?
   
   BRUTE FORCE - O(n!):
   - Try every possible ordering of cities
   - Starting from A:
     * A → B → C → D → A (distance = 50)
     * A → B → D → C → A (distance = 45)
     * A → C → B → D → A (distance = 60)
     * A → C → D → B → A (distance = 55)
     * A → D → B → C → A (distance = 48)
     * A → D → C → B → A (distance = 52)
   - That's 3! = 6 orderings to check (for 3 cities after start)
   
   The Problem: Recalculates same partial paths repeatedly
   - Route "A → B → C → ?" recalculates "A → B" cost
   - Route "A → C → B → ?" also recalculates "A → B" cost (when going B→A at end)
   - Route "A → D → B → C → ?" recalculates "B → C" cost
   - Same segments computed over and over through different orderings
   
   TC: O(n!) - factorial growth
   - 4 cities: 3! = 6 orderings
   - 10 cities: 9! = 362,880 orderings
   - 15 cities: 14! = 87 billion orderings
   
   WITH DP - O(n² x 2^n):
   - Cache: "What's the shortest path from city X, having visited cities S?"
   - Example states:
     * From B, visited {A,B}: shortest to finish = 30
     * From C, visited {A,C}: shortest to finish = 35
     * From B, visited {A,B,C}: shortest to finish = 20
   
   The Win: Each (current_city, visited_set) computed once and reused
   - "From B, visited {A,B}" computed once, not 6 times
   - Total unique states: 4 cities x 2^4 visited combinations = 64 states
   
   TC: O(n² x 2^n) where n = number of cities
   - 4 cities: 4² x 2^4 = 256 operations vs 6 orderings (similar for small n)
   - 15 cities: 15² x 2^15 = 7.4 million vs 87 billion (11,700x faster!)
   
   Real savings appear at n ≥ 10 where factorial growth becomes impossible

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
        SC: 
        - O(n) - with DP array, store n values in the 
        - O(1) - space optimized - only keep track of last 2 values
        """
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
            dp[i][0] = 1  # Set first col (col 0) in each row
        
        # Base case: first row - only one way to reach (go right)
        for j in range(n):  # Iterate through all n cols and row stays 0
            dp[0][j] = 1  # Set first row (row 0) in each col
        
        # Fill the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                # Total unique paths to current = paths from above + paths from l
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
    
    # Space-optimized version: O(n) space 
    # Key Insight: We only ever need the previous row and current row to compute values. We don't need the entire 2D grid!
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
PATTERN 3: 0/1 KNAPSACK (SUBSET SELECTION) - TOP-DOWN APPROACH

PATTERN EXPLANATION: Choose items to include or exclude to meet a target constraint (sum, weight, capacity). Each item can be used at most once. 

Use recursion with memoization to explore both choices (include/exclude) for each item, starting from the problem goal and working down to base cases.

TYPICAL STEPS (TOP-DOWN):
1. Define recursive function: can_make(i, remaining) = can we achieve 'remaining' using items from index i onwards?
2. Base cases: 
   - remaining == 0: True (found exact match)
   - remaining < 0 or i >= n: False (overshot or ran out of items)
3. For each item at index i:
   - Option 1: include item -> can_make(i+1, remaining - item)
   - Option 2: exclude item -> can_make(i+1, remaining)
4. Memoize results using (i, remaining) as key
5. Return result of recursive call starting at index 0

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
    
    How it works (Top-Down):
    1. If total sum is odd, can't partition equally -> return False
    2. Problem becomes: can we find subset with sum = total/2?
    3. For each number in the array, make a choice: include it or exclude it
    4. Recursively check if remaining sum can be made with remaining numbers
    5. Memoize (index, remaining_sum) to avoid recomputing same subproblems
    """
    def canPartition(self, nums: List[int]) -> bool: # LC 416
        """
        TC: O(n * sum) where sum = total sum / 2
        SC: O(n * sum) - recursion stack + memoization cache
        """
        total = sum(nums)
        
        # If total is odd, impossible to split equally
        if total % 2 != 0:
            return False
        
        target = total // 2
        memo = {} # key=(index, remaining_sum), val=bool
        
        def can_make_sum(index, remaining_sum):
            """
            Question: Can we make 'remaining_sum' using numbers from "index" onwards?
            
            Example: can_make_sum(0, 11) asks:
            "Can I make sum=11 using all numbers starting from index 0?" -> [1,5,11,5]
            """
            
            # BASE CASE 1 -> SUCCESS: We've made exactly the target sum!
            if remaining_sum == 0:
                return True
            
            # BASE CASE 2 -> FAILURE: Either went negative or ran out of numbers
            if remaining_sum < 0 or index >= len(nums):
                return False
            
            # Already solved this subproblem? Return cached answer
            if (index, remaining_sum) in memo:
                return memo[(index, remaining_sum)]
            
            current_number = nums[index]
            
            # CHOICE 1: Include curr number in subset
            # - Use the number, so subtract it from remaining_sum, move to next number (index + 1)
            take_it = can_make_sum(index + 1, remaining_sum - current_number)
            
            # CHOICE 2: Exclude current num from subset
            # - Don't use the number, so remaining_sum stays samem, move to next number (index + 1)
            skip_it = can_make_sum(index + 1, remaining_sum)
            
            # Success if EITHER choice works
            result = take_it or skip_it
            
            # Cache the result for this subproblem - Can we make remaining_sum using numbers from index onwards?
            memo[(index, remaining_sum)] = result
            
            return result
        
        # Start at index 0 with full target sum to make
        return can_make_sum(0, target)

# Example trace:
# nums = [1, 5, 11, 5], target = 11
#
# can_make_sum(0, 11): "Can I make 11 using [1,5,11,5]?"
#   take_it: can_make_sum(1, 10): "Can I make 10 using [5,11,5]?"
#     take_it: can_make_sum(2, 5): "Can I make 5 using [11,5]?"
#       take_it: can_make_sum(3, -6) -> False (went negative)
#       skip_it: can_make_sum(3, 5): "Can I make 5 using [5]?"
#         take_it: can_make_sum(4, 0) -> True! ✓ (found exact match)
#
# Found subset: [1, 5, 5] = 11
# Other subset: [11] = 11
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
    4. Pattern: dp[i] = max(dp[j] + 1) for all j < i where nums[j] < nums[i]
    """
    def lengthOfLIS(self, nums: List[int]) -> int: # LC 300
        """
        TC: O(n²) - for each element, check all previous elements
        SC: O(n) - dp array
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

# Example:
# nums = [10, 9, 2, 5, 3, 7, 101, 18]
#
# DP progression:
# Index:  0   1  2  3  4  5   6    7
# nums:  10   9  2  5  3  7  101  18
# dp:    [1]  1  1  1  1  1   1    1   (initial)
# 
# i=1 (9): 9 > 10? No. dp[1] = 1
# i=2 (2): 2 > 10? No, 2 > 9? No. dp[2] = 1 (no extension)
# i=3 (5): 5 > 10? No, 5 > 9? No, 5 > 2? Yes. dp[3] = dp[2] + 1 = 2 [2,5]
# i=4 (3): 3 > 10? No, 3 > 9? No, 3 > 2? Yes. dp[4] = dp[2] + 1 = 2 [2,3]
# i=5 (7): 7 > 10? No, 7 > 9? No, 7 > 2? Yes. dp[5] = max(1, dp[2] + 1) = 2
#          7 > 5? Yes. dp[5] = max(2, dp[3] + 1) = 3 [2,5,7]
#          7 > 3? Yes. dp[5] = max(3, dp[4] + 1) = 3
# i=6 (101): 101 > 10? Yes. dp[6] = max(1, dp[0] + 1) = 2
#            101 > 9? Yes. dp[6] = max(2, dp[1] + 1) = 2
#            101 > 2? Yes. dp[6] = max(2, dp[2] + 1) = 2
#            101 > 5? Yes. dp[6] = max(2, dp[3] + 1) = 3
#            101 > 3? Yes. dp[6] = max(3, dp[4] + 1) = 3
#            101 > 7? Yes. dp[6] = max(3, dp[5] + 1) = 4 [2,5,7,101]
# i=7 (18): 18 > 10? Yes. dp[7] = max(1, dp[0] + 1) = 2
#           18 > 9? Yes. dp[7] = max(2, dp[1] + 1) = 2
#           18 > 2? Yes. dp[7] = max(2, dp[2] + 1) = 2
#           18 > 5? Yes. dp[7] = max(2, dp[3] + 1) = 3
#           18 > 3? Yes. dp[7] = max(3, dp[4] + 1) = 3
#           18 > 7? Yes. dp[7] = max(3, dp[5] + 1) = 4 [2,5,7,18]
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
    2. If characters match, add 1 to LCS of previous characters
    3. If they don't match, take best from excluding either character
    4. Pattern: if match: dp[i][j] = dp[i-1][j-1] + 1
               else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    """
    def longestCommonSubsequence(self, text1: str, text2: str) -> int: # LC 1143
        """ 
        TC: O(m * n) - fill entire 2D table
        SC: O(m * n) - 2D dp table (can optimize to O(min(m,n)))
        """
        m, n = len(text1), len(text2)
        
        # dp[i][j] = LCS length of text1[0:i] and text2[0:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]: # index off by one
                    # Characters match - extend LCS from previous chars
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # Characters don't match - take best of two options:
                    # - exclude current char from text1 (dp[i-1][j])
                    # - exclude current char from text2 (dp[i][j-1])
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]

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
    Problem: You are given an array prices where prices[i] is the price of a stock on day i.

    You can complete as many transactions as you like with the following restrictions: After you sell your stock, you cannot buy stock on the next day (cooldown 1 day)
    
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
       - hold = max(hold, rest - price)
       - sold = hold + price
       - rest = max(rest, sold)
    """
    def maxProfit_2d(self, prices: List[int]) -> int: # LC 309
        """
        TC: O(n) -> loop through n days
        SC: O(n) -> create 2d array of size n * 3
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
            dp[i][0] = max(dp[i-1][0], # Continue holding -> You already held stock yesterday
                           dp[i-1][2] - prices[i]) # Buy today -> You were resting yesterday, buy today
            
            # Sold state: only one way to be in sold state
            dp[i][1] = dp[i-1][0] + prices[i] # Must have been holding stock yesterday and sell today
            
            # Rest state: find most profitable way to be resting
            dp[i][2] = max(dp[i-1][2], # Continue resting -> You were already resting yesterday
                           dp[i-1][1]) # Enter cooldown -> you sold yesterday and now must cooldown
        
        # Return max of sold or rest on last day
        return max(dp[n-1][1], dp[n-1][2])

sol = StateMachineDP()
print("Max profit with cooldown:", sol.maxProfit_2d([1,2,3,0,2]))  # 3
print("Max profit with cooldown:", sol.maxProfit_2d([1]))  # 0