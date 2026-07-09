# 344. Reverse String

# Topics: String, Two Pointer

# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

# How to Solve:
    # Initialize two pointers: one at the start (l) and one at the end (r) # of the list
    # While the left pointer is less than the right pointer:
    #     Swap the elements at the left and right pointers
    #     Move the left pointer right and the right pointer left
    # This process reverses the list in-place without using extra space

    # Time Complexity: O(n), where n is the length of the list
    # - Even though the loop runs only n/2 times, Big-O notation ignores #   constant factors
    # - So O(n/2) simplifies to O(n)
    # - Using two pointers makes it more efficient, but not faster in 
    #   asymptotic terms

    # Space Complexity: O(1), as the reversal is done in-place


from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

sol = Solution()
print(sol.reverseString(["h","e","l","l","o"]))
print(sol.reverseString(["H","a","n","n","a","h"]))
