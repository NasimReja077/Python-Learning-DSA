class Graph:
    def __init__(self, vertex):
        # Initialize an adjacency matrix of size (vertex x vertex)
        self.mat = [[0] * vertex for _ in range(vertex)]
        self.size = vertex

    def add_edge(self, src, dest):
        # Since it's an undirected graph, we mark both directions
        if 0 <= src < self.size and 0 <= dest < self.size:
            self.mat[src][dest] = 1
            self.mat[dest][src] = 1
        else:
            print(f"Invalid Edge: {src}-{dest}")

    def print_matrix(self):
        for row in self.mat:
            print(' '.join(map(str, row)))

    def dfs_recursive(self, src, visited=None):
        # Initialize the visited list on the very first call
        if visited is None:
            visited = [False] * self.size

        # 1. Mark the current node as visited and print it
        visited[src] = True
        print(src, end=" -> ")

        # 2. Look at all potential neighbors in the adjacency matrix
        for neighbor in range(self.size):
            # If there is a connection (1) and the neighbor hasn't been visited
            if self.mat[src][neighbor] == 1 and not visited[neighbor]:
                # 3. Recurse: Move deeper into the graph starting from this neighbor
                self.dfs_recursive(neighbor, visited)

# --- Main Execution ---
if __name__ == "__main__":
    # Initialize graph with 6 vertices (0 to 5)
    g = Graph(6)

    # Adding the edges from your screenshot
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)

    print("Adjacency Matrix:")
    g.print_matrix()

    print("\nDFS Traversal (Recursive) starting from node 0:")
    g.dfs_recursive(0)
    print("Done")