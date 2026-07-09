# 543. Diameter of Binary Tree

# Tree, Depth-First Search, Binary Tree

# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

# Example 1:
# 
#         1
#        / \
#       /   \
#      2     3
#     / \
#    4   5
#
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

# Example 2: 
# Input: root = [1,2]
# Output: 1

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        max_diameter = float('-inf')
        def dfs(node):
            if not node:
                return 0
            left_depth = 1 + dfs(node.left)
            right_depth = 1 + dfs(node.right)
            max_diameter = max(max_diameter, left_depth + right_depth)
            return 

        return max_diameter
        

my_tree = TreeNode(1, TreeNode(2, TreeNode(4, None, None), TreeNode(5, None, None)), TreeNode(3, None, None))
my_tree_2 = TreeNode(1, TreeNode(2), None)
my_solution = Solution()
print(my_solution.diameterOfBinaryTree(my_tree))
print(my_solution.diameterOfBinaryTree(my_tree_2))