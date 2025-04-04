import heapq

def dijkstra(graph, start):
    """
    Implements Dijkstra's algorithm to find the shortest path from the start node to all other nodes in the graph.
    :param graph: Dictionary where keys are nodes and values are lists of tuples (neighbor, weight)
    :param start: The starting node
    :return: Dictionary of shortest distances from start to each node
    """
    priority_queue = [(0, start)]  # (distance, node)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Example usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print(shortest_paths)
