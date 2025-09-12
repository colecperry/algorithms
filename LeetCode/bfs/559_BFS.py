# 559. Maximum Depth of N-ary Tree

# Topics: Tree, DFS, BFS

# Given a n-ary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

#  Ex. 1
#
#
#       1
#     / | \
#    3  2  4
#   / \
#  5   6
#

# Input: root = [1,null,3,2,4,null,5,6]
# Output: 3

# Ex. 2
#
#                     1
#                 /    |    \     \
#                2     3     4     5
#                            |
#                            6
#                           / \
#                          7   8
#                             / \
#                            9  10
#                               |
#                              11
#                                \
#                                12
#                                  \
#                                  13
#                                    \
#                                    14
#


# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: 5

# How to Solve (Big Picture) - Level Based BFS
    # An N-ary tree is a tree where each node can have multiple children, so we know that the list of children is either an empty list or a list of nodes with no null values
    # Track depth, use a deque starting with the root, and for each level of the tree, pop off each node and add it's children, adding one to the depth for each level processed

# Time complexity: Each node is processed once -> We remove it from the queue and add it's children -> O(n)
# Space complexity: O(w) -> The max number of nodes held in the queue at one time is the max number of nodes on the any level

from collections import deque

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root): # Level Based BFS
        if not root: # Edge case, empty tree
            return 0
        
        depth = 0 # Track the max depth
        queue = deque([root]) # Initialize a deque with the root

        while queue: 
            level_size = len(queue) # Get number of nodes on current tree level
            for _ in range(level_size):
                node = queue.popleft() # Pop off each node on that level
                queue.extend(node.children) # Add all children at once instead of looping
            depth += 1 # Add one to the depth after whole level processed

        return depth
    
    def maxDepth(self, root: 'Node') -> int: # Tuple Based BFS
        if not root: # Edge case, empty tree
            return 0
        queue = deque([(root, 1)]) # Initialize a deque with the root and depth 1
        while queue: # Process each level
            node, depth = queue.popleft() # Pop off the node and its depth
            for i in range(len(node.children)): # Loop through each child
                queue.append((node.children[i], depth + 1)) # Add child and increment depth
        return depth # The last depth processed is the max depth of the tree

# ----------- Tree 1 -----------

# Tree 1: [1,null,3,2,4,null,5,6]
#         1
#       / | \
#      3  2  4
#     / \
#    5   6

node5 = Node(5)
node6 = Node(6)
node3 = Node(3, [node5, node6])
node2 = Node(2)
node4 = Node(4)
root1 = Node(1, [node3, node2, node4])

# ----------- Tree 2 -----------

# Tree 2 is a deeply nested structure
node14 = Node(14)
node13 = Node(13, [node14])
node12 = Node(12, [node13])
node11 = Node(11, [node12])
node10 = Node(10, [node11])
node9 = Node(9)
node8 = Node(8, [node9, node10])
node7 = Node(7)
node6 = Node(6, [node7, node8])
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
root2 = Node(1, [node2, node3, node4, node5])
node5.children = [node6]  # Add node6 as a child of node5

# ----------- Testing -----------

sol = Solution()
print("Tree 1 Max Depth:", sol.maxDepth(root1))  # Should return 3
print("Tree 2 Max Depth:", sol.maxDepth(root2))  # Should return 5 or more depending on children nesting