# INSERT -> Insert the value into the next open space so the tree remains complete
# Compare the inserted value to it's parent, if it is larger, swap them
# Continue this process until the node is smaller than it's parent node

# Big 0 of insert: O(log n): Logarithmic Time Complexity: Reduces the problem size in each step by a constant fraction
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

    # Insert a node at the end of the list and bubble the node up to satisfy the heap property
    def insert(self, value):
        self.heap.append(value) # Append value to the end of the list
        current = len(self.heap) - 1 # Create a pointer starting at the last index

        while current > 0 and self.heap[current] > self.heap[self.parent(current)]: # Create a while loop that runs as long as current index > 0 and the value at current is greater than the value of it's parent element
            self.swap(current, self.parent(current)) # Swap the current node with the parent node
            current = self.parent(current) # Move current pointer to the parent node

# Create the heap
myheap = MaxHeap()
myheap.insert(99)
myheap.insert(72)
myheap.insert(61)
myheap.insert(58)

print(myheap.heap)

# Bubble up 100 via insert
myheap.insert(100)
print(myheap.heap)

# Bubble up 75 via insert
myheap.insert(75)
print(myheap.heap)

