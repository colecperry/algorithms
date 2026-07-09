# 796. Rotate String

# Topics: String, String Matching

# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after one shift.

# Example 1:
# Input: s = "abcde", goal = "cdeab"
# Output: true

# Example 2:
# Input: s = "abcde", goal = "abced"
# Output: false

# How To Solve:
    # Define a function to determine if one string is a rotation of another
    # Loop through the string s up to its length to simulate all possible rotations
    # In each iteration:
    #   - Extract the first character of s
    #   - Rotate s by removing the first character and appending it to the end
    #   - Check if the rotated version matches the goal string
    #   - If a match is found, return True immediately
    # If no match is found after trying all rotations, return False

    # Time Complexity: O(n), where n is the length of the string
    # - Each rotation (slice and concatenate) takes O(n) time
    # - We perform up to n such rotations

# Space Complexity: O(n)
# - A new rotated string of length n is created in each iteration


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for _ in range(len(s)):
            char = s[:1]
            s = s[1:] + char
            if s == goal:
                return True

        return False

sol = Solution()
print(sol.rotateString("abcde", "cdeab"))