# 700. Search in a Binary Search Tree

# Topics: Tree, Binary Search Tree, Binary Tree

# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

# Ex. 1
#                  4
#                 / \
#                /   \
#               2     7
#              / \
#             1   3
# 
# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]

# Ex. 2
#                  4
#                 / \
#                /   \
#               2     7
#              / \
#             1   3
# 
# Input: root = [4,2,7,1,3], val = 5
# Output: []

# How to Solve (Recursive)
    # Step 1: Define a recursive function that takes the current node and the target value
    # Step 2: Base case — if the current node is None, return None (target not found)
    # Step 3: If the current node's value matches the target, return the node
    # Step 4: If target is less than current node's value, recurse on the left child
    # Step 5: If target is greater than current node's value, recurse on the right child

    # Time Complexity: O(h)
    # - h = height of the tree
    # - Worst case: O(n)
    # - Best case: O(log n)

    # Space Complexity: O(h)
    # - Due to the recursive call stack
    # - Worst case: O(n) for skewed trees
    # - Best case: O(log n) for balanced trees

# How to Solve (Iterative)
    # Step 1: Start at the root of the tree
    # Step 2: Loop while the current node is not None
    # Step 3: At each step, compare the current node's value to the target value
    # - If equal, return the current node (we found the target)
    # - If target is less, move to the left child
    # - If target is greater, move to the right child
    # Step 4: If the loop exits, return None (target not found in the tree)

    # Time Complexity: O(h)
    # - h = height of the tree
    # - Worst case: O(n) for a skewed tree
    # - Best case (balanced): O(log n)

    # Space Complexity: O(1)
    # - No recursion or additional data structures used

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBSTRecursive(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: # Empty tree or we reached the end of the tree -> Base case
            return None
        if root.val == val: # At each node, check if node's val == val passed in
            return root
        if val < root.val: 
            return self.searchBSTRecursive(root.left, val) # Recurse left
        else: 
            return self.searchBSTRecursive(root.right, val) # Search right
        
    def searchBSTIterative(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: # Edge case for an empty tree
            return None
        while root: # Iterate until we hit None
            if root.val == val: # Check if values match
                return root # Return subtree
            if val < root.val: # If val is less
                root = root.left # Iterate left
            else:
                root = root.right # Iterate right

sol = Solution()
t1 = TreeNode(4)
t1.left = TreeNode(2)
t1.right = TreeNode(7)
t1.left.left = TreeNode(1)
t1.left.right = TreeNode(3)
print(sol.searchBSTRecursive(t1, 2))
print(sol.searchBSTRecursive(t1, 5))


