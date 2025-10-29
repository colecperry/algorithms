# Remove - we only ever remove the item at the top 
# Doesn't matter if we have a min heap or max heap
# Once we remove the top element we no longer have a valid heap, so we have to rearrange it
# Step 1: Make the tree complete
# We can do this in one step by moving the last item in the list to the first item in the list
# Now we do the reverse of what we did with insert -> sink the element down by comparing it to it's children and swap if necessary until the element is in the right position

# Big 0 of remove: O(log n): Logarithmic Time Complexity: Reduces the problem size in each step by a constant fraction
# Sinking down the element by the height of the tree is Log N

class MaxHeap:
    def __init__(self):
        self.heap = [] # We store the heap using a list
    
    def left_child(self, index): # Helper method gives us the left child of the idx we pass in
        return 2 * index + 1

    def right_child(self, index): # Helper method gives us the left child of the idx we pass in
        return 2 * index + 2
    
    def parent(self, index): # Helper method gives us the parent index of a child 
        return (index - 1) // 2
    
    def swap(self, index1, index2): # Helper method swaps the two elements we pass in
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value) # Append value to the end of the list
        current = len(self.heap) - 1 # Create a pointer starting at the last index

        while current > 0 and self.heap[current] > self.heap[self.parent(current)]: # Create a while loop that runs as long as current index > 0 and the value at current is greater than the value at the parent element
            self.swap(current, self.parent(current)) # Swap the current node with the parent node
            current = self.parent(current) # Move current pointer to the parent node
    
def remove(self):
    """Remove and return the root (max element in max-heap)"""
    if len(self.heap) == 0: 
        return None  # Empty heap - nothing to remove
    
    if len(self.heap) == 1: 
        return self.heap.pop()  # Only one element - just pop and return it
    
    # Step 1: Save the root value (what we're actually removing and will return)
    max_value = self.heap[0]
    
    # Step 2: Move the LAST element to the ROOT position (index 0)
    # This temporarily breaks the heap property but is O(1)
    self.heap[0] = self.heap.pop()
    
    # Step 3: Restore heap property by sinking the new root down
    self.sink_down(0)
    
    # Step 4: Return the original root (the max value we removed)
    return max_value

def sink_down(self, index):
    """
    Restore heap property by moving element at 'index' down the tree.
    Compares with children and swaps with larger child until heap property restored.
    """
    max_index = index  # Track the index of the largest value among parent and children
    
    while True:
        left_index = self.left_child(index)
        right_index = self.right_child(index)

        # Check if left child exists AND is larger than current max
        if (left_index < len(self.heap) and 
            self.heap[left_index] > self.heap[max_index]): 
            max_index = left_index  # Left child is larger
        
        # Check if right child exists AND is larger than current max
        if (right_index < len(self.heap) and 
            self.heap[right_index] > self.heap[max_index]): 
            max_index = right_index  # Right child is larger
        
        # If max_index changed, we found a larger child - swap and continue
        if max_index != index:
            self.swap(index, max_index)  # Swap parent with larger child
            index = max_index  # Move down to child's position and check again
        else:
            # max_index == index means element is in correct position
            return  # Heap property restored - done!


myheap = MaxHeap()
myheap.insert(95)
myheap.insert(75)
myheap.insert(80)
myheap.insert(55)
myheap.insert(60)
myheap.insert(50)
myheap.insert(65)

print(myheap.heap)

myheap.remove()
print(myheap.heap)

myheap.remove()
print(myheap.heap)