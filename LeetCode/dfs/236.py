# 236. Lowest Common Ancestor of a Binary Tree

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Note to self: Lowest means lowest depth on the tree from the top

# How to solve: (without extra space)
    # There are three cases:
        # When p and q are on opposite sides of the tree (the root is the LCA)
        # When q is a descendant of p (p is the LCA)
        # When p is a descendant of q (q is the LCA)
    # Do a DFS from the root
        # Check if current node is p or q 
        # No -> recursively call the left sub tree
        # Yes - > return p or q to the parent node
    # Stop searching left side when you first find p or q -> other val (p or q) is under that node or on the other side
    # Now search the right sub tree
        # If we do not find p or q, return None to the parent
        # If we find p or q, return that Node to the parent
    # Return to root node:
        # If we have returned both left and right to the root, the LCA == root
        # If we return only left to the root, left is the LCA
        # If we return only right to the root, right is the LCA

    # Time complexity: O(n) -> worst case, we search every node
    # Space complexity: O(1) if not counting recursive stack frames -> We do not define any other data structures, O(n) if we are counting recursive stack frames -> worst case is that we have a recursive call stack frame for every node in the tree

# How to Solve: (with extra space)
    # Start at the root (which is a common ancestor of every tree)
    # Create three arrays -> one tracks current path, one tracks path to p, and one tracks path to q
    # Create recursive function for depth first search, pass in root
        # Create base case -> If we reach none, return (just return)
        # Append each node to the current path
        # If we come across p or q, append each node in current path to p or q path arrays
        # Recursively call dfs to left of current node
        # Recursively call dfs to right of current node
        # Once we search left and right and hit base case, pop last node off (return to last call and search other direction requires updating the current path array)
    # Call the dfs function
    # Assume the answer is the root
    # Loop through arrays (whichever is shorter length of p and q arrays)
    # If we find the same value on the same index, we found a deeper common ancestor

    # Time complexity: O(n) -> worst case, we have to visit every node from the input
    # Space complexity: O(n) -> worst case, we have to add every node from the input to the current path array

# Example 1

#                3
#              /   \
#             /     \
#            /       \
#           5         1
#          / \       / \
#         /   \     /   \
#        6     2   0     8
#             / \ 
#            7   4

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

# Note to self: the lowest value on the tree that is a common ancestor of both 5 and 1 is 3


# Example 2: 
#                3
#              /   \
#             /     \
#            /       \
#           5         1
#          / \       / \
#         /   \     /   \
#        6     2   0     8
#             / \ 
#            7   4

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

# Note to self: the lowest value on the tree that is a common ancestor of 5 and 4 is 5 (5 is an ancestor to itself)

# Example 3:
#           1
#          /
#         2

# Input: root = [1,2], p = 1, q = 2
# Output: 1

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # Answer without extra memory
    def lowestCommonAncestor(self, root, p, q):
        if not root: # If we have no root, return None
            return None
        
        if root == p or root == q: # If we find p or q
            return root # Return that node to the caller (parent)
        
        # DFS: # If we do not find p or q, 
        l = self.lowestCommonAncestor(root.left, p, q) # Call left subtree recursively
        r = self.lowestCommonAncestor(root.right, p, q) # Call right subtree recursively

        if l and r: # If left and right both return non Null -> current node we are at is the LCA
            return root 
        else: # If only left or right is non null
            return l or r # The returned node is the LCA (the other is a child)


    # Answer with extra memory
    def lowestCommonAncestor2(self, root, p, q):
        current_path = [] # Holds the current path from our depth first search
        p_path = [] # Holds the path to q
        q_path = [] # Holds the path to p

        def dfs(current_node):
            if current_node == None: # Base case -> we reach the end of the path
                return # We return back to the caller in the last call stack
            current_path.append(current_node) # Append the node we are on to the current path
            if current_node.val == p.val: # If we find p
                for ele in current_path: # Append all nodes in current path to p_path array
                    p_path.append(ele)
            if current_node.val == q.val: # If we find q
                for ele in current_path: # Append all ndoes in current path to q_path array
                    q_path.append(ele)
            dfs(current_node.left) # Recursive call for dfs searches all the way to the left first
            dfs(current_node.right) # Once we finish searching left until base case, search right
            current_path.pop() # Once we search all the way to the right, update path
            # (when we get to 6, search left (None), search right from 6 (None), pop 6, return to 5)
        
        dfs(root) # Call the dfs function starting at the root

        ans = root # Assume the answer is the root (any two nodes have common ancestor root)
        for i in range(min(len(p_path), len(q_path))): # Loop through which ever arrary is smaller
            if p_path[i] == q_path[i]: # If we find a common value
                ans = p_path[i] # Update the answer (we found a deeper common ancestor)
        
        return ans
    
# Build the tree for testing
def build_tree():
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    return root

# Create the tree and test cases
root = build_tree()
solution = Solution()

# Test case 1: LCA of 5 and 1 should be 3
p = root.left  # Node with value 5
q = root.right  # Node with value 1
print("LCA of 5 and 1:", solution.lowestCommonAncestor(root, p, q).val)  # Expected output: 3

# Test case 2: LCA of 5 and 4 should be 5
p = root.left  # Node with value 5
q = root.left.right.right  # Node with value 4
print("LCA of 5 and 4:", solution.lowestCommonAncestor(root, p, q).val)  # Expected output: 5