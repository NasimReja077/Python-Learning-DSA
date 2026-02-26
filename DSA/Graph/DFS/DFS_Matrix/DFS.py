class Graph:
    def __init__(self, vertex):
        # Initializes an adjacency matrix with zeros
        self.mat = [[0] * vertex for x in range(vertex)]
        self.size = vertex

    def add_edge(self, src, dest):
        # Adds an undirected edge between src and dest
        if (0 <= src < self.size and 0 <= dest < self.size):
            self.mat[src][dest] = 1
            self.mat[dest][src] = 1
        else:
            print("Invalid Edge")

    def print(self):
        # Prints the adjacency matrix
        for row in self.mat:
            print(' '.join(map(str, row)))

    def dfs(self, src):
        # Iterative Depth-First Search using a stack
        visited = [False] * self.size
        stack = [src]

        while(stack):
            v = stack.pop()

            if (visited[v] == False):
                print(v, end=" -> ")
                visited[v] = True

                # Check for adjacent unvisited nodes
                for i in range(self.size):
                    if self.mat[v][i] == 1 and visited[i] == False:
                        stack.append(i)

# --- Execution ---
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)

g.dfs(0)