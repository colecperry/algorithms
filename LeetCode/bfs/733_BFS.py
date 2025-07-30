# 733. Flood Fill

# Given a 2D image represented by an integer matrix, each integer represents the pixel value of the image, and two integers sr and sc representing the starting pixel (row and column) of the flood fill, and a new color value, flood fill the image starting from the pixel (sr, sc).

# The flood fill algorithm works as follows:
# 1. If the starting pixel's color is equal to the new color, return the image.
# 2. Otherwise, change the color of the starting pixel to the new color.
# 3. Recursively apply the flood fill algorithm to the neighboring pixels (up, down, left, right) that have the same original color as the starting pixel.

# Example 1:
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]

# Explanation:
# [               [
#   [1, 1, 1],      [2, 2, 2],
#   [1, 1, 0],   -> [2, 2, 0],
#   [1, 0, 1],      [2, 0, 1],
# ]                ]

# From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.

# Note the bottom corner is not colored 2, because it is not horizontally or vertically connected to the starting pixel.

# Example 2:
# Input: image = [[0,0,0],[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 0
# Output: [[0,0,0],[0,0,0],[0,0,0]]

# Explanation:

# The starting pixel is already colored with 0, which is the same as the target color. Therefore, no changes are made to the image.

# -----------------------
# 💡 How to Solve:
# -----------------------

# Use Breadth-First Search (BFS) to flood-fill all connected pixels that have the same original color

# 1. Get the number of rows and columns in the image
# 2. Store the original color of the starting pixel
# 3. If the original color is already the target color, return the image as-is (no change needed)
# 4. Initialize a queue with the starting pixel (sr, sc)
# 5. Use a list of 4 directional tuples (row, col) to explore up, down, left, and right neighbors
# 6. While the queue is not empty:
#     - Pop a pixel from the queue
#     - Change its color to the target color
#     - For each of the 4 neighbors:
#         - If the neighbor is within bounds and has the original color (accounts for dups), enqueue it

# -----------------------
# ⏱️ Time Complexity:
# -----------------------

# O(n * m)
# - In the worst case, every pixel in the image may need to be visited once
# - n = number of rows, m = number of columns

# -----------------------
# 📦 Space Complexity:
# -----------------------

# O(n * m)
# - In the worst case, the queue can hold up to all pixels in the image (if all need to be colored)


from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], start_row: int, start_col: int, new_color: int) -> List[List[int]]:
        num_rows, num_cols = len(image), len(image[0])  # dimensions of the image
        original_color = image[start_row][start_col]    # color to replace

        # If the starting pixel already has the target color, nothing to do
        if original_color == new_color:
            return image

        # Initialize BFS with the starting pixel
        queue = deque([(start_row, start_col)])  # queue holds (row, col) positions

        # Direction vectors: up, down, left, right
        direction_deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            current_row, current_col = queue.popleft()

            # Recolor the current pixel
            image[current_row][current_col] = new_color

            # Visit all 4-connected neighbors
            for delta_row, delta_col in direction_deltas:
                neighbor_row = current_row + delta_row
                neighbor_col = current_col + delta_col

                # Check that neighbor is in bounds and matches the original color
                if (0 <= neighbor_row < num_rows and
                    0 <= neighbor_col < num_cols and
                    image[neighbor_row][neighbor_col] == original_color):
                    queue.append((neighbor_row, neighbor_col))

        return image


sol = Solution()
print(sol.floodFill([[1,1,1],
                     [1,1,0],
                     [1,0,1]], 1, 1, 2))
print(sol.floodFill([[0,0,0],
                     [0,0,0],
                     [0,0,0]], 0, 0, 2))