import sys

class Graph:
    def __init__(self, vertex):
        self.mat = [[0] * vertex for _ in range(vertex)]
        self.size = vertex

    def add_edge(self, src, dest, weight):

        if 0 <= src < self.size and 0 <= dest < self.size:
            self.mat[src][dest] = weight
            self.mat[dest][src] = weight

    def prim_mst(self):
        key = [sys.maxsize] * self.size
        parent = [None] * self.size
        visited = [False] * self.size

        key[0] = 0
        parent[0] = -1
        
        for _ in range(self.size):

            u = self.min_key(key, visited) 
            visited[u] = True

            for v in range(self.size): 
                if 0 < self.mat[u][v] < key[v] and not visited[v]:
                    key[v] = self.mat[u][v]
                    parent[v] = u

        self.print_mst(parent)

    def min_key(self, key, visited):
        min_val = sys.maxsize
        min_index = -1 #
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