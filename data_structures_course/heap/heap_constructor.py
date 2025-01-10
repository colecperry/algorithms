# Similar to a BST - it is a Binary Tree
# Each node has a number than is higher than all of it's descendants
# The order only applies to descendants -> for example, this is a valid heap:
#             99
#            /   \
#           /     \
#          72     58
#         / \     / \
#        /   \   /   \
#       61   55 27   18

# A Heap is a complete tree -> filled from left to right with no gaps
# Heaps can have duplicates
# Heaps are not good for searching -> Heaps are only good for being able to track the largest or smallest value at the top and quickly remove it
# Max heap - highest value at the top
# Min heap - lowest value at the top

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


