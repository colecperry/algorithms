# 340. Longest Substring with At Most K Distinct Characters

# Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

# Example 1:
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: The substring is "ece" with length 3.

# Example 2:
# Input: s = "aa", k = 1
# Output: 2
# Explanation: The substring is "aa" with length 2.

# How to Solve (sliding window):
# Big Picture: 
    # Use a sliding window that expands and contracts as we iterate through the string
    # If we expand the window and exceed k distinct characters (we know this due to using a dict w/ char frequencies where repeated characters only count once), we shrink the window until the left pointer is valid
    # Update the max window size each iteration of the right pointer

# Code: 
    # Store character frequencies in the current window, max window length, and init l ptr
    # Loop through array with right pointer
        # Add char in the string to the dict if not present, increment by 1
        # Decrease window if more characters in dict than k
            # Decrement the character (left ptr) freq from the dictionary
            # Delete the char from the dict if freq = zero (ensure distinct chars in window)
            # Move the left pointer forward
        # Update max window size if current window (r - l + 1) is bigger

# Time complexity: O(n) the loop runs n times because l only moves forward, but each character can be processed twice (r and l pointers)
# Space complexity: O(k) the dictionary storing character counts can store at most k keys, which is the number of unique characters allowed, but worst case it is O(n) because it could store the keys of each ele in the array once




class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        letters_dict = {}  # Dictionary to store character counts
        max_window_length = 0
        l = 0  # Left pointer

        for r in range(len(s)): # Loop right pointer
            letters_dict[s[r]] = letters_dict.get(s[r], 0) + 1  # Add character to dictionary
            
            while len(letters_dict) > k:  # Shrink window if more than k distinct characters
                letters_dict[s[l]] -= 1 # Decrement freq for char leaving window
                if letters_dict[s[l]] == 0: # If freq gets to zero
                    del letters_dict[s[l]] # Delete the char
                l += 1  # Move left pointer forward
            
            max_window_length = max(max_window_length, r - l + 1)  # Update max window size

        return max_window_length
    
my_solution = Solution()
print(my_solution.lengthOfLongestSubstringKDistinct("eceba", 2))
print(my_solution.lengthOfLongestSubstringKDistinct("aa", 1))
