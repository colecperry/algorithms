# 101. Symmetric Tree

# Topics: Tree, DFS, BFS, Binary Tree

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Ex. 1
# #           1
# #         /   \
# #        2     2
# #       / \   / \
# #      3   4 4   3
# # # Input: root = [1,2,2,3,4,4,3]
# # Output: True    

# Ex. 2
# #           1
# #         /   \
# #        2     2
# #         \     \
# #          3     3
# # # Input: root = [1,2,2,null,3,null,3]
# # Output: False   

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            elif left.val != right.val:
                return False
            
            left = dfs(left.left, right.right)
            right = dfs(left.right, right.left)

            return right and left

        return dfs(root.left, root.right)

# #           1
# #         /   \
# #        2     2
# #       / \   / \
# #      3   4 4   3

sol = Solution()
# Tree 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(2)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(4)
root1.right.left = TreeNode(4)
root1.right.right = TreeNode(3)

print(sol.isSymmetric(root1))

# Tree 2
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.right = TreeNode(3)
root2.right.right = TreeNode(3)

print(sol.isSymmetric(root2))