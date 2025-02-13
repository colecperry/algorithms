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

# === In Order Iterative Approach ===

# Big idea: We have a stack to store nodes for our iteration, and a list to store our results. We continue iterating left and pushing nodes onto the stack until we reach our base case, then we pop the top node off the stack, add it to our results, and move the current pointer to the right. Once our stack is empty we know we have finished processing the tree and we can return the results. 

# 1. Create an empty stack and set a pointer (cur) to the root node.
# 2. While cur is not None or the stack is not empty -> once stack becomes empty we return, and at that point current will be None
#    a. Inner loop keeps traversing left and pushing nodes onto the stack.
#    b. Once we reach None (end of left subtree), exit inner while loop and pop the top node from the stack.
#    c. Append the popped node's value to the result list.
#    d. Move to the right child and repeat the process.
# 3. Continue until both the stack is empty and cur is None.
# 4. Return the result list containing in-order values.

# === Time & Space Complexity ===
# - Time Complexity: O(n) (Every node is visited once)
# - Space Complexity:
#   - Worst case: O(n) (Skewed tree → recursive call stack OR iterative stack stores all nodes)
#   - Best case: O(log n) (Balanced tree → stack depth is proportional to tree height)


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
# Iterative solution
    def inorderTraversal(self, root):
        res = [] # Array to store result
        stack = [] # Array to store iterative stack
        cur = root # Pointer

        # Continue as long as pointer is non null or stack is not empty
        while cur or stack:
            while cur: # While pointer is non null
                stack.append(cur) # Append node to the stack
                cur = cur.left # Move the pointer left
            cur = stack.pop() # Once our ptr reaches null, pop from the stack
            res.append(cur.val) # Append popped node to the result
            cur = cur.right # Move our pointer right
        
        return res
    
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

    # Iterative
    def preorderTraversal(self, root):

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

    def postorderTraversal(self, root):
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

root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)

print(my_solution.inorderTraversal(root1))
print(my_solution.preorderTraversal(root1))
print(my_solution.postorderTraversal(root1))

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.right.right = TreeNode(8)
root2.right.right.left = TreeNode(9)
root2.left.right.left = TreeNode(6)
root2.left.right.right = TreeNode(7)

print(my_solution.inorderTraversal(root2))
print(my_solution.preorderTraversal(root2))
print(my_solution.postorderTraversal(root2))

root3 = None 
print(my_solution.inorderTraversal(root3))
print(my_solution.preorderTraversal(root3))
print(my_solution.postorderTraversal(root3))


root4 = TreeNode(1)
print(my_solution.inorderTraversal(root4))
print(my_solution.preorderTraversal(root4))
print(my_solution.postorderTraversal(root4))

