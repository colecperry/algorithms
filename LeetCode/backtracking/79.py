# 79. Word Search

# Topics: Array, String, Backtracking, Depth-First Search, Matrix

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:
# Input: board = [
# ["A","B","C","E"],
# ["S","F","C","S"],
# ["A","D","E","E"]]
# word = "ABCCED"
# Output: true

# Example 2:
# Input: board = [
# ["A","B","C","E"],
# ["S","F","C","S"],
# ["A","D","E","E"]]
# word = "SEE"
# Output: true

# Example 3:
# Input: board = [
# ["A","B","C","E"],
# ["S","F","C","S"],
# ["A","D","E","E"]]
# word = "ABCB"
# Output: false

from typing import List

class Solution:
    """
    Key insight:
    - Same cell can appear in DIFFERENT paths (different searches)
    - Same cell CANNOT appear TWICE in SAME path (mark visited temporarily)
    - Mark cell with special character during exploration (e.g., '#')
    - Unmark when backtracking so other paths can use it
    - Try all 4 directions: if ANY succeeds, entire search succeeds
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        TC: O(m * n * 4^L) where m = rows, n = cols, L = len(word)
            - Try each cell as starting point: O(m * n)
            - From each start, explore up to 4^L paths (4 directions, L levels deep)
        
        SC: O(L)
            - O(L) recursion depth (one call per character in word)
            - In-place marking on board (no extra visited structure)
        """
        rows, cols = len(board), len(board[0])
        
        def backtrack(r, c, index):
            """
            Search for word starting from board[r][c] matching word[index].
            
            Args:
                r: Current row position
                c: Current column position
                index: Current position in word we're trying to match
            
            Returns:
                True if word can be formed from this position, False otherwise
            """
            # BASE CASE: Matched entire word starting from curr cell & recursing
            if index == len(word):
                return True
            
            # BOUNDARY CHECKS: Invalid if any of these true
            if (r < 0 or r >= rows or          # Out of bounds vertically
                c < 0 or c >= cols or          # Out of bounds horizontally
                board[r][c] != word[index] or  # Character mismatch
                board[r][c] == '#'):           # Already visited in this path
                return False
            
            # FOUND MATCH (board[r][c] == word[index])

            # STEP 1: MARK as visited in current path
            # Save original character and replace with '#' marker
            # This prevents using same cell twice in THIS path
            temp = board[r][c]
            board[r][c] = '#'
            
            # STEP 2: EXPLORE all 4 directions
            # Try moving: down, up, right, left
            # If ANY direction finds the word, return True
            # Use 'or' short-circuit: stops as soon as one succeeds
            found = (backtrack(r + 1, c, index + 1) or  # DOWN
                    backtrack(r - 1, c, index + 1) or   # UP
                    backtrack(r, c + 1, index + 1) or   # RIGHT
                    backtrack(r, c - 1, index + 1))     # LEFT
            
            # STEP 3: UNMARK (BACKTRACK)
            # Restore original character so other previous paths can use this cell
            # This is CRITICAL: same cell might be part of different valid path
            board[r][c] = temp
            
            return found
        
        # Try starting from EACH cell in grid
        # Word could start anywhere, so check all positions
        for r in range(rows):
            for c in range(cols):
                # If search from (r,c) succeeds, word exists
                if backtrack(r, c, 0):
                    return True
        
        # Tried all starting positions, word not found
        return False

sol = Solution()
board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
print("Word Search 'ABCCED':", sol.exist(board, "ABCCED"))  # True
print("Word Search 'SEE':", sol.exist(board, "SEE"))        # True
print("Word Search 'ABCB':", sol.exist(board, "ABCB"))      # False

# ═══════════════════════════════════════════════════════════════════
# DECISION TREE: exist(board, "AB")
# ═══════════════════════════════════════════════════════════════════
#
# Board: [["A","B"],        Word: "AB"
#         ["C","D"]]
#
# Starting from (0,0) = 'A':
#
#                              (0,0) 'A'
#                               idx=0
#                            'A'='A' ✓
#                         /    |    |    \
#                    ↓   /   ↑ |  → |   ← \
#                      /       |    |       \
#                 (1,0)    (-1,0)  (0,1)   (0,-1)
#                  'C'      OOB     'B'      OOB
#                 idx=1    idx=1   idx=1    idx=1
#                'C'≠'B'    ✗     'B'='B'    ✗
#                   ✗              ✓
#                                  |
#                               idx=2
#                            len(word)=2
#                                 ✓
#                            WORD FOUND!

# WHY UNMARK?
# Same cell may be needed in a different path from the same search.
#
# word = "ABFC"
# board = [["A","B","C"],
#          ["D","F","E"],
#          ["G","H","I"]]
#
# Path 1: A → B → F → ??? (no 'C' adjacent to F, fails)
# Path 2: A → B → C ← needs to try this, but if F still '#', board is corrupted
#
# Unmarking F lets us backtrack to B and explore other directions cleanly.