# 98. Validate Binary Search Tree

# Topics: Tree, DFS, BST, Binary Tree

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Ex. 1
#
#            2
#          /   \
#         /     \
#        1       3
#
# Input: root = [2,1,3]
# Output: true

# Ex. 2
#
#            5
#          /   \
#         /     \
#        1       4
#               / \
#              /   \
#             3     6
# 
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# BST Pattern 1: BST Validation using In-order Traversal Property
# Key insight: In-order traversal on a valid BST builds a strictly increasing array

# APPROACH:
    # 1. Perform in-order traversal to collect all node values in order
    # 2. Check if resulting array is strictly increasing (no duplicates, no decreasing values)
    # 3. Return True if strictly increasing, False otherwise

# INORDER + ARRAY SOLUTION:
    # - Traversal: DFS in-order to build sorted array from BST
    # - Validation: Check if array[i] > array[i-1] for all consecutive pairs
    # - TC: O(n) - visit each node once + O(n) array validation = O(n) total
    # - SC: O(n) for array storage + O(h) for recursion stack = O(n) total

# KEY INSIGHT: 
# Valid BST property: In-order traversal produces strictly increasing sequence
# Invalid BST indicators: Duplicates or decreasing values in in-order sequence

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool: # O(n) Space
        arr = [] # In order traversal on a BST builds a sorted array of strictly increasing values (no dupliates)
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)
        dfs(root)
        
        # Check if the array is sorted -> don't use sorted() because it includes duplicates
        for i in range(1, len(arr)): 
            if arr[i] <= arr[i - 1]: # If curr val is less than or equal to the prev value, array is not sorted
                return False
        return True
    
    # BST Pattern 6: Top Down Context Passing

    # APPROACH:
    # 1. Pass valid range bounds (min, max) down to each node during traversal
    # 2. Check if current node value violates its inherited bounds
    # 3. Update bounds for children: left gets (min, node.val), right gets (node.val, max)
    # 4. Return True only if current node is valid AND both subtrees are valid

    # BOUNDS CHECKING SOLUTION:
        # - Traversal: DFS with min/max bounds passed down to each recursive call
        # - Validation: Each node checks if node.val is within (min_val, max_val) range
        # - TC: O(n) - visit each node once with constant time bound checks
        # - SC: O(h) for recursion stack only, no extra array storage needed

    # KEY INSIGHT: 
    # Valid BST property: Each node must satisfy bounds inherited from ancestors
    # Left child bounds: (ancestor_min, parent_val), Right child bounds: (parent_val, ancestor_max)
    # Validation happens during traversal, eliminating need for array storage
    
    def isValidBSTBounds(self, root: Optional[TreeNode]) -> bool: # O(1) Space
        """
        Validate BST using bounds checking - O(1) extra space
        Time: O(n), Space: O(h) recursion stack only
        """
        def validate(node, min_val, max_val):
            if not node: # Base case -> an empty node is a valid BST, we reached the end of the path
                return True
            
            # Check if current node violates BST property
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # Recursively validate subtrees with updated bounds:
                # between -inf and node.val for left subtree
                # between node.val and inf for right subtree
            return (validate(node.left, min_val, node.val) and 
                    validate(node.right, node.val, max_val)) # Both subtrees must return True for the subtree to be a valid BST
        
        return validate(root, float('-inf'), float('inf')) # Pass in inf bounds for the root node
    
#            2
#          /   \
#         /     \
#        1       3

# Tree 1: [2,1,3]
root1 = TreeNode(2, TreeNode(1), TreeNode(3))

# Tree 2: [5,1,4,null,null,3,6]  
root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))

sol = Solution()
print(sol.isValidBST(root1)) # True
print(sol.isValidBST(root2)) # False

print(sol.isValidBSTBounds(root1)) # True
print(sol.isValidBSTBounds(root2)) # False