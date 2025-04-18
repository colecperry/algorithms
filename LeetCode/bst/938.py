# 938. Range Sum of BST

# Topics: Tree, DFS, Binary Search Tree, Binary Tree

# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

# Ex. 1
#                   10
#                  /  \
#                 /    \
#                5     15
#               / \      \
#              3   7      18
#
# 
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

# Ex. 1
#                   10
#                  /  \
#                 /    \
#                5     15
#               / \    / \
#              3   7  13  18
#             /   /
#            1   6
#
# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

# -------------------------------------------------------------------
# 🔁 Iterative DFS Solution with a Stack
# -------------------------------------------------------------------
# - Initialize a stack with the root node to simulate DFS.
# - Traverse the tree manually using the stack.
# - For each node:
#     - If its value is within the range [low, high]:
#         - Add its value to the sum.
#         - Push both children onto the stack to continue exploring.
#     - If it's less than low:
#         - Skip the left child (entire left subtree is too small).
#         - Explore only the right subtree.
#     - If it's greater than high:
#         - Skip the right child (entire right subtree is too large).
#         - Explore only the left subtree.
# - Continue this process until the stack is empty.
# - Return the accumulated sum.

# Time Complexity:
# - O(n) in the worst case (visiting every node).
# - Less if pruning many branches (BST property).

# Space Complexity:
# - O(h), where h = height of the tree (stack holds nodes).
# - Worst case = O(n), Best case (balanced) = O(log n)


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBSTIterative(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root: # Empty tree
            return 0
        sum = 0 # Track sum
        stack = [root] # Simulate DFS

        while stack:
            node = stack.pop() # Pop the node off the stack
            if low <= node.val and node.val <= high: # If node in range
                if node.left: # If non empty child
                    stack.append(node.left) # Append child
                if node.right:
                    stack.append(node.right)
                sum += node.val # Add node's val to sum
            elif low > node.val: # If node not in range (too low)
                if node.right: 
                    stack.append(node.right) # Append only right child
            elif high < node.val: # If node not in range (too high)
                if node.left:
                    stack.append(node.left) # Append only left child
        return sum
    
    # -------------------------------------------------------------------
    # 🔁 Recursive DFS with Pruning
    # -------------------------------------------------------------------
    # - Use a recursive DFS helper function.
    # - At each node:
    #     - If it's None, return 0 (base case).
    #     - If its value is within the range [low, high]:
    #         - Recurse into both left and right subtrees.
    #         - Return the sum of current node + left + right.
    #     - If it's less than low:
    #         - Entire left subtree is too small; only recurse right.
    #     - If it's greater than high:
    #         - Entire right subtree is too large; only recurse left.
    # - The recursion will automatically stop at leaves or pruned paths.
    # - Final result is returned up the recursive call stack.

    # Time Complexity:
    # - O(n) in the worst case (every node visited).
    # - Potentially faster with effective pruning (BST helps skip subtrees).

    # Space Complexity:
    # - O(h) recursion stack, h = tree height.
    # - Worst case = O(n), Best case (balanced) = O(log n)


    def rangeSumBSTRecursive(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node, low, high):
            if not node: # Base case
                return 0 # Empty node adds zero to the sum
            
            if low <= node.val and node.val <= high: # If node in range
                left_sum = dfs(node.left, low, high) # Calc left sum
                right_sum = dfs(node.right, low, high) # Calc right sum
                return node.val + left_sum + right_sum # Return total subtree sum to left_sum or right_sum of prev stack
            
            elif low > node.val: # If node not in range (too low)
                return dfs(node.right, low, high) # Recurse right
            
            elif high < node.val: # If node not in range (too high)
                return dfs(node.left, low, high) # Recurse left
        
        return dfs(root, low, high) # Call helper function
    
sol = Solution()
t1 = TreeNode(10)
t1.left = TreeNode(5)
t1.right = TreeNode(15)
t1.left.left = TreeNode(3)
t1.left.right = TreeNode(7)
t1.right.right = TreeNode(18)

print("Iterative ex. 1", sol.rangeSumBSTIterative(t1, 7, 15))
print("Recursive ex. 1", sol.rangeSumBSTRecursive(t1, 7, 15))
