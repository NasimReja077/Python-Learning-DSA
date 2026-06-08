## Graph Adjacency Matrix - Line by Line Explanation

---

### Class Definition & Constructor

```python
class Graph:
```
Creates a class called `Graph` to represent an **undirected graph**.

---

```python
def __init__(self, vertex):
```
Constructor that runs when you create a Graph object. Takes `vertex` = number of nodes.

---

```python
self.mat = [ [0]*vertex for x in range(vertex)]
```
Creates a **2D matrix (list of lists)** filled with zeros.
For `vertex = 5`, it creates a **5×5 matrix**:

```
  0  1  2  3  4   ← destination
0[0, 0, 0, 0, 0]
1[0, 0, 0, 0, 0]
2[0, 0, 0, 0, 0]
3[0, 0, 0, 0, 0]
4[0, 0, 0, 0, 0]
↑ source
```

---

```python
self.size = vertex
```
Stores `5` as the size — used later for **boundary checking**.

---

### add_edge Method

```python
def add_edge(self, src, dest):
```
Method to connect two nodes `src` (source) and `dest` (destination).

---

```python
if(0 <= src < self.size and 0 <= dest < self.size):
```
**Validates** that both nodes are within range (0 to 4). Prevents index-out-of-bound errors.

---

```python
self.mat[src][dest] = 1
self.mat[dest][src] = 1
```
Sets **both directions** to `1` because it's an **undirected graph**.
- `mat[src][dest] = 1` → edge from src → dest
- `mat[dest][src] = 1` → edge from dest → src (reverse)

---

### print Method

```python
for row in self.mat:
    print(' '.join(map(str, row)))
```
Loops through each row and prints it as a space-separated string.
`map(str, row)` converts integers to strings so `join` can work.

---

## Visual Diagram — After All Edges Are Added

```
G.add_edge(0,1) → connects 0 and 1
G.add_edge(0,2) → connects 0 and 2
G.add_edge(1,3) → connects 1 and 3
G.add_edge(2,4) → connects 2 and 4
G.add_edge(3,4) → connects 3 and 4
G.add_edge(2,3) → connects 2 and 3
```

### Graph Structure:
```
        0
       / \
      1   2
      |  / \
      3 ----4
```

---

### Final Adjacency Matrix:

```
   0  1  2  3  4
0[ 0, 1, 1, 0, 0 ]   → 0 connects to 1, 2
1[ 1, 0, 0, 1, 0 ]   → 1 connects to 0, 3
2[ 1, 0, 0, 1, 1 ]   → 2 connects to 0, 3, 4
3[ 0, 1, 1, 0, 1 ]   → 3 connects to 1, 2, 4
4[ 0, 0, 1, 1, 0 ]   → 4 connects to 2, 3
```

**Rule:** `mat[i][j] = 1` means node `i` and node `j` are connected.
Since the graph is **undirected**, the matrix is always **symmetric** (mirrored along the diagonal).