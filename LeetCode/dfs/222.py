# 222. Count Complete Tree Nodes

# Given the root of a complete binary tree, return the number of the nodes in the tree.

# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Design an algorithm that runs in less than O(n) time complexity.

# Example 1:
# Input: root = [1,2,3,4,5,6]
# Output: 6

#             1
#           /   \
#          /     \
#         2       3
#        / \     /
#       4   5   6

# Example 2:
# Input: root = []
# Output: 0

# Example 3:
# Input: root = [1]
# Output: 1

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    - TC: O((log n)²)
        - Tree height h = log n
        - Recursion follows at most one path down the tree: O(log n) calls because one subtree is always perfect and returns immediately, the other path hits the base case and returns after going O(log n) calls deep
        - Each recursive call computes left_height and right_height: O(log n) each
        - Total: O(log n) calls * O(log n) work per call = O((log n)²)
    - SC: O(log n)
        - Recursion stack depth = tree height = O(log n) worst case when none of the subtrees are equal
        - Each stack frame uses O(1) space
        - No additional data structures
    """
    def countNodes(self, root):
        if not root:
            return 0
        
        def get_left_height(node):
            """Count levels going all the way left"""
            height = 0
            while node:
                height += 1
                node = node.left
            return height
        
        def get_right_height(node):
            """Count levels going all the way right"""
            height = 0
            while node:
                height += 1
                node = node.right
            return height
        
        # Compute heights
        left_height = get_left_height(root)
        right_height = get_right_height(root)
        
        if left_height == right_height:
            # Perfect tree: use formula
            return (2 ** left_height) - 1
        else:
            # Not perfect: recurse on subtrees
            left_subtree_height = self.countNodes(root.left)
            right_subtree_height = self.countNodes(root.right)
            return 1 + left_subtree_height + right_subtree_height
        
sol = Solution()
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
print(sol.countNodes(root))