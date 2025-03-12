# 257 - Binary Tree Paths

# Topics: String, Backtracking, Tree, DFS, Binary Tree

# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.

# Example 1:
#         
#          1
#         / \
#        /   \
#       2     3
#        \
#         5


# Input: root = [1,2,3,null,5]
# Output: ["1->2->5", "1->3"]

# Example 2:
# Input: root = [1]
# Output: ["1"]

# DFS Solution
    # Big Picture: each recursive call we append the current node to the current path, and if we are on a leaf node, append the current path to the output array
    # Code:
    # Create an output array and call dfs with the root and an empty array for the current path
    # Base case -> If node is None return to prev call stack
    # Append the current path array
    # If we are on a leaf node, join the current path with -> and append to the res
    # Recursively call the left and right subtrees

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution(object):
    def binaryTreePaths(self, root): # DFS
        def dfs(node, path):
            if not node:  # Base case: If node is None, return
                return
            
            path.append(str(node.val))  # Add current node value to path
            
            if not node.left and not node.right:  # If it's a leaf node
                paths.append("->".join(path))  # Convert path list to string and store result
            else:
                dfs(node.left, path[:])  # Pass a copy of path for left subtree
                dfs(node.right, path[:])  # Pass a copy of path for right subtree
        
        paths = [] # Output array
        dfs(root, []) # Call dfs fuction with the root Node and output array
        return paths
    
    # Line by Line Code:
    # dfs(1, [])
        # append '1' to path
        # Calls dfs(2, ['1'])
    # dfs(2, ['1'])
        # append '2' to path
        # Calls dfs(None, ['1', '2'])
    # dfs(None, ['1', '2'])
        # hits base case and returns to prev call stack
    # dfs(2, ['1', '2'])
        # calls dfs(5, ['1', '2'])
        # append '5' to path
        # if not node.left and if not node.right == True (leaf Node)
        # append ['1->2->5'] to paths
    # Back to original call stack dfs(1, ['1'])
        # Unpauses at # dfs(node.left, path[:])
        # Calls dfs(3, ['1'])
    # dfs(3, ['1'])
        # append '3' to path
        # if not node.left and if not node.right == True (leaf Node)
        # Append ['1->3'] to paths
    # Back to original call stack dfs(1, ['1'])
        # return paths = ['1->2->5', '1->3']
    
    def binaryTreePaths2(self, root): # BFS
        if not root:
            return []
        
        result = [] # Outut array
        queue = deque([(root, str(root.val))])  # Store (node, path string)
        
        while queue:
            node, path = queue.popleft() # Dequeue and destructure
            
            # If it's a leaf node, add the path to the result
            if not node.left and not node.right:
                result.append(path)
            
            # Add left child to the queue with updated path
            if node.left:
                queue.append((node.left, path + "->" + str(node.left.val)))
            
            # Add right child to the queue with updated path
            if node.right:
                queue.append((node.right, path + "->" + str(node.right.val)))

        return result
    
# Code Explanation (BFS):
    # Big Picture, we create a queue with a tuple (the root node and the value as a string (path)), and loop until the queue is empty popping off the first tuple in the queue, appending the current path if it's a leaf node, and then appending the left and right children to the queue with the updated paths. Eventually we will reach the leaf nodes and correct paths will be appended to res.
    # Create an output arr and a deque with a tuple (root, root.val)
    # Enter while loop until queue is empty:
        # Dequeue node, unpack the tuple into variables node and path
        # If node is a leaf node, append current path to output array
        # If node has a left child, append to the queue the left child with the updated path (path + "->" + str(node.left.val))
        # If node has a right child, append to the queue the right child with the updated path (path + "->" + str(node.right.val))

    # Time Complexity: O(n)
    # - We visit each node exactly once.
    # - Each node is dequeued and processed in constant time O(1).
    # - Therefore, the total time complexity is O(n), where n is the number of nodes in the tree.

    # Space Complexity: O(n) (Worst Case)
    # - The queue stores O(1) nodes in a skewed tree (1 node) because each iteration we pop from the left and append the children (one node), so it can only hold one node at a time.
    # - In a balanced tree, the queue holds O(n/2) nodes at most which would be when it holds the last level of the tree.
    # - The result list also holds O(n/2) paths in the worst case, and since .5 is a constant factor, we drop it and it simplifies to O(n)



my_tree = TreeNode(1, 
                    TreeNode(2, None, TreeNode(5)),  # Left subtree
                    TreeNode(3))  # Right subtree

my_solution = Solution()
print(my_solution.binaryTreePaths2(my_tree))


