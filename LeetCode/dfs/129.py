# 129. Sum Root to Leaf Numbers

# You are given the root of a binary tree containing digits from 0 to 9 only.

# Each root-to-leaf path in the tree represents a number.

# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

# A leaf node is a node with no children.

# Example 1:
#
#             1
#            / \
#           2   3

# Input: root = [1,2,3]
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.

# Example 2:

#              4
#            /   \
#           /     \
#          9       0
#         /   
#        5     

# Input: root = [4,9,0,5]
# Output: 535
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 40 = 535.

class Solution:
    def sumNumbers(self, root):  # LC 129 - Sum Root to Leaf Numbers
        """
        - TC: O(n) - visit each node once
        - SC: O(h) - recursion stack depth = tree height
        """
        def helper(node, current_num):
            """
            Accumulate path number as we traverse.
            - node: current node being visited
            - current_num: accumulated number built so far (0 → 1 → 12)
            """
            # Base case: end of path -> null node contributes nothing to sum
            # Hit when a node has one child
            if not node:
                return 0
            
            # ACCUMULATE: Build number by appending current digit
            # Example: current_num=1, node.val=2 → 1*10 + 2 = 12
            current_num = current_num * 10 + node.val
            
            # BASE CASE: Leaf node -> no children? Completed a path, return the number
            if not node.left and not node.right:
                return current_num
            
            # RECURSIVE CASE: 2 children -> Explore both directions, pass accumulated number
            left_sum = helper(node.left, current_num)
            right_sum = helper(node.right, current_num)

            return left_sum + right_sum
        
        # Start recursion: root node, number starts at 0
        return helper(root, 0)

# ═══════════════════════════════════════════════════════════════════
# TRACE: sumNumbers(root) - Sum Root to Leaf Numbers
# ═══════════════════════════════════════════════════════════════════
# 
# Tree:       1
#            / \
#           2   3
# 
# Goal: Calculate 12 + 13 = 25
# 
# ┌─ helper(node=1, current_num=0)
# │  🧮 Build number: 0 * 10 + 1 = 1
# │  📍 Not a leaf, explore both children
# │
# │  ┌─ LEFT: helper(node=2, current_num=1)
# │  │  🧮 Build number: 1 * 10 + 2 = 12
# │  │  🍃 LEAF! Return 12
# │  └─ Returns: 12
# │
# │  ┌─ RIGHT: helper(node=3, current_num=1)
# │  │  🧮 Build number: 1 * 10 + 3 = 13
# │  │  🍃 LEAF! Return 13
# │  └─ Returns: 13
# │
# │  ➕ Sum children: 12 + 13 = 25
# │  ✅ Return 25
# └─────────────────────────────────────────────────────────────────
# 
# 🎯 FINAL ANSWER: 25

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

sol = Solution()

# Test sum numbers
tree = TreeNode(1, TreeNode(2), TreeNode(3))
print("Sum Root to Leaf:", sol.sumNumbers(tree))  # 25

# Example 2
root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)
root.left.left = TreeNode(5)
print("Sum Root to Leaf:", sol.sumNumbers(root))  # 535