# 125. Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# How to solve: 
    # Method 1: Generator expression + .join method + reversed method
    # Use a generator expression which is a consise and efficient way to create an iterator in python (generator = (expression for item in iterable if condition))
    # Use the .join method to concatenate elements of an iterable. '' is the seperator
    # Use a generator expression + the join method to clean the string
    # Get a reversed string of the clean string: The reversed() function takes an iterable (like a string, list, or tuple) and returns an iterator that yields the elements in reverse order.
    # Compare the two elements, if they are the same it is a palindrome

    # Method 2: Two pointer
    # Create left and right pointer
    # Create a while loop
        # Check if left and right are alphanumeric, if not move right and left pointers
        # If they are both alphanumeric, compare them
            # If equal, move both pointers
            # If not equal, return False
            # Once we get to where l = r, return True


# Example 1: Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2: Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3: Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

class Solution(object):
    def isPalindrome(self, s):
        clean_string = ''.join(char.lower() for char in s if char.isalnum()) # Use a generator expression and join method
        reversed_string = ''.join(reversed(clean_string))
        return clean_string == reversed_string
    
    def isPalindrome2(self, s):
        l, r = 0, len(s) - 1 # Create left and right pointers
        while l < r:
            # Skip non-alphanumeric characters
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            # Compare characters (case-insensitive)
            elif s[l].lower() != s[r].lower():
                return False
            else: # If they are equal move pointers
                l += 1
                r -= 1
        return True


solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))