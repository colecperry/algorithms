# 547. Number of Provinces

# Topics: Depth-First Search, Breadth-First Search, Union Find, Graph

# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

# Ex. 1 
#          1 ------ 2
#
#              3
#
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2

# Ex. 2
#         
#         1       2
#
#             3
#
# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3

# How to Solve (DFS):
    # Initialize visited list to track which cities have been visited
    # Initialize a counter to count the number of provinces (connected components)

    # Define a helper DFS function to explore all cities connected to the current city
    # If a city is connected (value is 1) and hasn't been visited, keep exploring recursively

    # Loop through each city:
    #   - If it's not visited, start a new DFS traversal and increment the province count
    #   - This traversal will mark all cities connected to this city as visited

    # Time Complexity: O(n^2)
    #   - We may potentially explore every pair of cities and neighbors
    # Space Complexity: O(n)
    #   - Visited list + recursion stack in the worst case

from typing import List
from collections import deque

class Solution:
    def findCircleNumDFS(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            visited[city] = True # mark the city as visited
            for neighbor in range(len(isConnected)): # loop through each neighbor
                if isConnected[city][neighbor] == 1 and not visited[neighbor]: # if we find a new path that is unvisited
                    dfs(neighbor) # Keep exploring the path 

        n = len(isConnected)
        visited = [False] * n # Track visited cities
        provinces = 0 # Track number of provinces (number of components)

        for city in range(n): # Loop through each city
            if not visited[city]: # If the city is not yet visited
                provinces += 1 # Increment the number of provinces
                dfs(city) # explore the city

        return provinces
    
# How to Solve (BFS):
    # Similar to DFS, but we use a queue to explore neighbors level by level

    # For each unvisited city:
    #   - Create a visited list to track visited nodes
    #   - Loop through each city, and if that city is unvisited, create a BFS queue for that city to explore it's neighbors
    #   - While the queue is not empty:
    #       - Pop a city from the queue
    #       - Mark it as visited
    #       - Enqueue all unvisited neighbors connected to this city (value is 1) and that have not been visited
    #   - After the queue is empty, we've finished exploring a province -> Increment the province count

    # Time Complexity: O(n^2)
    #   - Still checking each possible connection between cities
    # Space Complexity: O(n)
    #   - Visited list + queue space in worst case
    
    def findCircleNumBFS(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n # Track visited nodes
        provinces = 0

        for city in range(n): # Loop through each city (inner list)
            if not visited[city]: # We found new disconnected component -> perform BFS
                queue = deque([city]) # Create queue for each component (connected part of the graph)
                while queue:
                    current = queue.popleft() # Pop off the city
                    visited[current] = True # Mark as visited
                    for neighbor in range(n): # Loop thru neighbors of that city
                        if isConnected[current][neighbor] == 1 and not visited[neighbor]: # If the current city is connected to a neighbor and the neighbor hasn't been visited
                            queue.append(neighbor) # Add unvisited connected neighbor to the BFS queue to be explored
                provinces += 1 # Increment provinces by one at the end of the path

        return provinces


sol = Solution()
print(sol.findCircleNumBFS([[1,1,0],[1,1,0],[0,0,1]]))
print(sol.findCircleNumBFS([[1,0,0],[0,1,0],[0,0,1]]))