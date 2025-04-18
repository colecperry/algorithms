# Prim's Algorithm - it's goal is to find a minimum spanning tree of connected, weighted, and undirected 
#                    graph. It finds a subset of edges that connects all vertitices, has no cycles, and has 
#                    the minimum total possible edge weight among all such trees.
# 
# High-Level Steps:
# 1. Start with an arbitrary node (the 'start' node) and initialize a priority queue with its edges.
# 2. While the priority queue is not empty:
#    a. Extract the edge with the smallest weight.
#    b. If the connected node has not been visited:
#        i. Mark it as visited.
#        ii. Add the edge to the Minimum Spanning Tree (MST).
#        iii. Add all of its outgoing edges to the priority queue (only to unvisited nodes).
# 3. Repeat until all nodes have been visited and the MST includes exactly (V - 1) edges.

# Time Complexity:
# - O(E log V), where E is the number of edges and V is the number of vertices.
# - Each edge insertion/extraction in the priority queue (heap) takes log V time, and we may process each edge once.

# Space Complexity:
# - O(V + E) for storing the graph, the visited set, the MST, and the priority queue.


import heapq

def prim(graph, start):
    """
    Implements Prim's algorithm to find the Minimum Spanning Tree (MST) of a graph.
    :param graph: Dictionary where keys are nodes and values are lists of tuples (neighbor, weight)
    :param start: The starting node
    :return: List of edges in the MST
    """
    priority_queue = [(0, start, None)]  # (weight, node, parent)
    visited = set()
    mst = [] # minimum spanning tree
    
    while priority_queue:
        weight, node, parent = heapq.heappop(priority_queue) # unpack tuple -> will always pop node with the smallest weight (heapq is a min heap in python)
        
        if node in visited: # if node already visited, skip loop
            continue
        
        visited.add(node) # add node to visited
        if parent is not None:
            mst.append((parent, node, weight)) # add tuple to MST
        
        for neighbor, edge_weight in graph[node]: # loop thru all neighbors
            if neighbor not in visited:
                heapq.heappush(priority_queue, (edge_weight, neighbor, node)) # push neighbor into priority queue
    
    return mst

# Example usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_node = 'A'
# shortest_paths = dijkstra(graph, start_node)
# print("Dijkstra's shortest paths:", shortest_paths)

mst = prim(graph, start_node)
print("Prim's MST:", mst)