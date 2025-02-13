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
    
    def remove(self):
        if len(self.heap) == 0:
            return None  # Return None if heap is empty
        
        if len(self.heap) == 1:
            return self.heap.pop()  # If only one element, pop and return it
        
        max_value = self.heap[0]  # Extract the max value
        self.heap[0] = self.heap.pop()  # Move last element to root
        self.sink_down(0)  # Restore heap property by sinking down
        return max_value  # Return the removed max value
    
    def sink_down(self, index):
        max_index = index  # Start sinking from the given index
        while True:
            left_index = self.left_child(index)
            right_index = self.right_child(index)

            # Find the larger child
            if (left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]):
                max_index = left_index
            
            if (right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]):
                max_index = right_index
            
            # Swap and continue sinking if necessary
            if max_index != index:
                self.swap(index, max_index)
                index = max_index
            else:
                return  # Stop if the element is in the right place
    
    def heapify(self):
        # Heapify works by starting from the last non-leaf node and calling sink_down on each.
        # This ensures that each subtree is converted into a valid heap before moving upwards.
        # The process moves from bottom to top, ensuring the heap property is maintained efficiently.
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.sink_down(i)


# Create an out-of-order heap (not a valid max heap)
out_of_order_heap = MaxHeap()
out_of_order_heap.heap = [50, 95, 80, 60, 75, 55, 65]  # Not a valid max heap
print("Out-of-order heap:", out_of_order_heap.heap)

# Fix the heap using heapify
out_of_order_heap.heapify()
print("Heap after heapify:", out_of_order_heap.heap)

# Perform standard heap operations
out_of_order_heap.remove()
print("Heap after removal:", out_of_order_heap.heap)