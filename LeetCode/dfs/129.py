class HelperRecursion:
    """
    Problem 4: Sum all root-to-leaf numbers.
    
    Example:
        Tree:    1
                / \
               2   3
        
        Paths: 12, 13
        Sum: 12 + 13 = 25
    
    How it works:
    1. Helper accumulates number as we traverse
    2. At each node: current_num = prev * 10 + node.val
    3. At leaf: add to total sum
    """
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
            # Base case: null node contributes nothing
            if not node:
                return 0
            
            # ACCUMULATE: Build number by appending current digit
            # Example: current_num=1, node.val=2 → 1*10 + 2 = 12
            current_num = current_num * 10 + node.val
            
            # BASE CASE: Leaf node? We've completed a path, return the number
            if not node.left and not node.right:
                return current_num
            
            # RECURSIVE CASE: Internal node? Sum both subtree paths
            # Pass accumulated number to children (they'll build on it)
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
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

sol = HelperRecursion()

# Test sum numbers
tree = TreeNode(1, TreeNode(2), TreeNode(3))
print("Sum Root to Leaf:", sol.sumNumbers(tree))  # 25