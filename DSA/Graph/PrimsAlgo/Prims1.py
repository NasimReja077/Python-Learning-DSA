# Option A → Adjacency Matrix (O(V²))
import sys

class Graph:
    def __init__(self, vertex):
        # Initialize matrix with zeros
        self.mat = [[0] * vertex for _ in range(vertex)]
        self.size = vertex

    def add_edge(self, src, dest, weight):
        # Adding weighted undirected edges
        if 0 <= src < self.size and 0 <= dest < self.size:
            self.mat[src][dest] = weight
            self.mat[dest][src] = weight

    def prim_mst(self):
        # Key values used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.size
        parent = [None] * self.size # Array to store constructed MST
        visited = [False] * self.size

        # Start with the first vertex
        key[0] = 0
        parent[0] = -1 # First node is always the root of MST

        for _ in range(self.size):
            # Pick the minimum distance vertex from the set of vertices not yet processed
            u = self.min_key(key, visited)
            visited[u] = True

            # Update key value and parent index of the adjacent vertices
            for v in range(self.size):
                # mat[u][v] is non-zero only for adjacent vertices
                # visited[v] is false for vertices not yet included in MST
                # Update the key only if mat[u][v] is smaller than key[v]
                if 0 < self.mat[u][v] < key[v] and not visited[v]:
                    key[v] = self.mat[u][v]
                    parent[v] = u

        self.print_mst(parent)

    def min_key(self, key, visited):
        min_val = sys.maxsize
        min_index = -1
        for v in range(self.size):
            if key[v] < min_val and not visited[v]:
                min_val = key[v]
                min_index = v
        return min_index

    def print_mst(self, parent):
        print("Edge \tWeight")
        total_weight = 0
        for i in range(1, self.size):
            weight = self.mat[i][parent[i]]
            print(f"{parent[i]} - {i} \t{weight}")
            total_weight += weight
        print(f"Total MST Weight: {total_weight}")

# --- Execution ---
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

g.prim_mst()