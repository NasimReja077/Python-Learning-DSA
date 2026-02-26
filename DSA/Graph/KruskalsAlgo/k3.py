def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, x, y):
    parent[find(parent, x)] = find(parent, y)

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])  # sort by weight
    parent = list(range(n))
    mst = []
    total = 0

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst.append((u, v, w))
            total += w

    return mst, total


# Example
edges = [
    (0, 1, 1),
    (1, 2, 2),
    (0, 2, 3),
    (1, 3, 4),
    (2, 3, 5)
]

mst, weight = kruskal(4, edges)
print("MST:", mst)
print("Total Weight:", weight)