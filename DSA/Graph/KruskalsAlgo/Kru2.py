class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
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
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append([w, u, v])   # weight first → sorting works

    def kruskal_mst(self):
        # Sort edges by increasing weight
        self.edges.sort()

        ds = DisjointSet(self.V)

        result = []           # MST edges
        mst_weight = 0
        edges_used = 0

        for w, u, v in self.edges:
            if ds.union(u, v):
                result.append([u, v, w])
                mst_weight += w
                edges_used += 1

                # Early stop — we have enough edges
                if edges_used == self.V - 1:
                    break

        # Print result
        print("Edges in the Minimum Spanning Tree:")
        for u, v, w in result:
            print(f"  {u:2} -- {v:2}  (weight {w})")

        print(f"\nTotal weight of MST: {mst_weight}")

        # Very useful check (especially in exams)
        if edges_used != self.V - 1:
            print("\nWarning: Graph is disconnected → this is a Minimum Spanning Forest")
            print(f"Only {edges_used} edges found (expected {self.V-1})")


# ─── Test ────────────────────────────────────────
if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    g.kruskal_mst()