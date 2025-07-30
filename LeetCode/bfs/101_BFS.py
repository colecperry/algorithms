# 101. Symmetric Tree

# Topics: Tree, DFS, BFS, Binary Tree

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Ex. 1
# #           1
# #         /   \
# #        2     2
# #       / \   / \
# #      3   4 4   3
# # # Input: root = [1,2,2,3,4,4,3]
# # Output: True    

# Ex. 2
# #           1
# #         /   \
# #        2     2
# #         \     \
# #          3     3
# # # Input: root = [1,2,2,null,3,null,3]
# # Output: False   


# BIG IDEA (KEY INSIGHT):
# - Instead of just comparing left and right nodes directly, compare them as mirrored pairs:
#   * The left child of the left subtree must equal the right child of the right subtree.
#   * The right child of the left subtree must equal the left child of the right subtree.
# - This mirrored comparison must be done recursively (DFS) or level-by-level (BFS using a queue of node pairs).

# HOW TO SOLVE (BFS approach):
# - Use a queue to hold pairs of nodes to compare.
# - Start with the left and right children of the root.
# - At each step, pop a pair:
#     * If both are None, continue (they’re symmetric).
#     * If only one is None or their values differ, return False.
#     * Otherwise, enqueue their children in a tuple in mirrored order:
#       left.left vs right.right, left.right vs right.left.
# - If the entire queue is processed without mismatch, the tree is symmetric.

# TIME COMPLEXITY:
# - O(N), where N is the number of nodes in the tree.
# - Every node is visited once during traversal.

# SPACE COMPLEXITY:
# - O(N) in the worst case for the queue (BFS), especially if the tree is wide.
# - Balanced trees use O(log N) space; skewed or full trees may use O(N).


from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: # edge case
            return True
        queue = deque([(root.left, root.right)]) # start on second level (first is always symmetric)
        while queue:
            node1, node2 = queue.popleft()
            if not node1 and not node2: # both nodes are none -> symmetric
                continue
            if not node1 or not node2: # one node is none but other isn't -> asymmetric
                return False
            if node1.val != node2.val: # vals are differet -> asymmetric
                return False
            queue.append((node1.left, node2.right)) # append the mirror images as tuple
            queue.append((node1.right, node2.left))
        return True


sol = Solution()
# Tree 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(2)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(4)
root1.right.left = TreeNode(4)
root1.right.right = TreeNode(3)

print(sol.isSymmetric(root1))

# Tree 2
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.right = TreeNode(3)
root2.right.right = TreeNode(3)

print(sol.isSymmetric(root2))