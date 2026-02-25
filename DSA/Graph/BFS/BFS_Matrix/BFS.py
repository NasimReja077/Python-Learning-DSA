from collections import deque

class Graph:
    def __init__(self, vertex):
        # Initialize an adjacency matrix with zeros
        self.mat = [[0] * vertex for x in range(vertex)]
        self.size = vertex

    def add_edge(self, src, dest):
        # Add undirected edges
        if (0 <= src < self.size and 0 <= dest < self.size):
            self.mat[src][dest] = 1
            self.mat[dest][src] = 1
        else:
            print("Invalid Edge")

    def BFS(self, src):
        # 1. Setup: Track visited nodes and initialize the Queue
        visited = [False] * self.size
        queue = deque([src])
        visited[src] = True

        # 2. Loop while the queue is not empty
        while(queue):
            v = queue.popleft() # Remove from the front (First-In, First-Out)
            print(v, end=" ")

            # 3. Explore all neighbors
            for i in range(self.size):
                # If there is an edge AND the neighbor isn't visited
                if(self.mat[v][i] == 1 and visited[i] == False):
                    visited[i] = True
                    queue.append(i) # Add to the back of the queue

# --- Execution ---
g = Graph(8)
g.add_edge(0,1)
g.add_edge(0,3)
g.add_edge(1,3)
g.add_edge(3,5)
g.add_edge(3,4)
g.add_edge(4,5)
g.add_edge(4,6)
g.add_edge(6,2)
g.add_edge(6,7)

print("BFS Traversal starting from 0:")
g.BFS(0)