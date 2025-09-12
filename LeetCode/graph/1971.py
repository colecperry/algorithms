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
#
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

# How to solve: (BFS)
    # - Build an adjacency list from the edge list.
    # - Use Breadth-First Search (BFS) starting from the source node.
    # - Use a queue to explore each node's neighbors.
    # - Track visited nodes to avoid cycles and redundant work.
    # - If we reach the destination during traversal, return True.
    # - If traversal finishes and destination wasn't found, return False.

    # Time Complexity: O(n + e)
    # - n = number of nodes
    # - e = number of edges
    # - We visit each node and edge once in BFS.

    # Space Complexity: O(n + e)
    # - Adjacency list uses O(n + e) space.
    # - Visited list and queue each use O(n) space.

from typing import List
from collections import defaultdict, deque

class Solution: # BFS Solution
    def validPathBFS(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Step 1: Build the adjacency list for the graph
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)  # Add b as a neighbor of a
            graph[b].append(a)  # Add a as a neighbor of b (undirected graph)
        
        # Step 2: Initialize visited array to track visited nodes
        seen = [False] * n
        seen[source] = True  # Mark the source node as visited
        
        # Step 3: Initialize a queue for BFS and start with the source node
        queue = deque([source])

        # Step 4: Perform BFS
        while queue:
            current = queue.popleft()

            # If we reach the destination node, return True
            if current == destination:
                return True

            # Explore all unvisited neighbors
            for neighbor in graph[current]: # Find curr nodes neighbors using adj list
                if not seen[neighbor]: # If that neighbor has not been seen
                    seen[neighbor] = True # Mark true in visited array
                    queue.append(neighbor) # Append neighbor to queue

        # If BFS completes without finding destination, return False
        return False
    
    # How to solve: (DFS)
        # - Build an adjacency list from the given edge list.
        # - Use Depth-First Search (DFS) starting from the source node.
        # - Recursively visit each unvisited neighbor.
        # - Track visited nodes using a seen[] list to avoid infinite loops.
        # - If we reach the destination during any recursive call, return True.
        # - If all paths are explored and destination isn't reached, return False.

        # Time Complexity: O(n + e)
        # - n = number of nodes
        # - e = number of edges
        # - Each node and edge is visited once in DFS.

        # Space Complexity: O(n + e)
        # - O(n + e) for the adjacency list
        # - O(n) for the seen[] list
        # - O(n) worst-case recursion stack depth


    def validPathDFS(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Step 1: Build the adjacency list from the edge list
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)  # Add b as a neighbor of a
            graph[b].append(a)  # Add a as a neighbor of b (undirected)

        # Step 2: Track visited nodes to avoid cycles
        seen = [False] * n

        # Step 3: Define the DFS function
        def dfs(curr_node):
            # Base case: if we reach the destination, return True
            if curr_node == destination:
                return True

            # Mark the current node as visited
            seen[curr_node] = True

            # Recursively visit all unvisited neighbors
            for neighbor in graph[curr_node]:
                if not seen[neighbor]:
                    if dfs(neighbor):  # If a valid path is found through recursion
                        return True

            # If no path is found from this node
            return False

        # Step 4: Start DFS from the source node
        return dfs(source)
    
    # How to solve: (DFS Iterative)
        # - Convert the edge list into an adjacency list to represent the graph.
        # - Use an iterative Depth-First Search (DFS) with a stack (LIFO order).
        # - Start from the source node and mark it as visited.
        # - At each step, pop a node from the stack and explore all its unvisited neighbors.
        # - If you encounter the destination during traversal, return True.
        # - After traversal, return whether the destination node was visited.

        # Time Complexity: O(n + e)
        # - n = number of nodes
        # - e = number of edges
        # - Each node and edge is visited once in DFS.

        # Space Complexity: O(n + e)
        # - O(n + e) for the adjacency list
        # - O(n) for the seen[] list
        # - O(n) worst-case for the stack

    
    def validPathIterative(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Step 1: Build the adjacency list representation of the graph
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)  # a is connected to b
            graph[b].append(a)  # b is connected to a (undirected graph)
        
        # Step 2: Initialize visited array to avoid revisiting nodes
        seen = [False] * n
        seen[source] = True  # mark the source as visited

        # Step 3: Use a stack for iterative DFS (LIFO)
        stack = [source]

        # Step 4: Iterative DFS loop
        while stack:
            curr_node = stack.pop()

            # Explore all neighbors of the current node
            for neighbor in graph[curr_node]:
                # If we reach the destination node, return True
                if neighbor == destination:
                    return True

                # If the neighbor hasn't been visited, add it to the stack
                if not seen[neighbor]:
                    seen[neighbor] = True
                    stack.append(neighbor)

        # Step 5: After the loop, check if destination was visited
        return seen[destination]



sol = Solution()
print(sol.validPathBFS(3, [[0,1],[1,2],[2,0]], 0, 2))
print(sol.validPathBFS(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))