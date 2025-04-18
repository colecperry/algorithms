# 832. Flipping an Image

# Topics: Array, Two Pointers, Bit Manipulation, Matrix, Simulation

# Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

# To flip an image horizontally means that each row of the image is reversed.
# For example, flipping [1,1,0] horizontally results in [0,1,1].

# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
# For example, inverting [0,1,1] results in [1,0,0].

# Example 1:

# Input: image = [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

# Example 2:
# Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
# Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

# How to Solve:
    # Iterate through each row in the image matrix
    # For each row, perform two steps:
    #   1. Flip the row horizontally using two-pointer swap (left ↔ right)
    #   2. Invert each element in the row: change 0 to 1 and 1 to 0

    # Flipping is done in-place using a while loop with two pointers moving toward the center
    # After the row is flipped, iterate through it again to invert each binary value

    # Time Complexity: O(n * m)
    #   - Where n is the number of rows and m is the number of columns
    #   - Each element is touched twice: once during flip, once during invert

    # Space Complexity: O(1)
    #   - Modifications are done in-place; no extra space proportional to input size is used


from typing import List
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for inner_image in image: # Loop trough each inner list
            l, r = 0, len(inner_image) - 1 # Init l and r pointers for horizontal flip
            while l < r: 
                inner_image[l], inner_image[r] = inner_image[r], inner_image[l] # Flip
                l += 1; r -= 1 # Move ptrs
            
            for i in range(len(inner_image)): # iterate through inner list again
                if inner_image[i] == 0: # Invert image (swap 0's and 1's)
                    inner_image[i] = 1
                else:
                    inner_image[i] = 0
        return image


sol = Solution()
print(sol.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
print(sol.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))