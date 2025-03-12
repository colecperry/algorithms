# 1046. Last Stone Weight

# Topics: Array, Heap (Priority Queue)

# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the weight of the last remaining stone. If there are no stones left, return 0.

# Example 1:
# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

# Example 2:
# Input: stones = [1]
# Output: 1

# How to Solve - Big Picture (Max Heap) -> B/c we are taking the max stones each iteration
    # O(n) -> transform this array into a heap using heapify
    # Get the max element from the heap -> log (n) * n times
    # Python does not have a max heap function, so we need to simulate a max heap using a min heap by multiplying every value in the heap by negative 1
    # Ex.     Max Heap               Min Heap
    #            8                      -8
    #           / \                     / \
    #          3   5                  -3  -5

# How to Solve (Code)
    # Since we want to find the two heaviest stones on each iteration, we can use a max heap, but since python does not have a max heap, we use a min heap with negative numbers -> using a list comprehension transform the array into the same array but with negative nums
    # Turn the array into a valid min heap by importing heapq and using heapq.heapify on the arr
    # Loop through the heap until we have 1 or 0 stones
        # Pop the root ele (largest ele), and pop the largest ele again, assign to first and second variables (largest stone and second largest stone)
        # If statement: Since we're using a min heap with negative nums, so if first stone popped = 8, and second stone = 7, it is really first = -8, and second = -7, so we need to reverse our logic
        # If true, push the new node into the heap accounting for the negative number min heap, so first-second = -8 - -7 = -1
    # Return the value of the last remaining stone, if the arr is empty (no stones left), return 0

"""
    Time Complexity: 
    - Converting the list to a max heap (using min heap with negation): O(n)
    - Each pop operation from the heap takes O(log n)
    - Since we perform at most (n - 1) collisions, the worst case is O(n log n)

    Overall Time Complexity: O(n log n)

    Space Complexity: 
    - The heap stores n elements in the worst case.
    - We modify the list in place, so additional space is O(1).

    Overall Space Complexity: O(n)
    """


import heapq

def lastStoneWeight(stones):
    stones = [-s for s in stones] # Multiply every num in the arr by -1 -> converts to max heap
    heapq.heapify(stones) # Turn the arr into a max heap using a min heap

    while len(stones) > 1: # Continue until 1 stone or 0 stones
        first = heapq.heappop(stones) # Get largest stone
        second = heapq.heappop(stones) # Get second largest stone
        # We popped 1st and 2nd ele's off the heap, so if they are equal no further action needed
        if second > first: # If second stone is greater than first stone -> remember negatives & reverse logic
            heapq.heappush(stones, first - second) # Push a new ele into the heap with the diff

    
    return abs(stones[0]) if stones else 0 # Return value of the stone at negative zero -> account for neg values, if stones arr is empty, return 0



print(lastStoneWeight([2,7,4,1,8,1]))
print(lastStoneWeight([1]))