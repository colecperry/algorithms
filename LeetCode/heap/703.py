# 703. Kth Largest Element in a Stream

# Topics: Tree, Design, Binary Search Tree, Heap (Priority Queue), Binary Tree, Data Stream

# You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

# You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth highest score in the sorted list of all scores.

# Implement the KthLargest class:

# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
# int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool of test scores so far.

# Example 1:
# Input:
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

# Output: [null, 4, 5, 5, 8, 8]

# Explanation:

# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3); // return 4
# kthLargest.add(5); // return 5
# kthLargest.add(10); // return 5 !!!
# kthLargest.add(9); // return 8
# kthLargest.add(4); // return 8

# Example 2:
# Input:
# ["KthLargest", "add", "add", "add", "add"]
# [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]

# Output: [null, 7, 7, 7, 8]

# Explanation:

# KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);
# kthLargest.add(2); // return 7
# kthLargest.add(10); // return 7
# kthLargest.add(9); // return 7
# kthLargest.add(9); // return 8

# How to solve: Brute Force
# in the add function, we add the new value to the array, sort the array, and then return ele at nums[k-1]

# How to solve Optimal: Min Heap of size k:
    # Big Idea : We start out with an array of size N, and we turn it into a min heap. If we keep popping off the smallest element until we reach a heap of size k, the root element will be the kth largest element. We start with a min heap from the input array by using heapify, and we keep popping off the root until we reach an array of size k.
    # Each time we add an element, push it onto the heap, and then pop off the min element to maintain a heap of size k (only once we have our heap has k elements)
    # Time complexity: Popping and pushing into the heap: O(log n), getting min val O(1)

import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.min_heap = nums # Create min heap
        heapq.heapify(self.min_heap) # Heapify the heap
        while len(self.min_heap) > k: # Create a min heap of size k
            heapq.heappop(self.min_heap) # Pop off all smallest elements until len of heap = k & then root element will be the third largest
        
    def add(self, val):
        heapq.heappush(self.min_heap, val) # Push the new val onto the heap
        if len(self.min_heap) > self.k: # Only pop if we have more than k elements in the heap
            heapq.heappop(self.min_heap) # Pop off the min ele
        return self.min_heap[0] # Will return third largest


obj = KthLargest(3, [4, 5, 8, 2])
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))