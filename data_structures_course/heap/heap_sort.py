# Binary heap:  a nearly complete binary tree that satisfies the heap ordering property
# Heap ordering property
    # max-heap: the value of each node is less than or equal to the value of it's parent, with the max value element at the root
    # min heap, the value of each node is greater than or equal to the value of it's parent, with the minimum value element at the root
# Height of a heap: equal to the height of a root (O(n log n))

# Heap sort high level
    # Each remove() operation extracts the max element, pops off the last element in the heap and assigns to index 0 or the root, and uses sink down to restore the heap ordering property, then stores the max element in the sorted list

# Time Complexity analysis:
    # Building the max heap with heapify() -> O(n): Heapify runs in O(n) because most nodes in a binary heap move only a few levels down, not log n levels. The number of nodes increases exponentially at lower levels, but their work per node decreases, forming a geometric series that sums to O(n). Unlike Heap Sort (O(n log n)), which repeatedly extracts elements, heapify processes each node at most once in a bottom-up manner, making it O(n).
    # Heap sort -> remove max elements one by one with remove(): each remove operation takes O(log n), and we do n removals. Total complexity O(n log n) for worst case (each remove operations requires a sink_down() to the bottom of the tree), average case (sink_down moves log n levels), and best case 
# Space Complexity: 
    # Heapify -> O(1): does not take extra space
    # Heap_sort -> O(1) if sorting in place, O(n) if using another list

# Edge Cases: 
    # Already sorted list: Heapify still runs in O(n), and heap_sort takes O(log n) per element, leading to O(n log n) per element
    # Reverse sorted list: Heapify runs in O(n) but this is the worst case scenario because every parent is smaller than it's child, requiring elements to be moved significantly. Heap_sort: Each removal requires maximum reordering, leading to O(n log n). Total = O(n log n) 
    # Partially sorted list: Heapify runs in O(n) if the list is mostly correct, heapify() finishes quickly. Heap_sort() runs in O(n log n) where some remove() operations might require less work, but worst case remains O(n log n). Total: O(nlogn)

class MaxHeap:
    def __init__(self):
        self.heap = []  # We store the heap using a list
    
    def left_child(self, index):
        return 2 * index + 1  # Left child index formula

    def right_child(self, index):
        return 2 * index + 2  # Right child index formula
    
    def parent(self, index):
        return (index - 1) // 2  # Parent index formula
    
    def swap(self, index1, index2):
        # Swap two elements in the heap
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        # Insert the new value at the end of the heap
        self.heap.append(value)
        current = len(self.heap) - 1  # Index of the newly inserted element

        # Bubble up the new element to maintain heap property
        while current > 0 and self.heap[current] > self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
    # removes last element
    def remove(self):
        if len(self.heap) == 0:
            return None  # Return None if heap is empty
        
        if len(self.heap) == 1:
            return self.heap.pop()  # If only one element, pop and return it
        
        max_value = self.heap[0]  # Extract the max value
        self.heap[0] = self.heap.pop()  # Pop off last element (65) and assign to idx 0
        self.sink_down(0)  # Restore heap property by sinking down 
        return max_value  # Return the removed max value
    
    def sink_down(self, index):
        max_index = index  # Assume 
        while True:
            left_index = self.left_child(index)
            right_index = self.right_child(index)

            # Find larger child and set to max idx
            if (left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]):
                max_index = left_index
            
            if (right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]):
                max_index = right_index
            
            # If ele at index of either child is > ele of parent
            if max_index != index:
                self.swap(index, max_index) # Swap vals
                index = max_index # Start loop again from greater child index
            else:
                return  # Stop if the element is in the right place
    
    def heapify(self):
        # Heapify -> starts from last non-leaf node at index 2 (80) and calling sink_down on each node moving backwards to index 0
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.sink_down(i)

    # Heap sort repeatedly removes the max element and places it at the end of the array
    def heap_sort(self):
        sorted_list = []
        while self.heap:
            # Each time we remove the root
            sorted_list.append(self.remove()) 
        return sorted_list[::-1]  # Reverse to get ascending order


# Start with a unsorted heap
out_of_order_heap = MaxHeap()
out_of_order_heap.heap = [50, 95, 80, 60, 75, 55, 65]  # Not a valid max heap
#                         0   1   2   3   4   5   6
print("Out-of-order heap:", out_of_order_heap.heap)

# Use heapify to convert it to a max heap -> [95, 75, 80, 60, 50, 55, 65]
out_of_order_heap.heapify()
print("Heap after heapify:", out_of_order_heap.heap)

# Perform heap sort
sorted_heap = out_of_order_heap.heap_sort()
print("Sorted elements:", sorted_heap)

# Line by line execution -> heapify()
# call heapify() on heap [50, 95, 80, 60, 75, 55, 65]
    # call sink_down on 80 or index 2 (last non leaf node)
        # check if ele's at child indexes 5 & 6 are larger than ele at idx 2 -> No, no swaps
    # call sink_down on 95 or index 1 (looping backwards)
        # check if ele's at child indexes 3 & 4 are larger than ele at idx 1 -> No, no swaps
    # call sink_down on 50 or index 0
        # check if ele's at child indexes 1 & 2 are larger than ele at index 0
            # both are, but ele at index 1 is the largest
            # swap elements at index 0 & 1 -> [95, 50, 80, 60, 75, 55, 65], set index to max_index (1)
        # keep sinking down the element we just swapped from index 0 (50) to index 1 -> check if ele's at child indexes 3 & 4 are larger than ele at index 1 (50)
            # both are, but ele at index 4 is the largest
            # swap elements at index 1 & 4 -> [95, 75, 80, 60, 50, 55, 65], set index to max_index (4)
        # check if ele's at child indexes 9 & 10 aare larger than ele at index 4
            # indexes OOB -> 9 & 10 (left and right indexes) > len(self.heap)



