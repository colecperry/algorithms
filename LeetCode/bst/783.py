# 783. Minimum Distance Between BST Nodes

# Topics: Tree, Depth First Search, Breadth First Search, Binary Search Tree, Binary Tree

# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

# Ex. 1
#               4
#              / \
#             2   6
#            / \
#           1   3
#
# Input: root = [4,2,6,1,3]
# Output: 1

# Ex. 2
#               1
#              / \
#             0   48
#                 / \
#                12 49
#
# Input: root = [1,0,48,null,null,12,49]
# Output: 1

# -------------------------------------------------------------------
# 🔍 Solution: In-Order Traversal + Linear Scan
# -------------------------------------------------------------------
# Strategy:
# - Perform an in-order DFS traversal of the BST to collect node values in sorted order.
# - Store these values in an array.
# - Because in-order traversal of a BST gives values in ascending order, the minimum difference between any two nodes must be between two consecutive values.
# - Loop through the sorted array and compare each adjacent pair to find the minimum difference.

# Time Complexity:
# - O(n) to traverse the entire tree using DFS
# - O(n) to scan the array and compute differences
# - Total: O(n)

# Space Complexity:
# - O(n) to store the in-order array of node values
# - O(h) for the recursion stack, where h is the height of the tree
# - Total space: O(n)


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        arr = [] # Array stores in order DFS elements from in order traversal (sorted)
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            arr.append(node.val) # Create an in order array
            dfs(node.right)
            return
        dfs(root) # Call helper
        min_diff = float('inf') # Track min difference
        for i in range(1, len(arr)): # Loop through sorted array from index 1
            diff = arr[i] - arr[i-1] # Calc the difference
            min_diff = min(min_diff, diff) # Update min diff
        return min_diff
    
sol = Solution()
t1 = TreeNode(4)
t1.left = TreeNode(2)
t1.right = TreeNode(6)
t1.left.left = TreeNode(1)
t1.left.right = TreeNode(3)

print(sol.minDiffInBST(t1))