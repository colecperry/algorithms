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

# ============================ #
# Preorder Traversal (Recursive) - Process Node, Left, Right
# ============================ #
# How to Solve:
# 1. Process the current node (append its value to the result list).
# 2. Recursively traverse the left subtree until reaching a `None` node (base case).
# 3. Return to the previous function call (backtrack to the parent).
# 4. Recursively traverse the right subtree until reaching a `None` node.
# 5. Once both left and right subtrees have been processed, return to the previous call stack.
# 6. Final result: Nodes are visited in preorder (Root → Left → Right) order.

# Time Complexity: O(n) - Each node is visited exactly once.
# Space Complexity: 
#   - O(n) in the worst case (skewed tree, deep recursion call stack).
#   - O(log n) in the best case (balanced tree, recursion depth ~ tree height).

# ============================ #
# Preorder Traversal (Iterative)
# ============================ #

# Big Idea:
#  The stack helps us **remember the right child** before we traverse left, ensuring that after finishing the left subtree, we correctly return to the right subtree.
# Since preorder follows **Root → Left → Right**, we must process nodes in this order.
    # We process (append) the current node first.
    # We **push the right child first** so that the left child is processed before it.
# This ensures when we pop from the stack, we continue in preorder order.
# By popping nodes from the stack, we simulate recursive backtracking, allowing us to return to the correct subtree at the right time.



# How to Solve:
# 1. Create:
#    - A pointer (`cur`) initialized to `root` to traverse the tree.
#    - A stack to store nodes for backtracking.
#    - A result list (`res`) to store the traversal order.
# 2. Iterate while `cur` is not None or the stack is not empty:
#    - Process the current node by appending its value to `res`.
#    - Push the right child onto the stack (if it exists) before moving left.
#    - Move left by setting `cur = cur.left`.
# 3. When `cur` reaches `None` (end of a left path):
#    - Pop from the stack to backtrack to the right child.
#    - Set `cur` to the popped node and continue traversal.
# 4. Final result: Nodes are visited in preorder (Root → Left → Right) order.

# Time Complexity: O(n) - Each node is visited exactly once.
# Space Complexity:
#   - O(n) in the worst case (skewed tree, stack holds all nodes).
#   - O(log n) in the best case (balanced tree, stack depth ~ tree height).



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

    
    # Iterative
    def preorderTraversal2(self, root):

        res = [] # Output array
        stack = [] # Top of the stack is the end 
        cur = root

        while cur or stack: # Iterate until current and stack are non empty
            if cur: # If cur ptr is non null
                res.append(cur.val) # Append current pointer's val to res
                stack.append(cur.right) # Append right child to stack
                cur = cur.left # Move pointer left
            else: # If cur ptr is null
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



