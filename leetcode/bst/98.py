# 98. Validate Binary Search Tree

# Topics: Tree, DFS, BST, Binary Tree

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Ex. 1

#            2
#          /   \
#         /     \
#        1       3

# Input: root = [2,1,3]
# Output: true

# Ex. 2

#            5
#          /   \
#         /     \
#        1       4
#               / \
#              /   \
#             3     6

# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        TC: O(n) -> visit each node once for DFS + O(n) for validation loop = O(n)
        SC: O(n) -> arr stores all n node values
        """
        arr = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            arr.append(node.val)  # In-order appends values in sorted order for a valid BST
            dfs(node.right)

        dfs(root)

        # A valid BST's in-order traversal produces strictly increasing values
        for i in range(1, len(arr)):
            if arr[i] <= arr[i - 1]:  # Equal values also invalid — BST requires strictly increasing
                return False

        return True
    
    def isValidBSTBounds(self, root: Optional[TreeNode]) -> bool:
        """
        TC: O(n) -> visit each node once
        SC: O(h) -> call stack depth equals tree height
                 -> O(log n) balanced, O(n) worst case skewed
        """
        def pre_order(node, min, max):
            if not node:  # Reached end without violation
                return True
            if node.val <= min or node.val >= max:  # Bounds violated — not a valid BST
                return False
            left_is_valid = pre_order(node.left, min, node.val)   # Left child must be < current node
            right_is_valid = pre_order(node.right, node.val, max) # Right child must be > current node

            return left_is_valid and right_is_valid  # Both subtrees must be valid

        return pre_order(root, float('-inf'), float('inf'))  # Root has no constraints yet
    
#            2
#          /   \
#         /     \
#        1       3

# Tree 1: [2,1,3]
root1 = TreeNode(2, TreeNode(1), TreeNode(3))

# Tree 2: [5,1,4,null,null,3,6]  
root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))

sol = Solution()
print(sol.isValidBST(root1)) # True
print(sol.isValidBST(root2)) # False

print(sol.isValidBSTBounds(root1)) # True
print(sol.isValidBSTBounds(root2)) # False