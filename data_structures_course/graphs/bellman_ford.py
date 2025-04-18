# Goal of the Algorithm:
# -  The Bellman-Ford algorithm finds the shortest path from a single source to all other vertices in a weighted graph.
# -  Unlike Dijkstra's algorithm, it works with graphs that have negative edge weights and can detect negative weight cycles.

# High-Level Steps:
# 1. Initialize distances from the source to all nodes as 
#    infinity, except the source itself (set to 0).
# 2. Repeat |V| - 1 times: In the worst case, the shortest path #    from the source to a vertex could involve |V| - 1 edges.
#    Example: In a graph of 5 nodes, the longest simple path 
#    (no cycles) could go through 4 edges. By relaxing every 
#    edge |V| - 1 times, we ensure that even the longest path 
#    has a chance to update correctly.

#    - Next, go through every vertex node, and every edge of 
#    that node and relax it (update distance if a shorter path #    is found).

# 3. Check for negative weight cycles by seeing if any edge can #    still be relaxed.
#    - If yes, report that a negative cycle exists. This means #    that there is a cycle that keeps getting cheaper infinitely

# Time Complexity:
#   - O(V * E), where V is the number of vertices and E is the #   number of edges.

# Space Complexity:
#   - O(V) for storing distances and predecessors.

class BellmanFord:
    def __init__(self, graph, source):
        self.graph = graph  # Graph is a dictionary where keys are vertices and values are lists of edges (tuples of target and weight)
        self.source = source # Source node
        self.distances = {} # Shortest distance from src node to other nodes
        self.predecessors = {} # Predecessor for each node's shortest path 

    # Method for initializing single-source distances
    def single_source_initialization(self):
        for vertex in self.graph:
            self.distances[vertex] = float('inf')  # Set all distances to infinity
            self.predecessors[vertex] = None  # No predecessors initially
        self.distances[self.source] = 0  # Distance to the source is 0

    # relaxation -> see if we can improve the shortest path 
    def relaxation(self):
        for vertex in self.graph: # loop through each vertex as src
            for neighbor, weight in self.graph[vertex]: # loop through each neighbor
                if self.distances[vertex] + weight < self.distances[neighbor]: # if the shortest dist starting from the vertex node plus the new weight is smaller than the current shortest dist to that neighbor
                    self.distances[neighbor] = self.distances[vertex] + weight # Shorter distance found
                    self.predecessors[neighbor] = vertex # update node's predecessor

    # Bellman-Ford algorithm
    def bellman_ford(self):
        self.single_source_initialization()  # Step 1: Initialize the distances
        for _ in range(len(self.graph) - 1):  # Step 2: Relax all edges |V| - 1 times
            self.relaxation()

        # Step 3: Check for negative-weight cycles
        for vertex in self.graph:
            for neighbor, weight in self.graph[vertex]:
                if self.distances[vertex] + weight < self.distances[neighbor]:
                    print("Graph contains negative weight cycle")
                    return None

        return self.distances, self.predecessors


# Example usage
graph = {
    0: [(1, -1), (2, 4)],
    1: [(2, 3), (3, 2), (4, 2)],
    2: [(3, 5)],
    3: [(1, 1), (2, 5)],
    4: [(3, -3)],
}

source = 0
bf = BellmanFord(graph, source)
distances, predecessors = bf.bellman_ford()

if distances:
    print("Shortest distances from source:", distances)
    print("Predecessors:", predecessors)