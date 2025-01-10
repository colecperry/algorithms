from collections import defaultdict
import heapq

# There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

# Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

# Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

# Example 1: 
# Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
# Output: 3
# Explanation: The figure above describes the graph. 
# The neighboring cities at a distanceThreshold = 4 for each city are:
# City 0 -> [City 1, City 2] 
# City 1 -> [City 0, City 2, City 3] 
# City 2 -> [City 0, City 1, City 3] 
# City 3 -> [City 1, City 2] 
# Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.

# Example 2:
# Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
# Output: 0
# Explanation: The figure above describes the graph. 
# The neighboring cities at a distanceThreshold = 2 for each city are:
# City 0 -> [City 1] 
# City 1 -> [City 0, City 4] 
# City 2 -> [City 3, City 4] 
# City 3 -> [City 2, City 4]
# City 4 -> [City 1, City 2, City 3] 
# The city 0 has 1 neighboring city at a distanceThreshold = 2.

# How to Solve
# Find the city that can reach the fewest number of cities with the sum of the edges of each path of travel less than the distanceThreshold. If there are two cities that have the same number of cities they can reach, return the one with the larger value (if both city 1 and city 3 can reach two cities, return city 3 because 3 > 1)
# Use Dykstra's Algorithm to find the shortest path from each node to all nodes we can reach, count these nodes and return them

# Time Complexity:
# Use a min heap -> greedy algorithm
# Pushing and popping from the heap is log(n)
# To run a dykstra's, each node could be added to the heap n^2 times b/c that is the number of edges in the graph
# Total time complexity -> n^3log(n)

# Code explained
# adj = defaultdict(list) -> Convert edges list into an adjancency list using a default dictionary where the default value is a list b/c for every node we want to map it to a list of it's neighbors


class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        adj = defaultdict(list) # Convert list of edges into an adjancency list
        for v1, v2, dist in edges: # Loop through each value in each edge
            adj[v1].append((v2, dist)) # Add a tuple of neighbors
            adj[v2].append((v1, dist))
        
        def dijkstra(src):
            heap = [(0, src)]
            visit = set()

            while heap:
                dist, node = heapq.heappop(heap)
                if node in visit:
                    continue
                visit.add(node)
                for nei, dist2 in adj[node]:
                    nei_dist = dist + dist2
                    if nei_dist <= distanceThreshold:
                        if nei_dist <= distanceThreshold:
                            heapq.heappush(heap, (nei_dist, nei))
            return len(visit) - 1


        res, min_count = -1, n
        for src in range(n):
            count = dijkstra(src)
            if count <= min_count:
                res, min_count = src, count
        return res

# Example 1
n1 = 4
edges1 = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
distanceThreshold1 = 4

solution = Solution()
print("Example 1 Output:", solution.findTheCity(n1, edges1, distanceThreshold1))

# Example 2
n2 = 5
edges2 = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
distanceThreshold2 = 2

print("Example 2 Output:", solution.findTheCity(n2, edges2, distanceThreshold2))