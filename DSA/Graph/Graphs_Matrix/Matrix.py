'''
Directed + Weighted Graph (Adjacency Matrix)
Key Points:
Directed → Only one direction (src → dest)
Weighted → Store weight instead of 1
Matrix is NOT symmetric
'''

class Graph:
    def __init__(self, vertex):
        # Initialize matrix with 0 (no edge)
        self.size = vertex
        self.mat = [[0] * vertex for _ in range(vertex)]

    def add_edge(self, src, dest, weight):
        if 0 <= src < self.size and 0 <= dest < self.size:
            # Directed edge (only one direction)
            self.mat[src][dest] = weight
        else:
            print("Invalid Edge")

    def print_matrix(self):
        print("Adjacency Matrix:")
        for row in self.mat:
            print(' '.join(map(str, row)))


# -------- Execution --------
G = Graph(4)

# src, dest, weight
G.add_edge(0, 1, 5)
G.add_edge(0, 2, 3)
G.add_edge(1, 3, 2)
G.add_edge(2, 3, 7)

G.print_matrix()