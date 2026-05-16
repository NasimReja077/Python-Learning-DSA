## Prim's Algorithm

---

## What is Prim's Algorithm?

Prim's Algorithm is a **greedy algorithm** that finds the **Minimum Spanning Tree (MST)** by **growing a single tree one vertex at a time** — always adding the cheapest edge that connects the current tree to a new unvisited vertex.

> Think of it like growing a tree from a seed — you always extend the tree by the cheapest available branch, never jumping to a disconnected part of the forest.

---

## Core Idea

```
┌─────────────────────────────────────────────────────────┐
│                                                          │
│  1. Start from ANY vertex                               │
│                                                          │
│  2. Always pick the CHEAPEST edge that:                 │
│       → Connects a VISITED vertex                       │
│       → To an UNVISITED vertex                          │
│                                                          │
│  3. Add that vertex to the tree                         │
│                                                          │
│  4. REPEAT until ALL vertices are in the tree           │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## Prim's vs Kruskal's — Key Difference

```
Kruskal's                          Prim's
──────────────────────────         ──────────────────────────
Looks at ALL edges globally        Looks at edges from
                                   CURRENT TREE only

Grows a FOREST                     Grows a SINGLE TREE
(multiple components               (one connected component
 merged together)                   expanded step by step)

Best for SPARSE graphs             Best for DENSE graphs

Uses Union-Find                    Uses Min-Heap
```

---

## The Algorithm

```
PRIM(graph, start):

  1. Initialize:
       visited   = {start}
       MST       = []
       min_heap  = all edges from start vertex

  2. While heap is NOT empty AND MST is incomplete:
       a. Pop MINIMUM weight edge (weight, u, v) from heap
       b. IF v is already visited → SKIP (cycle)
       c. IF v is not visited:
            → ADD edge (u, v, weight) to MST
            → Mark v as visited
            → Push all edges from v to unvisited
              neighbors into heap

  3. STOP when all V vertices visited (V-1 edges added)

  4. Return MST
```

---

## Example Graph

```
Vertices: A  B  C  D  E  F

           (1)
      A ─────── B
      │        /│\
     (3)    (5)(4)(6)
      │    /    │   \
      C ─────── D    E
           (2)        │
                     (8)
                      │
                      F

All edges:
  A-B: 1    B-D: 4    D-E: 7
  A-C: 3    B-C: 5    E-F: 8
  C-D: 2    B-E: 6
```

---

## Step-by-Step Working

### Starting from vertex A

```
Initial State:
  Visited  = {A}
  MST      = []
  Total    = 0
  Heap     = edges from A → [(1,A,B), (3,A,C)]
```

---

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1: Pop minimum edge from heap → A-B (weight 1)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Is B visited? NO ✅ → ADD edge A-B

  Mark B as visited
  Push B's edges to unvisited neighbors:
    → B-C(5), B-D(4), B-E(6)

  Visited  = {A, B}
  MST      = [A-B(1)]
  Total    = 1
  Heap     = [(3,A,C), (4,B,D), (5,B,C), (6,B,E)]

  Current Tree:
    A ─(1)─ B
```

---

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 2: Pop minimum edge from heap → A-C (weight 3)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Is C visited? NO ✅ → ADD edge A-C

  Mark C as visited
  Push C's edges to unvisited neighbors:
    → C-D(2)

  Visited  = {A, B, C}
  MST      = [A-B(1), A-C(3)]
  Total    = 4
  Heap     = [(2,C,D), (4,B,D), (5,B,C), (6,B,E)]

  Current Tree:
    A ─(1)─ B
    │
   (3)
    │
    C
```

---

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 3: Pop minimum edge from heap → C-D (weight 2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Is D visited? NO ✅ → ADD edge C-D

  Mark D as visited
  Push D's edges to unvisited neighbors:
    → D-E(7)

  Visited  = {A, B, C, D}
  MST      = [A-B(1), A-C(3), C-D(2)]
  Total    = 6
  Heap     = [(4,B,D), (5,B,C), (6,B,E), (7,D,E)]

  Current Tree:
    A ─(1)─ B
    │
   (3)
    │
    C ─(2)─ D
```

---

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 4: Pop minimum edge from heap → B-D (weight 4)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Is D visited? YES ❌ → SKIP (would create cycle)

  Heap     = [(5,B,C), (6,B,E), (7,D,E)]

  Tree UNCHANGED:
    A ─(1)─ B
    │
   (3)
    │
    C ─(2)─ D
```

---

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 5: Pop minimum edge from heap → B-C (weight 5)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Is C visited? YES ❌ → SKIP (would create cycle)

  Heap     = [(6,B,E), (7,D,E)]

  Tree UNCHANGED
```

---

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 6: Pop minimum edge from heap → B-E (weight 6)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Is E visited? NO ✅ → ADD edge B-E

  Mark E as visited
  Push E's edges to unvisited neighbors:
    → E-F(8)

  Visited  = {A, B, C, D, E}
  MST      = [A-B(1), A-C(3), C-D(2), B-E(6)]
  Total    = 12
  Heap     = [(7,D,E), (8,E,F)]

  Current Tree:
    A ─(1)─ B ─(6)─ E
    │
   (3)
    │
    C ─(2)─ D
```

---

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 7: Pop minimum edge from heap → D-E (weight 7)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Is E visited? YES ❌ → SKIP (would create cycle)

  Heap     = [(8,E,F)]

  Tree UNCHANGED
```

---

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 8: Pop minimum edge from heap → E-F (weight 8)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Is F visited? NO ✅ → ADD edge E-F

  Mark F as visited
  All vertices visited! ← DONE ✅

  Visited  = {A, B, C, D, E, F}
  MST      = [A-B(1), A-C(3), C-D(2), B-E(6), E-F(8)]
  Total    = 20

  Final Tree:
    A ─(1)─ B ─(6)─ E ─(8)─ F
    │
   (3)
    │
    C ─(2)─ D
```

---

## Final MST

```
    A ─(1)─ B ─(6)─ E ─(8)─ F
    │
   (3)
    │
    C ─(2)─ D


  MST Edges : A-B(1), C-D(2), A-C(3), B-E(6), E-F(8)
  Total Cost : 1 + 2 + 3 + 6 + 8 = 20  ← Minimum!
  Edges used : V-1 = 5 ✅
```

---

## Complete Decision Table

```
  Step  Edge    Weight   Visited?   Action
  ──────────────────────────────────────────────
   1    A-B       1       B=No    →  ADD  ✅
   2    A-C       3       C=No    →  ADD  ✅
   3    C-D       2       D=No    →  ADD  ✅
   4    B-D       4       D=Yes   →  SKIP ❌
   5    B-C       5       C=Yes   →  SKIP ❌
   6    B-E       6       E=No    →  ADD  ✅
   7    D-E       7       E=Yes   →  SKIP ❌
   8    E-F       8       F=No    →  ADD  ✅
```

---

## How the Tree Grows — Visualization

```
Step 1          Step 2          Step 3
────────        ────────        ────────
A─B             A─B             A─B
                │               │
                C               C─D


Step 4(skip)    Step 5(skip)    Step 6
────────────    ────────────    ────────
A─B             A─B             A─B─E
│               │               │
C─D             C─D             C─D


Step 7(skip)    Step 8 ✅
────────────    ────────────────
A─B─E           A─B─E─F
│               │
C─D             C─D   ← MST COMPLETE!
```

---

## Code

### Prim's Algorithm — Using Min-Heap
```python
import heapq

def prim(graph, start):
    """
    graph : adjacency dict → {vertex: {neighbor: weight}}
    start : starting vertex
    """
    visited      = set([start])
    mst          = []
    total_weight = 0

    # Min-heap: (weight, from_vertex, to_vertex)
    heap = [(w, start, v) for v, w in graph[start].items()]
    heapq.heapify(heap)

    print(f"Start vertex: {start}")
    print(f"Initial heap: {heap}\n")

    while heap and len(visited) < len(graph):
        weight, u, v = heapq.heappop(heap)    # Pick minimum edge

        if v in visited:                       # Already in tree?
            print(f"  SKIP  {u}-{v} (weight {weight}) → {v} already visited")
            continue

        # Add edge to MST
        visited.add(v)
        mst.append((u, v, weight))
        total_weight += weight
        print(f"  ADD   {u}-{v} (weight {weight}) → Total: {total_weight}")

        # Push all edges from new vertex to unvisited neighbors
        for neighbor, w in graph[v].items():
            if neighbor not in visited:
                heapq.heappush(heap, (w, v, neighbor))

    return mst, total_weight


# ── Graph Definition ─────────────────────────────────────────
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'C': 5, 'D': 4, 'E': 6},
    'C': {'A': 3, 'B': 5, 'D': 2},
    'D': {'C': 2, 'B': 4, 'E': 7},
    'E': {'B': 6, 'D': 7, 'F': 8},
    'F': {'E': 8}
}

mst, total = prim(graph, 'A')

print("\n─── MST Result ───")
for u, v, w in mst:
    print(f"  {u} ─── {v}  (weight {w})")
print(f"\nTotal MST Weight: {total}")
```

### Output
```
Start vertex: A
Initial heap: [(1, 'A', 'B'), (3, 'A', 'C')]

  ADD   A-B (weight 1) → Total: 1
  ADD   A-C (weight 3) → Total: 4
  ADD   C-D (weight 2) → Total: 6
  SKIP  B-D (weight 4) → D already visited
  SKIP  B-C (weight 5) → C already visited
  ADD   B-E (weight 6) → Total: 12
  SKIP  D-E (weight 7) → E already visited
  ADD   E-F (weight 8) → Total: 20

─── MST Result ───
  A ─── B  (weight 1)
  A ─── C  (weight 3)
  C ─── D  (weight 2)
  B ─── E  (weight 6)
  E ─── F  (weight 8)

Total MST Weight: 20
```

---

### Prim's with Key Array (Alternative approach)
```python
import sys

def prim_key_array(graph, V):
    """
    graph : 2D adjacency matrix
    V     : number of vertices
    """
    # key[i]    = minimum edge weight to include vertex i
    # parent[i] = parent of vertex i in MST
    # in_mst[i] = whether vertex i is in MST

    key    = [sys.maxsize] * V
    parent = [-1]          * V
    in_mst = [False]       * V

    key[0] = 0                              # Start from vertex 0

    for _ in range(V):
        # Pick vertex with minimum key not yet in MST
        u = min_key(key, in_mst, V)
        in_mst[u] = True

        # Update keys of adjacent vertices
        for v in range(V):
            if (graph[u][v] > 0 and          # Edge exists
                not in_mst[v] and            # Not yet in MST
                graph[u][v] < key[v]):       # Better weight found
                key[v]    = graph[u][v]
                parent[v] = u

    # Print MST
    total = 0
    print("Edge    Weight")
    for i in range(1, V):
        print(f"  {parent[i]}─{i}  :  {graph[i][parent[i]]}")
        total += graph[i][parent[i]]
    print(f"Total   : {total}")


def min_key(key, in_mst, V):
    """Find vertex with minimum key value not in MST"""
    minimum = sys.maxsize
    min_idx = -1
    for v in range(V):
        if key[v] < minimum and not in_mst[v]:
            minimum = key[v]
            min_idx = v
    return min_idx
```

---

### Prim's — Shortest Path Tracking
```python
import heapq

def prim_with_path(graph, start):
    """Returns MST with full parent tracking"""
    visited = set([start])
    parent  = {start: None}
    cost    = {start: 0}
    heap    = [(0, start)]

    while heap:
        weight, u = heapq.heappop(heap)

        for v, w in graph[u].items():
            if v not in visited:
                visited.add(v)
                parent[v] = u
                cost[v]   = w
                heapq.heappush(heap, (w, v))

    # Reconstruct MST
    mst = []
    for v, u in parent.items():
        if u is not None:
            mst.append((u, v, cost[v]))

    return mst, sum(cost.values())
```

---

## Time & Space Complexity

### Using Min-Heap (Binary Heap)

| Operation | Times Called | Cost Each | Total |
|---|---|---|---|
| **Extract min from heap** | V times | O(log E) | O(V log E) |
| **Insert edge into heap** | E times | O(log E) | O(E log E) |
| **Total** | | | **O(E log E)** |

> Since E ≤ V², we have log E ≤ 2 log V, so **O(E log E) = O(E log V)**

### Using Fibonacci Heap (Optimal)

| Operation | Cost | Total |
|---|---|---|
| **Extract min** | O(log V) amortized | O(V log V) |
| **Decrease key** | O(1) amortized | O(E) |
| **Total** | | **O(E + V log V)** |

### Using Simple Array (No heap)

| Operation | Times Called | Cost Each | Total |
|---|---|---|---|
| **Find minimum key** | V times | O(V) | O(V²) |
| **Update keys** | E times | O(1) | O(E) |
| **Total** | | | **O(V²)** |

```
Summary:

  Implementation      Time           Best for
  ─────────────────────────────────────────────
  Simple array      O(V²)          Dense graphs
  Binary heap       O(E log V)     Sparse graphs
  Fibonacci heap    O(E + V log V) Best overall


  Dense graph (E ≈ V²):
    Array → O(V²)          ✅ better
    Heap  → O(V² log V)    ❌ worse

  Sparse graph (E ≈ V):
    Array → O(V²)          ❌ worse
    Heap  → O(V log V)     ✅ better
```

### Space Complexity

| Structure | Space | Purpose |
|---|---|---|
| **Visited set** | O(V) | Track visited vertices |
| **Min-Heap** | O(E) | Store candidate edges |
| **MST result** | O(V) | Store V-1 edges |
| **Total** | **O(V + E)** | |

---

## Advantages

```
✅  Optimal solution guaranteed
      Always produces a true MST with the
      absolute minimum total edge weight.

✅  Efficient on dense graphs
      With a simple array, runs in O(V²) which
      is optimal when E ≈ V² (lots of edges).

✅  Grows one connected tree
      Always maintains a single connected
      component — easier to visualize and verify.

✅  No need to sort all edges upfront
      Unlike Kruskal's, Prim's doesn't need
      to sort all edges before starting.

✅  Naturally handles weighted graphs
      Designed specifically for weighted
      undirected graphs.

✅  Easy to implement with adjacency matrix
      Simple array version is very clean
      and efficient for dense graphs.

✅  Easier to understand conceptually
      "Grow the tree greedily" is very
      intuitive and maps well to real problems.
```

---

## Disadvantages

```
❌  Requires a connected graph
      If the graph is disconnected, Prim's
      won't reach all vertices. Must modify
      to produce a spanning forest.

❌  Only for undirected graphs
      Cannot directly handle directed graphs
      (use Edmonds' algorithm instead).

❌  Slower on sparse graphs (without heap)
      Simple array version is O(V²) —
      very slow when E << V² (few edges).

❌  Heap version complexity
      Binary heap version O(E log V) is
      more complex to implement correctly.

❌  Dependent on start vertex choice
      Different start vertices may produce
      different (but equally valid) MSTs.

❌  Not suitable for dynamic graphs
      If edges are added/removed, must
      rerun entire algorithm from scratch.

❌  Memory intensive for dense graphs
      Storing all edges in heap for dense
      graphs uses significant memory O(E).
```

---

## Prim's vs Kruskal's — Full Comparison

| Property | Prim's | Kruskal's |
|---|---|---|
| **Strategy** | Expand nearest vertex | Pick cheapest global edge |
| **Growth** | Single tree | Forest merged into tree |
| **Data structure** | Min-Heap / Array | Union-Find + sorted edges |
| **Starting point** | Needs start vertex | No start needed |
| **Best for** | Dense graphs | Sparse graphs |
| **Time (dense)** | O(V²) with array ✅ | O(E log E) ❌ |
| **Time (sparse)** | O(E log V) ❌ | O(E log E) ✅ |
| **Space** | O(V + E) | O(V + E) |
| **Disconnected graph** | Needs modification | Natural forest |
| **Edge sorting** | Not needed | Required upfront |
| **Cycle detection** | Visited array | Union-Find |

```
Choose Prim's when:              Choose Kruskal's when:
────────────────────────         ────────────────────────
✔ Graph is DENSE (E ≈ V²)        ✔ Graph is SPARSE (E ≈ V)
✔ Using adjacency matrix         ✔ Edges given as a list
✔ Start vertex is known          ✔ No start vertex needed
✔ Want single tree growth        ✔ Parallel processing needed
```

---

## Real-World Applications

| Application | How Prim's Helps |
|---|---|
| **Network design** | Minimum cable to connect all offices |
| **Road planning** | Cheapest roads to connect all cities |
| **Power grid** | Minimum wire from plant to all homes |
| **Water supply** | Cheapest pipeline connecting all areas |
| **Telecommunications** | Minimum fiber optic between towers |
| **Cluster analysis** | Group nearby data points together |
| **PCB design** | Minimize wire length on circuit boards |
| **Game maps** | Connect all map regions with minimum paths |

---

## Quick Summary

```
┌──────────────────────────────────────────────────────────┐
│                   PRIM'S ALGORITHM                        │
│                                                           │
│  Type       → Greedy Algorithm                           │
│  Goal       → Minimum Spanning Tree                      │
│  Strategy   → Grow one tree from a start vertex         │
│  Key Tool   → Min-Heap (or simple array)                 │
│                                                           │
│  Steps:                                                   │
│    1. Start from any vertex                              │
│    2. Always pick cheapest edge to an unvisited vertex   │
│    3. Add that vertex to the tree                        │
│    4. Repeat until all vertices are included             │
│                                                           │
│  Time  →  O(E log V) with heap                          │
│           O(V²) with array                               │
│  Space →  O(V + E)                                       │
│  Best  →  Dense graphs                                   │
└──────────────────────────────────────────────────────────┘
```

Prim's Algorithm is powerful because it **always knows exactly where its tree is** and just keeps **greedily grabbing the cheapest branch** — making it one of the most elegant and practical algorithms for network design and optimization problems.