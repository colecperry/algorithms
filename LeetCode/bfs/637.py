# 637. Average of Levels in Binary Tree

# Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree

# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

# Ex.1 
#         3
#        / \
#       /   \
#      9    20
#           / \
#         15   7
#
#

# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
# Hence return [3, 14.5, 11].

# Ex. 2
#         3
#        / \
#       /   \
#      9    20
#     / \
#   15   7
#
#
# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]

# Problem: Return a list of average values of each level in a binary tree.
    # Approach:
    # 1. Use Breadth-First Search (BFS) to traverse the tree level by level.
    # 2. For each level:
    #    - Keep track of the number of nodes at that level (level_size).
    #    - Sum up all node values in that level.
    #    - Compute the average and add it to the result list.
    # 3. Return the list of averages after traversal.

# Time Complexity: O(n)
# - We visit every node in the tree exactly once.
# - For each node, we do constant-time operations (add to sum, queue children).

# Space Complexity: O(w)
# - 'w' is the maximum width of the tree (i.e., the max number of nodes on any level).
# - In the worst case, this is O(n) if the tree is completely balanced at the bottom level.
# - The output list also stores O(h) averages, where h is the height of the tree (log n for balanced trees).


from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        queue = deque([root]) # BFS queue
        output_arr = []
        while queue:
            level_size = len(queue) # Get number of nodes on this BFS level
            sum = 0 # Sum for each level
            for _ in range(level_size): # Only loop through each level
                node = queue.popleft() # Pop off the left node
                sum += node.val # Calc the sum
                if node.left: # Don't append None -> will cause errors
                    queue.append(node.left) # Append the children l & r
                if node.right:
                    queue.append(node.right)
            output_arr.append(sum/level_size) # Append the average
        
        return output_arr


sol = Solution()

t1 = TreeNode(3)
t1.left = TreeNode(9)
t1.right = TreeNode(20)
t1.right.left = TreeNode(15)
t1.right.right = TreeNode(7)

print(sol.averageOfLevels(t1))

