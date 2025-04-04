# 543. Diameter of Binary Tree

# Tree, Depth-First Search, Binary Tree

# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

# Example 1:
# 
#         1
#        / \
#       /   \
#      2     3
#     / \
#    4   5
#
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

# Example 2: 
# Input: root = [1,2]
# Output: 1

# How to Solve (DFS): -> 
    # Solution seems obvious at first -> go through the root, and find the longest path on the left and right sides and that is the answer. But here is an edge case where the longest path does not run through the root:
    #                 1
    #                  \
    #                   \
    #                    3
    #                   / \ 
    #                  /   \
    #                 4     5
    #                / \   / \
    #               6   7 8   9
    #
    # If we try to calculate through the root our answer would be 3, but look at node 3 -> length of the left side is 2, and right = 2, so the answer is 4, so we need to calculate the diameter through every single node in the tree
    #
    # Big picture: Traverse through the tree using DFS, and at each node, calculate the max length (diameter) of each node by adding left and right subtrees, update result, and return to the parent the height of that subtree
    # Once we hit the base case, we return 0 for left and right to the parent node
    # For each node, we update global diameter variable 
    # Return 1 (path from current node to parent) plus the max height of the left and right subtrees which is the height of the current node's subtree

    #  Time Complexity: O(N)
    #    - Each node is visited **once** in the DFS traversal.
    #    - The function **does constant work** at each node (computing max and returning height).
    #    - Therefore, the total time complexity is **O(N)**, where N is the number of nodes in the tree.

    #    Space Complexity: O(N) (worst case), O(log N) (best case)
    #    - The function **uses recursion**, and the depth of recursion is equal to the **height of the tree**.
    #    - **Best case (balanced tree):** The recursion depth is **O(log N)**.
    #    - **Worst case (skewed tree, like a linked list):** The recursion depth is **O(N)**.
    #    - **Auxiliary space (excluding recursion stack) is O(1)**, since we only store `self.diameter`.
    #    



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.diameter = 0 # Store the diameter as a global var

        def dfs(node):
            if not node: # Base case -> Returns 0 to left & right
                return 0
            left = dfs(node.left) # Recursive calls
            right = dfs(node.right)

            self.diameter = max(self.diameter, left + right) # Set diameter for each node -> the edges of the left and right subtrees combined
            return 1 + max(left, right) # Return the height of subtree (either left or right)
        
        dfs(root) # Call entry with root of tree
        return self.diameter
    

my_tree = TreeNode(1, TreeNode(2, TreeNode(4, None, None), TreeNode(5, None, None)), TreeNode(3, None, None))
my_tree_2 = TreeNode(1, TreeNode(2), None)
my_solution = Solution()
print(my_solution.diameterOfBinaryTree(my_tree))
print(my_solution.diameterOfBinaryTree(my_tree_2))