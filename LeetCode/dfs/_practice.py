from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = [(())]
        def dfs(left, right):
            node_1, node_2 = stack.pop()
            if not node_1 and not node_2:
                return True

            if not node_1 or not node_2:
                return False
            
            if node_1.val != node_2.val:
                return False
            
            stack.append((node_1.left.val, node_2.right.val))
            stack.append((node_1.right.val, node_2.left.val))

        return dfs(root.left, root.right)
    
# Ex. 2
#               1
#              / \
#             /   \
#            2     2
#             \     \
#              3     3

sol = Solution()

t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(2)
t1.left.left = TreeNode(3)
t1.left.right = TreeNode(4)
t1.right.left = TreeNode(4)
t1.right.right = TreeNode(3)

t2 = TreeNode(1)
t2.left = TreeNode(2)
t2.right = TreeNode(2)
t2.left.right = TreeNode(3)
t2.right.right = TreeNode(3)


print(sol.isSymmetric(t1))
print(sol.isSymmetric(t2))

# print(sol.isSymmetricIterative(t1))
# print(sol.isSymmetricIterative(t2))