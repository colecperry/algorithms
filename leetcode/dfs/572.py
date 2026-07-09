# 572. Subtree of Another Tree

# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Ex. 1
#
#                root               subroot
# 
#                 3                    4
#               /   \                /   \
#              /     \              /     \
#             4       5            1       2
#            / \
#           /   \
#          1     2
#
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# Ex. 2
#
#                root               subroot
# 
#                 3                    4
#               /   \                /   \
#              /     \              /     \
#             4       5            1       2
#            / \
#           /   \
#          1     2
#               /
#              0
#
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false

# PATTERN: Combines DFS Pattern 1: visit every node in tree and Pattern 2: For every vistied node, perform dual tree comparison

# APPROACH:
    # 1. Use BFS/DFS to traverse main tree and find nodes matching subtree root value
    # 2. For each match, use helper function to check if trees are identical
    # 3. Return True if any match is found, False otherwise

# ITERATIVE SOLUTION: 
    # - Main function: BFS with queue to find matching root values
    # - Helper function: DFS with stack to compare tree structures
    # - TC: O(m*n) - m = nodes in main tree, n = nodes in subtree. Worst case check every main tree node and compare entire subtree each time
    # - SC: O(w + h)) where w=max width for BFS queue, h=height for DFS stack. BFS queue holds one level at a time, comparison stack goes deep

# RECURSIVE SOLUTION:
    # - Main function: BFS with queue to find matching root values
    # - Helper function: Recursively compare corresponding nodes
    # - TC: O(m*n) where m=main tree nodes, n=subtree nodes
    # - SC: O(h1 + h2) for recursion stack, where h1 = height of main tree, h2 = height of subtree

# KEY INSIGHT: 
# Need to check EVERY node in main tree as potential subtree root, not just first match


from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtreeIterative(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            def sameTree(root1, root2):
                stack = [(root1, root2)] # Store tuple of tree & subtree nodes in iterative stack
                while stack:
                    curr1, curr2 = stack.pop()
                    
                    if not curr1 and not curr2: # If both null -> trees still same
                        continue
                    if not curr1 or not curr2: # If only one node null -> trees not same
                        return False
                    if curr1.val != curr2.val: # If values different -> trees not same
                        return False
                    stack.append((curr1.right, curr2.right))
                    stack.append((curr1.left, curr2.left)) # Explore children -> DFS order pops left off first
                return True

            q = deque([root]) # BFS search until you find the first subroot node in the tree
            while q:
                curr = q.popleft()
                if curr.val == subRoot.val: # Once you find potential subtree
                    result = sameTree(curr, subRoot) # Call helper function and store res
                    if result: # Return true to main function if we find a same tree
                        return True
                
                # Explore children
                if curr.left: 
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            return False # Return False if we explore the whole tree and find no matches

    def isSubtreeRecursive(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(left, right):
            if not left and not right: # If both null -> trees still same
                return True
            if not left or not right: # If only one node null -> trees not same
                return False
            if left.val != right.val: # If values different -> trees not same
                return False
            return (isSameTree(left.left, right.left) and isSameTree(left.right, right.right)) # Explore left then right (DFS)

        if not root:
            return False
            
        queue = deque([root]) # Initialize BFS stack

        while queue: 
            node = queue.popleft()
            
            # Check if current node could be the root of subRoot
            if isSameTree(node, subRoot):
                return True
            
            # Add children to continue BFS traversal
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return False  # Not found after checking all nodes

# Main tree: [3,4,5,1,2]
root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))

# Subtree: [4,1,2]  
subRoot = TreeNode(4, TreeNode(1), TreeNode(2))

sol = Solution()
print(sol.isSubtreeIterative(root, subRoot)) # True
print(sol.isSubtreeRecursive(root, subRoot)) # True

# Main tree: [3,4,5,1,2,null,null,null,null,0]
root2 = TreeNode(3, TreeNode(4, TreeNode(1, None, TreeNode(0)), TreeNode(2)), TreeNode(5))

# Subtree: [4,1,2]  
subRoot2 = TreeNode(4, TreeNode(1), TreeNode(2))

print(sol.isSubtreeIterative(root2, subRoot2)) # False
print(sol.isSubtreeRecursive(root2, subRoot2)) # False