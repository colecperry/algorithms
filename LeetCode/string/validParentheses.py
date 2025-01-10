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

# Steps to solve
# Create a dictionary of matching open/close bracket pairs
# Create an empty stack
# Iterate over the string, if the char is an opening bracket, push to the stack
# If the char is a closing bracket:
    # If there is characters in the stack and the top of the stack (open bracket) matches the closing bracket, pop the open bracket off the stack
    # If there is no characters in the stack, that means we have a closing bracket without an opening bracket, or if the brackets don't match, return false
# Return true if after iterating over the whole list the stack is empty, else False (we have extra open brackets that were not matched)


class Solution(object):
    def isValid(self, s):
        closeToOpen = { # Create key value pairs for each parentheses pair
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        stack = [] # Create an empty stack
        for char in s: # Iterate over the string s
            # Closing bracket case
            if char in closeToOpen: # char is a key when we check the dict
                if len(stack) != 0 and stack[-1] == closeToOpen[char]: # Check if the stack is non-empty and the char at top of the stack is the matching opening parentheses
                # closeToOpen[char] is passing in the closing brace to get the open brace
                    stack.pop() # Pop from the stack if they match and stack is not empty
                else:
                    return False # If they don't match return false
            # Open bracket case
            else:
                stack.append(char)
        return True if len(stack) == 0 else False # If we go through the whole list and the stack is empty return False, if the stack is not empty return True

s1 = "()"
s2 = "()[]{}"
s3 = "(]"
s4 = "([])"


solution = Solution()
print(solution.isValid(s1))
print(solution.isValid(s2))
print(solution.isValid(s3))
print(solution.isValid(s4))
