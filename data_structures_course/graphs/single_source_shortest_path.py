class DAGShortestPath:
    def __init__(self, graph, source):
        self.graph = graph  # Graph represented as adjacency list (dict of lists)
        self.source = source
        self.distances = {}
        self.predecessors = {}

    # Helper method for topological sorting
    def topological_sort(self):
        visited = set()
        stack = []
        
        def dfs(v):
            visited.add(v)
            if v in self.graph:
                for neighbor, _ in self.graph[v]:
                    if neighbor not in visited:
                        dfs(neighbor)
            stack.append(v)
        
        for vertex in self.graph:
            if vertex not in visited:
                dfs(vertex)
        
        return stack[::-1]  # Reverse the stack to get the topological order

    # Helper method for relaxing edges
    def relaxation(self):
        for vertex in self.topological_order:
            for neighbor, weight in self.graph.get(vertex, []):
                if self.distances[vertex] + weight < self.distances[neighbor]:
                    self.distances[neighbor] = self.distances[vertex] + weight
                    self.predecessors[neighbor] = vertex

    # Main method to compute the shortest path
    def dag_shortest_path(self):
        # Step 1: Perform topological sort
        self.topological_order = self.topological_sort()

        # Step 2: Initialize distances and predecessors
        for vertex in self.graph:
            self.distances[vertex] = float('inf')  # Set all distances to infinity initially
            self.predecessors[vertex] = None  # No predecessors initially
        self.distances[self.source] = 0  # The distance to the source is 0

        # Step 3: Relax all edges in topological order
        self.relaxation()

        return self.distances, self.predecessors


# Example usage
graph = {
    0: [(1, 5), (2, 3)],
    1: [(2, 2), (3, 6)],
    2: [(3, 7)],
    3: []
}

source = 0
dag_sp = DAGShortestPath(graph, source)
distances, predecessors = dag_sp.dag_shortest_path()

print("Shortest distances from source:", distances)
print("Predecessors:", predecessors)