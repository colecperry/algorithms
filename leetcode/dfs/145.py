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
    
    # ============================= #
    # Post-Order Traversal (Iterative)
    # ============================= #

    # Big Idea: 
        # Since post order is Left -> Right -> Process Node, we use a stack and visited list to make sure:
            # If we iterate to a node and it's not visited yet, we need to process it's children and come back to it:
                # Push node back onto the stack but mark visited as true (next time we process it)
                # Push right child onto the stack and visit set (False) -> we want to pop this off second (left, right, root)
                # Push left child onto the stack and visit set (False) -> we want to visit this first (left, right, root)
            # If we iterate onto a node and it has been visited, we know that we have already processed it's children -> add to res

    # Example execution with tree:
    #
    #     1
    #    / \
    #   2   3
    #
    # Step | Stack         | Visit              | Action
    # -----|---------------|--------------------|-----------------------------------------
    # 1    | [1]           | [False]            | Pop 1(False) → first visit, add back 1(True), add children
    # 2    | [1,3,2]       | [True,False,False] | Pop 2(False) → first visit, add back 2(True), no children
    # 3    | [1,3,2]       | [True,False,True]  | Pop 2(True) → second visit, process 2!
    # 4    | [1,3]         | [True,False]       | Pop 3(False) → first visit, add back 3(True), no children
    # 5    | [1,3]         | [True,True]        | Pop 3(True) → second visit, process 3!
    # 6    | [1]           | [True]             | Pop 1(True) → second visit, process 1!
    #
    # Result: [2, 3, 1] ✓ (Left → Right → Root)


    # Time Complexity: O(n) - Each node is visited exactly once.
    # Space Complexity:
    #   - O(n) in the worst case (skewed tree, stack holds all nodes).
    #   - O(log n) in the best case (balanced tree, stack depth ~ tree height).
    
    def postorderTraversal2(self, root):
        if not root:
            return []  # Handle empty tree case

        stack = [root] # DFS stack (init with root)
        visit = [False] 
        res = []

        while stack:
            cur, v = stack.pop(), visit.pop() # pop and visit node
            if v: # If node already visited -> process itself
                res.append(cur.val) 
            else: # If node not visited -> process children
                stack.append(cur)  # Put back in stack to revisit after children 
                visit.append(True)  # So node gets processed next visit

                if cur.right:  # Push right child first (processed second)
                    stack.append(cur.right)
                    visit.append(False)

                if cur.left:  # Push left child last (processed first)
                    stack.append(cur.left)
                    visit.append(False)

        return res
    
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


