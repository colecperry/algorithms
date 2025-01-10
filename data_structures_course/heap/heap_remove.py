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
        if len(self.heap) == 0: # Edge case for when the heap is empty
            return None
        
        if len(self.heap) == 1: # Edge c ase for when heap is only 1 element
            return self.heap.pop() # Pop the element off the list and return it
        
        max_value = self.heap[0] # set max_value equal to the element initially at index 0
        self.heap[0] = self.heap.pop() # set the element at index 0 equal to the popped element (which comes from the last index)
        self.sink_down(0) # Call helper method to put element into correct position
        return max_value # Return the value we initially had at index 0
    
    def sink_down(self, index):
        max_index = index # Create variable max_index to start our loop
        while True: # Create an infinite loop
            left_index = self.left_child(index) # Get the index of the left and right children
            right_index = self.right_child(index)

            if (left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]): 
                # Make sure left index has an element (tree can be complete with no children on parent node)
                # & compare val at left_child to max_index
                max_index = left_index # If true move max index to left index
            
            if (right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]): 
            # Make sure right index has an element(tree can be complete without a final right child)
            # & compare the val at right child to max_index
                max_index = right_index # If true move max index to right index
            
            # This code helps stop the code if the element is in the correct spot (if the two pointers are equal, we don't run the code)
            if max_index != index: # If max_index is not equal to index
                self.swap(index, max_index) # Swap index and max_index
                index = max_index # Move index down to max_index
            else: # If they are equal, stop the code
                return


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