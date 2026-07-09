# 557. Reverse Words in a String III

# Topics: Two Pointers, String

# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# Example 1:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# Example 2:
# Input: s = "Mr Ding"
# Output: "rM gniD"

# How to Solve: High Level
    # Convert the input string to a list for easier character manipulation
    # Iterate over the string in 2k-sized blocks
    # For each block, reverse the first k characters in-place
    # Skip the next k characters to leave them unchanged
    # Repeat this pattern until the entire string is processed
    # Reassemble the list into a string and return the result

    # Time Complexity: O(n) – Each character is visited at most once during reversal
    # Space Complexity: O(n) – Due to converting the string to a list and then back to a string

class Solution:
    def reverseWords(self, s: str) -> str:
        char_list = list(s) # Convert string into a list
        start = 0 # pointer where to start the reversal

        for i in range(len(char_list)):
            if char_list[i] == " ": # When we hit a whitespace
                char_list[start:i] = reversed(char_list[start:i]) # reverse
                start = i + 1 # move ptr one past the whitespace
            elif i == len(char_list) - 1: # If we hit the last index
                char_list[start:] = reversed(char_list[start:]) # Reverse to end
        
        return ''.join(char_list)

sol = Solution()
print(sol.reverseWords("Let's take LeetCode contest"))
print(sol.reverseWords("Mr Ding"))