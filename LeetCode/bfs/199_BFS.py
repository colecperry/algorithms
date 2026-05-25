# 199. Binary Tree Right Side View

# Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.


# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

# Explanation:
#           1 <-
#          / \
#         /   \
#        2     3 <-
#         \     \
#          5     4 <-

# Example 2:
# Input: root = [1,2,3,4,null,null,null,5]
# Output: [1,3,4,5]

# Explanation:
#           1 <-
#          / \
#         /   \
#        2     3 <-
#       /
#      4 <-
#     /
#    5 <-

# Example 3:
# Input: root = [1,null,3]
# Output: [1,3]

# Example 4:
# Input: root = []
# Output: []

# How to Solve: BFS
    # Use level-order traversal (BFS) to process nodes level by level
    # Initialize a queue and add the root node
    # For each level:
    #   - Determine the number of nodes at this level (level size)
    #   - Iterate through all nodes in the level:
    #       - Pop a node from the queue
    #       - Add its left and right children to the queue if they exist
    #       - Track the last node processed in this level
    #   - After the level is complete, add the last node's value to the result list
    # Edge case: if the tree is empty, return an empty list immediately

# Time Complexity: O(n), where n is the number of nodes (each visited once)
# Space Complexity: O(n), for the queue and the result list in the worst case


from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        TC: O(n) -> we process each node once
        SC: O(w) -> the queue gets as wide as the largest tree level
        """
        if not root:
            return []
        output = []
        queue = deque([root])
        while queue:
            for _ in range(len(queue)): # BFS loops "level" times
                node = queue.popleft() # queue pops right node last
                if node.left: # Append left then right
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append(node.val) # last node popped from queue is rightmost
        
        return output
    
sol = Solution()

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.right = TreeNode(5)
root1.right.right = TreeNode(4)

print(sol.rightSideView(root1))

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.left.left = TreeNode(5)

print(sol.rightSideView(root2))