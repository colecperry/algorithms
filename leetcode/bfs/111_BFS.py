# 111. Minimum Depth of Binary Tree

# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Example 1:
#               3
#              / \
#             9   20
#                /  \
#               15   17

# root = [3,9,20,null,null,15,7]
# Output = 2

# Example 2:
#               2
#                \
#                 3
#                  \
#                   4 
#                    \
#                     5
#                      \ 
#                       6

# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5

# How to solve (DFS):
    # 

# Time Complexity: We will traverse each node in the tree only once; hence, the total time complexity would be O(N).
# Space Complexity: The only space required is the stack space; the maximum number of active stack calls would equal the maximum depth of the tree, which could equal the total number of nodes in the tree. Hence, the space complexity would equal O(N).

# CALL STACK (Last In, First Out)

# 1. dfs(3)   ← waiting for results from dfs(9) and dfs(20)
# │   2. dfs(9)   → returns 1 
# │   3. dfs(20)  ← waiting for results from dfs(15) and dfs(7)
# │   │   4. dfs(15) → returns 1
# │   │   5. dfs(7)  → returns 1
# │   6. dfs(20)  → returns 2
# 7. dfs(3)   → returns 2

# How to solve (BFS):




from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # DFS Solution
    def minDepth(self, root):
        # Define the depth-first search
        def dfs(root): # we go straight to the return statement
            if root is None: # Base case -> when we hit the end of a path
                return 0
            # If either node has an empty left or right node, go opposite direction
            if root.left is None:
                return 1 + dfs(root.right) # Add one for current node, search right
            elif root.right is None:
                return 1 + dfs(root.left) # Add one for current node, search left
            # Both children are non-null, hence call for both children.
            return 1 + min(dfs(root.left), dfs(root.right)) # Add one for current node

        return dfs(root)# Call dfs function
    
    # 1. dfs(3)   ← waiting for results from dfs(9) and dfs(20)
    # │   2. dfs(9)   → returns 1 to dfs(3) 
    # │   3. dfs(20)  ← waiting for results from dfs(15) and dfs(7)
    # │   │   4. dfs(15) → returns 1 to dfs(20)
    # │   │   5. dfs(17)  → returns 1 to dfs(20)
    # │   6. dfs(20)  → returns 2 to dfs(3) -> 1 + min(1, 1)
    # 7. dfs(3)   → returns 2  -> 1 + min(dfs(9), dfs(20)) -> 1 + min(1, 2)

    # Example 1:
    #               3
    #              / \
    #             9   20
    #                /  \
    #               15   17

    # How to Solve - BFS (Level-based)
        # - Use BFS to traverse the tree level by level.
        # - Initialize the queue with the root node and a depth counter starting at 1.
        # - While the queue is not empty:
        #     - For each node in the current level (detected using the current queue length):
        #         - Pop the node.
        #         - If the node is a leaf (no left or right child), return the current depth as the minimum depth.
        #         - Otherwise, add the node’s left and right children to the queue for the next level.
        #     - After processing the level, increment the depth counter.
        # - This ensures you find the shallowest leaf node by level order.

        # Time Complexity: O(N), because each node is visited once in the worst case.
        # Space Complexity: O(N), because in the worst case the queue holds up to N/2 nodes at the last level.


    def minDepth2(self, root): # level-based
        if not root: # Edge case for empty tree
            return 0
        q = deque([root]) # Init the queue with the root
        depth = 1 # track depth to return min depth
        while q: # level based logic -> for loop with len of q for each level inside while loop
            for _ in range(len(q)):
                node = q.popleft()
                if not node.left and not node.right: # if we found a leaf
                    return depth # return depth
                if node.left:
                    q.append(node.left) # append left and right children
                if node.right:
                    q.append(node.right)
            depth += 1 # increase depth each level
    
    # How to Solve - BFS (Tuple)
        # - Use BFS to traverse the tree level by level.
        # - Store tuples of (node, current depth) in the queue to track depth.
        # - Start by adding the root with depth 1 to the queue.
        # - While the queue is not empty:
        #     - Pop the front node and its depth.
        #     - If the node is a leaf (no left or right child), return its depth as the minimum depth.
        #     - Otherwise, add the node’s children to the queue with depth incremented by 1.
        # - This guarantees the first leaf reached has the minimum depth.

        # Time Complexity: O(N), because each node is visited once in the worst case.
        # Space Complexity: O(N), because in the worst case (complete binary tree) the queue holds up to N/2 nodes.

    
    def minDepth3(self, root): # tuple-based
        if root is None: # Edge case for empty tree
            return 0
        q = deque([(root, 1)]) # create an it list w/ node & depth tuple
        while q: 
            node, depth = q.popleft() # unpack tuple
            if node.left is None and node.right is None: # if leaf node
                return depth 
            if node.left: 
                q.append((node.left, depth + 1)) # add left child
            if node.right:
                q.append((node.right, depth + 1)) # add right child




my_solution = Solution()

root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(17)

print(my_solution.minDepth(root1))

root2 = TreeNode(2)
root2.right = TreeNode(3)
root2.right.right = TreeNode(4)
root2.right.right.right = TreeNode(5)
root2.right.right.right.right = TreeNode(6)

print(my_solution.minDepth(root2))