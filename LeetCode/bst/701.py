# 701. Insert into a Binary Search Tree

# Topics: Tree, Binary Search Tree, Binary Tree

# You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

# Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

# Ex. 1
#                  4                           4
#                 / \                        /   \
#                /   \                      /     \
#               2     7         ->         2       7
#              / \                        / \     /
#             1   3                      1   3   5
#
#
# Input: root = [4,2,7,1,3], val = 5
# Output: [4,2,7,1,3,5]

# Ex. 2
# Input: root = [40,20,60,10,30,50,70], val = 25
# Output: [40,20,60,10,30,50,70,null,null,25]

# Ex. 3
# Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
# Output: [4,2,7,1,3,5]

# How to Solve (Iterative)

    # 1. If the root is None, simply return a new TreeNode — this value becomes the new root.
    # 2. Use a pointer (temp) to traverse the tree without modifying the original root reference.
    # 3. Loop indefinitely until we find the correct spot to insert:
    #    - If the value is less than the current node:
    #       → If the left child is None, insert here and return the original root.
    #       → Otherwise, move temp to the left child.
    #    - If the value is greater or equal:
    #       → If the right child is None, insert here and return the root.
    #       → Otherwise, move temp to the right child.
    # 4. Return the original root since the structure has been updated in place.

    # Key Difference from Recursive:
    # - No call stack; all navigation happens via a loop.
    # - Structure is updated in place using a moving pointer.

    # Time Complexity: O(H)
    # - H = height of the tree
    # - Worst case: unbalanced tree → O(N)
    # - Best case: balanced tree → O(log N)

    # Space Complexity: O(1)
    # - No recursion → constant space usage
    # - Tree is modified in place with


# How to Solve (Recursive)

    # 1. Define a recursive helper function that takes a node and the value to insert.
    # 2. Base case: If the current node is None, we've found the empty spot where the new value should go.
    #    → Return a new TreeNode with the value.
    # 3. If the value is less than the current node's value, we go left.
    #    → Call the helper recursively on node.left and assign the result back to node.left.
    # 4. If the value is greater than the current node's value, we go right.
    #    → Call the helper recursively on node.right and assign the result back to node.right.
    # 5. After processing, return the current node (with updated children if any).
    #    → This is key: recursion "bubbles" the updated tree back up to the root.

    # 6. From the main function, call the recursive helper with the root node and return the result.
    #    → This ensures we return the correct new root, especially in the case where the input root is None.

    # Notes on recursion:
    # - We're always returning the subtree we're currently working on.
    # - The recursion stack handles the path down, and the return values re-link the updated structure as we go back up.
    # - This is a common recursive pattern for modifying trees in place.

    # Time Complexity: O(H)
    # - Where H is the height of the tree.
    # - In the worst case (unbalanced tree), H = N (linked-list shape) → O(N)
    # - In the best case (balanced tree), H = log N → O(log N)

    # Space Complexity: O(H)
    # - Due to the recursive call stack.
    # - No additional data structures are used.
    # - Same H = O(N) in the worst case, O(log N) in the best case.



from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBSTIterative(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: # If root is empty
            return TreeNode(val) # Insert and return root
        temp = root # Create pointer variable -> traverse with temp so we can return original root
        while True:
            if val < temp.val: # Val we're inserting is less
                if not temp.left: # Check if spot open to the left
                    temp.left = TreeNode(val) # If so, insert and return 
                    return root
                else:
                    temp = temp.left # If not recurse left
            else: # If val we're inserting is more
                if not temp.right: # Check if spot is open to the right
                    temp.right = TreeNode(val) # If so, insert and return
                    return root
                else:
                    temp = temp.right # If not recurse right
        
    def insertIntoBSTRecursive(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def insert(node, val):
            if not node: # Base case -> when we find an empty spot
                return TreeNode(val) # Create a new node and assign it to node.left or node.right
            if val < node.val:
                node.left = insert(node.left, val) 
            else:
                node.right = insert(node.right, val)
            return node # Returns the newly updated node to the prev call stack -> unrolls the recursive calls back to the root
        
        return insert(root, val) # Returns the root, but updated with the new tree connections in each node
    
    
    


sol = Solution()
t1 = TreeNode(4)
t1.left = TreeNode(2)
t1.right = TreeNode(7)
t1.left.left = TreeNode(1)
t1.left.right = TreeNode(3)

sol.insertIntoBSTRecursive(t1, 5)

