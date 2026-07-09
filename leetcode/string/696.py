# 696. Count Binary Substrings

# Topics: Two Pointer, String

# Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively. (Note -> grouped consecutively means '0101' would not count).

# Substrings that occur multiple times are counted the number of times they occur.

# Example 1:

# Input: s = "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
# Notice that some of these substrings repeat and are counted the number of times they occur.
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
# Example 2:

# Input: s = "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

# How to Solve:
    # The goal is to count valid binary substrings where a group of 0's is followed by a group of 1's (or
    # vice versa)
    # AND both groups have the same length.
    # Example: In "0011", "00" (Group 1) and "11" (Group 2) → min(2,2) = 2 valid substrings ("01", "0011")

    # Key Insight: every valid substring is formed at the boundary between two different character groups.
    # The number of valid substrings from this boundary = min(length of the previous group, length of the current group).

    # Initialize counters:
    # - count_substrings: total valid substrings found so far
    # - prev_group_length: length of the last group of characters (e.g., "00")
    # - curr_group_length: length of the current group of characters being counted (e.g., "11")
    # Start with curr_group_length = 1 because the first character forms a group of at least one.

    # Loop through the string from index 1 to the end:
    # For each character, compare it with the previous one:
    # - If they are different (e.g., '0' → '1'), it means we've reached a
    #   boundary like "00|11"
    #     - At this boundary, calculate valid substrings: min
    #       (prev_group_length, curr_group_length)
    #         - In "0011", after seeing "00|11", prev = 2, curr = 2 → min(2,
    #           2) = 2 substrings: "01", "0011"
    #     - Add this count to the total result (count_substrings)
    #     - Then, shift the groups:
    #         - prev_group_length becomes curr_group_length (since we just 
    #           finished it)
    #         - curr_group_length is reset to 1 (starting a new group with
    #           the current character)
    # - If they are the same (e.g., '0' → '0' or '1' → '1'):
    #     - Just increase curr_group_length by 1 since we're still in the 
    #       same group.

    # After finishing the loop, one last boundary still needs to be processed.
    # - Add min(prev_group_length, curr_group_length) one more time for the
    #   final group boundary.
    #     - This is needed because the last group might also form valid 
    #       substrings (like "11" at the end of "0011")

    # Time Complexity: O(n), where n is the length of the string
    # - We make one pass through the string, processing each character once.

    # Space Complexity: O(1)
    # - Only a fixed number of counters are used, no additional space 
    #   depending on input size.



class Solution:
    def countBinarySubstrings(self, s: str) -> int:
    # Initialize result counter, previous group length, and current group length
        count_substrings = 0
        prev_group_length = 0 # Stores prev group length of consecutive O's or 1's
        curr_group_length = 1  # The first character starts a current group of at least length 1

        # Iterate through the string starting from the second character
        for i in range(1, len(s)):
            if s[i] != s[i - 1]: # We reached a boundary
                count_substrings += min(prev_group_length, curr_group_length) # The min of the two groups is the max number of substrings we can form
                prev_group_length = curr_group_length # Update group lengths: previous becomes current, 
                curr_group_length = 1 # and start a new current group
            else:
                curr_group_length += 1 # If current char is same as prev, extend current group

        # Add the last group comparison after the loop ends
        count_substrings += min(prev_group_length, curr_group_length)

        return count_substrings


sol = Solution()
print(sol.countBinarySubstrings("00110011"))
print(sol.countBinarySubstrings("10101"))