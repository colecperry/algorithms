#104 - Maximum Depth of Binary Tree

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# How to Solve
# Solution 1: Recursive DFS
    # Make base case -> Stop the recursion when we reach an empty node and return 0
    # Recursively call the left and right children
    # Return the current node (1) plus the max depth of left and right children to caller

# Example walk through
# maxDepth(3)	Calls maxDepth(9)
# maxDepth(9)	Calls maxDepth(None) (returns 0)
# maxDepth(9)	Calls maxDepth(None) (returns 0)
# maxDepth(9)	Computes 1 + max(0, 0) = 1, returns 1
# maxDepth(3)	Calls maxDepth(20)
# maxDepth(20)	Calls maxDepth(15)
# maxDepth(15)	Calls maxDepth(None) (returns 0)
# maxDepth(15)	Calls maxDepth(None) (returns 0)
# maxDepth(15)	Computes 1 + max(0, 0) = 1, returns 1
# maxDepth(20)	Calls maxDepth(7)
# maxDepth(7)	Calls maxDepth(None) (returns 0)
# maxDepth(7)	Calls maxDepth(None) (returns 0)
# maxDepth(7)	Computes 1 + max(0, 0) = 1, returns 1
# maxDepth(20)	Computes 1 + max(1, 1) = 2, returns 2
# maxDepth(3)	Computes 1 + max(1, 2) = 3, returns 3 (Final Answer)

# Time complexity: O(n): each node is visited once
# Space complexity: O(h): height of the tree, worst case O(n) for skewed tree: This is due to the recursion call stack, which stores function calls during the recursive traversal.

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

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional

class Solution(object):
    # Recursive DFS
    def maxDepth1(self, root):
        if not root: # Base case
            return 0
        
        left_depth = self.maxDepth1(root.left) # Call fn on the left child
        right_depth = self.maxDepth1(root.right) # Call fn on the right child


        return 1 + max(left_depth, right_depth) # Take max of both children and add one for current node
    
    # How to Solve - Level Based BFS: 
    # Big idea: Create a deque and start with the root as the only element, process each level (while loop with a nested for loop) by popping off that element and adding it's children

    # Handle edge case if root is None
    # Initialize variable to count the tree levels and a deque to insert children nodes
    # Loop until the deque is empty
    # Loop over each element in the deque (each level)
        # Pop off the node (popleft() for a queue since it's FIFO
        # Add left and right children nodes if they exist
    # Increment the level

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

    # Iterative DFS
    def maxDepth4(self, root):
        stack = [[root, 1]]
        res = 1

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res


my_solution = Solution()
root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
root2 = root = TreeNode(1, None, TreeNode(2))
print(my_solution.maxDepth3(root1))
print(my_solution.maxDepth1(root2))


