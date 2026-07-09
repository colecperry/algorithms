# 783. Minimum Distance Between BST Nodes

# Tree, Depth-First Search, Breadth-First Search, Binary Search Tree, Binary Tree

# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

# Ex. 1
#         4
#        / \
#       /   \
#      2     6
#     / \
#   1    3

# Input: root = [4,2,6,1,3]
# Output: 1

# Ex. 2
#         1
#        / \
#       /   \
#      0     48
#            / \
#          12   49

# Input: root = [1,0,48,null,null,12,49]
# Output: 1

# HOW TO SOLVE:
# - Use BFS (level-order traversal) to visit every node and collect their values.
# - Store all node values in a list during traversal.
# - After traversal, sort the list so values are in ascending order.
# - Iterate through the sorted list and compute the differences between consecutive values.
# - Keep track of the smallest difference found; return it at the end.

# TIME COMPLEXITY (TC):
# - O(N) to traverse all nodes during BFS.
# - O(N log N) to sort the list of N values.
# - O(N) to scan through the sorted list for differences.
# - Overall: O(N log N), since sorting dominates.

# SPACE COMPLEXITY (SC):
# - O(N) to store the list of node values.
# - O(W) for the queue during BFS, where W is the maximum width of the tree (worst-case O(N)).
# - Overall: O(N) auxiliary space.



from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root is None: # Edge case, empty tree
            return 0
        q = deque([root]) # Initialize a deque with the root node
        values = [] # List to store values of nodes after running BFS
        while q:
            node = q.popleft() # Pop the node from the queue
            values.append(node.val) # Append the value of the node to the values list
            if node.left: # If the left child exists, append it to the queue
                q.append(node.left)
            if node.right: # If the right child exists, append it to the queue
                q.append(node.right)
        values.sort() # Sort the values list to find the minimum difference afterwards
        min_diff = float('inf')
        for i in range(1, len(values)): # Loop through the sorted values list
            min_diff = min(min_diff, values[i] - values[i - 1]) # Calc min difference
        return min_diff
    
sol = Solution()

root1 = TreeNode(4)
root1.left = TreeNode(2)
root1.right = TreeNode(6)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(3)

print(sol.minDiffInBST(root1))  # Expected output: 1




