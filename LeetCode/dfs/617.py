# 617. Merge Two Binary Trees

# Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree

# You are given two binary trees root1 and root2.

# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

# Return the merged tree.

# Note: The merging process must start from the root nodes of both trees.

# Ex 1.
#           1                   2                           3
#          / \                 / \                         / \
#         /   \               /   \                       /   \
#        3     2     +       1     3         ->          4     5
#       /                     \     \                   / \     \
#      5                       4     7                 5   4     7
#
# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# Output: [3,4,5,5,4,null,7]

# Ex. 2
# Input: root1 = [1], root2 = [1,2]
# Output: [2,2]

# Note: How would I have known to use DFS instead of BFS on this problem?
# The problem has a natural recursive nature -> Each node depends on two input nodes at the same position, and the recursive merging of their left and right children. Each solution at a node is composed of the same operation on it's children
# BFS relies more on level by level processing (printing levels, finding the deepest level, etc). BFS shines when you want the shortest path (unweighted graphs and trees), need to process nodes layer by layer, or need to avoid stack overflows (huge trees)

# How To Solve:
    # Choose if we want to use BFS or DFS -> choose DFS because we have to visit each node and combine data

# 1. Use Depth-First Search (DFS) to traverse both trees simultaneously.
#    - We recursively visit corresponding nodes from both trees.
# 2. Base Case:
#    - If one of the nodes is None, return the other node.
#      This handles cases where a subtree exists in only one of the trees.
# 3. Merge Step:
#    - If both nodes exist:
#       a. Add their values.
#       b. Recursively merge their left children.
#       c. Recursively merge their right children.
# 4. Return the updated node from the first tree.
#    - The merged tree is constructed by modifying the first input tree in place.
# This approach works because:
# - The recursive structure mirrors the shape of the trees.
# - The base case ensures we handle None values gracefully.
# - Each merge operation is localized to a pair of corresponding nodes.


# Time complexity: O(n+m) -> we iterate through each node in both trees once to combine them
# Space complexity: O(h) -> the depth of the recursive calls, one per tree level. Best case in a balanced tree, the height is O(log n), worst case, the height is O(n) (a linked list like tree)


from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def mergeTreesDFS(self, root1, root2): # DFS
        if root1 is None: # Base case -> when either node is none
            return root2 # Takes care of the case where left tree has no node
            
        if root2 is None: # Case where right tree has no node
            return root1 
        
        root1.val += root2.val # Update the current node in the left tree with the sum of both nodes
        root1.left = self.mergeTreesDFS(root1.left, root2.left) # Recurse left, return val for the left child and assign it to node's left
        root1.right = self.mergeTreesDFS(root1.right, root2.right) # Recurse right, return val the right child, assign to node's right
        
        return root1 # First tree

def print_tree(root):
    if not root:
        print("Empty tree")
        return

    q = deque([root])
    res = []
    while q:
        node = q.popleft()
        if node:
            res.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        else:
            res.append("null")

    while res and res[-1] == "null":
        res.pop()

    print(" ".join(res))

if __name__ == "__main__":
    # Test input

    t1 = TreeNode(1)
    t1.left = TreeNode(3)
    t1.right = TreeNode(2)
    t1.left.left = TreeNode(5)
    
    t2 = TreeNode(2)
    t2.left = TreeNode(1)
    t2.right = TreeNode(3)
    t2.left.right = TreeNode(4)
    t2.right.right = TreeNode(7)

    sol = Solution()
    merged = sol.mergeTreesDFS(t1, t2)
    print_tree(merged)

