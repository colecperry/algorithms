# 101. Symmetric Tree

# Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Ex. 1
#               1
#              / \
#             /   \
#            2     2
#           / \   / \
#          3   4 4   3
#
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Ex. 2
#               1
#              / \
#             /   \
#            2     2
#             \     \
#              3     3
#
# Input: root = [1,2,2,null,3,null,3]
# Output: false

# How to solve: (Recursive)
    # First we need to check if each root node is equal -> this is the second level because the first node is always the same
    # Then, we need to check if the left child of the first subtree is equal to the right child of the second subtree, and vice versa
    # This means comparing: left.left with right.right, and left.right with right.left
    # Base case -> Null nodes are symmetric or if one node is null and the other is not -> not symmetric
    # Check if both nodes exist but their values are different -> not symmetric
    # Use DFS to recursively compare these mirror pairs at each level of the tree
    # Return True only if all mirror pairs match in both structure and value

# Time complexity: O(n) -> we visit each node once
# Space complexity: O(h) -> all dfs algos

# How to solve (Iteratively)
    # 1. Use a stack to simulate recursive DFS.
    #    - Instead of comparing single nodes, push pairs of nodes to compare.
    # 2. Start by pushing a tuple of the root’s left and right children into the stack.
    # 3. While the stack is not empty:
    #    - Pop a pair of nodes from the stack (left, right).
    #    - If both nodes are None, continue (this means symmetry at this level).
    #    - If only one is None or their values differ, return False (asymmetry detected).
    # 4. If the pair is valid:
    #    - Push their children into the stack in mirror order:
    #        - Push (left.left, right.right)
    #        - Push (left.right, right.left)
    # 5. Repeat until the stack is empty.
    #    - If you never return False, then the tree is symmetric — return True.

# Time Complexity: O(n)
# - Every node is visited once during the comparison.

# Space Complexity: O(h)
# - 'h' is the height of the tree.
# - The stack will hold up to O(h) pairs of nodes in the worst case.


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetricRecursive(self, root: Optional[TreeNode]) -> bool: # Recursive
        def dfs(left, right):
            if not left and not right:  # Base case -> both nodes are None
                return True  # That is symmetrical
            if not left or not right:  # One of the nodes is None
                return False  # Not symmetrical 

            # Get boolean values
            values_match = left.val == right.val # Compare values
            outer_pair = dfs(left.left, right.right) # Traverse to outer pairs (left.left and right.right)
            inner_pair = dfs(left.right, right.left) # Traverse to inner pairs (left.right and right.left)

            return values_match and outer_pair and inner_pair # current node & subtrees match at each level

        return dfs(root.left, root.right) # Two DFS calls starting at second level
    
    def isSymmetricIterative(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True  # An empty tree is symmetric

        # Use a stack where each element is a tuple simulate DFS; store node pairs to compare
        stack = [(root.left, root.right)]

        while stack:
            left, right = stack.pop() # Unpack the tuple

            # Case 1: Both nodes are None -> symmetric at this point
            if not left and not right:
                continue

            # Case 2: One is None or values don't match -> not symmetric -> if False is hit at any point, function ends
            if not left or not right or left.val != right.val:
                return False

            # Push mirrored child pairs to stack for future comparison
            stack.append((left.left, right.right))   # outer pair
            stack.append((left.right, right.left))   # inner pair -> eventually you will append none and hit the base case

        return True  # All checks passed; tree is symmetric


sol = Solution()

t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(2)
t1.left.left = TreeNode(3)
t1.left.right = TreeNode(4)
t1.right.left = TreeNode(4)
t1.right.right = TreeNode(3)

t2 = TreeNode(1)
t2.left = TreeNode(2)
t2.right = TreeNode(2)
t2.left.right = TreeNode(3)
t2.right.right = TreeNode(3)


print(sol.isSymmetricRecursive(t1))
print(sol.isSymmetricRecursive(t2))

print(sol.isSymmetricIterative(t1))
print(sol.isSymmetricIterative(t2))