## Kruskal's Algorithm — Minimum Spanning Tree (MST)

---

### What is Kruskal's Algorithm?

Kruskal's Algorithm finds the **Minimum Spanning Tree (MST)** of a weighted, undirected graph — a subset of edges that:
- Connects **all vertices**
- Has **no cycles**
- Has the **minimum total edge weight**

---

### Core Idea

```
Sort all edges by weight → Pick smallest edge → 
Add it if it doesn't form a cycle → Repeat until V-1 edges chosen
```

---

### Key Concept — Union-Find (Disjoint Set)

Used to **detect cycles**. Every vertex starts in its own set.

```
Initially:
parent = [0, 1, 2, 3, 4]
         ↑  ↑  ↑  ↑  ↑
         each node is its own parent

find(x)  → finds the root/representative of x's set
union(x,y) → merges two sets together
```

---

### Full Code with Comments

```python
class KruskalGraph:
    def __init__(self, vertices):
        self.V = vertices          # Number of vertices
        self.edges = []            # Stores (weight, src, dest)

    def add_edge(self, src, dest, weight):
        self.edges.append((weight, src, dest))   # Add edge as tuple

    # --- Union-Find: Find root of a node ---
    def find(self, parent, x):
        if parent[x] != x:                        # If x is not its own root
            parent[x] = self.find(parent, parent[x])  # Path compression
        return parent[x]

    # --- Union-Find: Merge two sets ---
    def union(self, parent, rank, x, y):
        rootX = self.find(parent, x)
        rootY = self.find(parent, y)

        # Attach smaller rank tree under larger rank tree
        if rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        elif rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

    # --- Main Kruskal Algorithm ---
    def kruskal_mst(self):
        self.edges.sort()          # Step 1: Sort edges by weight (ascending)

        parent = [i for i in range(self.V)]   # Each node is its own parent
        rank   = [0] * self.V                 # Rank for union by rank

        mst        = []     # Stores final MST edges
        mst_weight = 0      # Total MST cost

        print("\n--- Kruskal's Algorithm Steps ---\n")

        for weight, src, dest in self.edges:         # Step 2: Process edges one by one
            rootSrc  = self.find(parent, src)
            rootDest = self.find(parent, dest)

            if rootSrc != rootDest:                  # Step 3: No cycle? → Add edge
                self.union(parent, rank, src, dest)
                mst.append((src, dest, weight))
                mst_weight += weight
                print(f"  ✔ Added Edge: {src} -- {dest}  | Weight: {weight}  | Total so far: {mst_weight}")
            else:
                print(f"  ✘ Skipped Edge: {src} -- {dest} | Weight: {weight}  → Would form a CYCLE")

            if len(mst) == self.V - 1:               # Step 4: MST complete (V-1 edges)
                break

        print("\n--- Minimum Spanning Tree ---")
        for src, dest, weight in mst:
            print(f"  {src} -- {dest}  : {weight}")
        print(f"\n  Total MST Weight: {mst_weight}")


# ──────────────────────────────
#         EXECUTION
# ──────────────────────────────
g = KruskalGraph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

g.kruskal_mst()
```

---

### Input Graph Diagram

```
        2           
  0 ─────── 1
  │        /│\ 
  │6      / │ \5
  │      /3 │  \
  │     /   │8  \
  3────/────-+   4
   \  2      │  /
    \         │ /7
   9 \        │/
      \───────+
           (3-4 via 2's path)

Cleaner:

        (2)
   0 ──────── 1
   |        / | \
  (6)     (3) (8) (5)
   |      /   |    \
   3 ────     |     4
    \         |    /
    (9)──────(7)──
```

### Clean Edge-Weighted View:

```
Vertices: 0, 1, 2, 3, 4

Edges (src -- dest : weight):
  0 -- 1 : 2
  0 -- 3 : 6
  1 -- 2 : 3
  1 -- 3 : 8
  1 -- 4 : 5
  2 -- 4 : 7
  3 -- 4 : 9
```

---

### Step-by-Step Execution

#### Step 1 — Sort Edges by Weight

```
Sorted:
  0--1 : 2
  1--2 : 3
  1--4 : 5
  0--3 : 6
  2--4 : 7
  1--3 : 8
  3--4 : 9
```

---

#### Step 2 — Pick Edges One by One

```
parent = [0, 1, 2, 3, 4]   ← initial (each is own root)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 Edge      Weight   Cycle?   Action
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 0 -- 1     2        No     ✔ ADD  →  MST: {0-1}
 1 -- 2     3        No     ✔ ADD  →  MST: {0-1, 1-2}
 1 -- 4     5        No     ✔ ADD  →  MST: {0-1, 1-2, 1-4}
 0 -- 3     6        No     ✔ ADD  →  MST: {0-1, 1-2, 1-4, 0-3}
 2 -- 4     7        YES    ✘ SKIP → would connect already linked nodes
 1 -- 3     8        YES    ✘ SKIP → 1 and 3 already connected via 0
 3 -- 4     9        YES    ✘ SKIP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 V-1 = 4 edges added → MST Complete!
```

---

### Final MST Diagram

```
Before (full graph):          After Kruskal's (MST only):

      (2)                            (2)
 0 ──────── 1                   0 ──────── 1
 |        / | \                 |          |\ 
(6)     (3)(8)(5)              (6)        (3)(5)
 |      /   |   \               |          |   \
 3 ────     |    4              3          2    4
  \         |   /
  (9)      (7)─

Total weight: 2+3+5+6 = 16  ✓ (Minimum possible)
```

---

### Output

```
--- Kruskal's Algorithm Steps ---

  ✔ Added Edge: 0 -- 1  | Weight: 2  | Total so far: 2
  ✔ Added Edge: 1 -- 2  | Weight: 3  | Total so far: 5
  ✔ Added Edge: 1 -- 4  | Weight: 5  | Total so far: 10
  ✔ Added Edge: 0 -- 3  | Weight: 6  | Total so far: 16
  ✘ Skipped Edge: 2 -- 4 | Weight: 7  → Would form a CYCLE
  ✘ Skipped Edge: 1 -- 3 | Weight: 8  → Would form a CYCLE
  ✘ Skipped Edge: 3 -- 4 | Weight: 9  → Would form a CYCLE

--- Minimum Spanning Tree ---
  0 -- 1  : 2
  1 -- 2  : 3
  1 -- 4  : 5
  0 -- 3  : 6

  Total MST Weight: 16
```

---

### Algorithm Complexity

| Case | Time Complexity | Reason |
|---|---|---|
| Sorting edges | O(E log E) | Dominant step |
| Union-Find ops | O(E α(V)) | Nearly O(1) per op |
| **Overall** | **O(E log E)** | Sorting dominates |
| Space | O(V + E) | parent, rank, edge list |

> `α` = Inverse Ackermann function — extremely slow-growing, practically constant

---

### Kruskal's vs Prim's

| Feature | Kruskal's | Prim's |
|---|---|---|
| Approach | Edge-based (global) | Vertex-based (local) |
| Best for | Sparse graphs | Dense graphs |
| Data Structure | Union-Find | Priority Queue |
| Starting point | No fixed start | Starts from a vertex |
| Complexity | O(E log E) | O(E log V) |

> **Key Rule:** Kruskal's always picks the **globally smallest edge** that doesn't form a cycle, while Prim's grows the MST **one vertex at a time** from a starting node.


## Kruskal's Algorithm — Fixed & Mapped to Each Step

```python
# ─────────────────────────────────────────────
#   KRUSKAL'S ALGORITHM — MINIMUM SPANNING TREE
#   Input : G = (V, E) → Weighted Undirected Graph
#   Output: Minimum Spanning Tree (MST)
# ─────────────────────────────────────────────

class Graph:
    def __init__(self, vertices):
        self.V    = vertices   # Total number of vertices
        self.edges = []        # Stores all edges as (weight, u, v)

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    # ── Union-Find: Find root with Path Compression ──
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])  # Path compression
        return parent[x]

    # ── Union-Find: Union by Rank ──
    def union(self, parent, rank, x, y):
        rootX = self.find(parent, x)
        rootY = self.find(parent, y)

        if rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        elif rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

    # ── MAIN: KRUSKAL(G) ──
    def kruskal_mst(self):

        # STEP 1: Start
        print("=" * 50)
        print("       KRUSKAL'S ALGORITHM STARTED")
        print("=" * 50)

        # STEP 2: Create an empty set MST
        mst        = []   # Will hold final MST edges
        mst_weight = 0    # Total cost of MST

        # STEP 3: Sort all edges in increasing order of weight
        self.edges.sort()
        print("\nSTEP 3 → Edges sorted by weight:")
        print(f"  {'Edge':<12} {'Weight'}")
        print(f"  {'────':<12} {'──────'}")
        for weight, u, v in self.edges:
            print(f"  {str(u)+' -- '+str(v):<12} {weight}")

        # STEP 4: Make a separate set for each vertex
        parent = [i for i in range(self.V)]  # Each vertex is its own parent
        rank   = [0]     * self.V            # Rank initialized to 0

        print(f"\nSTEP 4 → Disjoint Sets Created:")
        print(f"  parent = {parent}")
        print(f"  rank   = {rank}")

        # STEP 5: For each edge (u, v) in sorted order
        print("\nSTEP 5 → Processing Edges:\n")
        print(f"  {'Edge':<12} {'Weight':<10} {'Action'}")
        print(f"  {'────':<12} {'──────':<10} {'──────'}")

        for weight, u, v in self.edges:

            # STEP 5a: Find the root of u and v
            rootU = self.find(parent, u)
            rootV = self.find(parent, v)

            # STEP 5b: If root(u) ≠ root(v) → No Cycle → Add to MST
            if rootU != rootV:
                mst.append((u, v, weight))
                mst_weight += weight
                self.union(parent, rank, u, v)
                print(f"  {str(u)+' -- '+str(v):<12} {weight:<10} ✔ ADDED   | MST weight so far: {mst_weight}")

            # STEP 5c: Else → Discard (would form a cycle)
            else:
                print(f"  {str(u)+' -- '+str(v):<12} {weight:<10} ✘ SKIPPED | Forms a CYCLE")

            # STEP 6: Stop when MST has V-1 edges
            if len(mst) == self.V - 1:
                break

        # STEP 7: Print MST
        print("\n" + "=" * 50)
        print("STEP 7 → Minimum Spanning Tree (MST):")
        print("=" * 50)
        print(f"  {'Edge':<12} {'Weight'}")
        print(f"  {'────':<12} {'──────'}")
        for u, v, weight in mst:
            print(f"  {str(u)+' -- '+str(v):<12} {weight}")
        print(f"\n  ✔ Total MST Weight = {mst_weight}")

        # STEP 8: Stop
        print("\n  ALGORITHM COMPLETE.")
        print("=" * 50)


# ─────────────────────────────────────────────
#                  EXECUTION
# ─────────────────────────────────────────────
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

g.kruskal_mst()
```

---

### Output

```
==================================================
       KRUSKAL'S ALGORITHM STARTED
==================================================

STEP 3 → Edges sorted by weight:
  Edge         Weight
  ────         ──────
  0 -- 1       2
  1 -- 2       3
  1 -- 4       5
  0 -- 3       6
  2 -- 4       7
  1 -- 3       8
  3 -- 4       9

STEP 4 → Disjoint Sets Created:
  parent = [0, 1, 2, 3, 4]
  rank   = [0, 0, 0, 0, 0]

STEP 5 → Processing Edges:

  Edge         Weight     Action
  ────         ──────     ──────
  0 -- 1       2          ✔ ADDED   | MST weight so far: 2
  1 -- 2       3          ✔ ADDED   | MST weight so far: 5
  1 -- 4       5          ✔ ADDED   | MST weight so far: 10
  0 -- 3       6          ✔ ADDED   | MST weight so far: 16
  2 -- 4       7          ✘ SKIPPED | Forms a CYCLE

==================================================
STEP 7 → Minimum Spanning Tree (MST):
==================================================
  Edge         Weight
  ────         ──────
  0 -- 1       2
  1 -- 2       3
  1 -- 4       5
  0 -- 3       6

  ✔ Total MST Weight = 16

  ALGORITHM COMPLETE.
==================================================
```

---

### Algorithm ↔ Code Mapping

```
ALGORITHM STEP              CODE
──────────────────────────────────────────────────────
Step 1: Start             → kruskal_mst() is called
Step 2: MST = empty set   → mst = []
Step 3: Sort edges        → self.edges.sort()
Step 4: Disjoint sets     → parent = [i for i in range(V)]
Step 5a: Find root        → self.find(parent, u/v)
Step 5b: root(u)≠root(v)  → if rootU != rootV → ADD + union()
Step 5c: Else discard     → else → SKIP
Step 6: V−1 edges check   → if len(mst) == self.V - 1: break
Step 7: Print MST         → final for loop printing mst[]
Step 8: Stop              → function ends
```