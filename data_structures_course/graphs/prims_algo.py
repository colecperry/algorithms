def prim(graph, start):
    """
    Implements Prim's algorithm to find the Minimum Spanning Tree (MST) of a graph.
    :param graph: Dictionary where keys are nodes and values are lists of tuples (neighbor, weight)
    :param start: The starting node
    :return: List of edges in the MST
    """
    priority_queue = [(0, start, None)]  # (weight, node, parent)
    visited = set()
    mst = []
    
    while priority_queue:
        weight, node, parent = heapq.heappop(priority_queue)
        
        if node in visited:
            continue
        
        visited.add(node)
        if parent is not None:
            mst.append((parent, node, weight))
        
        for neighbor, edge_weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (edge_weight, neighbor, node))
    
    return mst

# Example usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print("Dijkstra's shortest paths:", shortest_paths)

mst = prim(graph, start_node)
print("Prim's MST:", mst)