# https://csiflabs.cs.ucdavis.edu/~tyfeng/ecs34/C++/graphs5.html

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1
            return True
        return False

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = [] # List to store [weight, u, v]

    def add_edge(self, u, v, w):
         # Store edges as [weight, source, destination]
        self.edges.append([w, u, v]) # weight first → sorting works

    def kruskal_mst(self):
        # 1. Sort all edges by weight
        self.edges.sort()
        
        ds = DisjointSet(self.V)
        mst = [] # To store the edges of the MST
        
        mst_weight = 0
        for w, u, v in self.edges:
            # 2. Check if adding edge (u, v) creates a cycle
            # 2. If u and v are not in the same set, no cycle is formed
            if ds.union(u, v):
                mst.append([u, v, w])
                mst_weight += w

        # Print the resulting Minimum Spanning Tree
        # Output the MST
        print("Edges in the Minimum Spanning Tree:")
        print("Edge \tWeight")
        for u, v, w in mst:
            print(f"{u} - {v} \t{w}")
        print(f"Total MST Weight: {mst_weight}")

# --- Example Execution ---
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

g.kruskal_mst()