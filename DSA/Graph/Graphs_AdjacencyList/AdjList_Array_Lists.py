class Graph:
    def __init__(self, vertex):
        self.V = vertex # Number of vertices
        self.adj = [[] for _ in range(vertex)] # Array of Lists
    
    def add_edge(self, src, dest):
        if 0 <= src < self.V and 0 <= dest < self.V:
            self.adj[src].append(dest)
            self.adj[dest].append(src) # Undirected Graph
        else:
            print("Invalid Edge")
    
    def print_graph(self):
        print("Adjacency List:")
        for i in range(self.V):
            print(i, "→", self.adj[i])


# ------------------- Execution -------------------
if __name__ == "__main__":
    G = Graph(5)  # Create graph with 5 vertices (0 to 4)
    
    G.add_edge(0, 1)
    G.add_edge(0, 2)
    G.add_edge(1, 3)
    G.add_edge(2, 4)
    G.add_edge(3, 4)
    G.add_edge(2, 3)
    
    G.print_graph()