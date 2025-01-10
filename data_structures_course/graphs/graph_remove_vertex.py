# Time complexity - Remove a vertex
# Adjacency List: O(V + E) Remove the vertex from the list, iterate through every edge and remove all common edges
# Adjacency Matrix: O(N)^2 You have to remove the row and columns

class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])
    
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self, vertex): # Remove a vertex node and all edges it has with other nodes
        if vertex in self.adj_list.keys(): # Make sure the vertex exists in our graph
            for other_vertex in self.adj_list[vertex]: # Loop through the edges of that vertex
                self.adj_list[other_vertex].remove(vertex) # Go to that other vertex, and remove the edge (equal to the vertex we are removing)
            del self.adj_list[vertex] # Delete the vertex from the list
            return True # Return True if removed
        return False # Return false if vertex doesn't exist

my_graph = Graph()

my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('A', 'D')
my_graph.add_edge('B', 'D')
my_graph.add_edge('C', 'D')

my_graph.remove_vertex('D')

my_graph.print_graph()

