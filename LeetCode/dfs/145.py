# 145. Binary Tree Postorder Traversal

# Topics - Stack, Tree, DFS, Binary Tree

# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [3,2,1]

#  1
#   \
#    2
#   /
#  3

# Example 2:
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [4,6,7,5,2,9,8,3,1]

#           1
#         /   \
#        /     \
#       2       3
#      / \       \
#     4   5       8
#        / \     /
#       6   7   9
#         
#

# Example 3:
# Input: root = []
# Output: []

# Example 4:
# Input: root = [1]
# Output: [1]

# ============================= #
# Post-Order Traversal (Recursive) - Left, Right, Process Node
# ============================= #
# How to Solve:
# 1. Recursively traverse the left subtree first until reaching a `None` node (base case).
# 2. Return to the current node and recursively traverse the right subtree until reaching a `None` node.
# 3. Once both left and right subtrees have been fully processed, process (append) the current node.
# 4. Backtrack to the previous call stack (parent node) and repeat the process.
# 5. Final result: Nodes are visited in post-order (Left → Right → Root) order.

# Time Complexity: O(n) - Each node is visited exactly once.
# Space Complexity:
#   - O(n) in the worst case (skewed tree, deep recursion call stack).
#   - O(log n) in the best case (balanced tree, recursion depth ~ tree height).

# ============================= #
# Post-Order Traversal (Iterative)
# ============================= #
# How to Solve:
# 1. Create:
#    - A stack to store nodes for traversal.
#    - A `visit` list to track whether a node has been visited before.
#    - A result list (`res`) to store the traversal order.
# 2. Push the root node onto the stack and mark it as unvisited (`False`).
# 3. While the stack is not empty:
#    - Pop a node and its visit status.
#    - If the node is marked as visited (`True`), append its value to `res` (process it).
#    - Otherwise:
#      - Push the node back onto the stack and mark it as visited (`True`).
#      - Push the right child first (so it is processed second).
#      - Push the left child last (so it is processed first).
# 4. Final result: Nodes are visited in post-order (Left → Right → Root) order.

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
    def postorderTraversal(self, root):
        res = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)

        dfs(root)

        return res
    
    def postorderTraversal2(self, root):
        if not root:
            return []  # Handle empty tree case

        stack = [root]
        visit = [False]
        res = []

        while stack:
            cur, v = stack.pop(), visit.pop()
            if cur:
                if v:
                    res.append(cur.val)  # Process node after left & right subtrees
                else:
                    # Post-order (Left → Right → Root)
                    stack.append(cur)  # Re-add node to stack for post-processing
                    visit.append(True)  # Mark for processing after children

                    if cur.right:  # Push right child first (processed second)
                        stack.append(cur.right)
                        visit.append(False)

                    if cur.left:  # Push left child last (processed first)
                        stack.append(cur.left)
                        visit.append(False)

        return res
    



my_solution = Solution()

# Example 1: root = [1, null, 2, 3]
# Post-order output: [3, 2, 1]
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)

print(my_solution.postorderTraversal2(root1))

# Example 2: root = [1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9]
# Post-order output: [4, 6, 7, 5, 2, 9, 8, 3, 1]
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.right.right = TreeNode(8)
root2.left.right.left = TreeNode(6)
root2.left.right.right = TreeNode(7)
root2.right.right.left = TreeNode(9)

print(my_solution.postorderTraversal2(root2))

# Example 3: root = [] (Empty tree)
# Post-order output: []
root3 = None

print(my_solution.postorderTraversal2(root3))

# Example 4: root = [1]
# Post-order output: [1]
root4 = TreeNode(1)

print(my_solution.postorderTraversal2(root4))


