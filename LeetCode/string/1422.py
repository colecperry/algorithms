# 1422. Maximum Score After Splitting a String

# Topics: String, Prefix Sum

# Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

# The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

# Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

# The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.


# Example 1:
# Input: s = "011101"
# Output: 5 
# Explanation: 
# All possible ways of splitting s into two non-empty substrings are:
# left = "0" and right = "11101", score = 1 + 4 = 5 
# left = "01" and right = "1101", score = 1 + 3 = 4 
# left = "011" and right = "101", score = 1 + 2 = 3 
# left = "0111" and right = "01", score = 1 + 1 = 2 
# left = "01110" and right = "1", score = 2 + 1 = 3

# Example 2:
# Input: s = "00111"
# Output: 5
# Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5

# Example 3:
# Input: s = "1111"
# Output: 3

# High-Level Idea: (Brute Force)
        # Try every possible split of the string into two non-empty parts.
        # For each split, count the number of '0's in the left part
        # and the number of '1's in the right part.
        # The score is the sum of those counts. Track the maximum score.

        # Time Complexity: O(n^2)
        # - For each split point, we use .count() on a substring (O(n) each),
        #   and we do this for n-1 split points => total is O(n^2)

        # Space Complexity: O(n)
        # - Slicing strings creates new substrings which take space proportional to the length.

class Solution:
    def maxScore(self, s: str) -> int: # Brute Force O(n^2)
        max_score = float('-inf')
        for i in range(1, len(s)):
            string_1 = s[:i]
            str_1_count = string_1.count('0')
            string_2 = s[i:]
            str_2_count = string_2.count('1')
            max_score = max(max_score, str_1_count + str_2_count)
        return max_score
    
    # High-Level Idea: (Optimized)
        # Instead of counting from scratch for each split, we:
        # - Count total number of '1's at the start.
        # - Then scan the string once, updating:
        #     * count of '0's on the left (as we move right),
        #     * count of '1's remaining on the right.
        # At each position, compute score as left '0's + right '1's and track the max.

        # Time Complexity: O(n)
        # - We go through the string once to count '1's,
        #   and once more to compute the score => total O(n)

        # Space Complexity: O(1)
        # - We use a constant number of variables for tracking counts.
    
    def maxScore2(self, s: str) -> int: # Optimized O(n)
        # Total number of '1's in the string
        total_ones = s.count('1')

        max_score = 0 # Output
        zeros_on_left = 0
        ones_on_right = total_ones

        # Go through each split point from index 0 to len(s) - 2
        for i in range(len(s) - 1):
            if s[i] == '0': # Get the number of zeros on left &
                zeros_on_left += 1
            else: # Ones on the right each iteration
                ones_on_right -= 1

            current_score = zeros_on_left + ones_on_right
            max_score = max(max_score, current_score) # Update score

        return max_score


sol = Solution()
print(sol.maxScore2("011101"))
print(sol.maxScore("00111"))
print(sol.maxScore("1111"))