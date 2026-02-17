# 530. Minimum Absolute Difference in BST

# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

# Example 1:
# Input: root = [4,2,6,1,3]
# Output: 1

#             4
#           /   \
#          /     \
#         2       6
#        / \     
#       1   3   

# Example 2:
# Input: root = [1,0,48,null,null,12,49]
# Output: 1

#             1
#           /   \
#          /     \
#         0      48
#               /  \
#              12  49

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int: # O(n) space version
            """
            TC: O(n) 
                - In-order traversal: O(n) to visit all nodes
                - Loop through array: O(n) to find min difference
                - Total: O(n)

            SC: O(n)
                - nodes array: O(n) to store all values
                - Recursion stack: O(h) 
                - Total: O(n) + O(h) = O(n) since array dominates
            """
            nodes = [] # store nodes in sorted order
            def in_order(root):
                if not root:
                    return

                in_order(root.left)
                nodes.append(root.val)
                in_order(root.right)

            in_order(root)

            min_diff = float('inf')
            for i in range(1, len(nodes)): # compare adjacent nodes to find min diff
                min_diff = min(min_diff, nodes[i] - nodes[i - 1])
            
            return min_diff

    def getMinimumDifference2(self, root: Optional[TreeNode]) -> int: # O(log n) space version
        """
        TC: O(n) -> we visit each node once and process the min diff
        SC: O(h) -> the max depth of the call stack is the height of the tree which is O(log n) average and O(h) for a skewed tree
        NOTE: Since an in-order travesal in a BST visits nodes in sorted order, visit each node, and track the prev node and update the min diff as you go. Use non local to update variables inside the nested function
        """
        min_diff = float('inf') # Track min difference
        prev = None # Track prev node in in-order traversal

        def in_order(node):
            nonlocal min_diff, prev # allows nested function to modify outer scope vars

            if not node:
                return

            in_order(node.left)
            if prev: # only update min difference if prev is past the first in order node
                min_diff = min(min_diff, node.val - prev.val)
            prev = node # update previous node
            in_order(node.right)

        in_order(root)
        
        return min_diff

#             4
#           /   \
#          /     \
#         2       6
#        / \     
#       1   3   


root1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
root2 = TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49)))
sol = Solution()
print(sol.getMinimumDifference(root1)) # 1
print(sol.getMinimumDifference(root2)) # 1

