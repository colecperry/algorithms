# Time complexity - Add edge
# Adjacency List - O(1) - Append to the value list in the dict
# Adjacency Matrix - O(1) - Update the edge to 1 in the matrix

class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])
    
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys(): # Check for duplicates in our graph
            self.adj_list[vertex] = [] # Create a new dictionary item with the vertex as the key and an empty list as the value
            return True # Return true if added
        return False # Return false if not added
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys(): # If vertex 1 and vertex 2 both exist
            self.adj_list[v1].append(v2) # Use v1 as the key to access it's value, which is a list
            self.adj_list[v2].append(v1)
            return True # Return true if we add the edge
        return False # Add false if either vertex don't exist

my_graph = Graph()

my_graph.add_vertex(1)
my_graph.add_vertex(2)

my_graph.add_edge(1,2)

my_graph.print_graph()