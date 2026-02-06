# 112. Path Sum

# Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree

# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

# Ex. 1
#               5 x
#              / \
#             /   \
#            4 x   8
#           /     / \
#          /     /   \
#         11 x  13    4
#        /  \          \
#       7    2 x        1
#
#
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.

# Ex. 2
#
#         1
#        / \
#       2   3
#
# Input: root = [1,2,3], targetSum = 5
# Output: false
# Explanation: There are two root-to-leaf paths in the tree:
# (1 --> 2): The sum is 3.
# (1 --> 3): The sum is 4.
# There is no root-to-leaf path with sum = 5.

# Ex. 3
# Input: root = [], targetSum = 0
# Output: false
# Explanation: Since the tree is empty, there are no root-to-leaf paths.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution: 
    # Recursive remaining sum solution - no helper fn
    def hasPathSumRecursive(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        - TC: O(n) -> Worst case, we visit each node once
        - SC: O(h) -> The deepest recursion stack depth is equal to the tree height
        - NOTE: If we have only a left child or right child, we recurse and hit Base Case 1
        """
        # Base Case 1
        if not root: # Empty Tree
            return False
        
        # Base Case 2
        elif not root.left and not root.right: # Leaf Node
            return targetSum - root.val == 0

        # Recursive Case -> Check both left and right
        found_sum_left = self.hasPathSumRecursive(root.left, targetSum - root.val)
        found_sum_right = self.hasPathSumRecursive(root.right, targetSum - root.val)

        return found_sum_left or found_sum_right
    
    # Recursive helper version with running sum
    def hasPathSumRecursive2(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: # Check for empty tree
            return False

        def dfs(node, currSum):
            # Base case -> we hit a leaf node, check if we found the path sum
            if not node.left and not node.right:
                return currSum == targetSum

            # Recursive case: explore left child if it exists
            if node.left: # Must check for null first because if node.left is null we can't access it's val -> error
                left = dfs(node.left, currSum + node.left.val) # Returns true if any path == target or false if no such path exists, add the val each call to track the current sum
            else:
                left = False 

            # Explore right child if it exists
            if node.right: # Must check for null first because if node.right is null we can't access it's val
                right = dfs(node.right, currSum + node.right.val)
            else:
                right = False

            return left or right # For each curr node, return true if any branch finds the target 

        return dfs(root, root.val)
    
    
    def hasPathSumIterative(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: # Empty tree
            return False
        
        stack = [(root, targetSum)] # For each node, we store the node and the remaining sum for that specific node

        while stack:
            node, current_sum = stack.pop() # Pop a node off the stack and destructure tuple
            remaining_sum = current_sum - node.val # Update the remaining sum
            if not node.left and not node.right and remaining_sum == 0: # Check if we are at a leaf node and found path
                return True
            if node.right: # Push right first so left is processed next when we pop (mimics DFS order)
                stack.append((node.right, remaining_sum)) # Append tuple
            if node.left:
                stack.append((node.left, remaining_sum)) # Append tuple

        return False # Stack is empty and we never found a valid path
    


sol = Solution()

t1 = TreeNode(5)
t1.left = TreeNode(4)
t1.right = TreeNode(8)
t1.left.left = TreeNode(11)
t1.right.left = TreeNode(13)
t1.right.right = TreeNode(4)
t1.left.left.left = TreeNode(7)
t1.left.left.right = TreeNode(2)
t1.right.right.right = TreeNode(1)

print(sol.hasPathSumRecursive(t1, 22))
print(sol.hasPathSumIterative(t1, 22))


