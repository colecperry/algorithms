class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = set()

    def add_edge(self, source, target):
        self.add_vertex(source)
        self.add_vertex(target)
        self.graph[source].add(target) # Only add edge one direction

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]  # Remove the vertex itself
            for neighbors in self.graph.values():
                neighbors.discard(vertex)

    def remove_edge(self, source, target):
        if source in self.graph and target in self.graph[source]:
            self.graph[source].remove(target)

    def has_vertex(self, vertex):
        return vertex in self.graph

    def has_edge(self, source, target):
        return source in self.graph and target in self.graph[source]

    def get_neighbors(self, vertex):
        return self.graph.get(vertex, set())

    def display(self):
        for vertex, neighbors in self.graph.items():
            print(f"{vertex} -> {', '.join(map(str, neighbors))}")

# Example usage
graph = DirectedGraph()

# Add edges (this also adds the vertices)
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "D")
graph.add_edge("E", "F")

# Display initial graph
print("Initial graph:")
graph.display()

# Check if vertices exist
print("\nCheck vertices:")
print("Graph has vertex A?", graph.has_vertex("A"))   # True
print("Graph has vertex Z?", graph.has_vertex("Z"))   # False

# Check if edges exist
print("\nCheck edges:")
print("Edge A-B exists?", graph.has_edge("A", "B"))   # True
print("Edge A-D exists?", graph.has_edge("A", "D"))   # False

# Get neighbors
print("\nNeighbors of C:", graph.get_neighbors("C"))  # Should show A and D

# Remove an edge
print("\nRemoving edge between B and D...")
graph.remove_edge("B", "D")
graph.display()

# Remove a vertex
print("\nRemoving vertex C...")
graph.remove_vertex("C")
graph.display()

# Try adding a self-loop (should raise ValueError)
try:
    graph.add_edge("X", "X")
except ValueError as e:
    print("\nError:", e)