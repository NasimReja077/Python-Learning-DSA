# 📚 Complete Graph Unit — Step-by-Step Learning Guide

# 🗺️ Learning Roadmap

```
STEP 1 → Graph Basics & Terminology        (Day 1)
STEP 2 → Graph Representation              (Day 2)
STEP 3 → Path Matrix                       (Day 2)
STEP 4 → BFS Traversal                     (Day 3)
STEP 5 → DFS Traversal                     (Day 3)
STEP 6 → Minimum Spanning Tree (Prim's)    (Day 4)
STEP 7 → Minimum Spanning Tree (Kruskal's) (Day 5)
STEP 8 → Practice Questions                (Day 6)
```

---

# ✅ STEP 1 — Graph Basics & Terminology

## 📖 Theory

A **Graph** is a non-linear data structure consisting of:
- **Vertices (V)** → Nodes/Points
- **Edges (E)** → Connections between nodes
- Written as **G = (V, E)**

---

## 📌 Types of Graphs

### 1. Undirected Graph
- Edges have **no direction**
- If A→B exists, then B→A also exists

```
    A --- B
    |     |
    C --- D
```

### 2. Directed Graph (Digraph)
- Edges have **direction** (arrow)
- A→B does NOT mean B→A

```
    A --→ B
    ↓     ↓
    C --→ D
```

### 3. Weighted Graph
- Each edge has a **weight/cost**

```
    A --5-- B
    |       |
    3       7
    |       |
    C --2-- D
```

### 4. Complete Graph
- Every vertex connected to every other vertex
- Edges = **n(n-1)/2** for undirected
- Example: 4 vertices → 4×3/2 = **6 edges**

### 5. Connected Graph
- There is a path between every pair of vertices

### 6. Disconnected Graph
- Some vertices have no path between them

### 7. Cyclic Graph
- Contains at least one **cycle** (closed path)

### 8. Acyclic Graph
- Contains **no cycle**

---

## 📌 Important Terminology

| Term | Definition | Example |
|------|-----------|---------|
| **Vertex/Node** | Basic unit of graph | A, B, C |
| **Edge** | Connection between 2 vertices | A-B |
| **Degree** | Number of edges at a vertex | deg(A) = 3 |
| **In-degree** | Edges coming INTO vertex (directed) | |
| **Out-degree** | Edges going OUT of vertex (directed) | |
| **Path** | Sequence of vertices connected by edges | A→B→C |
| **Cycle** | Path that starts and ends at same vertex | A→B→C→A |
| **Adjacent** | Two vertices connected by an edge | |
| **Isolated Vertex** | Vertex with degree 0 | |

---

## 🧠 Important Formulas (1 Mark Questions)

```
✅ Edges in complete graph (undirected) = n(n-1)/2
✅ Edges in complete graph (directed)   = n(n-1)
✅ Adjacency Matrix size                = n × n
✅ Elements in adjacency matrix         = n²
   (7 vertices → 7×7 = 49 elements)
✅ Sum of all degrees = 2 × (number of edges)
```

---

# ✅ STEP 2 — Graph Representation

## 📖 Theory

Two main ways to store a graph in memory:

---

## 2A. Adjacency Matrix

- A **2D array** of size V×V
- `matrix[i][j] = 1` if edge exists between i and j
- `matrix[i][j] = 0` if no edge

### Example Graph:
```
    0 --- 1
    |   / |
    |  /  |
    2 --- 3
```

### Adjacency Matrix:
```
     0  1  2  3
0  [ 0  1  1  0 ]
1  [ 1  0  1  1 ]
2  [ 1  1  0  1 ]
3  [ 0  1  1  0 ]
```

### ✅ Python Code — Adjacency Matrix

```python
# Graph Representation using Adjacency Matrix

class GraphMatrix:
    def __init__(self, vertices):
        self.V = vertices
        # Create V×V matrix filled with 0
        self.matrix = [[0] * vertices for _ in range(vertices)]
    
    def add_edge(self, u, v):
        # Undirected graph — add both directions
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1
    
    def display(self):
        print("Adjacency Matrix:")
        print("  ", end="")
        for i in range(self.V):
            print(i, end=" ")
        print()
        for i in range(self.V):
            print(i, end=" ")
            for j in range(self.V):
                print(self.matrix[i][j], end=" ")
            print()

# ---- MAIN PROGRAM ----
g = GraphMatrix(4)   # 4 vertices: 0,1,2,3
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.display()
```

### Output:
```
Adjacency Matrix:
   0 1 2 3
0  0 1 1 0
1  1 0 1 1
2  1 1 0 1
3  0 1 1 0
```

---

## 2B. Adjacency List

- Array of **linked lists**
- Each vertex stores list of its neighbors
- **Better for sparse graphs** (fewer edges)

### Example:
```
0 → [1, 2]
1 → [0, 2, 3]
2 → [0, 1, 3]
3 → [1, 2]
```

### ✅ Python Code — Adjacency List

```python
# Graph Representation using Adjacency List

class GraphList:
    def __init__(self, vertices):
        self.V = vertices
        # Dictionary to store adjacency list
        self.adj = {i: [] for i in range(vertices)}
    
    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)   # Undirected
    
    def display(self):
        print("Adjacency List:")
        for vertex in self.adj:
            print(f"{vertex} → {self.adj[vertex]}")

# ---- MAIN PROGRAM ----
g = GraphList(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.display()
```

### Output:
```
Adjacency List:
0 → [1, 2]
1 → [0, 2, 3]
2 → [0, 1, 3]
3 → [1, 2]
```

---

## 📊 Comparison Table

| Feature | Adjacency Matrix | Adjacency List |
|---------|:----------------:|:--------------:|
| Space | O(V²) | O(V+E) |
| Add Edge | O(1) | O(1) |
| Check Edge | O(1) | O(V) |
| Best For | Dense Graph | Sparse Graph |

---

# ✅ STEP 3 — Path Matrix

## 📖 Theory

- Also called **Reachability Matrix**
- `path[i][j] = 1` if there is a path from vertex i to j
- `path[i][j] = 0` if no path exists
- Uses **Warshall's Algorithm**

### Algorithm:
```
1. Start with Adjacency Matrix as Path Matrix
2. For each intermediate vertex k:
   For each i:
     For each j:
       path[i][j] = path[i][j] OR (path[i][k] AND path[k][j])
```

### ✅ Python Code — Path Matrix

```python
# Path Matrix using Warshall's Algorithm

def path_matrix(graph, V):
    # Copy adjacency matrix
    path = [row[:] for row in graph]
    
    # Add self-loops (vertex can reach itself)
    for i in range(V):
        path[i][i] = 1
    
    # Warshall's Algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                path[i][j] = path[i][j] or (path[i][k] and path[k][j])
    
    return path

def display_matrix(matrix, V, title):
    print(f"\n{title}:")
    print("  ", end="")
    for i in range(V): print(i, end=" ")
    print()
    for i in range(V):
        print(i, end=" ")
        for j in range(V):
            print(matrix[i][j], end=" ")
        print()

# ---- MAIN PROGRAM ----
V = 4
# Adjacency Matrix
graph = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]

display_matrix(graph, V, "Adjacency Matrix")
result = path_matrix(graph, V)
display_matrix(result, V, "Path Matrix")
```

### Output:
```
Adjacency Matrix:
   0 1 2 3
0  0 1 0 0
1  0 0 1 0
2  0 0 0 1
3  0 0 0 0

Path Matrix:
   0 1 2 3
0  1 1 1 1
1  0 1 1 1
2  0 0 1 1
3  0 0 0 1
```

---

# ✅ STEP 4 — BFS (Breadth First Search)

## 📖 Theory

- Traverses graph **level by level**
- Uses **QUEUE** data structure
- Visits all neighbors before going deeper

### BFS on this graph:
```
        0
       / \
      1   2
     / \
    3   4
```
**BFS order starting from 0: 0 → 1 → 2 → 3 → 4**

---

## 📌 BFS Algorithm

```
BFS(Graph G, start vertex s):
1. Create empty Queue Q
2. Create visited[] array, set all = False
3. Mark visited[s] = True
4. Enqueue s into Q
5. While Q is not empty:
   a. Dequeue vertex u from Q
   b. Print u
   c. For each neighbor v of u:
      If visited[v] == False:
         Mark visited[v] = True
         Enqueue v into Q
6. End
```

---

## ✅ Python Code — BFS

```python
# BFS - Breadth First Search
from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = {i: [] for i in range(vertices)}
    
    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
    
    def BFS(self, start):
        # Step 1: Create visited array
        visited = [False] * self.V
        
        # Step 2: Create Queue
        queue = deque()
        
        # Step 3: Mark start as visited and enqueue
        visited[start] = True
        queue.append(start)
        
        print("BFS Traversal: ", end="")
        
        # Step 4: Loop until queue empty
        while queue:
            # Dequeue vertex
            vertex = queue.popleft()
            print(vertex, end=" ")
            
            # Visit all neighbors
            for neighbor in self.adj[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        print()

# ---- MAIN PROGRAM ----
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)

print("Graph Edges: 0-1, 0-2, 1-3, 1-4, 2-5")
g.BFS(0)
```

### Output:
```
Graph Edges: 0-1, 0-2, 1-3, 1-4, 2-5
BFS Traversal: 0 1 2 3 4 5
```

### 📊 BFS Complexity
| Case | Time | Space |
|------|------|-------|
| All cases | O(V+E) | O(V) |

---

# ✅ STEP 5 — DFS (Depth First Search)

## 📖 Theory

- Traverses graph **as deep as possible** first
- Uses **STACK** data structure (or Recursion)
- Backtracks when no unvisited neighbor found

### DFS on same graph:
```
        0
       / \
      1   2
     / \
    3   4
```
**DFS order starting from 0: 0 → 1 → 3 → 4 → 2 → 5**

---

## 📌 DFS Algorithm

```
DFS(Graph G, start vertex s):
1. Create visited[] array, set all = False
2. Call DFS_Visit(s)

DFS_Visit(vertex u):
1. Mark visited[u] = True
2. Print u
3. For each neighbor v of u:
   If visited[v] == False:
      Call DFS_Visit(v)
```

---

## ✅ Python Code — DFS (Recursive)

```python
# DFS - Depth First Search (Recursive)

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = {i: [] for i in range(vertices)}
    
    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
    
    def DFS_visit(self, vertex, visited):
        # Mark current vertex as visited
        visited[vertex] = True
        print(vertex, end=" ")
        
        # Recursively visit all unvisited neighbors
        for neighbor in self.adj[vertex]:
            if not visited[neighbor]:
                self.DFS_visit(neighbor, visited)
    
    def DFS(self, start):
        # Create visited array
        visited = [False] * self.V
        print("DFS Traversal: ", end="")
        self.DFS_visit(start, visited)
        print()

# ---- MAIN PROGRAM ----
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)

print("Graph Edges: 0-1, 0-2, 1-3, 1-4, 2-5")
g.DFS(0)
```

### Output:
```
Graph Edges: 0-1, 0-2, 1-3, 1-4, 2-5
DFS Traversal: 0 1 3 4 2 5
```

---

## ✅ Python Code — DFS (Using Stack — Iterative)

```python
# DFS using Stack (Iterative)

def DFS_stack(adj, start, V):
    visited = [False] * V
    stack = []
    
    stack.append(start)
    print("DFS (Stack): ", end="")
    
    while stack:
        vertex = stack.pop()
        
        if not visited[vertex]:
            visited[vertex] = True
            print(vertex, end=" ")
            
            # Push neighbors in reverse order
            for neighbor in reversed(adj[vertex]):
                if not visited[neighbor]:
                    stack.append(neighbor)
    print()
```

---

## 📊 BFS vs DFS Comparison (Very Important!)

| Feature | BFS | DFS |
|---------|-----|-----|
| **Data Structure** | Queue | Stack/Recursion |
| **Traversal** | Level by level | Depth first |
| **Time Complexity** | O(V+E) | O(V+E) |
| **Space Complexity** | O(V) | O(V) |
| **Shortest Path** | ✅ Yes | ❌ No |
| **Used For** | Shortest path, web crawling | Topological sort, cycle detection |
| **Memory** | More (stores all level nodes) | Less |

---

# ✅ STEP 6 — Prim's Algorithm (MST) 🔴 Most Important!

## 📖 Theory

- Finds **Minimum Spanning Tree (MST)**
- MST = connects all vertices with **minimum total edge weight** and **no cycle**
- Prim's starts from one vertex and **grows** the tree

### Example Graph:
```
       2      3
   A ----- B ----- C
   |      /|       |
  6|    /  |4     |5
   |  / 1  |       |
   D ----- E ----- F
       4       6
```

---

## 📌 Prim's Algorithm

```
PRIM(Graph G, start vertex):
1. Create key[] = infinity for all vertices
2. Create parent[] = -1 for all vertices
3. Create inMST[] = False for all vertices
4. Set key[start] = 0
5. Repeat V times:
   a. Pick vertex u with minimum key NOT in MST
   b. Add u to MST (inMST[u] = True)
   c. For each neighbor v of u:
      If v not in MST AND weight(u,v) < key[v]:
         key[v] = weight(u,v)
         parent[v] = u
6. MST edges = (parent[v], v) for all v
```

---

## ✅ Python Code — Prim's Algorithm (MAKAUT Exam Ready!)

```python
# Prim's Algorithm - Minimum Spanning Tree
# 🔴 Most Important — 10 marks in Paper 3!

import sys

class PrimsMST:
    def __init__(self, vertices):
        self.V = vertices
    
    def min_key(self, key, inMST):
        # Find vertex with minimum key value not in MST
        minimum = sys.maxsize
        min_vertex = -1
        
        for v in range(self.V):
            if key[v] < minimum and not inMST[v]:
                minimum = key[v]
                min_vertex = v
        
        return min_vertex
    
    def prim_mst(self, graph):
        # Step 1: Initialize arrays
        key = [sys.maxsize] * self.V    # Key values
        parent = [-1] * self.V          # Parent array
        inMST = [False] * self.V        # MST set
        
        # Step 2: Start from vertex 0
        key[0] = 0
        
        print("Prim's MST Algorithm")
        print("=" * 40)
        
        # Step 3: Find MST with V vertices
        for _ in range(self.V):
            # Pick minimum key vertex not in MST
            u = self.min_key(key, inMST)
            
            # Add to MST
            inMST[u] = True
            
            # Update neighbors
            for v in range(self.V):
                # Check: edge exists, v not in MST,
                # weight is less than current key
                if (graph[u][v] > 0 and
                    not inMST[v] and
                    graph[u][v] < key[v]):
                    
                    key[v] = graph[u][v]
                    parent[v] = u
        
        # Step 4: Print MST
        total_weight = 0
        print("\nEdge \t Weight")
        print("-" * 20)
        for i in range(1, self.V):
            print(f"{parent[i]} - {i} \t {graph[i][parent[i]]}")
            total_weight += graph[i][parent[i]]
        
        print("-" * 20)
        print(f"Total MST Weight: {total_weight}")

# ---- MAIN PROGRAM ----
# Graph as Adjacency Matrix (0 = no edge)
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

p = PrimsMST(5)
p.prim_mst(graph)
```

### Output:
```
Prim's MST Algorithm
========================================

Edge     Weight
--------------------
0 - 1    2
1 - 2    3
0 - 3    6
1 - 4    5
--------------------
Total MST Weight: 16
```

### 📊 Prim's Complexity
| Complexity | Value |
|-----------|-------|
| Time | O(V²) |
| Space | O(V) |
| Best For | Dense Graphs |

---

# ✅ STEP 7 — Kruskal's Algorithm (MST)

## 📖 Theory

- Also finds **Minimum Spanning Tree**
- Sorts ALL edges by weight
- Adds edges one by one, **skipping edges that form a cycle**
- Uses **Union-Find** (Disjoint Set) data structure

---

## 📌 Kruskal's Algorithm

```
KRUSKAL(Graph G):
1. Sort all edges by weight (ascending)
2. Create parent[] for Union-Find
3. For each edge (u, v) in sorted order:
   a. Find root of u and root of v
   b. If roots are different (no cycle):
      Add edge to MST
      Union(u, v)
4. Stop when MST has V-1 edges
```

---

## ✅ Python Code — Kruskal's Algorithm

```python
# Kruskal's Algorithm - Minimum Spanning Tree

class KruskalMST:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []   # List of (weight, u, v)
    
    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))
    
    # Find root of vertex (with path compression)
    def find(self, parent, vertex):
        if parent[vertex] != vertex:
            parent[vertex] = self.find(parent, parent[vertex])
        return parent[vertex]
    
    # Union two sets
    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
    
    def kruskal_mst(self):
        # Step 1: Sort edges by weight
        self.edges.sort()
        
        # Step 2: Initialize Union-Find
        parent = list(range(self.V))
        rank = [0] * self.V
        
        mst = []
        total_weight = 0
        
        print("Kruskal's MST Algorithm")
        print("=" * 40)
        print("Sorted Edges:", self.edges)
        print()
        
        # Step 3: Process each edge
        for weight, u, v in self.edges:
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)
            
            # No cycle — add to MST
            if root_u != root_v:
                mst.append((u, v, weight))
                total_weight += weight
                self.union(parent, rank, root_u, root_v)
                print(f"Added edge: {u} - {v}, Weight: {weight}")
            else:
                print(f"Skipped (cycle): {u} - {v}, Weight: {weight}")
            
            # MST complete
            if len(mst) == self.V - 1:
                break
        
        print("\nFinal MST:")
        print("Edge \t Weight")
        print("-" * 20)
        for u, v, w in mst:
            print(f"{u} - {v} \t {w}")
        print("-" * 20)
        print(f"Total MST Weight: {total_weight}")

# ---- MAIN PROGRAM ----
g = KruskalMST(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

g.kruskal_mst()
```

### Output:
```
Kruskal's MST Algorithm
========================================
Sorted Edges: [(2,0,1),(3,1,2),(5,1,4),(6,0,3),(7,2,4),(8,1,3),(9,3,4)]

Added edge: 0 - 1, Weight: 2
Added edge: 1 - 2, Weight: 3
Added edge: 1 - 4, Weight: 5
Added edge: 0 - 3, Weight: 6

Final MST:
Edge     Weight
--------------------
0 - 1    2
1 - 2    3
1 - 4    5
0 - 3    6
--------------------
Total MST Weight: 16
```

---

## 📊 Prim's vs Kruskal's Comparison

| Feature | Prim's | Kruskal's |
|---------|--------|-----------|
| **Approach** | Vertex based | Edge based |
| **Data Structure** | Priority Queue | Union-Find |
| **Time Complexity** | O(V²) | O(E log E) |
| **Best For** | Dense graph | Sparse graph |
| **Starting Point** | Any vertex | Smallest edge |
| **Cycle Check** | Not needed | Union-Find |

---

# ✅ STEP 8 — Complete Combined Program

```python
# ============================================
# COMPLETE GRAPH PROGRAM — MAKAUT Exam Ready
# MCAN-201 | All Topics in One File
# ============================================

from collections import deque
import sys

class CompleteGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = {i: [] for i in range(vertices)}
        self.matrix = [[0]*vertices for _ in range(vertices)]
    
    def add_edge(self, u, v, weight=1):
        self.adj[u].append(v)
        self.adj[v].append(u)
        self.matrix[u][v] = weight
        self.matrix[v][u] = weight
    
    # ---- BFS ----
    def BFS(self, start):
        visited = [False] * self.V
        queue = deque([start])
        visited[start] = True
        result = []
        while queue:
            v = queue.popleft()
            result.append(v)
            for n in self.adj[v]:
                if not visited[n]:
                    visited[n] = True
                    queue.append(n)
        return result
    
    # ---- DFS ----
    def DFS(self, start):
        visited = [False] * self.V
        result = []
        self._dfs(start, visited, result)
        return result
    
    def _dfs(self, v, visited, result):
        visited[v] = True
        result.append(v)
        for n in self.adj[v]:
            if not visited[n]:
                self._dfs(n, visited, result)
    
    # ---- Prim's MST ----
    def prims(self):
        key = [sys.maxsize] * self.V
        parent = [-1] * self.V
        inMST = [False] * self.V
        key[0] = 0
        for _ in range(self.V):
            u = min((v for v in range(self.V) 
                     if not inMST[v]), key=lambda v: key[v])
            inMST[u] = True
            for v in range(self.V):
                if (self.matrix[u][v] and not inMST[v] and
                    self.matrix[u][v] < key[v]):
                    key[v] = self.matrix[u][v]
                    parent[v] = u
        return [(parent[i], i, self.matrix[i][parent[i]]) 
                for i in range(1, self.V)]

# ---- MAIN ----
g = CompleteGraph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)

print("BFS from 0:", g.BFS(0))
print("DFS from 0:", g.DFS(0))
print("Prim's MST:", g.prims())
```

---

# 📋 Final Quick Revision Sheet

```
╔══════════════════════════════════════════════════╗
║           GRAPH QUICK REVISION                   ║
╠══════════════════════════════════════════════════╣
║ Adjacency Matrix size    → n × n                 ║
║ Complete graph edges     → n(n-1)/2              ║
║ BFS uses                 → QUEUE                 ║
║ DFS uses                 → STACK / Recursion     ║
║ BFS/DFS Time Complexity  → O(V+E)                ║
║ Prim's Time Complexity   → O(V²)                 ║
║ Kruskal's Time           → O(E log E)            ║
║ Prim's best for          → Dense graphs          ║
║ Kruskal's best for       → Sparse graphs         ║
║ MST has edges            → V-1 edges             ║
╚══════════════════════════════════════════════════╝
```

---

# 🗓️ 6-Day Study Plan

| Day | Topics | Time |
|-----|--------|------|
| **Day 1** | Terminology + Types of Graphs | 2 hrs |
| **Day 2** | Adjacency Matrix + List + Path Matrix | 3 hrs |
| **Day 3** | BFS (theory + code + trace) | 3 hrs |
| **Day 3** | DFS (theory + code + trace) | 3 hrs |
| **Day 4** | Prim's Algorithm (theory + code) 🔴 | 4 hrs |
| **Day 5** | Kruskal's Algorithm (theory + code) | 3 hrs |
| **Day 6** | Practice all 50 questions + revision | 4 hrs |