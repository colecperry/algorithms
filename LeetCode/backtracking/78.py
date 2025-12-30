# 78. Subsets

# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

from typing import List

# ============================================
# SOLUTION 1: Iterative Building (RECOMMENDED)
# ============================================

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(start, path):
            # Add current subset to result (every path is valid!)
            result.append(path[:])  # [:] creates a copy
            
            # Try adding each remaining element
            for i in range(start, len(nums)):
                path.append(nums[i])   # Choose: add nums[i]
                backtrack(i + 1, path) # Explore: build subsets with nums[i]
                path.pop()             # Undo: remove nums[i] to try next
        
        backtrack(0, [])
        return result
    
sol = Solution()
print(sol.subsets([1,2,3])) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print(sol.subsets([0])) # [[],[0]]
print(sol.subsets([1,2])) # [[], [1], [1,2], [2]]
    
# ═══════════════════════════════════════════════════════════════
# VISUAL CALL STACK TRACE: nums = [1,2]
# ═══════════════════════════════════════════════════════════════
# 
# Step 1: Call backtrack(0, [])
#   path = []
#   ├─ Append [] to result → result = [[]]
#   ├─ Loop: i goes from 0 to 1
#   │
#   │  ITERATION 1 (i=0):
#   │  ├─ path.append(nums[0]) → path = [1]
#   │  │
#   │  │  Step 2: Call backtrack(1, [1])  ← NEW CALL
#   │  │    path = [1]
#   │  │    ├─ Append [1] to result → result = [[], [1]]
#   │  │    ├─ Loop: i goes from 1 to 1
#   │  │    │
#   │  │    │  ITERATION 1 (i=1):
#   │  │    │  ├─ path.append(nums[1]) → path = [1, 2]
#   │  │    │  │
#   │  │    │  │  Step 3: Call backtrack(2, [1,2])  ← NEW CALL
#   │  │    │  │    path = [1, 2]
#   │  │    │  │    ├─ Append [1,2] to result → result = [[], [1], [1,2]]
#   │  │    │  │    ├─ Loop: range(2, 2) → EMPTY RANGE, no iterations
#   │  │    │  │    └─ RETURN ← Back to Step 2
#   │  │    │  │
#   │  │    │  ├─ path.pop() → path = [1]  ← BACKTRACK!
#   │  │    │  └─ Loop done (no more i values)
#   │  │    │
#   │  │    └─ RETURN ← Back to Step 1
#   │  │
#   │  ├─ path.pop() → path = []  ← BACKTRACK!
#   │  │
#   │  ITERATION 2 (i=1):
#   │  ├─ path.append(nums[1]) → path = [2]
#   │  │
#   │  │  Step 4: Call backtrack(2, [2])  ← NEW CALL
#   │  │    path = [2]
#   │  │    ├─ Append [2] to result → result = [[], [1], [1,2], [2]]
#   │  │    ├─ Loop: i goes from 2 to 1 (NO ITERATIONS - empty range!)
#   │  │    └─ RETURN ← Back to Step 1
#   │  │
#   │  ├─ path.pop() → path = []  ← BACKTRACK!
#   │  └─ Loop done
#   │
#   └─ RETURN

# FINAL: result = [[], [1], [1,2], [2]]
    
# ============================================
# SOLUTION 2: Binary Decision Tree (LEARNING)
# ============================================
class Solution2:
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        result = [] # final output
        subset = [] # curr subset
        
        def dfs(i):
            # Base case: considered all elements, save this subset
            if i >= len(nums):
                result.append(subset[:])  # [:] creates a copy
                return
            
            # LEFT BRANCH: INCLUDE nums[i] in subset
            subset.append(nums[i])
            dfs(i + 1)
            
            # RIGHT BRANCH: DON'T INCLUDE nums[i] (backtrack first)
            subset.pop()  # Undo the append above
            dfs(i + 1)
        
        dfs(0)  # Start decision tree at index 0
        return result


# ============================================
# VISUALIZATION FOR SOLUTION 2: nums=[1,2]
# ============================================
#
#                       dfs(0)
#                     /        \
#            include 1          exclude 1
#              [1]                  []
#             /    \              /     \
#      include 2  exclude 2   include 2  exclude 2
#        [1,2]      [1]         [2]         []
#
# Result: [[], [1], [1,2], [2]]  (builds right to left)

sol2 = Solution2()
print(sol2.subsets2([1,2,3])) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print(sol2.subsets2([0])) # [[],[0]]
print(sol.subsets([1,2])) # [[], [1], [1,2], [2]]