# 653. Two Sum IV - Input is a BST

# Topics: Hash Table, Two Pointers, Tree, Depth First Search, Breadth First Search, Binary Search Tree, Binary Tree

# Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

# Ex. 1
#                  5
#                 / \
#                /   \
#               3     6
#              / \     \
#             2   4     7
#
# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true

# Ex. 2
#                  5
#                 / \
#                /   \
#               3     6
#              / \     \
#             2   4     7
# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false

from typing import Optional
from collections import deque

# -------------------------------------------------------------------
# 🔍 Solution 1: DFS + Two Pointers (on a sorted array)
# -------------------------------------------------------------------
# Strategy:
# - Perform in-order traversal (DFS) to get a sorted list of node values.
# - Use two pointers (`l`, `r`) on the sorted array to find two values that sum to k.
# - If a pair is found, return True.
# - If pointers meet without finding a pair, return False.

# Time Complexity:
# - O(n) to traverse the tree (DFS).
# - O(n) for two-pointer search on the array.
# - Total: O(n)

# Space Complexity:
# - O(n) for the array to store in-order traversal.
# - O(h) recursion stack for DFS (h = height of tree).
# - Total space: O(n)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: # DFS + Binary Search Solution
    def findTargetDFS(self, root: Optional[TreeNode], k: int) -> bool:
        arr = [] # Create an output array -> BST creates a sorted arry if you run DFS in order
        def dfs(node):
            if not node: # Base case
                return
            dfs(node.left) # Traverse left until we hit base case
            arr.append(node.val) # Append the curr node
            dfs(node.right) # Traverse right
            return
        dfs(root) # Call helper function

        l, r = 0, len(arr) - 1 # l and r pointers for binary search
        while l < r: # Iterate until they meet (need two nodes to make sum)
            sum = arr[l] + arr[r] # Calc the sum
            if sum == k: # If we find k from our sum
                return True # Return True
            if sum > k: # If sum is too large
                r -= 1 # Decrease it
            else: # If sum is too small
                l += 1 # Increase
        return False # Return false if we don't find a match
    
    # -------------------------------------------------------------------
    # 🔍 Solution 2: Iterative DFS + Hash Set
    # -------------------------------------------------------------------
    # Strategy:
    # - Use a stack to iteratively traverse the tree (DFS).
    # - At each node, check if its value is in a set of previously seen complements (k - val).
    # - If found, return True.
    # - Otherwise, add (k - val) to the set and continue DFS.
    # - Return False if traversal completes without finding a match.

    # Time Complexity:
    # - O(n), where n is the number of nodes (each node visited once)

    # Space Complexity:
    # - O(n) for the set and stack in worst case (unbalanced tree)


    def findTargetIterative(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        
        diffs = set() # Create a set of differences (k - curr.val)
        stack = [root] # Initialize a stack
        while stack: 
            curr = stack.pop() # pop the node
            if curr.val in diffs: # Check if the current node is the matching value
                return True
            diffs.add(k - curr.val) # Add the difference between k and curr val to the set (matching value needed)
            if curr.left:
                stack.append(curr.left) # Append children if not None
            if curr.right:
                stack.append(curr.right)
        return False
    
    # -------------------------------------------------------------------
    # 🔍 Solution 3: Recursive DFS + Hash Set
    # -------------------------------------------------------------------
    # Strategy:
    # - Use recursion to traverse the tree (DFS).
    # - Maintain a set of diffs (k - val) needed to form the sum.
    # - At each node, check if the current value exists in the set.
    # - If yes, return True.
    # - If not, add (k - val) to the set and recurse left and right.
    # - Return True if any branch returns True; otherwise, return False.

    # Time Complexity:
    # - O(n), each node is visited once.

    # Space Complexity:
    # - O(n) for the set and recursion stack (worst case = unbalanced tree)

    
    def findTargetRecursive(self, root: Optional[TreeNode], k: int) -> bool:
        diffs = set() # Create a set of differences

        def dfs(node):
            if not node: # Base case -> reached a leaf node
                return False # If there is no node it can't be the match

            if node.val in diffs: # Check if we found the matching node
                return True
                
            diffs.add(k - node.val) # Add the difference needed to find match

            # Recursively search the left and right subtrees
            found_in_left = dfs(node.left) # Keeps searching left, returns True or False for each subtree
            found_in_right = dfs(node.right)

            return found_in_left or found_in_right # Return for each subtree and assign to found_in_left or found_in_right

        return dfs(root) # Call helper function with the root

sol = Solution()
t1 = TreeNode(5)
t1.left = TreeNode(3)
t1.right = TreeNode(6)
t1.left.left = TreeNode(2)
t1.left.right = TreeNode(4)
t1.right.right = TreeNode(7)
print(sol.findTargetRecursive(t1, 9))