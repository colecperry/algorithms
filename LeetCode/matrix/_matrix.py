# -----------------------------------------------------------------------------
# Pattern 6: Staircase Search in 2D Matrix
# -----------------------------------------------------------------------------

def search_matrix_ii(matrix, target):  # LC 240
    """
    Problem: Search for target in m×n matrix where each row is sorted left to right
    and each column is sorted top to bottom, but matrix is NOT flattened sorted.

    Example: matrix =  [[1,  4,  7,  11, 15],    target = 5 → False
                        [2,  5,  8,  12, 19],    target = 11 → True  
                        [3,  6,  9,  16, 22],
                        [10, 13, 14, 17, 24],
                        [18, 21, 23, 26, 30]]

    Key insight: Start from top-right or bottom-left corner where you can
    eliminate entire rows OR columns with each comparison. From top-right:
    left = smaller values, down = larger values.

    Why other corners don't work:
    - Top-left/bottom-right: both directions could contain target (no elimination)

    Pattern: Staircase elimination - move in L-shaped path, never backtrack
    """
    if not matrix or not matrix[0]:
        return False
        
    row, col = 0, len(matrix[0]) - 1  # Start from top-right corner

    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1  # Move left - eliminate entire right column
        else:
            row += 1  # Move down - eliminate entire top row
            
    return False

# Test cases  
print(search_matrix_ii([[1,4,7,11],[2,5,8,12],[3,6,9,16]], 5))   # False
print(search_matrix_ii([[1,4,7,11],[2,5,8,12],[3,6,9,16]], 11))  # True