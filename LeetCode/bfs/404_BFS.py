# 404. Sum of Left Leaves

# Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree

# Given the root of a binary tree, return the sum of all left leaves.

# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

# Example 1:
#
#            3
#           / \
#          /   \
#         9     20
#               / \
#              15  7
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

# Example 2:

# Input: root = [1]
# Output: 0

# How to Solve (BFS):
    # Create a deque with the first element as the root and the second a boolean to tell us if it's a left node
    # Create a variable to store the total sum
    # Loop through the queue, pop the first element and destructure it getting the node and is_left boolean
    # If the node has no childern and is a left node, add that node's value to the total sum
        # Append the left and right nodes with the boolean, try not to append null nodes

"""
    🕒 Time Complexity: O(N)
    - Each node is visited exactly once → O(N), where N is the number of nodes.
    - Enqueue and dequeue operations each take O(1).
    - Final time complexity: O(N).

    🖥 Space Complexity: O(N) (worst case), O(log N) (best case)
    - In a balanced tree, the queue holds at most one level at a time → O(log N).
    - In a skewed tree (like a linked list), each node is enqueued and dequeued N times, leading to O(N) operations
    - Final space complexity: O(N) (worst case), O(log N) (best case).
"""
    

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object): # DFS  
    def sumOfLeftLeaves(self, root): # BFS
        queue = deque([(root, False)]) # Use a deque of tuples (node, is_left)
        total_sum = 0
        while queue: # Loop until queue is empty
            node, is_left = queue.popleft() # Pop left node & unpack
            if node.left == None and node.right == None and is_left: # If the node is a left leaf node
                total_sum = total_sum + node.val # Update sum
            if node.left: # If non null node
                queue.append((node.left, True)) #Append child
            if node.right:
                queue.append((node.right, False))
        
        return total_sum


my_tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
my_solution = Solution()
print(my_solution.sumOfLeftLeaves2(my_tree))