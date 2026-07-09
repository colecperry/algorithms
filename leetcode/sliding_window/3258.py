# 3258. Count Substrings That Satisfy K-Constraint I

# You are given a binary string s and an integer k.

# A binary string satisfies the k-constraint if either of the following conditions holds:

# The number of 0's in the string is at most k.
# The number of 1's in the string is at most k.
# Return an integer denoting the number of substrings of s that satisfy the k-constraint.

# Example 1: 
# Input: s = "10101", k = 1
# Output: 12
# Explanation: Every substring of s except the substrings "1010", "10101", and "0101" satisfies the k-constraint.

# Example 2:
# Input: s = "1010101", k = 2
# Output: 25
# Explanation: Every substring of s except the substrings with a length greater than 5 ("10101", "01010") satisfies the k-constraint.

# Example 3:
# Input: s = "11111", k = 1
# Output: 15
# Explanation: All substrings of s satisfy the k-constraint.

# How to Solve (Sliding Window):
# - We’ll use two pointers (left and right) to represent a 
#   sliding window over the string.
# - We’ll keep track of the count of 0s and 1s inside the window.
# - As we move the right pointer across the string:
#     - Add the new character (0 or 1) into our counts.
#     - If both 0s and 1s exceed k, the window is invalid:
#         - Move the left pointer forward to shrink the window 
#           until it becomes valid again.
# - Once the window is valid:
#     - All substrings ending at `right` and starting between
#       `left` to `right` are valid
#     - ex. for s = "10101", k = 1, left = 1, right = 3,
#     - s[1:4] = "010", and since this window contains 2 zeros
#       and 1 one, it satisfies the constraint since 1 <= k.
#       Since the entire window is valid, we must count:
#           - s[1:4] = "010"
#           - s[2:4] = "10"
#           - s[3:4] = "0"
#     - The number of such substrings is: (right - left + 1)

# Final answer is the sum of all such valid substrings for each position of `right`.

# Time Complexity: O(n)
# - Each character is processed at most twice: once when right expands, once when left contracts.

# Space Complexity: O(1)
# - We only store integer counters (constant space), regardless of string size.

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        left = 0 # Left pointer
        num_strings = 0 # Result output
        num_zeros = 0 # Count for zeros & ones
        num_ones = 0
        
        for right in range(len(s)):
            # Add current char to the window
            if s[right] == '0': # Count R's 0's or 1's
                num_zeros += 1
            else:
                num_ones += 1
            
            # Shrink window if both counts exceed k
            while num_zeros > k and num_ones > k:
                if s[left] == '0':
                    num_zeros -= 1
                else:
                    num_ones -= 1
                left += 1 # Move L ptr to shrink window

            # At this point, window [left:right] is valid
            valid_substrings = right - left + 1
            num_strings += valid_substrings # Count the number of substrings that start in the window and end at R
        return num_strings



sol = Solution()
print(sol.countKConstraintSubstrings("10101", 1)) # 12
print(sol.countKConstraintSubstrings("1010101", 2)) # 25
print(sol.countKConstraintSubstrings("11111", 1)) # 15