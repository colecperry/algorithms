# 226. Invert Binary Tree

# Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree

# Given the root of a binary tree, invert the tree, and return its root.

# Ex. 1

#               4                    4
#              / \                  / \
#             /   \                /   \
#            2     7      ->      7     2
#           / \   / \            / \   / \
#          1   3 6   9          9   6 3   1

# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Ex. 2
# Input: root = [2,1,3]
# Output: [2,3,1]

# Ex. 3
# Input: root = []
# Output: []

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTreeRecursive(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        TC: O(n) -> visit each node once
        SC: O(h) -> call stack depth equals tree height
                -> O(log n) balanced, O(n) worst case skewed
        """
        if not root: # Edge case for empty tree 
            return  # & base case for end of recursion
        # Swap the children
        root.left, root.right = root.right, root.left
        # Recur on the children
        self.invertTreeRecursive(root.left) # ignore return values
        self.invertTreeRecursive(root.right)
        
        return root # matters for original caller only
    
    #               4                    4
    #              / \                  / \
    #             /   \                /   \
    #            2     7      ->      7     2
    #           / \   / \            / \   / \
    #          1   3 6   9          9   6 3   1
    
    def invertTreeIterative(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        - TC: O(n) -> visit each node once
        - SC: O(w) -> stack holds at most w nodes where w is max width of the tree
            -> O(n) worst case for a perfect binary tree (bottom level has n/2 nodes)
            -> O(1) best case for a skewed tree (only one node in stack at a time)
        """
        if not root: # Empty tree
            return None
        
        stack = [root] # Iterative stack starting with the root

        while stack:
            node = stack.pop() # Pop node off the end of the stack
            node.left, node.right = node.right, node.left # Swap children
            if node.right:
                stack.append(node.right) # Add the children -> R then L for DFS
            if node.left:
                stack.append(node.left)
        
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

