# 100. Same Tree

# Topics: Tree, DFS, BFS, Binary Tree

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Ex. 1

#           1              1
#         /   \          /   \
#        2     3        2     3
# 
#  
# Input: p = [1,2,3]   q = [1,2,3]
# Output : True


# Ex. 2

#           1              1
#         /                  \
#        2                    2
# 
#  
# Input: p = [1,2]   q = [1,null,3]
# Output : False

# Ex. 3

#           1              1
#         /   \          /   \
#        2     1        1     2
# 
#  
# Input: p = [1,2,1]   q = [1,1,2]
# Output : False

from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q): # DFS
        """
        - TC: O(p + q) -> Worst case we have to iterate through every node in both trees
        - SC: O(h) -> recursion depth equals tree depth
        """
        if not p and not q:  # Both trees are empty -> We reach base case
            return True # need to check this first or we get an error
        if not p or not q:  # One tree is empty, the other is not
            return False
        if p.val != q.val:  # Mismatched values
            return False
        
        # Recursively check left and right subtrees
        left_same = self.isSameTree(p.left, q.left) # Recursively step into left subtree -> Returns True or False
        right_same = self.isSameTree(p.right, q.right) # Recursively step into right subtree -> Returns True or False 
        
        # Both left and right subtrees must be identical
        return left_same and right_same
    
    def isSameTree2(self, p, q): # BFS
        """
        - TC: O(p + q) -> we traverse every node of each tree
        - SC: 
        """
        queue = deque([(p, q)])  # Always wrap root nodes/tuples in a list when creating a deque so it's iterable

        while queue:
            node1, node2 = queue.popleft()  # Pop off pair of nodes p, q

            if not node1 and not node2:  # Both nodes are None, continue checking, need to check this first or we get an error
                continue 
            if not node1 or not node2:  # If only one is None, trees are different
                return False
            if node1.val != node2.val:  # Different values
                return False

            # Add left children and right children to the queue
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))

        return True  # If we never return False, the trees are identical


p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))

p2 = TreeNode(1, TreeNode(2), None)
q2 = TreeNode(1, None, TreeNode(2))

p3 = TreeNode(1, TreeNode(2), TreeNode(1))
q3 = TreeNode(1, TreeNode(1), TreeNode(2))

my_solution = Solution()
print(my_solution.isSameTree2(p, q)) # Same trees -> True
print(my_solution.isSameTree2(p2, q2)) # Different tree structure -> False
print(my_solution.isSameTree2(p3, q3)) # Different tree values -> False

