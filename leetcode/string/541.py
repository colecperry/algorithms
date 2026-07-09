# 541. Reverse String II

# Topics: Two Pointer, String

# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

# Example 1:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"

# Example 2:
# Input: s = "abcd", k = 2
# Output: "bacd"

# How to Solve:
    # Convert the input string to a list to allow in-place modifications
    # Process the string in chunks of 2k characters
    # For each 2k chunk, reverse only the first k characters
    # Leave the second k characters in each 2k chunk unchanged
    # Continue this process until the end of the string is reached
    # Join the modified list back into a string and return the result


    # Time Complexity: O(n), where n is the length of the string — each character is visited at most once
    # Space Complexity: O(n), due to converting the string to a list and then back to a string


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)  # Convert string to list for in-place editing
        ptr_1, ptr_2 = 0, k # Start one pointer at 0 and one at k
        
        while ptr_1 < len(s):
            # Reverse the next k characters if there are at least k left
            s[ptr_1:ptr_2] = reversed(s[ptr_1:ptr_2])
            
            # Move both pointers forward by 2k
            ptr_1 += 2 * k
            ptr_2 = min(ptr_1 + k, len(s))  # Avoid going out of bounds
        
        return ''.join(s)



sol = Solution()
print(sol.reverseStr("abcdefg", 2))
print(sol.reverseStr("abcd", 2))
