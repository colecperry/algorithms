class UndirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = set() # Set vertex to empty set (edges)

    def add_edge(self, vertex1, vertex2):
        if vertex1 == vertex2:
            raise ValueError("Self-loops are not allowed in an undirected graph.")
        self.add_vertex(vertex1) # Add both vertexes
        self.add_vertex(vertex2)
        self.graph[vertex1].add(vertex2) # Add both edges
        self.graph[vertex2].add(vertex1)

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            for neighbor in list(self.graph[vertex]):
                self.graph[neighbor].remove(vertex)
            del self.graph[vertex]

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
            self.graph[vertex1].remove(vertex2)
            self.graph[vertex2].remove(vertex1)

    def has_vertex(self, vertex):
        return vertex in self.graph

    def has_edge(self, vertex1, vertex2):
        return vertex1 in self.graph and vertex2 in self.graph[vertex1] # Check if the vertex is in the list as a key and other vertex (edge) is a value for the key

    def get_neighbors(self, vertex):
        return self.graph.get(vertex, set())

    def display(self):
        for vertex, neighbors in self.graph.items():
            print(f"{vertex}: {', '.join(map(str, neighbors))}")


# === Full usage demonstration ===
graph = UndirectedGraph()

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
