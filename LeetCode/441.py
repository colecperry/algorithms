# 441. Arranging Coins

# Topics - Binary Search, Math

# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

# Ex. 1
#
#  +-----+
#  |  $  |
#  +-----+-----+
#  |  $  |  $  |
#  +-----+-----+-----+
#  |  $  |  $  |     |
#  +-----+-----+-----+
#

# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.


# Ex. 2
#
#  +-----+
#  |  $  |
#  +-----+-----+
#  |  $  |  $  |
#  +-----+-----+-----+
#  |  $  |  $  |  $  |
#  +-----+-----+-----+-----+
#  |  $  |  $  |     |     |
#  +-----+-----+-----+-----+
#

# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.

# How to Solve (Binary Search)
    # Set up a search range from 0 to n -> because if we had 0 coins the answer would be 0, and if we had 1 coin the answer would be 1 (or n)
    # Midpoint guess -> In each iteration, we guess the number of rows by taking the midpoint of the range from l to r
    # Calculate the required coins -> Use the triangular number formula which calculates the sum of the first "x" natural numbers. For example, if x = 5, the sum of the first 5 natural numbers (1+2+3+4+5) = (5(5+1)) / 2 =  (5 * 6) / 2 = 15
    # Based on the number of rows we guessed, use the triangular number formula to calculate the number of coins needed to complete "rows"
    # Compare the number of coins to n -> 
        # If they are equal, return rows
        # If the number of coins calculated is larger than n, we have too many rows -> search l
        # If the number of coins calculated is smaller than n, we have too few rows -> search r
    # Once loop finishes, if we don't find an exact match, our while loop condition will be false, and right will be the last valid number of complete rows that didn't exceed "n" coins


# Runtime Complexity: O(log n)
# - The algorithm uses binary search over the range [0, n]. 
#   Since each iteration halves the search space, it takes logarithmic time relative to n.
#
# Space Complexity: O(1)
# - Only a fixed number of variables are used regardless of the input size.


class Solution(object):
    def arrangeCoins(self, n):
        left, right = 0, n
        while left <= right:
            rows = (right + left) // 2 # Guess num of rows in middle
            coins = rows * (rows + 1) // 2 # Number of coins to fill "mid" rows
            if coins == n: # If num of coins with rows guess perfectly fills n coins
                return rows
            if coins > n: # If num of coins with rows guess is greater than n coins
                right = rows - 1 # We have too many rows, search left
            else:
                left = rows + 1 # We have too few rows, search right
        return right # Return last valid number of complete rows when l crosses r 
    


my_solution = Solution()
print(my_solution.arrangeCoins(5))
print(my_solution.arrangeCoins(8))