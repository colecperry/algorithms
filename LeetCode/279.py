# 279. Perfect Squares

# Given an integer n, return the least number of perfect square numbers that sum to n.

# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.


# Example 1:
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.

# Example 2:
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

# How to solve:
# Use Dynamic Programming because:
# Optimal Substructure: The solution for n can be built using solutions for smaller values of n
# Overlapping Subproblems: Many subproblems are solved repeatedly

# Code in detail -> 
# def numSquares(self, n) -> function numSquares takes in an Integer n, which represents the number we need to use to find the least number of perfect squares that sum to it
# dp = [n] * (n+1) -> Create a dynamic programming array. Each index represents the minimum number of perfect squares that sum to i. For index 1, the value represents the minimum number of perfect squares that sum to 1. We initially set each index to n, which is the worst case value for n (the worst case number of perfect squares for n = 4 is 4, because 1*1*1*1 = 4). 
# dp[0] = 0 -> This is the base case because the number 0 can be represented as the sum of zero perfect squares. For n = 4, the list would be [0, 4, 4, 4, 4]
# for target in range(1, n + 1) -> The outer loop iterates over all values from 1 to n, solving for dp[target] incrementally. Each number (target) represents the number for which we are calculating the min number of perfect squares. For n = 5, the target values will be 1, 2, 3, 4, 5
# for s in range(1, target + 1) -> Inner loop iterates over integers s from 1 to target. For target = 5, the loop would iterate over s = 1, 2, 3, 4, 5
# square = s * s -> Compute the square of s for each iteration. For s = 1, 2, 3, 4, 5, the square would be 1, 4, 9, 16, 25. For target = 5 and s = 2, square = 4
# if target - square < 0 -> If subtracting target from square results in a negative value, break. For example for target = 5 and s = 3, target - square = -4 which is less than zero, so the loop breaks
# dp[target = min(dp[target], 1 + dp[target - square])] -> Update dp[target] by taking the minimum of it's current value and 1 + dp[target - square]. 1 accounts for the current perfect square s^2 and dp[target - square] is the result for the remaining sum
# For any target, the formaula ensures we are always building on the optimal solution for smaller problems (target - square). When we add "1" to the count becasuer we are using one perfect square. 
# dp[target - square] already contains the minimum number of squares required to su  because of memoization
# return dp[n] -> after filling the dp array, dp[n] contains the minimum number of perfet squares that sum to n


class Solution(object):
    def numSquares(self, n):
        dp = [n] * (n+1) # Create a list where dp[i] represents the min number of perfect squares that sum to i
        dp[0] = 0 # Set base case

        for target in range(1, n + 1): # Outer loop: Iterate over all values in the array
            for s in range(1, target + 1): # Inner loop: Iterate over the arrays again
                square = s * s # Take the square of each index
                if target - square < 0: # Only iterate up the point where the square isn't bigger than the target
                    break
                dp[target] = min(dp[target], 1 + dp[target - square]) # Make the index in dp array equal to the min of the current value and the value of 1 + dp[target - square] (smaller problem)
        return dp[n] # Return the array of element n

my_solution = Solution()
print(my_solution.numSquares(12))
print(my_solution.numSquares(13))


# Run the problem all the way through for 
# initialize array as [0, 5, 5, 5, 5, 5 ]

# Enter loops

# Outer loop: target = 1
# Inner loop: s = 1
# square = 1
# target - square = 1 - 1 = 0 (valid)
# dp[1] = min(dp[1], 1 + dp[0]) = min(5, 1 + 0) = 1
# dp = [0, 1, 5, 5, 5, 5]

# Outer loop: target = 2
# Inner loop: s = 1
# square = 1
# target - square = 2 - 1 = 1 (valid)
# dp[2] = min(dp[2], 1 + dp[1]) = min(5, 1 + 1) = 2
# dp = [0, 1, 2, 5, 5, 5]

# Outer loop: target = 2
# Inner loop: s = 2
# square = 4
# target - square = 2 - 4 = -2 (invalid)

# Outer loop: target = 3
# Inner Loop: s = 1
# square = 1 * 1 = 1
# target - square = 3 - 1 = 2 (valid)
# dp[3] = min(dp[3], 1 + dp[2]) = min(5, 1 + 2) = 3
# dp = [0, 1, 2, 3, 5, 5]

# Outer loop: target = 3
# Inner loop: s = 2
# square = 2 * 2 = 4
# target - square = 3 - 4 = -1 (invalid), break

# Outer loop: target = 4
# Inner loop: s = 1
# square = 1^2 = 1
# target - square = 4 - 1 = 3 (valid)
# dp[4] = min(dp[4], 1 + dp[3]) = min(5, 1 + 3) = 4

# Outer loop: target = 4, Inner loop: s = 2
# square = 2^2 = 4
# target - square = 4 - 4 = 0 (valid)
# dp[4] = min(dp[4], 1 + dp[0]) = min(4, 1 + 0) = 1
# dp = [0, 1, 2, 3, 1, 5]

# Outer loop: target = 5, Inner loop: s = 1
# square = 1^2 = 1
# target - square = 5 - 1 = 4 (valid)
# dp[5] = min(dp[5], 1 + dp[4]) = min(5, 1 + 1) = 2

# Outer loop: target = 5, Inner loop: s = 2
# square = 2^2 = 4
# target - square = 5 - 4 = 1 (valid)
# dp[5] = min(dp[5], 1 + dp[1]) = min(2, 1 + 1) = 2
# dp = [0, 1, 2, 3, 1, 2]
