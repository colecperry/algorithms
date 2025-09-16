# 102. Binary Tree Level Order Traversal

# Topics: Tree, BFS, Binary Tree

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Ex. 1
#            3
#           / \
#          /   \
#         9    20
#             /  \
#           15    7
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []


from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: # Edge case - empty tree
            return []
        queue = deque([root]) # BFS queue
        output = []
        while queue:
            inner = [] # collect BFS level
            for _ in range(len(queue)): # travese full BFS level
                node = queue.popleft()
                inner.append(node.val)
                if node.left: # Append children if non null (next level)
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append(inner) # Append the full level each iteration
        
        return output
    
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

sol = Solution()

print(sol.levelOrder(root)) # [[3],[9,20],[15,7]]
