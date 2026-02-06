# 662. Maximum Width of Binary Tree

# Given the root of a binary tree, return the maximum width of the given tree.

# The maximum width of a tree is the maximum width among all levels.

# The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

# It is guaranteed that the answer will in the range of a 32-bit signed integer.

# Example 1:
#              1
#             / \
#            /   \
#           3     2
#          / \     \
#         5   3     9

# Input: root = [1,3,2,5,3,null,9]
# Output: 4
# Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).

# Example 2:
#               1
#             /   \
#            /     \
#           3       2
#          /         \
#         5           9
#        /           /
#       6           7

# Input: root = [1,3,2,5,null,null,9,6,null,7]
# Output: 7
# Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).


# Example 3:
#              1
#             / \
#            /   \
#           3     2
#          / 
#         5 
# Input: root = [1,3,2,5]
# Output: 2
# Explanation: The maximum width exists in the second level with length 2 (3,2).

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        TC: O(n) -> We visit each node once
        SC: O(w) -> The max width of any level is the most we will hold in the queue at once
        """
        # Assign each node a pos as if the tree were a complete binary tree stored in an array -> start with root at pos 1
        queue = deque([(root, 1)]) 
        max_width = float('-inf')

        while queue:
            level_size = len(queue)
            _, first_pos = queue[0] # Get pos of 1st node in lvl (leftmost)
            
            for _ in range(level_size): # Process the whole level
                node, position = queue.popleft()

                # For any node at position p -> left child: 2 * p
                if node.left:
                    queue.append((node.left, 2 * position))
                
                if node.right: # right child: 2 * p + 1
                    queue.append((node.right, 2 * position + 1))
            
            # Width = last_pos - first_pos + 1 (l & r both inclusive)
            max_width = max(max_width, position - first_pos + 1)

        return max_width
    
#              1
#             / \
#            /   \
#           3     2
#          / \     \
#         5   3     9

# Input: root = [1,3,2,5,3,null,9]
tree_root1 = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))

# Input: root = [1,3,2,5,null,null,9,6,null,7]
tree_root2 = TreeNode(1, TreeNode(3, TreeNode(5, TreeNode(6)), None), TreeNode(2, None, TreeNode(9, TreeNode(7))))

# Input: root = [1,3,2,5]
tree_root3 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))

sol = Solution()
print(sol.widthOfBinaryTree(tree_root1)) # 4
print(sol.widthOfBinaryTree(tree_root2)) # 7
print(sol.widthOfBinaryTree(tree_root3)) # 2
