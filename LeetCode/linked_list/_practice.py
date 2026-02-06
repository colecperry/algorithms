from typing import Optional

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

# Manually creating Example 1: [1,2,3,4,5], [1,2,3,4,5,6]
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, (ListNode(6, None)))))))
solution = Solution()
solution.middleNode(head1)
solution.middleNode(head2)
