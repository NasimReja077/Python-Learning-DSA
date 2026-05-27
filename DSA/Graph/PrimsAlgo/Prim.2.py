# Option B → Min Heap / Priority Queue (O(E log V))

import heapq

def prim(n, adj): # n = number of vertices, adj = adjacency list
    visited = [False] * n
     # (weight, vertex, parent)
    min_heap = [(0, 0, -1)]
    total_weight = 0
    mst = []

    while min_heap:
        weight, u, parent = heapq.heappop(min_heap) # u = current vertex, parent = vertex from which u is reached

        if visited[u]:
            continue

        visited[u] = True
        total_weight += weight
        
        # Add edge only after vertex is selected
        if parent != -1: # Skip the first vertex which has no parent
            mst.append((parent, u, weight)) # 

        for v, w in adj[u]: # v = neighbor vertex, w = weight of edge u-v adj[u] contains (neighbor, weight) pairs
            
            if not visited[v]:
                heapq.heappush(min_heap, (w, v, u))
                # mst.append((u, v, w))
                
    print("MST Edges:")
    for u, v, w in mst:
        print(f"{u} - {v} = {w}")

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