# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

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
        clean_string = ''.join(char.lower() for char in s if char.isalnum())
        # print(clean_string)
        # print(clean_string[::-1]) <- This is another way to reverse a string
        reversed_string = ''.join(reversed(clean_string))
        # print(reversed_string)
        return clean_string == reversed_string
    
    def isPalindrome2(self, s):
        # Keep only alphanumeric characters and make them lowercase
        cleaned_text = ''.join([char.lower() for char in s if char.isalnum()])
        
        # Set pointers at the start and end of cleaned_text
        l, r = 0, len(cleaned_text) - 1
        
        # Check for palindrome by moving pointers towards the center
        while l < r:
            if cleaned_text[l] != cleaned_text[r]:
                return False
            l += 1
            r -= 1
            
        return True


solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))