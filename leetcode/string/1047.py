# 1047. Remove All Adjacent Duplicates In String

# Topics: String, Stack

# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

# Example 1:
# Input: s = "abbaca"
# Output: "ca"
# Explanation: 
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

# Example 2:
# Input: s = "azxxzy"
# Output: "ay"

# Use a stack to build the result string by removing adjacent duplicates.
        # High-Level Idea:
        # Iterate through each character in the string.
        # - If the stack is not empty and the top of the stack is equal to the current character,
        #   pop from the stack (remove both duplicates) & do not append anything
        # - Otherwise, push the character onto the stack.
        # At the end, join the stack to form the final string with all adjacent duplicates removed.

        # Time Complexity (TC): O(n)
        # - We iterate over the input string once, and each character is pushed and popped at most once.
        # - Total operations are proportional to the length of the string.

        # Space Complexity (SC): O(n)
        # - In the worst case (no duplicates), we store all characters in the stack.

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop() # If they are == , pop off stack and skip appending
            else:
                stack.append(char) # Append if the chars are not != 
        return ''.join(stack)


sol = Solution()
print(sol.removeDuplicates("abbaca"))
print(sol.removeDuplicates("azxxzy"))