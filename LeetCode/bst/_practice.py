from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []

        def dfs(root):
            # Base Case
            if not root:
                return
            
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)
        
        dfs(root)

        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                return False

        return True
    
#            5
#          /   \
#         /     \
#        1       4
#               / \
#              /   \
#             3     6

# Tree 1: [2,1,3]
root1 = TreeNode(2, TreeNode(1), TreeNode(3))

# Tree 2: [5,1,4,null,null,3,6]  
root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))

sol = Solution()
print(sol.isValidBST(root1)) # True
print(sol.isValidBST(root2)) # False