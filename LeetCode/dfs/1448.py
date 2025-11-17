# 1448. Count Good Nodes in Binary Tree

# Topics - Tree, DFS, BFS, Binary Tree

# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X. Return the number of good nodes in the binary tree.

# Example 1:
#                3
#               / \
#              /   \
#             1     4
#            /     / \
#           /     /   \
#          3     1     5
#
# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.

# Example 2:
#                3
#               / 
#              /   
#             3     
#            / \   
#           /   \    
#          4     2  
# Input: root = [3,3,null,4,2]
# Output: 3
# Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

# Example 3:
# Input: root = [1]
# Output: 1
# Explanation: Root is considered as good.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodesRecursive(self, root):
        def dfs(node, path_max):
            # Base case: empty node contributes nothing
            if not node:
                return 0
            
            # Check if current node is "good"
            is_good = 1 if node.val >= path_max else 0
            
            # Update the max value for the path going forward
            new_max = max(path_max, node.val)
            
            # Count good nodes in left and right subtrees
            left_count = dfs(node.left, new_max)
            right_count = dfs(node.right, new_max)
            
            # Total = current node (if good) + left subtree + right subtree
            return is_good + left_count + right_count
        
        return dfs(root, root.val)
    
#                3
#               / \
#              /   \
#             1     4
#            /     / \
#           /     /   \
#          3     1     5

    def goodNodesIterative(self, root):
        if not root:
            return 0
        
        # Stack stores tuples of (node, max_value_on_path_so_far)
        stack = [(root, root.val)]
        good_count = 0
        
        while stack:
            node, path_max = stack.pop()
            
            # Check if current node is good
            if node.val >= path_max:
                good_count += 1
            
            # Update the max for children
            new_max = max(path_max, node.val)
            
            # Add children to stack with updated max
            if node.right: # Add RIGHT first (so left gets popped first)
                stack.append((node.right, new_max))
            if node.left:
                stack.append((node.left, new_max))
        
        return good_count

t1 = TreeNode(3)
t1.left = TreeNode(1)
t1.right = TreeNode(4)
t1.left.left = TreeNode(3)
t1.right.left = TreeNode(1)
t1.right.right = TreeNode(5)

sol = Solution()
print(sol.goodNodesRecursive(t1)) # 4
print(sol.goodNodesIterative(t1)) # 4