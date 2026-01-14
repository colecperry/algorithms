from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p.left, q.left), (p.right, q.right)])

        while queue:
            left, right = queue.popleft()

            if not left or not right:
                return False

            elif left.val != right.val:
                return False

            elif left.val == right.val:
                queue.append((left.left, right.left))
                queue.append((left.right, right.right))

        return True

p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))

p2 = TreeNode(1, TreeNode(2), None)
q2 = TreeNode(1, None, TreeNode(2))

p3 = TreeNode(1, TreeNode(2), TreeNode(1))
q3 = TreeNode(1, TreeNode(1), TreeNode(2))

my_solution = Solution()
print(my_solution.isSameTree(p, q)) # Same trees -> True
print(my_solution.isSameTree(p2, q2)) # Different tree structure -> False
print(my_solution.isSameTree(p3, q3)) # Different tree values -> False