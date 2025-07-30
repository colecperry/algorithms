# 103. Binary Tree Zigzag Level Order Traversal

# Topics: Tree, Breadth-First Search, Binary Tree

# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

# Example 1:
# 
#          3
#         / \
#        /   \
#       9    20
#           /  \
#          15   7
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []

# -----------------------
# 💡 How to Solve:
# -----------------------

# Use Breadth-First Search (BFS) to perform a level-order traversal of the binary tree
# To achieve the zigzag pattern:
#   - Keep a flag that flips at each level to indicate whether to reverse the values or not

# 1. Handle the edge case where the root is None → return an empty list
# 2. Initialize a queue with the root node for BFS
# 3. For each level:
#     - Create a temporary list to store the values at that level
#     - For each node in the level:
#         - Pop from the queue and add its value to the temporary list
#         - Add its left and right children to the queue if they exist
#     - If the flag is True, reverse the list before adding to the result
#     - Flip the flag for the next level to toggle the zigzag order
# 4. Return the final output list after BFS traversal completes

# -----------------------
# ⏱️ Time Complexity:
# -----------------------

# O(n)
# - Each node is visited exactly once, and its value is appended and possibly reversed once

# -----------------------
# 📦 Space Complexity:
# -----------------------

# O(n)
# - The queue can store up to O(n) nodes in the worst case (last level)
# - The output list also stores all node values in total


from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: # Edge case for empty tree
            return []
        queue = deque([root]) # init deque for BFS
        output = [] # final output list
        flag = False # flag toggles whether we append each level in reverse order
        while queue:
            inner = [] # inner list to hold each level
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                inner.append(node.val) # append all values for the whole level
            if flag == False: # zigzag logic
                output.append(inner)
            else:
                output.append(list(reversed(inner)))
            flag = not flag # toggle flag each level
        return output
                
sol = Solution()

root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

print(sol.zigzagLevelOrder(root1)) # [[3],[20,9],[15,7]]