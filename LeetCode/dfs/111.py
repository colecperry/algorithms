# 111. Minimum Depth of Binary Tree

# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Example 1:
#               3
#              / \
#             9   20
#                /  \
#               15   17

# root = [3,9,20,null,null,15,7]
# Output = 2

# Example 2:
#               2
#                \
#                 3
#                  \
#                   4 
#                    \
#                     5
#                      \ 
#                       6

# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        TC: O(n) -> visit each node once
        SC: O(h) -> maximum recursion depth is tree height
        NOTE: Keep in mind BFS is more efficient for this problem because you can go level by level and early terminate when leaf node found
        """
        # Base case: no tree exists
        if not root:
            return 0
        
        # Base case: found a leaf node -> depth is just 1 for leaf nodes
        if not root.left and not root.right:
            return 1
        
        # Only left child exists -> keep exploring left, add that depth to curr node
        if not root.left:
            return 1 + self.minDepth(root.right)
        
        # Only right child exists -> keep exploring right, add that depth to curr node
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        # Normal case: both children exist -> keep exploring
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        return 1 + min(left_depth, right_depth) # Add one for curr node
    
    # Example 1:
    #               3
    #              / \
    #             9   20
    #                /  \
    #               15   17


my_solution = Solution()

root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(17)

print(my_solution.minDepth(root1)) # 2

#               2
#                \
#                 3
#                  \
#                   4 
#                    \
#                     5
#                      \ 
#                       6

root2 = TreeNode(2)
root2.right = TreeNode(3)
root2.right.right = TreeNode(4)
root2.right.right.right = TreeNode(5)
root2.right.right.right.right = TreeNode(6)

print(my_solution.minDepth(root2)) # 5