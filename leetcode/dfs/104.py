# 104 - Maximum Depth of Binary Tree

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:
#                3
#               / \
#              /   \
#             9     20
#                   / \
#                  /   \
#                 15    7
#
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
#                3
#                 \
#                  \
#                   2
#
# Input: root = [1,null,2]
# Output: 2

from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # Recursive DFS
    def maxDepth1(self, root):
        """
        - TC: O(n) — visit each node once
        - SC: O(h) — call stack depth equals tree height → O(log n) balanced, O(n) worst case skewed
        """
        if not root: # Base case
            return 0
        
        left_depth = self.maxDepth1(root.left) # Call fn on the left child
        right_depth = self.maxDepth1(root.right) # Call fn on the right child


        return 1 + max(left_depth, right_depth) # Take max of both children and add one for current node

    # Iterative DFS
    def maxDepth2(self, root):
        """
        TC: O(n) -> visit each node once
        SC: O(h) -> stack holds at most h nodes
                -> O(log n) balanced, O(n) worst case skewed
        """
        if not root:
            return 0

        stack = [(root, 1)]  # (node, depth at this node)
        max_depth = 0

        while stack:
            node, depth = stack.pop()

            max_depth = max(max_depth, depth)  # Is this the deepest node we've seen?

            if node.left:
                stack.append((node.left, depth + 1))   # Go deeper left
            if node.right:
                stack.append((node.right, depth + 1))  # Go deeper right

        return max_depth


my_solution = Solution()
root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
root2 = root = TreeNode(1, None, TreeNode(2))
print(my_solution.maxDepth2(root1))
print(my_solution.maxDepth1(root2))


