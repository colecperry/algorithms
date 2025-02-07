class Graph:
    def __init__(self, num_vertices, weighted=False, directed=False):
        """
        Initialize the graph.
        :param num_vertices: Number of vertices in the graph.
        :param weighted: Boolean indicating if the graph is weighted.
        :param directed: Boolean indicating if the graph is directed.
        """
        self.num_vertices = num_vertices
        self.weighted = weighted
        self.directed = directed
        # Initialize an adjacency matrix with 0s
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
    
    def add_edge(self, u, v, weight=1):
        """
        Add an edge to the graph.
        :param u: Starting vertex of the edge.
        :param v: Ending vertex of the edge.
        :param weight: Weight of the edge (default is 1 for unweighted graphs).
        """
        if u >= self.num_vertices or v >= self.num_vertices:
            print(f"Error: Vertex {u} or {v} does not exist.")
            return

        if self.weighted:
            self.adj_matrix[u][v] = weight
        else:
            self.adj_matrix[u][v] = 1
        
        if not self.directed:  # If it's undirected, add the reverse edge
            self.adj_matrix[v][u] = weight if self.weighted else 1

    def remove_edge(self, u, v):
        """
        Remove an edge from the graph.
        :param u: Starting vertex of the edge.
        :param v: Ending vertex of the edge.
        """
        if u >= self.num_vertices or v >= self.num_vertices:
            print(f"Error: Vertex {u} or {v} does not exist.")
            return

        self.adj_matrix[u][v] = 0
        if not self.directed:  # If it's undirected, remove the reverse edge as well
            self.adj_matrix[v][u] = 0

    def add_vertex(self):
        """
        Add a new vertex to the graph.
        """
        self.num_vertices += 1
        for row in self.adj_matrix:
            row.append(0)  # Add a new column for the new vertex
        self.adj_matrix.append([0] * self.num_vertices)  # Add a new row for the new vertex

    def remove_vertex(self, vertex):
        """
        Remove a vertex and its associated edges from the graph.
        :param vertex: The vertex to remove.
        """
        if vertex >= self.num_vertices:
            print(f"Error: Vertex {vertex} does not exist.")
            return

        # Remove the row corresponding to the vertex
        self.adj_matrix.pop(vertex)
        # Remove the column corresponding to the vertex in each row
        for row in self.adj_matrix:
            row.pop(vertex)
        self.num_vertices -= 1

    def print_graph(self):
        """Print the adjacency matrix of the graph."""
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(row)


if __name__ == "__main__":
    # Unweighted Undirected Graph
    print("Unweighted Undirected Graph:")
    g1 = Graph(num_vertices=4, weighted=False, directed=False)
    g1.add_edge(0, 1)
    g1.add_edge(0, 2)
    g1.add_edge(2, 3)
    g1.print_graph()

    print("\nWeighted Directed Graph:")
    # Weighted Directed Graph
    g2 = Graph(num_vertices=4, weighted=True, directed=True)
    g2.add_edge(0, 1, 5)
    g2.add_edge(0, 2, 3)
    g2.add_edge(2, 3, 7)
    g2.print_graph()

    print("\nUnweighted Directed Graph:")
    # Unweighted Directed Graph
    g3 = Graph(num_vertices=4, weighted=False, directed=True)
    g3.add_edge(0, 1)
    g3.add_edge(0, 2)
    g3.add_edge(2, 3)
    g3.add_edge(3, 1)
    g3.print_graph()

    print("\nAdd Vertex Example:")
    # Add a vertex and print the graph
    g3.add_vertex()
    g3.print_graph()

    print("\nRemove Vertex Example:")
    # Remove the newly added vertex and print the graph
    g3.remove_vertex(4)
    g3.print_graph()

    print("\nAdd Edge Example:")
    # Add a new edge and print the graph
    g3.add_edge(1, 3)
    g3.print_graph()

    print("\nRemove Edge Example:")
    # Remove the edge and print the graph
    g3.remove_edge(1, 3)
    g3.print_graph()
