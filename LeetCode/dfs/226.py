# 226. Invert Binary Tree

# Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree

# Given the root of a binary tree, invert the tree, and return its root.

# Ex. 1
#
#               4                    4
#              / \                  / \
#             /   \                /   \
#            2     7      ->      7     2
#           / \   / \            / \   / \
#          1   3 6   9          9   6 3   1
#
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Ex. 2
# Input: root = [2,1,3]
# Output: [2,3,1]

# Ex. 3
# Input: root = []
# Output: []

# How to solve (Recursive):
    # (Base Case):
        # Scenario A: I'm at a null node -> Return null immediately (nothing to invert)
    # Swap the children
    # Recursively call the fn on left and right subtrees (inverts them)
    # Return the root

# Time Complexity: O(n)
# - We visit every node exactly once

# Space Complexity: O(h), where h is the height of the tree
# - Due to recursive call stack
# - Worst case: O(n) for a skewed tree
# - Best case: O(log n) for a balanced tree

# How to solve (Iterative):
    # Create a stack and append the root node
    # Loop, pop node off the stack, swap it's children, then append it's children if not null

# Time complexity: O(n) -> we process every node once 
# Space complexity: Best case O(1) -> in a linked list like tree, we only store one node in the array at a time because we pop and push one each loop, O(h) worst case -> the number of nodes in the array at one time equals the height of the tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTreeRecursive(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: # Edge case for empty tree 
            return  # & base case for end of recursion
        # Swap the children
        root.left, root.right = root.right, root.left
        # Recur on the children
        self.invertTreeRecursive(root.left)
        self.invertTreeRecursive(root.right)
        return root
    
    def invertTreeIterative(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: # Empty tree
            return None
        
        stack = [root] # Iterative stack starting with the root

        while stack:
            node = stack.pop() # Pop node off the end of the stack
            node.left, node.right = node.right, node.left # Swap children
            if node.left:
                stack.append(node.left) # Add the children
            if node.right:
                stack.append(node.right)
        
        return root


sol = Solution()

t1 = TreeNode(4)
t1.left = TreeNode(2)
t1.right = TreeNode(7)
t1.left.left = TreeNode(1)
t1.left.right = TreeNode(3)
t1.right.left = TreeNode(6)
t1.right.right = TreeNode(9)

print(sol.invertTreeRecursive(t1))

t1 = TreeNode(4) # Restore the tree
t1.left = TreeNode(2)
t1.right = TreeNode(7)
t1.left.left = TreeNode(1)
t1.left.right = TreeNode(3)
t1.right.left = TreeNode(6)
t1.right.right = TreeNode(9)

print(sol.invertTreeIterative(t1))

