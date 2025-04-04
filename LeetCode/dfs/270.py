# 270. Closest Binary Search Tree Value

# Topics: Binary Search, Tree, Depth-First Search, Binary Search Tree, Binary Tree

# Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. If there are multiple answers, print the smallest.

# Example 1:
#
#          4
#         / \
#        /   \
#       2     5
#      / \
#     1   3
# 
# Input: root = [4,2,5,1,3], target = 3.714286
# Output: 4

# Example 2:
# root = [1], target = 4.428571
# Output: 1

# How to Solve (DFS)
    # Big Picture -> We need to use dfs to recurse through the tree and find the node with the smallest difference to the result
    # We need to store the variables result and min diff in the class using .self -> if we define variables result and min diff in the outer function, we can access them in the inner function but can't modfy them unless we use "non local (works if not in a class) or self. (for class based code)"
    # Define an inner function dfs() that starts with the root call in the outer function
    # In the inner function, we follow an in order traversal which has a base case and checks the node to see if it's a smaller difference, if it is, we update our answer in the class

    # Time complexity: O(n) -> we process each node
    # Space complexity: O(n) for the recursive call stack in a skewed tree (linked list like tree)

from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def closestValue(self, root, target):
        """
        Finds the value in the BST that is closest to the target.
        """
        self.result = None # Store the result in the class
        self.min_diff = float('inf') # Store the min difference in the class

        def dfs(node):
            if not node: # Base case -> Node = None
                return

            dfs(node.left) # Recruse to left node
            
            # Check if current node's diff is less than smallest diff
            if abs(node.val - target) < self.min_diff: 
                self.result = node.val # Store node as result
                self.min_diff = abs(node.val - target) # Update min diff

            dfs(node.right) # Recurse to the right node

        dfs(root) # Call dfs()
        
        return self.result


my_tree_1 = TreeNode(4, TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)), TreeNode(5, None, None))
my_tree_2 = TreeNode(1, None, None)

my_solution = Solution()
print(my_solution.closestValue(my_tree_1, 3.714286))
print(my_solution.closestValue(my_tree_2, 4.428571))