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
#                     / \    |    / \
#                    6   7   8   9  10
#                        |   |   |
#                        11  12  13
#                        |
#                        14


# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: 5

        # Big picture (DFS Recursive):
        # - We're doing a recursive depth-first search (DFS) to explore every path from the root to the leaves.
        # - At each node, we ask: what is the maximum depth of all my children?
        # - We add 1 to that maximum to account for the current node.
        # - The base case is simple: if the node has no children, its depth is 1 (it's a leaf).
        #
        # Time complexity: O(n) — We visit every node once.
        # Space complexity: O(h) — Due to the recursion stack, where h is the height of the tree.
        # In the worst case (a skewed tree), h can be as large as n.


# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepthRecursive(self, root):
        if not root:
            return 0

        def dfs(node):
            if not node.children:
                return 1  # A leaf node contributes depth of 1

            max_child_depth = 0 # Track max depth from current node
            for child in node.children: # Visit each child
                child_depth = dfs(child) # Track it's depth
                max_child_depth = max(max_child_depth, child_depth) # Take the max depth of all children

            return 1 + max_child_depth  # Include current node's level

        return dfs(root) # Returns 1 + max child depth for the root node
    
    def maxDepthIterative(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        # use depth first search
        stack = [(root, 1)] # Stack of tuples -> (node, depth)
        max_depth = 1 # Tracking max depth of tree
        
        while stack:
            curr, depth = stack.pop() # Pop off the node
            max_depth = max(max_depth, depth) # Update max depth with current node 
            if curr.children: # Check that the node has children -> Will get error if we encounter None
                for child in curr.children or []: # Append each child (node, depth) to the stack 
                    stack.append((child, depth + 1)) # Append the children their depths
        return max_depth


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
print("Tree 1 Max Depth Recursive:", sol.maxDepthRecursive(root1))  # Should return 3
print("Tree 2 Max Depth Recursive:", sol.maxDepthRecursive(root2))  # Should return 5 or more depending on children nesting

print("Tree 1 Max Depth Iterative:", sol.maxDepthRecursive(root1))  # Should return 3
print("Tree 2 Max Depth Iterative:", sol.maxDepthRecursive(root2))  # Should return 5 or more depending on children nesting