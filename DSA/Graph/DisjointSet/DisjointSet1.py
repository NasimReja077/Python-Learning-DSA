class DisjointSet:
    def __init__(self, n):
        # parent[i] = parent of i (initially each node is its own parent)
        self.parent = list(range(n))
        # rank[i] ≈ height of tree (used for union by rank)
        self.rank = [0] * n

    def find(self, x):
        # Path compression: make node point directly to root
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # recursion + compression
        return self.parent[x]

    def union(self, x, y):
        # Find root of both elements
        px = self.find(x)
        py = self.find(y)

        # Already in same set → no need to merge
        if px == py:
            return False

        # Union by rank: attach smaller tree under larger one
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[px] < self.rank[py]:
            self.parent[px] = py
        else:
            # equal rank → choose one and increase its rank
            self.parent[py] = px
            self.rank[px] += 1

        return True  # merge happened

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def print_sets(self):
        print("Parent array:", self.parent)
        print("Rank array  :", self.rank)


# ─── Example usage ───────────────────────────────────────────────
if __name__ == "__main__":
    ds = DisjointSet(6)  # nodes 0 to 5

    edges = [(0,1), (1,2), (2,3), (4,5), (0,4), (3,5)]

    print("Before unions:")
    ds.print_sets()

    for u, v in edges:
        merged = ds.union(u, v)
        print(f"Union({u},{v}) → merged = {merged}")

    print("\nAfter all unions:")
    ds.print_sets()

    print("\nIs 0 and 3 connected?", ds.connected(0, 3))
    print("Is 0 and 5 connected?", ds.connected(0, 5))