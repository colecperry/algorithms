class Solution(object):
    def isPalindrome(self, s):
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