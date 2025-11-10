# 1614. Maximum Nesting Depth of the Parentheses

# Topics: String, Stack

# Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

# Example 1:
# Input: s = "(1+(2*3)+((8)/4))+1"
# Output: 3
# Explanation:
# Digit 8 is inside of 3 nested parentheses in the string.

# Example 2:
# Input: s = "(1)+((2))+(((3)))"
# Output: 3
# Explanation:
# Digit 3 is inside of 3 nested parentheses in the string.

# Example 3:
# Input: s = "()(())((()()))"
# Output: 3

class Solution:
    """
    TC:
        - O(n) -> iterate through string once
    SC:
        - O(n) -> worst case half of your string is opening brackets added to the stack
    """
    def maxDepth(self, s: str) -> int:
        max_depth = 0  # Track the deepest nesting we've seen
        curr_depth = 0  # Track current nesting level
        stack = []
        
        for i in range(len(s)):
            if s[i] == '(': 
                stack.append(s[i])  # Going deeper - add opening bracket
                
            elif s[i] == ')': 
                stack.pop()  # Going shallower - remove matching opening bracket
                
            # Stack size = how many unclosed brackets = current depth
            curr_depth = len(stack)
            
            # Keep track of the maximum depth we've encountered
            max_depth = max(max_depth, curr_depth)
        
        return max_depth

sol = Solution()
print(sol.maxDepth("(1+(2*3)+((8)/4))+1"))
print(sol.maxDepth("(1)+((2))+(((3)))"))
print(sol.maxDepth("()(())((()()))"))



