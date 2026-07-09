# 110. Balanced Binary Tree

# Given a binary tree, determine if it is height-balanced.

# Example 1:
#                3
#               / \
#              /   \
#             9     20
#                   / \
#                  /   \
#                 15    7
# Input: root = [3,9,20,null,null,15,7]
# Output: True

# Example 2:
#                     1
#                   /   \
#                  2     2
#                 / \       
#                3   3       
#               / \     
#              4   4   
#         
#
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: False

# Example 3:
# Input: root = []
# Output: True

# Example 4:
# Input: root = [1, 2, 2, 3, null, null, null, 4, null, 5]
# Output: False
#         1
#        / \
#       2   2
#      /
#     3
#    /
#   4
#  /
# 5

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(node): # Post order: return null at base case, build answer bottom up
            if not node: # Base Case -> null node has height of 0
                return 0
            left_height = dfs(node.left) # Get height of L & R subtrees
            right_height = dfs(node.right)
            
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1 # propagate unbalanced signal up, or catch imbalance here

            # height here = max of left and right subtrees + 1 for current node
            return 1 + max(left_height, right_height) 
            
        return dfs(root) != -1 # check if root is height balanced
    
#         1
#        / \
#       2   2
#      /
#     3
#    /
#   4
#  /
# 5

sol = Solution()
root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
root2 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
root4 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5)))), TreeNode(2))
print(sol.isBalanced(root1)) # True
print(sol.isBalanced(root2)) # False -> -1 trigger by abs check
print(sol.isBalanced(root4)) # False -> -1 triggered by left check
