from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            if len(path) == k:
                res.append(path[:])
                return
            
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(1, [])

        return res
    
# ============================================
# VISUALIZATION FOR COMBINATIONS: n=4, k=2
# ============================================
#
#                           backtrack(start=1, path=[])
#                      /          |            |           \
#                  TRY 1        TRY 2         TRY 3       TRY 4
#                    /            |            |             \
#              path=[1]       path=[2]      path=[3]        path=[4]
#              start=2        start=3       start=4         start=5
#             /  |   \          /  \           |        (k not reached)
#         TRY   TRY   TRY     TRY   TRY      TRY 4
#          2     3     4       3     4         |
#          |     |     |       |     |         |
#       [1,2]  [1,3] [1,4]   [2,3] [2,4]     [3,4]
#         ✓      ✓     ✓       ✓     ✓         ✓
#       SAVE   SAVE  SAVE    SAVE   SAVE     SAVE
#
# Result: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]


sol = Solution()
print(sol.combine(4, 2)) # [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
print(sol.combine(1, 1)) # [[1]]
