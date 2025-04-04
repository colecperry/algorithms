# 404. Sum of Left Leaves

# Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree

# Given the root of a binary tree, return the sum of all left leaves.

# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

# Example 1:
#
#            3
#           / \
#          /   \
#         9     20
#               / \
#              15  7
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

# Example 2:

# Input: root = [1]
# Output: 0

# How to Solve (DFS):
    # We need a way to know if the node we are recursively searching is a left leaf node:   
        # To figure out if the node is a leaf node, we can check if the current node has a .left and .right
        # Each time we recurse left, we pass another argument is_left and set it to True, that way, we can use that to find out if the node is a left node (meaning we recursed left to get here)
        # If we find a left leaf node, we update the global variable total_sum

"""
    🕒 Time Complexity: O(N)  
    - Each node is visited once → O(N), where N is the number of nodes.

    🖥 Space Complexity: O(N) (worst case), O(log N) (best case) -> is based on the recursion depth
    - Best case: O(log N) for a balanced tree.
    - Worst case: O(N) for a skewed tree (linked list like tree)
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object): # DFS
    def sumOfLeftLeaves(self, root):
        self.total_sum = 0  # Store sum of left leaves
        
        def dfs(node, is_left):
            if not node:
                return

            # Check if this node is a left leaf (no children)
            if not node.left and not node.right and is_left:
                self.total_sum += node.val

            dfs(node.left, True) # Recurse left and mark as left child
            dfs(node.right, False) # Recurse right and mark as right child
        
        dfs(root, False)  # Start DFS from root, marking it as not left
        return self.total_sum
    
    def sumOfLeftLeaves2(self, root): # BFS
        queue = deque([(root, False)])
        total_sum = 0
        while queue:
            node, is_left = queue.popleft()
            if node.left == None and node.right == None and is_left:
                total_sum = total_sum + node.val
            if node.left:
                queue.append((node.left, True))
            if node.right:
                queue.append((node.right, False))
        
        return total_sum




my_tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
my_solution = Solution()
print(my_solution.sumOfLeftLeaves2(my_tree))