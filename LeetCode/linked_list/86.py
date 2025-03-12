# 86. Partition List

# LL: Partition List ( ** Interview Question)
# Implement the partitionList member function for the LinkedList class, which partitions the list such that all 
# nodes with values less than x come before nodes with values greater than or equal to x.
# Note:  This linked list class does NOT have a tail which will make this method easier to implement.
# The original relative order of the nodes should be preserved.

# Details:
# The function partitionList takes an integer x as a parameter and modifies the current linked list in place
# according to the specified criteria. If the linked list is empty (i.e., head is null), the function should 
# return immediately without making any changes.

# Example 1:
# Input:
# Linked List: 3 -> 8 -> 5 -> 10 -> 2 -> 1 x: 5
# Process:
# Values less than 5: 3, 2, 1
# Values greater than or equal to 5: 8, 5, 10
# Output:
# Linked List: 3 -> 2 -> 1 -> 8 -> 5 -> 10

# Example 2:
# Input:
# Linked List: 1 -> 4 -> 3 -> 2 -> 5 -> 2 x: 3
# Process:
# Values less than 3: 1, 2, 2
# Values greater than or equal to 3: 4, 3, 5
# Output:
# Linked List: 1 -> 2 -> 2 -> 4 -> 3 -> 5

# How to Solve
    # Initalize two dummy nodes for two seperate lists to hold values less than and greater than the value "X" passed in
    # Create pointers that will traverse each new list
    # Iterate through the original list, moving nodes to the new lists
    # Terminate the second list (since we re-use nodes, whatever we attach is still pointing at another node)
    # Connect the first list to the beginning of the second, past the dummy node
    # Return dummy.next

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        # Create a two dummy nodes, one to start each LL (first LL has nodes < X, second has nodes > X)
        dummy1 = ListNode(0, None)
        dummy2 = ListNode(0, None)
        # Loop through linked list starting from current
        current = head
        ptr1, ptr2 = dummy1, dummy2 # Create ptrs - 2 LL
        while current:
            if current.val < x: # Val is less
                ptr1.next = current # Attach that node 
                ptr1 = ptr1.next # Move ptr forward
            else:
                ptr2.next = current
                ptr2 = ptr2.next
            current = current.next # Move original ptr

        # Important: Terminate the second list to avoid cycles (since we are reusing nodes from the first list, the last node we add to the list is still pointing to something)
        ptr2.next = None 

        # Attach lists back together
        ptr1.next = dummy2.next

        return dummy1.next # Return the head of the first half

# Helper function to print linked list (for verification)
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

# Manually creating Example 1: [1,4,3,2,5,2]
head1 = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
solution = Solution()
new_head = solution.partition(head1, 3)
print_linked_list(new_head)# Expected Output: 1 -> 2 -> 2 -> 4 -> 3 -> 5
