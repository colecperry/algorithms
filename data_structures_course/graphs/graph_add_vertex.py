# Add a vertex into the graph

# Time complexity - Add vertex
# Adjacency List - O(1) - you just add a new key to the dict
# Adjacency Matrix - O(N)^2 - you have to add a new row and column and rewrite the whole matrix

class Graph:
    def __init__(self):
        self.adj_list = {} # Create a dictionary (adjacency list)
    
    def print_graph(self): # 
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])
    
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys(): # Check for duplicates in our graph
            self.adj_list[vertex] = [] # Create a new dictionary item with the vertex as the key and an empty list as the value
            return True # Return true if added
        return False # Return false if not added

my_graph = Graph()

my_graph.add_vertex('A')

my_graph.print_graph()