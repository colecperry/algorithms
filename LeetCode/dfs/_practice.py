from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # Base Case -> Leaf node
        if not root.left and not root.right:
            return 1 
        
        # Recursive Case -> 1 child: Explore one direction
        if not root.left:
            right = self.minDepth(root.right)
            return 1 + right
        
        elif not root.right:
            left = self.minDepth(root.left)
            return 1 + left
        
        # Recursive Case -> 2 children: Explore left and right
        else:
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)

            return 1 + min(left, right)

my_solution = Solution()

root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(17)

print(my_solution.minDepth(root1)) # 2

#               2
#                \
#                 3
#                  \
#                   4 
#                    \
#                     5
#                      \ 
#                       6

root2 = TreeNode(2)
root2.right = TreeNode(3)
root2.right.right = TreeNode(4)
root2.right.right.right = TreeNode(5)
root2.right.right.right.right = TreeNode(6)

print(my_solution.minDepth(root2)) # 5