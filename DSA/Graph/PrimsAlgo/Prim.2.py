# Option B → Min Heap / Priority Queue (O(E log V))

import heapq

def prim(n, adj):
    visited = [False] * n
    min_heap = [(0, 0)]  # (weight, vertex)
    total_weight = 0
    mst = []

    while min_heap:
        weight, u = heapq.heappop(min_heap)

        if visited[u]:
            continue

        visited[u] = True
        total_weight += weight

        for v, w in adj[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))
                mst.append((u, v, w))

    return total_weight


# Example (Adjacency List)
adj = {
    0: [(1,1), (2,3)],
    1: [(0,1), (2,2), (3,4)],
    2: [(0,3), (1,2), (3,5)],
    3: [(1,4), (2,5)]
}

print("Total Weight:", prim(4, adj))

'''
Time and Space Complexity
Using Min Heap:

Time Complexity:
O(E log V)

Space Complexity:
O(V + E)

Using Adjacency Matrix:
Time Complexity:
O(V2)
'''