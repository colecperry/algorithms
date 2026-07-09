# 144. Binary Tree Preorder Traversal

# Topics: Stack, Tree, DFS, Binary Tree

# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,2,3]

#  1
#   \
#    2
#   /
#  3

# Example 2:
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [1,2,4,5,6,7,3,8,9]

#           1
#         /   \
#        /     \
#       2       3
#      / \       \
#     4   5       8
#        / \     /
#       6   7   9

# Example 3:
# Input: root = []
# Output: []

# Example 4:
# Input: root = [1]
# Output: [1]

# ====================================================== #
# Preorder Traversal (Recursive) - Root → Left → Right
# ====================================================== #

# PATTERN: Process current node FIRST, then recurse left, then right

# Algorithm Steps:
# 1. BASE CASE: If node is None, return (hit a leaf's child)
# 2. PROCESS: Add current node's value to result 
# 3. RECURSE LEFT: Visit entire left subtree
# 4. RECURSE RIGHT: Visit entire right subtree

# Key Insight: Unlike inorder/postorder, we process the node IMMEDIATELY when we first visit it, not when we backtrack to it.

# Example execution on tree:    1
#                              / \
#                             2   3
#                            / \
#                           4   5
# 
# Call stack visualization:
    # Visit 1 → add 1 → go left
    #   Visit 2 → add 2 → go left  
    #     Visit 4 → add 4 → go left (None) → go right (None) → return
    #   Back to 2 → go right
    #     Visit 5 → add 5 → go left (None) → go right (None) → return
    #   Back to 2 → return
    # Back to 1 → go right
    #   Visit 3 → add 3 → go left (None) → go right (None) → return
    # Result: [1, 2, 4, 5, 3] ✓

# Time Complexity: O(n) - Each node is visited exactly once.
# Space Complexity: 
#   - O(n) in the worst case (skewed tree, deep recursion call stack).
#   - O(log n) in the best case (balanced tree, recursion depth ~ tree height).

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    # Recursive
    def preorderTraversal(self, root):
        res = [] # Output array to store results

        def dfs(root):
            if root is None: # Base case
                return
            res.append(root.val) # Append the value first
            dfs(root.left) # Recursively traverse left subtree
            dfs(root.right) # Recursively traverse right subtree
        
        dfs(root) # Call dfs fn

        return res


# =============================== #
# Preorder Traversal (Iterative)
# =============================== #

# Big Idea:
#  The stack helps us remember the right child when we process the current node and before we traverse left, ensuring that after finishing the left subtree (hit base case), we correctly return to the right subtree.
# Since preorder follows **Root → Left → Right**, we must process nodes in this order.
    # We process (append) the current node first.
    # We **push the right child first** so that the left child is processed before it.
# This ensures when we pop from the stack, we continue in preorder order.

# Big Idea
    # While we are processing the current node or there are still nodes left to visit, we check -> are we on a current node?
            # Yes -> process current node (pre-order), save right node to stack to process later, and move the pointer left
            # No -> we hit out base case, let's go back and pop the last right node we visited off the stack and visit it

# Time Complexity: O(n) - Each node is visited exactly once.
# Space Complexity:
#   - O(n) in the worst case (skewed tree, stack holds all nodes).
#   - O(log n) in the best case (balanced tree, stack depth ~ tree height).
    
    # Iterative PreOrder (Root -> Left -> Right)
    def preorderTraversal2(self, root):

        res = [] # Output array
        stack = [] # Top of the stack is the end 
        cur = root

        while cur or stack: # Iterate until current and stack are non empty
            if cur: # We can try to go left
                res.append(cur.val) # Process curr node
                stack.append(cur.right) # Save the right child for later
                cur = cur.left # Go left
            else: # We are at base case -> need to backtrack and go right
                cur = stack.pop() # set cur to node at top of the stack

        return res


    #           1
    #         /   \
    #        /     \
    #       2       3
    #      / \       \
    #     4   5       8
    #        / \     /
    #       6   7   9

my_solution = Solution()

# Example 1: root = [1, null, 2, 3]
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)

print(my_solution.preorderTraversal2(root1))

# Example 2: root = [1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9]
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.right.right = TreeNode(8)
root2.left.right.left = TreeNode(6)
root2.left.right.right = TreeNode(7)
root2.right.right.left = TreeNode(9)

print(my_solution.preorderTraversal2(root2))

# Example 3: root = [] (Empty tree)
root3 = None

print(my_solution.preorderTraversal(root3))

# Example 4: root = [1]
root4 = TreeNode(1)

print(my_solution.preorderTraversal(root4))



