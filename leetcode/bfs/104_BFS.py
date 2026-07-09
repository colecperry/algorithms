#104 - Maximum Depth of Binary Tree

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
from typing import Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # BFS - level based
    def maxDepth2(self, root):
        if not root:
            return 0
        
        level = 0 # Store the levels of the tree
        q = deque([root]) # Always wrap root in a list when creating a deque so it's iterable

        while q: # While the deque is not empty

            for i in range(len(q)): # It for each ele in deque
                node = q.popleft() # Pop the node off the deque
                if node.left: # Check if it has a left child
                    q.append(node.left) # Append to the deque
                if node.right:
                    q.append(node.right)
            
            level += 1 # Increment the level
        
        return level
    
    # BFS - tuple based
    def maxDepth3(self, root: Optional[TreeNode]) -> int:
        if root == None: # Edge case empty tree
            return 0
        max_depth = 1 # Track max depth
        q = deque([(root, 1)]) # Each tuple has ele & level
        while q: # Loop until queue is empty 
            node, depth = q.popleft() # Pop next tuple & destructure
            max_depth = max(max_depth, depth) # Update max depth
            if node.left: # Append left child if not None
                q.append((node.left, depth + 1)) 
            if node.right: # Append right child if not None
                q.append((node.right, depth + 1))
        return max_depth 
    
    # Example 1:
    #                3
    #               / \
    #              /   \
    #             9     20
    #                   / \
    #                  /   \
    #                 15    7


my_solution = Solution()
root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
root2 = root = TreeNode(1, None, TreeNode(2))
print(my_solution.maxDepth3(root1))
print(my_solution.maxDepth1(root2))


