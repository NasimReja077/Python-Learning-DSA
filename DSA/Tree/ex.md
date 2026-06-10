# Applications of Binary Trees — Complete In-Depth Explanation

---

## Overview of Binary Tree Applications

Binary Trees are not just a theoretical data structure. They form the foundation of some of the most important algorithms and systems in computer science. Every application listed below uses the binary tree structure in a specific way to solve a real problem efficiently.

```
Application 1  → Heap (Priority Queue, Heap Sort)
Application 2  → Expression Tree (Compiler Design, Calculator)
Application 3  → Huffman Coding Tree (Data Compression)
Application 4  → Decision Tree (AI, Machine Learning)
```

---

# APPLICATION 1 — HEAP

---

## What is a Heap?

A Heap is a special complete binary tree that satisfies the heap property. It is the most important application of binary trees because it powers priority queues and one of the best sorting algorithms (Heap Sort).

A complete binary tree means every level is completely filled except possibly the last level, and the last level is filled from left to right with no gaps.

The heap property defines the relationship between a parent and its children:

```
Max Heap Property:
  Every parent node is GREATER THAN OR EQUAL TO its children.
  The largest element is always at the ROOT.

Min Heap Property:
  Every parent node is LESS THAN OR EQUAL TO its children.
  The smallest element is always at the ROOT.
```

A heap is NOT a BST. There is no ordering between left and right children. A left child can be greater or smaller than the right child — only the parent-child relationship matters.

---

## Heap Stored as Array (Most Important Concept)

Because a heap is a complete binary tree, it can be stored efficiently in an array without any pointers. This is the most common and most efficient representation.

For a node at index i (using 1-based indexing):

```
Left child  → index 2 * i
Right child → index 2 * i + 1
Parent      → index i // 2
Root        → index 1

Example Max Heap:
          100
         /   \
        70    60
       / \   / \
      50  40 30  20

Array: [_, 100, 70, 60, 50, 40, 30, 20]
Index:   0   1   2   3   4   5   6   7

Node at index 2 (value=70):
  Left child  = index 4 (value=50) ✓
  Right child = index 5 (value=40) ✓
  Parent      = index 1 (value=100) ✓
```

---

## Max Heap vs Min Heap

```
Max Heap:                        Min Heap:
        100                              1
       /   \                           /   \
      70    60                         5    3
     / \   / \                        / \  / \
    50  40 30  20                    8   7 6   4

Root = Maximum element            Root = Minimum element
Used for: Heap Sort (desc),       Used for: Priority Queue (min),
          Priority Queue (max)              Dijkstra's algorithm,
                                           Prim's MST algorithm
```

---

## Operation 1 — Heapify (The Core Operation)

Heapify restores the heap property at a given node when it is violated. It assumes both subtrees are already valid heaps but the root might be in the wrong place.

### Max Heapify Algorithm

```
ALGORITHM: MaxHeapify(A, i, n)

Input  : Array A, index i, heap size n
Output : Max heap with root at i

Step 1: left  = 2 * i
        right = 2 * i + 1
        largest = i               ← assume current node is largest

Step 2: IF left <= n AND A[left] > A[largest]:
            largest = left        ← left child is larger

Step 3: IF right <= n AND A[right] > A[largest]:
            largest = right       ← right child is larger

Step 4: IF largest != i:
            Swap A[i] and A[largest]   ← move larger element up
            MaxHeapify(A, largest, n)  ← fix the subtree recursively
```

### Example — Max Heapify

```
Array: [_, 10, 70, 60, 50, 40, 30, 20]
         0   1   2   3   4   5   6   7

Node at index 1 (value=10) violates max heap:
          10        ← violates (should be max)
         /   \
        70    60
       / \   / \
      50  40 30  20

Heapify(A, 1, 7):
  left=2, right=3. largest=2 (value=70).
  Swap A[1] and A[2]: swap 10 and 70.

          70
         /   \
        10    60
       / \   / \
      50  40 30  20

  Heapify(A, 2, 7): ← fix subtree at index 2
  left=4(50), right=5(40). largest=4.
  Swap A[2] and A[4]: swap 10 and 50.

          70
         /   \
        50    60
       / \   / \
      10  40 30  20

  Heapify(A, 4, 7): left=8>7, right=9>7. No children. STOP.

Final: Valid max heap. ✓
```

### Python Code — Heapify

```python
def max_heapify(arr, i, n):
    largest = i
    left    = 2 * i
    right   = 2 * i + 1

    if left <= n and arr[left] > arr[largest]:
        largest = left

    if right <= n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]   # swap
        max_heapify(arr, largest, n)                  # recurse


def min_heapify(arr, i, n):
    smallest = i
    left     = 2 * i
    right    = 2 * i + 1

    if left <= n and arr[left] < arr[smallest]:
        smallest = left

    if right <= n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, smallest, n)
```

Complexity of Heapify:
```
Time  → O(log n)  — tree height, at most log n levels
Space → O(log n) recursive stack, O(1) iterative
```

---

## Operation 2 — Build Heap

Convert any arbitrary array into a valid heap. The key insight is that all leaf nodes (from index n//2 + 1 to n) are already valid heaps by themselves (single-node heaps). So we only need to heapify the internal nodes, starting from the last internal node (n//2) down to the root.

### Algorithm — Build Max Heap

```
ALGORITHM: BuildMaxHeap(A, n)

Step 1: FOR i = n//2 DOWNTO 1:
            MaxHeapify(A, i, n)

Step 2: Array A is now a valid max heap.
```

### Example — Build Max Heap from [_, 3, 9, 2, 1, 4, 5, 8, 6, 7]

```
Initial array: [_, 3, 9, 2, 1, 4, 5, 8, 6, 7]
n = 9, start heapify from i = 9//2 = 4

         3           (index 1)
        / \
       9   2         (index 2,3)
      / \ / \
     1  4 5  8       (index 4,5,6,7)
    / \
   6   7             (index 8,9)

Step 1: i=4, node value=1, children at 8(6),9(7). largest=9(7). Swap 1,7.
         3
        / \
       9   2
      / \ / \
     7  4 5  8
    / \
   6   1

Step 2: i=3, node value=2, children at 6(5),7(8). largest=7(8). Swap 2,8.
         3
        / \
       9   8
      / \ / \
     7  4 5  2
    / \
   6   1

Step 3: i=2, node value=9, children at 4(7),5(4). 9 is largest. No swap.

Step 4: i=1, node value=3, children at 2(9),3(8). largest=2(9). Swap 3,9.
         9
        / \
       3   8
      / \ / \
     7  4 5  2
    / \
   6   1

  Heapify subtree at index 2 (value=3):
  children 4(7),5(4). largest=4(7). Swap 3,7.
         9
        / \
       7   8
      / \ / \
     3  4 5  2
    / \
   6   1

  Heapify subtree at index 4 (value=3):
  children 8(6),9(1). largest=8(6). Swap 3,6.
  Final Max Heap:
         9
        / \
       7   8
      / \ / \
     6  4 5  2
    / \
   3   1

Array: [_, 9, 7, 8, 6, 4, 5, 2, 3, 1]
```

Complexity of Build Heap:
```
Naively looks O(n log n) but actual analysis:
  = O(n)  ← proven using sum of geometric series

This is because most nodes are at lower levels and heapify at lower
levels takes very few steps. The total work across all levels is O(n).
```

---

## Operation 3 — Insert into Heap

Insert a new element and maintain the heap property.

### Algorithm — Insert into Max Heap

```
ALGORITHM: InsertMaxHeap(A, key, n)

Step 1: n = n + 1                        ← increase heap size
        A[n] = key                       ← place new key at end

Step 2: i = n                            ← start from inserted position

Step 3: WHILE i > 1 AND A[i//2] < A[i]: ← while parent smaller than child
            Swap A[i] and A[i//2]        ← swap with parent (bubble up)
            i = i // 2                   ← move up to parent

Step 4: Heap property restored.
```

This process is called "bubble up" or "sift up" — the new element keeps swapping with its parent until it finds its correct position.

### Example — Insert 85 into Max Heap

```
Max heap before insert:
         100
        /   \
       70    60
      / \   / \
     50  40 30  20

Array: [_, 100, 70, 60, 50, 40, 30, 20]

Step 1: Place 85 at end. n becomes 8.
        Array: [_, 100, 70, 60, 50, 40, 30, 20, 85]

         100
        /   \
       70    60
      / \   / \
     50  40 30  20
    /
   85           ← new node at index 8

Step 2: i=8. Parent = 8//2 = 4 (value=50). 85 > 50 → SWAP.
        i becomes 4.

         100
        /   \
       70    60
      / \   / \
     85  40 30  20
    /
   50

Step 3: i=4. Parent = 4//2 = 2 (value=70). 85 > 70 → SWAP.
        i becomes 2.

         100
        /   \
       85    60
      / \   / \
     70  40 30  20
    /
   50

Step 4: i=2. Parent = 2//2 = 1 (value=100). 85 < 100. STOP.

Final Max Heap:
         100
        /   \
       85    60
      / \   / \
     70  40 30  20
    /
   50
```

Complexity of Insert:
```
Time  → O(log n)  — at most log n swaps (height of tree)
Space → O(1)
```

---

## Operation 4 — Extract Maximum (Delete Root)

Remove the root (maximum element) and restore the heap property.

### Algorithm — Extract Max

```
ALGORITHM: ExtractMax(A, n)

Step 1: max_val = A[1]                   ← save the maximum (root)

Step 2: A[1] = A[n]                      ← move last element to root
        n = n - 1                        ← decrease heap size

Step 3: MaxHeapify(A, 1, n)             ← restore heap property from root

Step 4: RETURN max_val
```

### Example — Extract Max

```
Max heap:
         100
        /   \
       85    60
      / \   / \
     70  40 30  20

Array: [_, 100, 85, 60, 70, 40, 30, 20]

Step 1: Save max = 100.
Step 2: Move last element (20) to root. Remove last.

         20           ← violates heap property
        /   \
       85    60
      / \   /
     70  40 30

Step 3: MaxHeapify(A, 1, 6):
  Children 85, 60. largest=2(85). Swap 20,85.

         85
        /   \
       20    60
      / \   /
     70  40 30

  MaxHeapify(A, 2, 6):
  Children 70, 40. largest=4(70). Swap 20,70.

         85
        /   \
       70    60
      / \   /
     20  40 30

  MaxHeapify(A, 4, 6): no children. STOP.

Final heap after extracting 100:
         85
        /   \
       70    60
      / \   /
     20  40 30

Returned value: 100
```

Complexity of Extract Max:
```
Time  → O(log n)  — heapify from root takes O(log n)
Space → O(1)
```

---

## Operation 5 — Heap Sort

Heap Sort is one of the most elegant sorting algorithms. It works in two phases:

```
Phase 1: Build a max heap from the input array.       Time: O(n)
Phase 2: Repeatedly extract max and place at end.     Time: O(n log n)
Total time: O(n log n) always.
```

### Algorithm — Heap Sort

```
ALGORITHM: HeapSort(A, n)

Phase 1 — Build Max Heap:
    FOR i = n//2 DOWNTO 1:
        MaxHeapify(A, i, n)

Phase 2 — Sort:
    FOR i = n DOWNTO 2:
        Swap A[1] and A[i]       ← move current max to end
        MaxHeapify(A, 1, i-1)    ← restore heap for remaining elements
```

### Full Python Code — Heap Implementation

```python
# ──────────────────────────────────────────────
#  COMPLETE HEAP IMPLEMENTATION
# ──────────────────────────────────────────────

class MaxHeap:
    def __init__(self):
        self.heap = [None]    # 1-based indexing, index 0 unused
        self.n    = 0

    # ── Heapify (sift down) ──
    def _heapify(self, i):
        largest = i
        left    = 2 * i
        right   = 2 * i + 1

        if left  <= self.n and self.heap[left]  > self.heap[largest]:
            largest = left
        if right <= self.n and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._heapify(largest)

    # ── Build heap from list ──
    def build_heap(self, data):
        self.heap = [None] + data[:]   # copy with 1-based indexing
        self.n    = len(data)
        for i in range(self.n // 2, 0, -1):
            self._heapify(i)
        print("Heap built:", self.heap[1:])

    # ── Insert ──
    def insert(self, key):
        self.heap.append(key)
        self.n += 1
        i = self.n
        while i > 1 and self.heap[i // 2] < self.heap[i]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //= 2
        print(f"Inserted {key}. Heap: {self.heap[1:]}")

    # ── Extract Max ──
    def extract_max(self):
        if self.n == 0:
            print("Heap empty")
            return None
        max_val       = self.heap[1]
        self.heap[1]  = self.heap[self.n]
        self.heap.pop()
        self.n       -= 1
        if self.n > 0:
            self._heapify(1)
        print(f"Extracted max: {max_val}. Heap: {self.heap[1:]}")
        return max_val

    # ── Peek Max ──
    def peek(self):
        if self.n == 0:
            return None
        return self.heap[1]

    # ── Heap Sort ──
    def heap_sort(self, arr):
        n = len(arr)
        # 1-based copy
        h = [None] + arr[:]

        # Build max heap
        for i in range(n // 2, 0, -1):
            def heapify(h, i, size):
                lg = i
                l, r = 2*i, 2*i+1
                if l <= size and h[l] > h[lg]: lg = l
                if r <= size and h[r] > h[lg]: lg = r
                if lg != i:
                    h[i], h[lg] = h[lg], h[i]
                    heapify(h, lg, size)
            heapify(h, i, n)

        # Extract max repeatedly
        for i in range(n, 1, -1):
            h[1], h[i] = h[i], h[1]
            heapify(h, 1, i-1)

        result = h[1:]
        print(f"Heap Sort result: {result}")
        return result


# ── MAIN ──
print("=" * 45)
print("         MAX HEAP DEMO")
print("=" * 45)

mh = MaxHeap()
mh.build_heap([3, 9, 2, 1, 4, 5, 8, 6, 7])
mh.insert(100)
mh.extract_max()
mh.extract_max()

print("\nHeap Sort:")
mh.heap_sort([64, 25, 12, 22, 11])
```

---

## Heap Complexity Summary

```
Operation          Time         Space
────────────────   ──────────   ──────────
Build Heap         O(n)         O(1)
Insert             O(log n)     O(1)
Extract Max/Min    O(log n)     O(1)
Peek Max/Min       O(1)         O(1)
Heapify            O(log n)     O(log n) recursive
Heap Sort          O(n log n)   O(1) in-place
Search             O(n)         O(1)
Delete arbitrary   O(log n)     O(1)
```

Heap Sort properties:
```
Best Case    : O(n log n) — always
Average Case : O(n log n) — always
Worst Case   : O(n log n) — always (unlike Quick Sort which is O(n²) worst)
Space        : O(1) — in-place sorting (unlike Merge Sort which needs O(n))
Stable       : NO — relative order of equal elements not preserved
```

---

# APPLICATION 2 — EXPRESSION TREE

---

## What is an Expression Tree?

An Expression Tree is a binary tree where:
- Leaf nodes contain operands (numbers or variables like a, b, x, y)
- Internal nodes contain operators (+, -, *, /, ^)
- The tree represents a mathematical expression

Expression trees are heavily used in compiler design, mathematical software, calculators, and expression evaluators.

```
Expression: (a + b) * (c - d)

         *
        / \
       +   -
      / \ / \
     a  b c  d

Expression: ((5 + 3) * 2) - (4 / 2)

              -
            /   \
           *     /
          / \   / \
         +   2 4   2
        / \
       5   3
```

---

## How Traversals Give Different Expression Forms

This is one of the most important and most asked exam topics:

```
Inorder   traversal = INFIX expression    (normal math notation)
Preorder  traversal = PREFIX expression   (Polish Notation)
Postorder traversal = POSTFIX expression  (Reverse Polish Notation)
```

### Example — All Three Forms from One Tree

```
Expression tree for: (5 + 3) * (2 - 1)

         *
        / \
       +   -
      / \ / \
     5  3 2  1

Inorder   (L→N→R): 5 + 3 * 2 - 1    → Infix  (add parentheses: (5+3)*(2-1))
Preorder  (N→L→R): * + 5 3 - 2 1    → Prefix (no parentheses needed!)
Postorder (L→R→N): 5 3 + 2 1 - *    → Postfix (no parentheses needed!)
```

Postfix and Prefix are parenthesis-free. This is why compilers use postfix (RPN) for evaluating expressions — no ambiguity, no parentheses needed.

---

## How to Build an Expression Tree from Postfix

```
Postfix expression: 5 3 + 2 1 - *

ALGORITHM: BuildExpressionTree(postfix)

Use a stack of tree nodes.

Step 1: Scan postfix from left to right.

Step 2: IF token is an OPERAND:
            Create leaf node with this value.
            Push onto stack.

Step 3: IF token is an OPERATOR:
            Pop right child from stack.
            Pop left child from stack.
            Create new node with this operator.
            new_node.right = right child
            new_node.left  = left child
            Push new_node onto stack.

Step 4: Stack has one element → that is the root of expression tree.
```

### Step-by-Step Trace

```
Postfix: 5 3 + 2 1 - *

Token=5: Create node(5). Push. Stack: [5]
Token=3: Create node(3). Push. Stack: [5, 3]
Token=+: Pop 3(right), pop 5(left). Create (+) with children 5,3. Push.
         Stack: [+]  where + has left=5, right=3
Token=2: Create node(2). Push. Stack: [+, 2]
Token=1: Create node(1). Push. Stack: [+, 2, 1]
Token=-: Pop 1(right), pop 2(left). Create (-) with children 2,1. Push.
         Stack: [+, -]
Token=*: Pop -(right), pop +(left). Create (*) with children +,-.
         Stack: [*]

Final tree:
         *
        / \
       +   -
      / \ / \
     5  3 2  1   ✓
```

---

## How to Evaluate an Expression Tree

```
ALGORITHM: Evaluate(root)

Step 1: IF root is a leaf (operand):
            RETURN root.value

Step 2: left_val  = Evaluate(root.left)
        right_val = Evaluate(root.right)

Step 3: Apply root.operator to left_val and right_val:
            IF root.data == '+': RETURN left_val + right_val
            IF root.data == '-': RETURN left_val - right_val
            IF root.data == '*': RETURN left_val * right_val
            IF root.data == '/': RETURN left_val / right_val
```

### Python Code — Expression Tree

```python
class ExprNode:
    def __init__(self, val):
        self.val   = val
        self.left  = None
        self.right = None

def build_from_postfix(postfix):
    stack   = []
    ops     = {'+', '-', '*', '/'}
    tokens  = postfix.split()

    for token in tokens:
        node = ExprNode(token)
        if token in ops:
            node.right = stack.pop()
            node.left  = stack.pop()
        stack.append(node)
    return stack[0]

def evaluate(root):
    if root.left is None and root.right is None:
        return float(root.val)
    left  = evaluate(root.left)
    right = evaluate(root.right)
    if root.val == '+': return left + right
    if root.val == '-': return left - right
    if root.val == '*': return left * right
    if root.val == '/': return left / right

def inorder(root):
    if root is None: return ''
    if root.left is None and root.right is None:
        return root.val
    return f"({inorder(root.left)} {root.val} {inorder(root.right)})"

def preorder(root):
    if root is None: return ''
    return f"{root.val} {preorder(root.left)} {preorder(root.right)}".strip()

def postorder(root):
    if root is None: return ''
    return f"{postorder(root.left)} {postorder(root.right)} {root.val}".strip()

# ── MAIN ──
postfix = "5 3 + 2 1 - *"
root    = build_from_postfix(postfix)

print("Inorder  (Infix) :", inorder(root))
print("Preorder (Prefix):", preorder(root))
print("Postorder(Postfix):", postfix)
print("Evaluated result :", evaluate(root))

# Output:
# Inorder  (Infix) : ((5 + 3) * (2 - 1))
# Preorder (Prefix): * + 5 3 - 2 1
# Postorder(Postfix): 5 3 + 2 1 - *
# Evaluated result : 8.0
```

---

## Expression Tree — Complexity

```
Operation               Time       Space
──────────────────────  ─────────  ──────────
Build from postfix      O(n)       O(n) stack
Evaluate                O(n)       O(h) recursion
Inorder traversal       O(n)       O(h)
Preorder traversal      O(n)       O(h)
Postorder traversal     O(n)       O(h)
```

---

# APPLICATION 3 — HUFFMAN CODING TREE

---

## What is Huffman Coding?

Huffman Coding is a lossless data compression algorithm invented by David Huffman in 1952. It assigns shorter binary codes to more frequent characters and longer codes to less frequent characters. This reduces the total number of bits needed to store or transmit data.

```
Standard ASCII: every character uses 8 bits.
Huffman:        frequent characters use 2-3 bits, rare ones use 5-6 bits.
                Overall file size reduces by 20% to 90% depending on data.

Used in: ZIP files, GZIP, JPEG, MP3, and many other formats.
```

---

## How Huffman Tree is Built

The Huffman Tree is a full binary tree (every internal node has exactly two children) where:
- Leaf nodes represent characters
- The path from root to a leaf encodes the character (left=0, right=1)
- More frequent characters have shorter paths (shorter codes)

### Algorithm — Build Huffman Tree

```
ALGORITHM: BuildHuffmanTree(characters, frequencies)

Step 1: Create a leaf node for each character.
        Each leaf node stores (character, frequency).

Step 2: Insert all leaf nodes into a MIN priority queue.
        (smallest frequency = highest priority)

Step 3: WHILE priority queue has more than 1 node:
            a) Extract two nodes with MINIMUM frequency: left, right.
            b) Create new internal node with:
                  frequency = left.freq + right.freq
                  left child  = left
                  right child = right
                  character   = None (internal nodes have no character)
            c) Insert new internal node back into priority queue.

Step 4: The single remaining node in the queue is the ROOT of Huffman tree.

Step 5: Generate codes by traversing tree:
            Going LEFT  → append 0 to code
            Going RIGHT → append 1 to code
            At LEAF     → assign code to that character
```

### Full Example — Huffman Coding

Character frequencies:
```
Character : A    B    C    D    E    F
Frequency : 5    1    6    3    9    8
```

Step-by-step construction:

```
Step 1: Create leaf nodes.
        Min Priority Queue (sorted by frequency):
        B(1), D(3), A(5), C(6), F(8), E(9)

Step 2: Extract B(1) and D(3). Create internal node BD(4).
        Reinsert BD(4).
        Queue: A(5), BD(4), C(6), F(8), E(9)
        → sorted: BD(4), A(5), C(6), F(8), E(9)

        Tree fragment:
             BD(4)
            /     \
          B(1)   D(3)

Step 3: Extract BD(4) and A(5). Create internal node BDA(9).
        Queue: C(6), F(8), E(9), BDA(9)

        Tree fragment:
              BDA(9)
             /      \
          BD(4)    A(5)
         /    \
       B(1)  D(3)

Step 4: Extract C(6) and F(8). Create internal node CF(14).
        Queue: E(9), BDA(9), CF(14)

Step 5: Extract E(9) and BDA(9). Create internal node EBDA(18).
        Queue: CF(14), EBDA(18)

Step 6: Extract CF(14) and EBDA(18). Create root CFEBDA(32).
        Queue: root(32) ← only one node remains.

Final Huffman Tree:
                   ROOT(32)
                  /         \
            CF(14)           EBDA(18)
           /      \          /       \
          C(6)   F(8)      E(9)    BDA(9)
                                  /      \
                               BD(4)    A(5)
                              /    \
                            B(1)  D(3)

Step 7: Assign codes (left=0, right=1):
        C  → ROOT left CF left  → 00
        F  → ROOT left CF right → 01
        E  → ROOT right EBDA left → 10
        A  → ROOT right EBDA right BD right → 111
        B  → ROOT right EBDA right BD left left → 1100
        D  → ROOT right EBDA right BD left right → 1101
```

### Huffman Codes Generated

```
Character  Frequency  Huffman Code  Bits Used
─────────  ─────────  ────────────  ─────────────────────────────
    C          6          00         2 bits
    F          8          01         2 bits
    E          9          10         2 bits
    A          5         111         3 bits
    B          1        1100         4 bits
    D          3        1101         4 bits

Without Huffman (3 bits each for 6 chars, 32 total chars):
  Total bits = 32 × 3 = 96 bits

With Huffman:
  A: 5×3=15,  B: 1×4=4,  C: 6×2=12,
  D: 3×4=12,  E: 9×2=18, F: 8×2=16
  Total = 15+4+12+12+18+16 = 77 bits

Compression ratio = (96-77)/96 × 100 = 19.8% reduction
```

### Python Code — Huffman Coding

```python
import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char  = char
        self.freq  = freq
        self.left  = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_dict):
    heap = [HuffmanNode(c, f) for c, f in freq_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left  = heapq.heappop(heap)   # smallest frequency
        right = heapq.heappop(heap)   # second smallest

        merged      = HuffmanNode(None, left.freq + right.freq)
        merged.left  = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]   # root of Huffman tree

def generate_codes(root, code='', codes={}):
    if root is None:
        return
    if root.char is not None:   # leaf node
        codes[root.char] = code if code else '0'
        return
    generate_codes(root.left,  code + '0', codes)
    generate_codes(root.right, code + '1', codes)
    return codes

def huffman_encode(text):
    if not text:
        return '', {}, None

    freq_dict = {}
    for ch in text:
        freq_dict[ch] = freq_dict.get(ch, 0) + 1

    root  = build_huffman_tree(freq_dict)
    codes = generate_codes(root)

    encoded = ''.join(codes[ch] for ch in text)
    return encoded, codes, root

def huffman_decode(encoded, root):
    if root.char is not None:   # single character tree
        return root.char * len(encoded)

    result  = ''
    current = root
    for bit in encoded:
        if bit == '0':
            current = current.left
        else:
            current = current.right
        if current.char is not None:
            result  += current.char
            current  = root
    return result

# ── MAIN ──
text    = "ABRACADABRA"
encoded, codes, root = huffman_encode(text)

print(f"Original text    : {text}")
print(f"Original bits    : {len(text) * 8} bits (8 bits/char ASCII)")
print(f"Huffman codes    : {codes}")
print(f"Encoded bits     : {encoded}")
print(f"Encoded length   : {len(encoded)} bits")
print(f"Compression ratio: {(1 - len(encoded)/(len(text)*8))*100:.1f}% reduction")
print(f"Decoded text     : {huffman_decode(encoded, root)}")
```

---

## Huffman Coding Complexity

```
Operation                Time           Space
──────────────────────   ─────────────  ──────────
Build frequency table    O(n)           O(k) k=unique chars
Build Huffman tree       O(k log k)     O(k)
Generate codes           O(k)           O(k)
Encode string            O(n)           O(n)
Decode string            O(n)           O(1)
Overall                  O(n + k log k) O(n + k)
```

---

# APPLICATION 4 — DECISION TREE

---

## What is a Decision Tree?

A Decision Tree is a binary (or multi-way) tree used to model decisions and their possible consequences. Each internal node represents a question or condition. Each branch represents an answer or outcome. Each leaf node represents a final decision or classification.

Decision trees are the foundation of:
- Machine Learning classification algorithms
- Game trees (chess, tic-tac-toe AI)
- Business decision analysis
- Medical diagnosis systems
- Expert systems

```
Binary Decision Tree structure:
  Internal node → a question or condition (e.g., "Is age > 30?")
  Left branch   → YES (True)
  Right branch  → NO (False)
  Leaf node     → Final answer (class label, decision, outcome)
```

---

## Example — Decision Tree for Loan Approval

```
                    [Income > 50000?]
                    /               \
                 YES                  NO
                /                       \
      [Credit Score > 700?]          [REJECTED]
      /              \
   YES                 NO
   /                     \
[APPROVED]         [Employment > 2yrs?]
                    /               \
                 YES                  NO
                /                       \
          [APPROVED              [REJECTED]
           with higher rate]
```

---

## Example — Decision Tree for Classifying Fruit

```
                 [Is it round?]
                /               \
             YES                  NO
            /                       \
   [Is it red?]                [Is it yellow?]
   /         \                  /            \
 YES          NO              YES              NO
 /              \             /                  \
[Apple]       [Orange]   [Banana]              [Grape]
```

---

## Building a Decision Tree (ID3 Algorithm Concept)

In machine learning, decision trees are built by choosing the best feature to split on at each node. The "best" feature is the one that provides the most information gain — it separates the data into the most pure groups.

```
ALGORITHM: BuildDecisionTree(data, features, target)

Step 1: IF all data points have same class:
            RETURN leaf node with that class.

Step 2: IF no features left:
            RETURN leaf node with majority class.

Step 3: Find the BEST feature to split on:
            best_feature = argmax(InformationGain(data, feature))
            for each feature.

Step 4: Create internal node using best_feature as the question.

Step 5: FOR each possible value of best_feature:
            subset = data where best_feature == value
            child  = BuildDecisionTree(subset, features - best_feature, target)
            Add child to node.

Step 6: RETURN node.
```

---

## Decision Tree Prediction Algorithm

```
ALGORITHM: Predict(tree, new_data_point)

Step 1: node = tree.root

Step 2: WHILE node is not a leaf:
            feature_value = new_data_point[node.feature]
            IF feature_value satisfies node.condition:
                node = node.left
            ELSE:
                node = node.right

Step 3: RETURN node.class_label   ← leaf = decision
```

---

## Python Code — Simple Decision Tree

```python
class DecisionNode:
    def __init__(self, question=None, yes_branch=None,
                 no_branch=None, label=None):
        self.question   = question    # for internal nodes
        self.yes_branch = yes_branch  # left child (True branch)
        self.no_branch  = no_branch   # right child (False branch)
        self.label      = label       # for leaf nodes (final decision)
        self.is_leaf    = label is not None

def predict(tree, data_point):
    node = tree
    while not node.is_leaf:
        feature, threshold = node.question
        if data_point.get(feature, 0) >= threshold:
            node = node.yes_branch
        else:
            node = node.no_branch
    return node.label

def print_tree(node, indent=0):
    prefix = "  " * indent
    if node.is_leaf:
        print(f"{prefix}→ DECISION: {node.label}")
        return
    feat, thresh = node.question
    print(f"{prefix}[{feat} >= {thresh}?]")
    print(f"{prefix}YES:")
    print_tree(node.yes_branch, indent + 1)
    print(f"{prefix}NO:")
    print_tree(node.no_branch, indent + 1)

# ── Build Loan Approval Decision Tree ──
loan_tree = DecisionNode(
    question=('income', 50000),
    yes_branch=DecisionNode(
        question=('credit_score', 700),
        yes_branch=DecisionNode(label='APPROVED'),
        no_branch=DecisionNode(
            question=('employment_years', 2),
            yes_branch=DecisionNode(label='APPROVED (higher rate)'),
            no_branch=DecisionNode(label='REJECTED')
        )
    ),
    no_branch=DecisionNode(label='REJECTED')
)

# ── Print tree ──
print("Loan Approval Decision Tree:")
print_tree(loan_tree)

# ── Predictions ──
print("\nPredictions:")
applicants = [
    {'income': 60000, 'credit_score': 750, 'employment_years': 3},
    {'income': 60000, 'credit_score': 650, 'employment_years': 1},
    {'income': 30000, 'credit_score': 800, 'employment_years': 5},
]
for i, app in enumerate(applicants, 1):
    result = predict(loan_tree, app)
    print(f"  Applicant {i}: {app}")
    print(f"  Decision   : {result}\n")
```

---

## Decision Tree Complexity

```
Operation              Time           Space
──────────────────     ─────────────  ──────────────
Build tree (n samples, O(n × d × log n) O(n × d)
  d features)          n=samples,     d=features
                        d=features
Predict (one sample)   O(depth)       O(1)
                       = O(log n) balanced
                       = O(n) worst case
Memory for tree        O(n) nodes     O(n)
```

---

## Summary — All Four Applications Compared

```
Application       Structure          Primary Use               Key Operation
───────────────   ────────────────   ───────────────────────   ─────────────────────
Heap              Complete BT        Priority Queue,           Heapify O(log n)
                  Array-stored       Heap Sort O(n log n)      Build Heap O(n)

Expression Tree   Full BT            Compiler expression       Postorder eval O(n)
                  Operators+operands parsing, calculators      Traversal for
                                                               infix/prefix/postfix

Huffman Tree      Full BT            Lossless data             Build O(k log k)
                  Leaf=characters    compression               Encode/Decode O(n)
                  Freq-weighted      ZIP, JPEG, MP3

Decision Tree     Binary/Multi-way   ML classification,        Predict O(depth)
                  Condition+labels   game AI, expert systems   Build O(n d log n)
```

---

## Most Important Exam Points

```
Heap:
  Point 1: Heap is stored as ARRAY using index formulas (2i, 2i+1, i//2).
  Point 2: Max heap → root is maximum. Min heap → root is minimum.
  Point 3: Build heap is O(n), NOT O(n log n). Counter-intuitive but proven.
  Point 4: Heap Sort is O(n log n) always — best, average, worst.
  Point 5: Heap Sort is in-place O(1) space unlike Merge Sort O(n) space.

Expression Tree:
  Point 6: Inorder=Infix, Preorder=Prefix, Postorder=Postfix.
  Point 7: Build from postfix using a stack — O(n) time.
  Point 8: Evaluate tree using postorder traversal recursively.
  Point 9: Prefix and Postfix expressions need no parentheses.

Huffman Coding:
  Point 10: Huffman uses a MIN priority queue (min-heap) to build the tree.
  Point 11: More frequent characters get SHORTER codes.
  Point 12: Huffman codes are prefix-free — no code is prefix of another.
  Point 13: The sum of freq×code_length is MINIMIZED by Huffman (optimal).
  Point 14: Total bits saved = original bits - huffman bits.

Decision Tree:
  Point 15: Internal nodes = questions/conditions. Leaves = decisions.
  Point 16: Prediction always O(depth) — follow one path from root to leaf.
  Point 17: Best split chosen by Information Gain or Gini Impurity.
  Point 18: Overfitting is a real problem — pruning techniques exist.
```