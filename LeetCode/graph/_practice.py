# 1971. Find if Path Exists in Graph

# Topics: DFS, BFS, Union Find, Graph

# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

# You want to determine if there is a valid path that exists from vertex source to vertex destination.

# Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

# Example 1:
#                0 ---- 1
#                 \    /
#                  \  /
#                   2 

# Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
# Output: true
# Explanation: There are two paths from vertex 0 to vertex 2:
# - 0 → 1 → 2
# - 0 → 2

# Example 2:
#                  3
#         1       | \
#        /        |  \
#       0         |   \
#        \        4 -- 5
#         2

# Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
# Output: false
# Explanation: There is no path from vertex 0 to vertex 5.

from typing import List
from collections import defaultdict, deque

class Solution: # BFS Solution
    def validPathBFS(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Build adj list
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        # Initalize visited set to protect against infinite loops, add the first node
        visited = set(source)

        # Initialize BFS queue with source node
        queue = deque([source])
        # Pop off curr node, check if it's the destination
        while queue:
            curr_dest = queue.popleft()
            if curr_dest == destination:
                return True
            # Add curr node's neighbors to the queue to visit if not already visited
            for neighbor in adj_list[curr_dest]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False
    
sol = Solution()
print(sol.validPathBFS(3, [[0,1],[1,2],[2,0]], 0, 2)) # True
print(sol.validPathBFS(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5)) # False