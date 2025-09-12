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

# How to Solve (Recursive):
    # Step 1: Handle the base case
    # If the current node is None, there is no path — return False

    # Step 2: Check if the current node is a leaf (no left or right children)
    # If it is, check if targetSum == root.val
    # If so, return True (this path matches the required sum)

    # Step 3: Otherwise, continue the DFS
    # Subtract the current node's value from targetSum
    # Recursively check both left and right subtrees
    # Return True if either left or right recursive call returns True

    # Step 4: If neither subtree leads to a valid path, return False

    # Time Complexity: O(n)
    # - We visit every node once in the worst case
    # - n = number of nodes in the tree

    # Space Complexity: O(h)
    # - Due to recursion stack
    # - h = height of the tree
    # - Best case (balanced): O(log n)
    # - Worst case (skewed tree): O(n)

# How to solve (Iterative)
    # Step 1: Handle the base case
    # If the root is None (empty tree), there are no paths — return False

    # Step 2: Initialize an explicit stack to simulate DFS
    # Each stack element is a tuple: (node, remaining_sum)
    # We start with the root node and the original targetSum

    # Step 3: Loop while the stack is not empty
    # Pop the top element: get the current node and remaining sum to reach target
    # Subtract the current node's value from the remaining sum

    # Step 4: Check if the current node is a leaf
    # If it is a leaf and the remaining sum after subtracting equals 0, return True

    # Step 5: If not a leaf, push the children onto the stack
    # For each child, pass the updated remaining sum (i.e., remaining_sum)

    # NOTE: In recursive DFS, the call stack naturally goes all the way down the left side first
    # In iterative DFS, we must push right first, then left, if we want to replicate that same behavior
    # However, for this specific problem, traversal order doesn’t matter — we just need to find *any* valid path

    # Step 6: If we exit the loop without finding a valid path, return False

    # Time Complexity: O(n)
    # - Every node is visited once in the worst case

    # Space Complexity: O(h)
    # - Due to the stack
    # - Worst case: O(n) for a skew



from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution: 
    # Recursive remaining sum solution
    def hasPathSumRecursive(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: # Base case -> empty tree
            return False
        if not root.left and not root.right: # If we are at a leaf node
            return targetSum == root.val # Check if equal to root.val because we haven't subtracted current node's val yet
        left_has_path = self.hasPathSumRecursive(root.left, targetSum - root.val) # Recurse L and R
        right_has_path = self.hasPathSumRecursive(root.right, targetSum - root.val) # Update rem sum
        return left_has_path or right_has_path # Returns True if either path leads to 0
    
    # Recursive running total dfs solution
    def hasPathSumRecursive2(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: # Check for empty tree
            return False

        def dfs(node, currSum):
            # Base case -> we hit a leaf node, check if we found the path sum
            if not node.left and not node.right:
                return currSum == targetSum

            # Recursive case: explore left child if it exists
            if node.left:
                left = dfs(node.left, currSum + node.left.val) # Returns true if any path == target or false if no such path exists, add the val each call to track the current sum
            else:
                left = False 

            # Explore right child if it exists
            if node.right:
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
            remaining_sum = current_sum - node.val # Get the total remaining sum including current node
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


