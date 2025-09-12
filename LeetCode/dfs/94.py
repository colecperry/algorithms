# 94: Binary Tree InOrder Traversal

# Topics: Stack, Tree, Depth First Search, Binary Tree

# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Note -> In in-order traversal: Recursively traverse the left subtree until reaching null. Then, process (append) the current node. After that, recursively traverse the right subtree."

# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,3,2]

#  1
#   \
#    2
#   /
#  3

# Example 2:
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [4,2,6,5,7,1,3,9,8]

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

# Note -> DFS explores as far as possible before backtracking (deep before wide). Can use recursion or a stack. BFS processes nodes level by level using a queue (wide before deep).

# In-Order Traversal (Left, Process Node, Right)

# === Recursive Approach ===
# 1. Base case: If the node is None, return.
# 2. Recursively traverse the left subtree.
# 3. Process (append) the current node.
# 4. Recursively traverse the right subtree.

# === Other Notes ===   
# - Lists are mutable objects that can be stored in outer functions and modified in-place from inner functions, while integers are immutable and would require reassignment (which needs nonlocal)
# - Storing res in the outer function scope keeps each method call independent instead of sharing state across all instances like a class variable would.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        res = [] # Store the result array

        def dfs(root):
            if root is None: # Base case -> when we hit the end of the path
                return # to prev call stack (node)
            dfs(root.left) # Recursively call left node until root is None
            res.append(root.val) # Return to prev call stack and append node
            dfs(root.right)
        
        dfs(root) # inOrderTraversal function goes straight here calls dfs()

        return res

#           1
#         /   \
#        /     \
#       2       3
#      / \       \
#     4   5       8
#        / \     /
#       6   7   9

#  1
#   \
#    2
#   /
#  3

# Call stack dfs(1) -> calls dfs(root.left) -> None and returns, appends 1 to array, calls dfs(root.right) -> 2 
# Call stack dfs(2) -> calls dfs(root.left) -> 3
# Call stack dfs(3) -> calls dfs(root.left) -> None and returns, appends 3 to array, calls dfs(root.right) -> None, code finishes and returns to call stack dfs(2)
# Call stack dfs(2) -> append 2 since we already called dfs(root.left), calls dfs(root.right) -> None, code finishes returns to call stack dfs(1) where we finish and return the result

# === Iterative Approach ===

# Big idea: We have a stack to store nodes for our iteration, a list to store our results, and a pointer for traversal. We continue iterating left and pushing nodes onto the stack until we reach our base case (replacing recursion), then we pop the top node off the stack and assign it to our pointer(mimics hitting base case), add it to our results, and move the current pointer to the right. Once our stack is empty we know we have finished processing the tree and we can return the results. 

# 1. Setup: Create empty res list, empty stack, set cur (pointer) = root
# 2. Main loop: While we have nodes to process (cur exists OR stack has nodes):
    # - Go left: Push all left nodes onto stack until we hit None
    # - Process: Pop from stack and assign to curr ptr (mimics moving back to last recursive call stack), add value to result 
    # - Go right: Move to right child and repeat
# 3. Done: Return result when both stack is empty and cur is None

# === Time & Space Complexity ===
# - Time Complexity: O(n) (Every node is visited once)
# - Space Complexity:
#   - Worst case: O(n) (Skewed tree → recursive call stack OR iterative stack stores all nodes)
#   - Best case: O(log n) (Balanced tree → stack depth is proportional to tree height)

    # Iterative solution
    def inorderTraversal2(self, root):
        res = [] # Array to store result
        stack = [] # Array to store iterative stack
        cur = root # Pointer

        # While ptr is non null or stack is not empty (keep going until we process everything)
        while cur or stack:
            while cur: # While pointer is non null (handles go left phase)
                stack.append(cur) # Append node to the stack
                cur = cur.left # Move the pointer left
            cur = stack.pop() # Once we finish going left, pop from the stack, move ptr back
            res.append(cur.val) # Append popped node to the result
            cur = cur.right # Move our pointer right
        
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


root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)

print(my_solution.inorderTraversal(root1))

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.right.right = TreeNode(8)
root2.right.right.left = TreeNode(9)
root2.left.right.left = TreeNode(6)
root2.left.right.right = TreeNode(7)

print(my_solution.inorderTraversal2(root2))

root3 = None 
print(my_solution.inorderTraversal(root3))

root4 = TreeNode(1)
print(my_solution.inorderTraversal(root4))
