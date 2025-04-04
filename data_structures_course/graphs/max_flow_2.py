from collections import deque

class EdmondsKarp:
    def __init__(self, graph, source, sink):
        self.graph = graph  # Graph represented as an adjacency matrix
        self.source = source
        self.sink = sink
        self.n = len(graph)  # Number of nodes
        self.residual_graph = [row[:] for row in graph]  # Copy the original graph for residual capacities
        self.flow = [[0] * self.n for _ in range(self.n)]  # Initialize flow to 0

    # Helper method to perform BFS and find an augmenting path
    def bfs(self, parent):
        visited = [False] * self.n
        queue = deque([self.source])
        visited[self.source] = True

        while queue:
            u = queue.popleft()

            for v in range(self.n):
                if not visited[v] and self.residual_graph[u][v] > 0:  # There is available capacity
                    parent[v] = u  # Track the parent to reconstruct the path
                    if v == self.sink:
                        return True  # We found a path to the sink
                    queue.append(v)
                    visited[v] = True

        return False  # No augmenting path found

    # Edmonds-Karp method to calculate the maximum flow
    def edmonds_karp(self):
        max_flow = 0
        parent = [-1] * self.n  # Array to store the path
        while True:
            # Step 1: Find an augmenting path using BFS
            if not self.bfs(parent):
                break  # No more augmenting paths found, we are done

            # Step 2: Find the minimum capacity in the augmenting path
            path_flow = float('Inf')
            v = self.sink
            while v != self.source:
                u = parent[v]
                path_flow = min(path_flow, self.residual_graph[u][v])
                v = parent[v]

            # Step 3: Update residual graph and reverse flow
            v = self.sink
            while v != self.source:
                u = parent[v]
                self.residual_graph[u][v] -= path_flow  # Decrease the capacity of the edge
                self.residual_graph[v][u] += path_flow  # Increase the reverse flow
                v = parent[v]

            # Add the flow to the total max_flow
            max_flow += path_flow

        return max_flow


# Example usage
graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]

source = 0
sink = 5
ek = EdmondsKarp(graph, source, sink)
max_flow = ek.edmonds_karp()

print("The maximum flow is:", max_flow)