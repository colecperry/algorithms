# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X. Return the number of good nodes in the binary tree.

# Example 1:
#                3
#               / \
#              /   \
#             1     4
#            /     / \
#           /     /   \
#          3     1     5
# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.

# Example 2:
#                3
#               / 
#              /   
#             3     
#            / \   
#           /   \    
#          4     2  
# Input: root = [3,3,null,4,2]
# Output: 3
# Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

# Example 3:
# Input: root = [1]
# Output: 1
# Explanation: Root is considered as good.

# How to solve:
# Use Preorder traversal - process each node before we recursively traverse to the left and right nodes
# As we traverse to each child, we want to keep track of the largest node value we have seen so far along that path
# When we get to each node, check if we have seen any value greater than the value of the node we are currently on, if we do, don't count that node as a good node, if we do not, count that node as a good node

# Defintion for binary tree node
# class TreeNode:
#      def __init__(self, val=0, left=None, right=None)
#           self.val = val
#           self.left = left
#           self.right = right

class Solution:
    def goodNodes(self, root):
        def dfs(node, max): # Define another function b/c need to pass in more than root
            if not node: # Base case
                return 0 # An empty tree has zero good nodes
        
            res = 1 if node.val >= max else 0# Now we got to a non-empty node - is this node a good node?
            max = max(max, node.val) # Take max of the current max val & current node val
            res += dfs(node.left, max) # Recursive call on left child & update res
            res += dfs(node.right, max) # Recursive call on right child & update res
            return res
        
        return dfs(root, root.val) # Call dfs on the root node, pass in root.val as the max b/c it will count as long it is greater than or equal to the max val so far