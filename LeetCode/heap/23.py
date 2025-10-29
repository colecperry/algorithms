import heapq

# PROBLEM: LC 23 - Merge k Sorted Lists

# Key Insight: Use min heap to track the smallest current element from each list.
#              Pop smallest, add to result, push next node from same list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MergeK:
    def mergeKLists(self, lists):
        '''
        You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.

        Ex. 1
            Input: lists = [[1,4,5],[1,3,4],[2,6]]
            Output: [1,1,2,3,4,4,5,6]
            Explanation: The linked-lists are:
            [
            1->4->5,
            1->3->4,
            2->6
            ]
            merging them into one sorted linked list:
            1->1->2->3->4->4->5->6

        TC:
            - O(k log k) - initial heap setup pushes k nodes into heap using heappush (log k)
            - O(n) for iterating through the heap (one iteration for each node)
            - Each iteration: O(log k) to pop + O(log k) to push
            - Total: O(k log k) + O(N log k) = O(N log k)
        SC: 
            - O(k) - the heap only stores at nost k nodes at once (one from each list)
        '''
        heap = []
        
        # Step 1: Add first node from each list to heap
        # Tuple: (node_value, list_index, node (head is a reference to list1, list2, etc))
        for i, head in enumerate(lists):
            if head: # protected against empty lists
                heapq.heappush(heap, (head.val, i, head)) # head is a pointer to the first node
        
        dummy = ListNode(0) # Start LL after dummy node
        current = dummy
        
        # Step 2: Extract min, add to result, push next from same list
        while heap: # Continue building merged LL until no more nodes
            val, list_idx, node = heapq.heappop(heap) # pop min val & destructure tuple
            
            # Add node to merged LL
            current.next = node
            current = current.next # Move pointer forward
            
            # Push next node from same list
            if node.next:
                heapq.heappush(heap, (node.next.val, list_idx, node.next)) 
        
        return dummy.next # Return first node in merged LL

# Example 1: lists = [[1,4,5],[1,3,4],[2,6]]
list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

list3 = ListNode(2)
list3.next = ListNode(6)

sol = MergeK()
print(sol.mergeKLists([list1, list2, list3]))
# Expected output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6