# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input
# string is valid.

# An input string is valid if:
    # Open brackets must be closed by the same type of brackets.
    # Open brackets must be closed in the correct order.
    # Every close bracket has a corresponding open bracket of the same type.
        # ([]){} - Valid
        # {[(])} - Invalid

# How to Solve
    # The last type of bracket that was opened, is the first bracket that needs to be closed - LIFO
    # This is how we know that we need to use a stack!

# Example 1:
    # Input: s = "()"
    # Output: true

# Example 2:
    # Input: s = "()[]{}"
    # Output: true

# Example 3:
    # Input: s = "(]"
    # Output: false

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [] # Use a list as a stack, as long as we only operate from one end (append and pop)
        pairs = {  # Create a dictionary that matches each corresponding opening bracket to it's closing bracket
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        for bracket in s: # Loop through the passed in string
            if bracket in pairs: # If the character is a key in the pairs dictionary,
                stack.append(bracket) # we will push it onto the stack
            elif len(stack) == 0 or bracket != pairs[stack.pop()]: # If the length of the stack is zero (no opening
            # bracket for the closing bracket) or the character is not a pair represented by the stack's popped character
                return False # Return false, otherwise the above evaluates to false and the loop continues
            
        return len(stack) == 0 # If you get through the loop and the length is zero, all the opening brackets have 
        # a corresponding closing bracket, so return True, else, return False

sol = Solution() # Create an instance of the solution class
result = sol.isValid('()') # Call the isValid method on the instance and pass in the string
print("test 1", result)

result2 = sol.isValid('()[]{}')
print("test 2", result2)

print("test 3", sol.isValid('(]')) #Another way of doing this


