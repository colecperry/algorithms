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

# How to Solve (DFS):
    # Check the root nodes -> 4 cases
        # 1. They are both null (empty nodes) -> Return True to prev call stack
        # 2. Only one is null (empty node) -> Return False to caller (non identical structure)
        # 3. The values are non equal -> Return False to the caller (non identical values)
        # 4. The values are equal -> Continue and recursively call the function on the left subtree (continues until we reach Base Case -> one of the three returns), and on the right subtree
        # The variables we store the boolean in represent the left subtree being the same from the node of the caller 
            # Ex. p = [1,2,1], q = [1,2,1], left_same = True means that the left subtreee of the root nodes are identical
            # We basically keep calling this recursively until we hit a False -> The left or right subtrees are not identical, or we hit a True -> we get to a base case where both nodes are none, so we return True all the way back to the root node caller
        # Return the result (both left and right subtrees must be True)

    # Time complexity: O(p + q) -> Worst case we have to iterate through every node in both trees
    # Space complexity: -> O(h): If the tree is balanced, the max deapth of recursion is O(log n) because at each level the tree splits into two subtrees, and for a skewed tree, each recursive call only processes one child at a time, resulting in n recursive calls in total before reaching the base case -> O(n)

# Line by line BFS:
    # Big Picture: We use a queue starting with the root, check our conditions for true or false, and then append the children to the queue. Essentially we check the next node each iteration, and the queue is a list of tuples where each tuple is a node from p and a node from q
    # Code: Initialize a deque with root nodes, loop and dequeue (pop from front) -> Check:
        # 1. If both nodes are None (same tree) -> continue to next loop
        # 2. If only one node is None (different structure) -> return False
        # 3. If node values are None (different values) -> return False
    # Append the left and right children to the queue and continue to next iteration

    
    # Line by Line:
    # queue = deque([(1, 1)]) -> start with root Node
    # popleft() -> node1 = 1, node2 = 1
    # don't enter any if statement, children of 1: (2, 2), (3, 3) 

    # queue = deque([(2, 2), (3, 3)]) -> appended children
    # popleft() -> node1 = 2, node2 = 2
    # don't enter any if statment, append childern of 2: (None, None), (None, None)

    # queue = deque([(3, 3), (None, None), (None, None)])
    # popleft() -> node1 = 3, node2 = 3
    # don't enter any if statment, append children of 3: (None, None), (None, None)

    # queue = deque([(None, None), (None, None), (None, None), (None, None)])
    # popleft() 4 times -> node1 = None, node2 = None 
    # Return True once Queue is empty

# Time Complexity: O(n)
# - Each node in both trees is processed exactly once.
# - Since we traverse all nodes, the time complexity is O(n), where n is the number of nodes in the trees.

# Space Complexity: O(n)
# - In the worst case (if the trees are completely unbalanced), the queue holds O(n) nodes.
# - In the best case (if the trees are balanced), the queue holds O(log n) nodes at a time.
# - Overall, the worst-case space complexity is O(n).

from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q): # DFS
        if not p and not q:  # Both trees are empty -> We reach base case
            return True
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
        queue = deque([(p, q)])  # Initialize queue with root nodes

        while queue:
            node1, node2 = queue.popleft()  # Pop off pair of nodes p, q

            if not node1 and not node2:  # Both nodes are None, continue checking
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

