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

# Solution uses a data structure called a stack
# Think of a stack as a stack of paper - with a stack you can only retreive, add, or delete elements from the top of the stack
# Step 1: Create an dictionary with key and value pairs for each type of opening and closing bracket. 
# Step 2: To use the stack, we need to initalize an empty list
# Step 3: We are going to iterate through our passed in string letter by letter, and if the letter on the index of our current iteration is equal to "(", "[", or "{", we are going to append it to the stack
# Step 4: If the letter on the top of the stack is equal to is equal to wordDict[s[i]] which is either wordDict[)] which equals "(", wordDict[]] which equals "[", or wordDict [}] which equals "{", we are going to pop it (remove) from our stack and continue the loop
# Step 5: If the letter on the top of the stack is equal to wordDict[s[i]] and the length of the stack is not equal to zero, we pop(delete) the letter on the top of the stack.
# Step 6: If the letter on the top of the stack is not equal to wordDict[s[i]] or the length of the stack is equal to zero, we return false because the order is not correct. We need to check the length of the stack because if it is empty, you can't pop from the stack and it will throw an error.
# Step 7: We check to see if the stack is empty. If all brackets match, it means that we popped everything off and the string is now empty. In this case, we return true. The edge case here for false is if we have opening brackets like this ("{[") passed in that never have the chance to be popped, in that case we would return false.


class Solution(object):
    def isValid(self, s):
        wordDict = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        stack = []
        # print(s)
        for i in range (len(s)):
            # print(stack)
            # print[s[i]]
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            elif s[i] == ")" or s[i] == "]" or s[i] == "}":
                if stack[len(stack) - 1] == wordDict[s[i]] and len(stack) != 0: # good case
                # if (s[i] == ")" and stack[len(stack) - 1] == "(") or \
                # (s[i] == "]" and stack[len(stack) - 1] == "[") or \
                # (s[i] == "}" and stack[len(stack) - 1] == "{"):
                    stack.pop()
                else:   # bad case
                    return False
        return len(stack) == 0 # is the stack empty?

solution = Solution()
print(solution.isValid("([)"))
