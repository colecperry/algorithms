# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2: 
# Input: s = "()[]{}"
# Output: true

# Example 3: 
# Input: s = "(]"
# Output: false


class Solution:
    def isValid(self, s: str) -> bool:
        """
        TC: O(n) - single pass through string
        SC: O(n) - stack stores up to n/2 opening brackets
        """
        bracket_map = {"(": ")", "[": "]", "{": "}"}
        stack = []
        
        for char in s:
            if char in bracket_map:  # Opening bracket
                stack.append(char) # Add it to the stack
            else:  # Closing bracket
                if not stack: # Nothing to match with -> closing w/o opening
                    return False
                opening = stack.pop()
                if bracket_map[opening] != char:  # Check if mismatch
                    return False
        
        return len(stack) == 0  # True if all brackets matched

s1 = "()"
s2 = "()[]{}"
s3 = "(]"
s4 = "([])"


solution = Solution()
print(solution.isValid(s1))
print(solution.isValid(s2))
print(solution.isValid(s3))
print(solution.isValid(s4))
