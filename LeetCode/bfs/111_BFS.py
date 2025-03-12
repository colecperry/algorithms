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

    
    def minDepth2(self, root):
        if not root:
            return 0
        q = deque([root])
        depth = 1
        while q:
            qSize = len(q)
            for _ in range(qSize):
                node = q.popleft()
                # Since we added nodes without checking null, we need to skip them here.
                if not node:
                    continue
                # The first leaf would be at minimum depth, hence return it.
                if not node.left and not node.right:
                    return depth
                q.append(node.left)
                q.append(node.right)
            depth += 1
        return -1




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