

import heapq

class Dijkstra:
    def __init__(self, graph, source):
        self.graph = graph  # Graph represented as adjacency list (dict of lists)
        self.source = source
        self.distances = {}
        self.predecessors = {}
        self.priority_queue = []

    # Helper method for single-source initialization
    def single_source_initialization(self):
        # Set all distances to infinity initially
        for vertex in self.graph:
            self.distances[vertex] = float('inf')
            self.predecessors[vertex] = None
        # The distance to the source is 0
        self.distances[self.source] = 0

    # Helper method for relaxing an edge
    def relax(self, u, v, weight):
        # If the distance to vertex v can be shortened via u, update the distance
        if self.distances[u] + weight < self.distances[v]:
            self.distances[v] = self.distances[u] + weight
            self.predecessors[v] = u
            # Push the updated vertex into the priority queue
            heapq.heappush(self.priority_queue, (self.distances[v], v))

    # Main method to run Dijkstra's algorithm
    def dijkstra(self):
        self.single_source_initialization()  # Step 1: Initialize distances and predecessors
        # Initialize the priority queue with the source vertex
        heapq.heappush(self.priority_queue, (0, self.source))
        
        while self.priority_queue:
            # Extract the vertex with the smallest distance from the priority queue
            current_distance, u = heapq.heappop(self.priority_queue)
            
            # If the distance is already greater than the current known distance, skip
            if current_distance > self.distances[u]:
                continue

            # Relax all edges from vertex u
            if u in self.graph:
                for v, weight in self.graph[u]:
                    self.relax(u, v, weight)

        return self.distances, self.predecessors


# Example usage
graph = {
    0: [(1, 5), (2, 3)],
    1: [(2, 2), (3, 6)],
    2: [(3, 7)],
    3: []
}

source = 0
dijkstra = Dijkstra(graph, source)
distances, predecessors = dijkstra.dijkstra()

print("Shortest distances from source:", distances)
print("Predecessors:", predecessors)
