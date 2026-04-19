# 235. Lowest Common Ancestor of a Binary Search Tree

# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Ex. 1

#             6
#           /   \
#          /     \
#         /       \
#        2         8
#       / \       / \
#      0   4     7   9
#         / \        
#        3   5

# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.

# Ex. 2

#             6
#           /   \
#          /     \
#         /       \
#        2         8
#       / \       / \
#      0   4     7   9
#         / \        
#        3   5

# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

# Example 3:
# Input: root = [2,1], p = 2, q = 1
# Output: 2

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        TC: O(h) -> only traverse one path, not all nodes
                -> O(log n) balanced, O(n) worst case skewed
        SC: O(h) -> call stack depth equals tree height
                -> O(log n) balanced, O(n) worst case skewed
        """
        # Split point found — root is between p and q (check both orderings since p/q order not guaranteed)
        if (p.val <= root.val <= q.val) or (q.val <= root.val <= p.val):
            return root

        # Both nodes smaller than root — LCA must be in left subtree
        elif p.val <= root.val and q.val <= root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # Both nodes larger than root — LCA must be in right subtree
        else:
            return self.lowestCommonAncestor(root.right, p, q)
            
#             6
#           /   \
#          /     \
#         /       \
#        2         8
#       / \       / \
#      0   4     7   9
#         / \        
#        3   5

root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
sol = Solution()

node_2 = TreeNode(2)
node_8 = TreeNode(8)
node_4 = TreeNode(4)
print(sol.lowestCommonAncestor(root, node_2, node_8)) # 6
print(sol.lowestCommonAncestor(root, node_2, node_4)) # 2