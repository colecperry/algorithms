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

# Big Idea -> Recursion 3 step process
    # What can I answer immediately? (Base Cases)
        # Scenario A: Null node -> return 0 (a null node has no tree depth)
        # Scenario B: Leaf node -> return 1 (just count this node since it's the end of the path)
        # Scenario C: Only one child exists -> keep exploring path (which returns the depth), and one for curr node
    # What do I need to know?
        # Numbers/Depth counts -> what's the min depth from any left/right child to any leaf?
        # Each recursive call returns an integer representing the shortest distance to a leaf
    # How do I combine the answers?
        # Math operation (min) + add 1

# Time Complexity: We will traverse each node in the tree only once; hence, the total time complexity would be O(N).
# Space Complexity: The only space required is the stack space; the maximum number of active stack calls would equal the maximum depth of the tree, which could equal the total number of nodes in the tree. Hence, the space complexity would equal O(N).

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # DFS Solution
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: no tree exists
        if not root:
            return 0
        
        # Base case: found a leaf node -> depth is just 1 for leaf nodes
        if not root.left and not root.right:
            return 1
        
        # Special case: only left child exists -> keep exploring left and add that depth to curr node
        if not root.left:
            return 1 + self.minDepth(root.right)
        
        # Special case: only right child exists -> keep exploring right and add that depth to curr node
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        # Normal case: both children exist -> keep exploring
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right)) # Return one for root and min depth of (L, R)
    
    # Example 1:
    #               3
    #              / \
    #             9   20
    #                /  \
    #               15   17

    
    def minDepth2(self, root): # BFS
        if not root:
            return 0
        q = deque([root])
        depth = 1
        while q:
            qSize = len(q)
            for _ in range(qSize):
                node = q.popleft()
                # Since we added nodes without checking null, we need to skip them here.
                if not node:
                    continue
                # The first leaf would be at minimum depth, hence return it.
                if not node.left and not node.right:
                    return depth
                q.append(node.left)
                q.append(node.right)
            depth += 1
        return -1


my_solution = Solution()

root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(17)

print(my_solution.minDepth(root1))

root2 = TreeNode(2)
root2.right = TreeNode(3)
root2.right.right = TreeNode(4)
root2.right.right.right = TreeNode(5)
root2.right.right.right.right = TreeNode(6)

print(my_solution.minDepth(root2))