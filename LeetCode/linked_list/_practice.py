class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        curr = head
        after = head
        for _ in range(n):
            after = after.next
        
        while after.next:
            curr = curr.next
            after = after.next
        
        curr.next = curr.next.next

        return head

# Manually creating Example 1: [1,2,3,4,5]
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
solution = Solution()
solution.removeNthFromEnd(head1, 2) # 1 -> 2 -> 3 -> 5

head2 = ListNode(1)
solution.removeNthFromEnd(head2, 1) # []