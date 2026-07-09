# 374. Guess Number Higher or Lower

# Topics - Binary Search, Interactive

# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

# You call a pre-defined API int guess(int num), which returns three possible results:

# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

# Example 1:
# Input: n = 10, pick = 6
# Output: 6

# Example 2:
# Input: n = 1, pick = 1
# Output: 1

# Example 3:
# Input: n = 2, pick = 1
# Output: 1

# Runtime Complexity: O(log n)
# - The solution uses binary search. In each iteration, it halves the search range,
#   so the number of iterations is logarithmic relative to n.
#
# Space Complexity: O(1)
# - Only a fixed number of variables are used regardless of the input size.


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        l = 1 # Set l and r pointers
        r = n
        while l <= r: # While loop for Binary Search
            mid = l + (r-1) // 2 # Calculte mid integer
            if guess(mid) == -1: # If return is -1, the number is higher than mid
                r = mid - 1 # Search right half
            elif guess(mid) == 1: # If return is 1, the number is lower than mid
                l = mid + 1 # Searh left half
            else: # We found correct number
                return mid
