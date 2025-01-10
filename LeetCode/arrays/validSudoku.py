# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition. (Of the total board)
# Each column must contain the digits 1-9 without repetition. (Of the total board)
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Example 1:

# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]

# Example 2:
# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

# How to solve:
    # Use a hash set to determine if any rows have duplicates. Each hash set is a hash map where they keys are unique. For the rows hash set, each key is the row 0-8 and the values are each number on the board that are in that row
    # Use a hash set to determine if any columns have duplicates. Each key is the column 0-8 and the values are each number on the board that are in that column
    # Use a hash set to represent each 3x3 grid. Each key in the hashmap are a pair of values converted by integer division 3 (ex. 8,8 -> 8//3, 8//3 -> 2,2) and the values are each number on the board that are in that pair of values (each of the mini boards)
    # We iterate over the board, and if any of the numbers we come across on the board are already in that row, column, or squares (each mini board) hash set, we return false because it is a duplicate
    # If they are not in any of the hash sets, we update each hash set accordingly

# Drawing:
# Each # 0-8 represents columns and rows
# Each # 0-2 represents which sudoku board
# Need to convert 0-8 for each column and row to 1-2 by dividing it by 3 (int division rounds down)
# 4,4 -> 4/3, 4/3 -> 1,1


#          0               1               2
#      0   1   2   |   3   4   5   |   6   7   8
#    0 .   .   .   |   .   .   .   |   .   .   .
# 0  1 .   .   .   |   .   .   .   |   .   .   .
#    2 .   .   .   |   .   .   .   |   .   .   .
#     --------------------------------------------
#    3 .   .   .   |   .   .   .   |   .   .   .
# 1  4 .   .   .   |   .   x   .   |   .   .   .
#    5 .   .   .   |   .   .   .   |   .   .   .
#     --------------------------------------------
#    6 .   .   .   |   .   .   .   |   .   .   .
# 2  7 .   .   .   |   .   .   .   |   .   .   .
#    8 .   .   .   |   .   .   .   |   .   .   .
# 

# Big O analysis
    # Time complexity: O (9^2)
    # Space complexity: O (9^2)

import collections

class Solution(object):
    def isValidSudoku(self, board):
        cols = collections.defaultdict(set) # Use a hashset(dict) where the key is the column # and the value is another set (all values in that column)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r/3, c/3)

        for r in range(9): # Iterate over the grid of 9
            for c in range(9):
                if board[r][c] == ".": # If we come across an empty space skip it
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[r //3, c // 3]): # If board number is already in our hashmap at that current row, column, or square we are in
                    return False
                cols[c].add(board[r][c]) # Update column c with board number
                rows[r].add(board[r][c]) # Update row r with board number
                squares[(r // 3, c // 3)].add(board[r][c]) # Update squares hashmap with board num
        return True # If we don't come across any duplicates



my_solution = Solution()
print(my_solution.isValidSudoku(
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

print(my_solution.isValidSudoku(
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))


