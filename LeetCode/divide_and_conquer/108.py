# 108. Convert Sorted Array to Binary Search Tree

# Topics: Array, Divide and Conquer, Tree, Binary Search Tree, Binary Tree

# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# Ex. 1
#                      0
#                     / \
#                   -3   9
#                   /   /
#                -10   5
#
#
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Ex. 2
#             3          1
#            /            \
#           1              3
#  

# Definition for a binary tree node.

# 🧠 High-Level Idea:
# - Use recursion with a divide-and-conquer strategy.
# - At each step, choose the middle element of the current subarray to be the root node.
# - Recursively build the left subtree from the left half of the array.
# - Recursively build the right subtree from the right half of the array.
# - This guarantees the BST is height-balanced.

# -------------------------------------------------------------------
# ✅ Why it works:
# - Picking the middle of each subarray ensures both subtrees are roughly equal in size.
# - This minimizes depth differences and guarantees balance.
# - The left half becomes the left subtree, right half becomes the right subtree.

# -------------------------------------------------------------------
# 🧪 Base case:
# - If the left index > right index, it means the subarray is empty.
# - Return None (no node to build).

# -------------------------------------------------------------------
# ⏱️ Time Complexity:
# - O(n) where n is the number of elements in the array.
# - Each element is visited exactly once to create a node.

# 💾 Space Complexity:
# - O(log n) for the recursion stack (since we're dividing the array in half each time).
# - O(n) total space if you include the space needed to store the tree nodes.

from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def recursive(left, right):
            if left > right: # Base case: no more elements to process
                return None # root.left or root.right becomes None
            
            mid = (left + right) // 2 # Get left middle element

            root = TreeNode(nums[mid]) # Create new node (root of that subtree)

            root.left = recursive(left, mid - 1) # Recursively call for left and right subtrees
            root.right = recursive(mid + 1, right)

            return root # Returns the new root node and assigns it to root.left and root.right

        return recursive(0, len(nums) - 1) # Pass in left and right indexes of the arr
    

sol = Solution()
print(sol.sortedArrayToBST([-10,-3,0,5,9]))

