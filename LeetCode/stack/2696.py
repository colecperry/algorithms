# 2696. Minimum String Length After Removing Substrings

# Topics - String, Stack, Simulation

# You are given a string s consisting only of uppercase English letters.
# You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings "AB" or "CD" from s.

# Return the minimum possible length of the resulting string that you can obtain.

# Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings.


# Example 1:
# Input: s = "ABFCACDB"
# Output: 2
# Explanation: We can do the following operations:
# - Remove the substring "ABFCACDB", so s = "FCACDB".
# - Remove the substring "FCACDB", so s = "FCAB".
# - Remove the substring "FCAB", so s = "FC".
# So the resulting length of the string is 2.
# It can be shown that it is the minimum length that we can obtain.

# Example 2:
# Input: s = "ACBBD"
# Output: 5
# Explanation: We cannot do any operations on the string so the length remains the same.

# How to solve: Brute Force
    # Use "in" operator to check if "AB" or "CD" is in the string
    # Strings are immutable (cannot be changed in memory after creation), so update s after replacing to point at newly created string with .replace()
    # Return final length

    # Time complexity: when we check for substrings "AB" and "CD" in s, we scan the entire string in O(n) time. Each call to .replace() creates a new string and scans s, which takes O(n): Total worst case time complexity: O(n^2)
    # Space complexity: strings are immutable, so each .replace() creates a new string in memory, in the worst case we store a new string each time leading to O(n) space complexity

# How to solve: w/ Stack
    # Iterate through the input string 
    # Check if stack has elements (edge case for empty stack we return 0)
    # & check if ele at top of stack is 'A' and curr ele is 'B' or ele at top of stack is 'B' and curr ele is 'D'
        # if so pop ele off top of stack (A or C) and move to next iteration without appending (will skip over B and C)
        # else append the char to the stack
    # return the length of the stack

class Solution(object):
    # Brute Force
    def minLength(self, s):
        while "AB" in s or "CD" in s:
            s = s.replace("AB", "").replace("CD", "")
        return len(s) 
    
    # Stack
    def minLength2(self, s):
        stack = []
        for char in s:
            # If char on top of stack is 'A' or 'B' and char we are iterating on is 'C' or 'D'
            if stack and ((stack[-1] == 'A' and char == 'B') or (stack[-1] == 'C' and char == 'D')):
                stack.pop()  # Remove char at top of stack
            else:
                stack.append(char)  # Otherwise, add the character to the stack
        return len(stack)  # Remaining characters in the stack




my_solution = Solution()
print(my_solution.minLength2("ABFCACDB"))
print(my_solution.minLength("ACBBD"))