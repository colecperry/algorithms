# 973. K Closest Points to Origin

# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., sqrt(x1 - x2)^2 + (y1 - y2)^2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# Ex. 1

#                  y
#                  |
#                5-|
#                  |
#                4-|
#                  |
#                3-|  x
#                  |
#            x   2-|  
#                  |
#                1-|
#                  |
#   -------------0-|————————————————————> x
#  -5 -4 -3 -2 -1  0  1  2  3  4  5
#
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

# Example 2:
# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.

from typing import List
from math import sqrt
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = [] # Max heap of size k guarentees root is kth smallest 
        for x, y in points:
            distance = sqrt(((x - 0)**2) + (y - 0)**2)
            heapq.heappush(max_heap, (-distance, [x,y])) # max heap w/ dist & coords tuple
            if len(max_heap) > k: # only keep k ele's in max heap
                heapq.heappop(max_heap) # guarentees root is kth smallest
        res = []
        for dist, point in max_heap: # Create result array
            res.append(point)
        return res

sol = Solution()
print(sol.kClosest([[1,3],[-2,2]], 1)) # [[-2,2]]
print(sol.kClosest([[3,3],[5,-1],[-2,4]], 2)) # [[3,3],[-2,4]]