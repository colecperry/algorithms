# 2685. Count the Number of Complete Components

# Topics: Depth-First Search, Breadth-First Search, Union Find, Graph

# You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

# Return the number of complete connected components of the graph.

# A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

# A connected component is said to be complete if there exists an edge between every pair of its vertices.

# Example 1:

#     5        0 ----- 1       3
#               \     /        |
#                \   /         |
#                 \ /          4
#                  2

# Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
# Output: 3
# Explanation: From the picture above, one can see that all of the components of this graph are complete.

# Example 2:

#            0 ----- 1       5 ------ 3
#             \     /                /
#              \   /                /
#               \ /                /
#                2                4

# Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
# Output: 1
# Explanation: The component containing vertices 0, 1, and 2 is complete since there is an edge between every pair of two vertices. On the other hand, the component containing vertices 3, 4, and 5 is not complete since there is no edge between vertices 4 and 5. Thus, the number of complete components in this graph is 1.

# How to Solve: 
# - Use BFS to explore each connected component of the graph.
# - For each component:
#     - Track the number of nodes and the number of edges.
#     - A component with k nodes is complete if it has exactly (k * (k - 1)) -> each node needs to connect to (k - 1) other nodes, and you multiply by k to count every edge twice (undirected), and divide by 2 to get the expected edges -> basically in the algo we count the edges both ways for each node in the connected component, and then divide that by two and compare to the expected edges calculation
# - Count how many components meet this condition.

# Implementation Details:
# 1. Build an adjacency list from the input edges using defaultdict(list) for convenience.
# 2. Use a `visited` set to track which nodes have been seen already, so we don’t revisit them.
# 3. For every unvisited node from 0 to n-1:
#     - Start a BFS from that node to find all nodes in its connected component.
#     - As we traverse, count:
#         a. The number of nodes in the component.
#         b. The total number of incident edges (i.e., sum of degrees).
# 4. Once the component is fully traversed:
#     - Compute the expected number of undirected edges for a complete graph of size k: (k * (k - 1)) // 2.
#     - Since we counted each undirected edge twice (once from each node), divide `edge_count` by 2.
#     - If actual == expected, increment the count of complete components.
# 5. Return the total number of complete components found.


from typing import List
from collections import defaultdict, deque

class Solution: # BFS
    def countCompleteComponentsBFS(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list) # adj list for the whole graph
        visited = set() # visited set for the whole graph
        num_components = 0 # number of fully connected components

        # Build the undirected adjacency list
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Loop over all nodes (to catch disconnected components too)
        for node in range(n):
            if node in visited:
                continue

            queue = deque([node]) # BFS traversal queue
            visited.add(node)
            nodes_in_component = {node} # set of nodes in curr component (no dups)
            edge_count = 0  # count of edges in current component

            while queue:
                current = queue.popleft()
                edge_count += len(adj[current]) # update edge count
                for neighbor in adj[current]: # loop thru neighbors
                    if neighbor not in visited: # if not visited
                        visited.add(neighbor) # add neighbor to visited set
                        nodes_in_component.add(neighbor) # update num of nodes in current component
                        queue.append(neighbor) # add the neighbor to be explored 
            
            # computing the number of expected edges based on the number of nodes in the component ((k - 1) edges per node, times k nodes, // 2 for double counting undirected edges))
            k = len(nodes_in_component)
            expected_edges = k * (k - 1) // 2 

            # Each undirected edge was counted twice in edge_count
            if edge_count // 2 == expected_edges:
                num_components += 1

        return num_components
    
    def countCompleteComponentsDFS(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = defaultdict(list)
        num_components = 0

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        if len(adj) != n:
            diff =  n - len(adj)
            num_components += diff

        def dfs(v):
            stack = deque([v])
            component = set([v])
            while stack:
                v = stack.pop()
                for u in adj[v]:
                    if u not in visited:
                        visited.add(u)
                        stack.append(u)
                        component.add(u)
            return component
        
        for key in adj.keys():
            if key not in visited:
                visited.add(key)
                component = dfs(key)
                complete_nodes = 0
                for v in component:
                    if len(adj[v]) != len(component) - 1:
                        break
                    complete_nodes += 1   
                if complete_nodes == len(component):
                    num_components += 1
                    
        return num_components



sol = Solution()
print(sol.countCompleteComponentsBFS(6, [[0,1],[0,2],[1,2],[3,4]])) # 3
print(sol.countCompleteComponents(6, [[0,1],[0,2],[1,2],[3,4],[3,5]])) # 1