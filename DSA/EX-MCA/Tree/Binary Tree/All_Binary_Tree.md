# Binary Tree — In-Depth: Representation, Traversals, Operations + Full Code

---

## PART 1 — Complexity of Binary Tree Operations

```
Operation              Best Case    Average Case    Worst Case    Space
─────────────────────  ─────────    ────────────    ──────────    ──────────────
Traversal (any)        O(n)         O(n)            O(n)          O(h) recursive
Search                 O(1)         O(n)            O(n)          O(h)
Insertion              O(1)         O(n)            O(n)          O(h)
Deletion               O(1)         O(n)            O(n)          O(h)
Find Height            O(n)         O(n)            O(n)          O(h)
Count Nodes            O(n)         O(n)            O(n)          O(h)
Find Min/Max           O(n)         O(n)            O(n)          O(h)
Level Order (BFS)      O(n)         O(n)            O(n)          O(w) = O(n)
─────────────────────────────────────────────────────────────────────────────────
h = height of tree
  = O(log n) for balanced tree
  = O(n)     for skewed tree
w = maximum width of tree
  = O(n/2) for last level of perfect binary tree
```

Note: A plain Binary Tree has no ordering property, so search is always O(n) in the worst case. Unlike BST, there is no way to eliminate half the tree at each step.

---

## PART 2 — Representation of Binary Tree

There are two ways to represent a binary tree in memory:

---

### Representation 1 — Linked Representation

Each node is a structure containing data and two pointers: one to the left child and one to the right child. Nodes are created dynamically in the heap.

**Node structure:**

```
[ Left Pointer | Data | Right Pointer ]
```

**When to use:**
- For dynamic, sparse, or unbalanced trees
- When tree structure changes frequently (insertions, deletions)
- Most common representation in practice

**Algorithm — Create Node:**

```
ALGORITHM: CreateNode(data)

Input  : data value
Output : new node with left = NULL, right = NULL

Step 1: Allocate memory for new node
Step 2: node.data  = data
Step 3: node.left  = NULL
Step 4: node.right = NULL
Step 5: RETURN node
```

**Algorithm — Insert Node (Level Order Insertion to build a complete binary tree):**

```
ALGORITHM: InsertNode(root, data)

Input  : root of tree, data to insert
Output : root of updated tree

Step 1: newNode = CreateNode(data)

Step 2: IF root == NULL:
            RETURN newNode   ← becomes the root

Step 3: Create empty Queue Q
        Enqueue(Q, root)

Step 4: WHILE Q is not empty:
            temp = Dequeue(Q)

            IF temp.left == NULL:
                temp.left = newNode   ← insert here
                RETURN root

            ELSE:
                Enqueue(Q, temp.left)

            IF temp.right == NULL:
                temp.right = newNode   ← insert here
                RETURN root

            ELSE:
                Enqueue(Q, temp.right)

Step 5: RETURN root
```

**Full Python Code — Linked Representation:**

```python
from collections import deque


# ─────────────────────────────────────────
#  NODE CLASS
# ─────────────────────────────────────────
class Node:
    def __init__(self, data):
        self.data  = data
        self.left  = None
        self.right = None


# ─────────────────────────────────────────
#  BINARY TREE CLASS (LINKED REPRESENTATION)
# ─────────────────────────────────────────
class BinaryTree:
    def __init__(self):
        self.root = None

    # ── Insert node (level order / complete binary tree style) ──
    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            print(data, "inserted as root")
            return

        queue = deque([self.root])

        while queue:
            temp = queue.popleft()

            if temp.left is None:
                temp.left = new_node
                print(data, "inserted as left child of", temp.data)
                return
            else:
                queue.append(temp.left)

            if temp.right is None:
                temp.right = new_node
                print(data, "inserted as right child of", temp.data)
                return
            else:
                queue.append(temp.right)

    # ── Display structure (simple level order print) ──
    def display(self):
        if self.root is None:
            print("Tree is empty")
            return

        queue = deque([self.root])
        print("Binary Tree (level order):")

        while queue:
            temp = queue.popleft()
            left  = temp.left.data  if temp.left  else "NULL"
            right = temp.right.data if temp.right else "NULL"
            print(f"  Node {temp.data} → left: {left}, right: {right}")

            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)


# ─────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────
bt = BinaryTree()
bt.insert(1)
bt.insert(2)
bt.insert(3)
bt.insert(4)
bt.insert(5)
bt.display()

# Output tree:
#         1
#        / \
#       2   3
#      / \
#     4   5
```

---

### Representation 2 — Array Representation

The tree is stored in a 1D array using index formulas. For a node at index i:

```
Left child  → 2 * i
Right child → 2 * i + 1
Parent      → i // 2
Root        → index 1 (index 0 is unused or used as dummy)
```

**When to use:**
- For complete or perfect binary trees
- When tree structure is fixed and no insertions/deletions
- Heaps use this representation (very efficient)

**Example:**

```
Tree:
            1          (index 1)
           / \
          2   3        (index 2, 3)
         / \
        4   5          (index 4, 5)

Array: [_, 1, 2, 3, 4, 5, _, _]
Index:   0  1  2  3  4  5  6  7

Index 0 is unused (dummy).
Node at index 2 (value=2):
    left  child → index 4 (value=4) ✓
    right child → index 5 (value=5) ✓
    parent      → index 1 (value=1) ✓
```

**Algorithm — Array Representation:**

```
ALGORITHM: ArrayRepresentation

Step 1: Create array A of size 2^(h+1) where h = height of tree
        (OR size n+1 for a complete binary tree with n nodes)

Step 2: Place root at A[1]

Step 3: FOR each node at index i:
            Place left child  at A[2*i]
            Place right child at A[2*i + 1]
            Leave A[index] = 0 or -1 if no child exists

Step 4: To find parent of node at index i:
            Parent is at A[i // 2]

Step 5: For level-order traversal:
            Simply traverse A[1] to A[n]
```

**Full Python Code — Array Representation:**

```python
# ─────────────────────────────────────────
#  BINARY TREE — ARRAY REPRESENTATION
# ─────────────────────────────────────────
class BinaryTreeArray:
    def __init__(self, max_size):
        self.size  = max_size + 1          # index 0 unused
        self.tree  = [None] * self.size    # None = no node
        self.count = 0

    # ── Insert node (level order, fills left to right) ──
    def insert(self, data):
        if self.count + 1 >= self.size:
            print("Tree is full. Cannot insert", data)
            return

        self.count += 1
        self.tree[self.count] = data
        index = self.count

        parent_index = index // 2
        if parent_index >= 1:
            side = "left" if index % 2 == 0 else "right"
            print(f"{data} inserted at index {index} "
                  f"({side} child of {self.tree[parent_index]})")
        else:
            print(f"{data} inserted as root at index {index}")

    # ── Get left child ──
    def left_child(self, index):
        left = 2 * index
        if left <= self.count and self.tree[left] is not None:
            return self.tree[left]
        return None

    # ── Get right child ──
    def right_child(self, index):
        right = 2 * index + 1
        if right <= self.count and self.tree[right] is not None:
            return self.tree[right]
        return None

    # ── Get parent ──
    def parent(self, index):
        if index <= 1:
            return None
        return self.tree[index // 2]

    # ── Display array ──
    def display_array(self):
        print("Array representation:")
        print("Index:", end=" ")
        for i in range(1, self.count + 1):
            print(i, end="\t")
        print()
        print("Value:", end=" ")
        for i in range(1, self.count + 1):
            print(self.tree[i], end="\t")
        print()

    # ── Display parent-child relationships ──
    def display_tree(self):
        print("Tree structure:")
        for i in range(1, self.count + 1):
            left  = self.left_child(i)
            right = self.right_child(i)
            print(f"  Node[{i}]={self.tree[i]} → "
                  f"left: {left}, right: {right}")

    # ── Inorder traversal using array ──
    def inorder(self, index=1):
        if index > self.count or self.tree[index] is None:
            return
        self.inorder(2 * index)
        print(self.tree[index], end=" → ")
        self.inorder(2 * index + 1)

    # ── Level order traversal (just read array left to right) ──
    def level_order(self):
        print("Level order:")
        for i in range(1, self.count + 1):
            if self.tree[i] is not None:
                print(self.tree[i], end=" → ")
        print()


# ─────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────
bta = BinaryTreeArray(10)
bta.insert(1)
bta.insert(2)
bta.insert(3)
bta.insert(4)
bta.insert(5)

bta.display_array()
bta.display_tree()

print("Inorder: ", end="")
bta.inorder()
print()
bta.level_order()

print("Parent of index 4:", bta.parent(4))
print("Left child of index 2:", bta.left_child(2))
print("Right child of index 2:", bta.right_child(2))
```

---

### Comparison — Array vs Linked Representation

```
Feature                   Array Representation        Linked Representation
───────────────────────   ─────────────────────────   ─────────────────────────
Memory layout             Contiguous                  Scattered (heap)
Best for                  Complete / Perfect trees    Any binary tree
Space (complete tree)     O(n) — efficient            O(n) — efficient
Space (sparse/skewed)     O(2^h) — wasteful           O(n) — efficient
Cache performance         Better (contiguous)         Worse (pointer chasing)
Insertion                 Simple (next index)         Complex (find position)
Deletion                  Complex (shifting needed)   Simple (pointer update)
Parent access             O(1) via i//2               O(n) — must traverse
Used in                   Heap, segment tree          General BST, AVL, etc.
```

---

## PART 3 — Binary Tree Traversals (Full Code + Algorithms)

We use this tree for all traversals:

```
        1
       / \
      2   3
     / \   \
    4   5   6
```

---

### Traversal 1 — Inorder (Left → Root → Right)

**Algorithm:**

```
ALGORITHM: Inorder(node)

Step 1: IF node == NULL: RETURN
Step 2: Inorder(node.left)    ← visit left subtree
Step 3: PRINT node.data       ← visit root
Step 4: Inorder(node.right)   ← visit right subtree
```

**Full Code:**

```python
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" → ")
    inorder(root.right)

# Output: 4 → 2 → 5 → 1 → 3 → 6
```

**Iterative Inorder (using explicit stack):**

```python
def inorder_iterative(root):
    stack = []
    current = root

    while current is not None or stack:
        # Reach the leftmost node
        while current is not None:
            stack.append(current)
            current = current.left

        # Current is None, pop from stack
        current = stack.pop()
        print(current.data, end=" → ")

        # Move to right subtree
        current = current.right

# Output: 4 → 2 → 5 → 1 → 3 → 6
```

---

### Traversal 2 — Preorder (Root → Left → Right)

**Algorithm:**

```
ALGORITHM: Preorder(node)

Step 1: IF node == NULL: RETURN
Step 2: PRINT node.data       ← visit root first
Step 3: Preorder(node.left)   ← visit left subtree
Step 4: Preorder(node.right)  ← visit right subtree
```

**Full Code:**

```python
def preorder(root):
    if root is None:
        return
    print(root.data, end=" → ")
    preorder(root.left)
    preorder(root.right)

# Output: 1 → 2 → 4 → 5 → 3 → 6
```

**Iterative Preorder (using explicit stack):**

```python
def preorder_iterative(root):
    if root is None:
        return

    stack = [root]

    while stack:
        node = stack.pop()
        print(node.data, end=" → ")

        # Push right first so left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# Output: 1 → 2 → 4 → 5 → 3 → 6
```

---

### Traversal 3 — Postorder (Left → Right → Root)

**Algorithm:**

```
ALGORITHM: Postorder(node)

Step 1: IF node == NULL: RETURN
Step 2: Postorder(node.left)   ← visit left subtree
Step 3: Postorder(node.right)  ← visit right subtree
Step 4: PRINT node.data        ← visit root last
```

**Full Code:**

```python
def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" → ")

# Output: 4 → 5 → 2 → 6 → 3 → 1
```

**Iterative Postorder (using two stacks):**

```python
def postorder_iterative(root):
    if root is None:
        return

    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    while stack2:
        node = stack2.pop()
        print(node.data, end=" → ")

# Output: 4 → 5 → 2 → 6 → 3 → 1
```

---

### Traversal 4 — Level Order (BFS)

**Algorithm:**

```
ALGORITHM: LevelOrder(root)

Step 1: IF root == NULL: RETURN
Step 2: Create empty Queue Q
Step 3: Enqueue(Q, root)

Step 4: WHILE Q is not empty:
            node = Dequeue(Q)
            PRINT node.data
            IF node.left  != NULL: Enqueue(Q, node.left)
            IF node.right != NULL: Enqueue(Q, node.right)
```

**Full Code:**

```python
from collections import deque

def level_order(root):
    if root is None:
        print("Tree is empty")
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.data, end=" → ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Output: 1 → 2 → 3 → 4 → 5 → 6
```

**Level Order — Print Level by Level (with newlines):**

```python
def level_order_levels(root):
    if root is None:
        return

    queue = deque([root])
    level = 1

    while queue:
        level_size = len(queue)        # number of nodes at current level
        print(f"Level {level}: ", end="")

        for _ in range(level_size):
            node = queue.popleft()
            print(node.data, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        print()
        level += 1

# Output:
# Level 1: 1
# Level 2: 2 3
# Level 3: 4 5 6
```

---

### Complete Traversal Code (All Together)

```python
from collections import deque


# ─────────────────────────────────────────
#  NODE CLASS
# ─────────────────────────────────────────
class Node:
    def __init__(self, data):
        self.data  = data
        self.left  = None
        self.right = None


# ─────────────────────────────────────────
#  BUILD THE TREE MANUALLY
# ─────────────────────────────────────────
def build_tree():
    root    = Node(1)
    root.left        = Node(2)
    root.right       = Node(3)
    root.left.left   = Node(4)
    root.left.right  = Node(5)
    root.right.right = Node(6)
    return root


# ─────────────────────────────────────────
#  TRAVERSALS
# ─────────────────────────────────────────
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" → ")
    inorder(root.right)


def preorder(root):
    if root is None:
        return
    print(root.data, end=" → ")
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" → ")


def level_order(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data, end=" → ")
        if node.left:  queue.append(node.left)
        if node.right: queue.append(node.right)


# ─────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────
root = build_tree()

print("Inorder    (L→N→R):", end=" "); inorder(root);     print()
print("Preorder   (N→L→R):", end=" "); preorder(root);    print()
print("Postorder  (L→R→N):", end=" "); postorder(root);   print()
print("Level Order       :", end=" "); level_order(root); print()

# ─── OUTPUT ───
# Inorder    (L→N→R): 4 → 2 → 5 → 1 → 3 → 6
# Preorder   (N→L→R): 1 → 2 → 4 → 5 → 3 → 6
# Postorder  (L→R→N): 4 → 5 → 2 → 6 → 3 → 1
# Level Order       : 1 → 2 → 3 → 4 → 5 → 6
```

---

## PART 4 — Binary Tree Operations (Full Code + Algorithms)

---

### Operation 1 — Search

**Algorithm:**

```
ALGORITHM: Search(root, key)

Step 1: IF root == NULL: RETURN False    ← not found
Step 2: IF root.data == key: RETURN True ← found
Step 3: left_result  = Search(root.left,  key)
Step 4: IF left_result == True: RETURN True
Step 5: RETURN Search(root.right, key)
```

**Code:**

```python
def search(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    return search(root.left, key) or search(root.right, key)
```

---

### Operation 2 — Count Nodes

**Algorithm:**

```
ALGORITHM: CountNodes(root)

Step 1: IF root == NULL: RETURN 0
Step 2: RETURN 1 + CountNodes(root.left) + CountNodes(root.right)
```

**Code:**

```python
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)
```

---

### Operation 3 — Find Height

**Algorithm:**

```
ALGORITHM: Height(root)

Step 1: IF root == NULL: RETURN 0
Step 2: left_height  = Height(root.left)
Step 3: right_height = Height(root.right)
Step 4: RETURN 1 + max(left_height, right_height)
```

**Code:**

```python
def height(root):
    if root is None:
        return 0
    left_h  = height(root.left)
    right_h = height(root.right)
    return 1 + max(left_h, right_h)
```

---

### Operation 4 — Find Minimum and Maximum

**Algorithm:**

```
ALGORITHM: FindMin(root)

Step 1: IF root == NULL: RETURN infinity
Step 2: RETURN min(root.data, FindMin(root.left), FindMin(root.right))

ALGORITHM: FindMax(root)

Step 1: IF root == NULL: RETURN -infinity
Step 2: RETURN max(root.data, FindMax(root.left), FindMax(root.right))
```

**Code:**

```python
def find_min(root):
    if root is None:
        return float('inf')
    return min(root.data, find_min(root.left), find_min(root.right))

def find_max(root):
    if root is None:
        return float('-inf')
    return max(root.data, find_max(root.left), find_max(root.right))
```

---

### Operation 5 — Count Leaf Nodes

**Algorithm:**

```
ALGORITHM: CountLeaves(root)

Step 1: IF root == NULL: RETURN 0
Step 2: IF root.left == NULL AND root.right == NULL:
            RETURN 1           ← it is a leaf node
Step 3: RETURN CountLeaves(root.left) + CountLeaves(root.right)
```

**Code:**

```python
def count_leaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1                     # it's a leaf
    return count_leaves(root.left) + count_leaves(root.right)
```

---

### Operation 6 — Delete a Node (Level Order Deletion)

In a binary tree (not BST), deletion is done by:
1. Finding the deepest rightmost node in the tree
2. Replacing the target node's data with the deepest node's data
3. Deleting the deepest rightmost node

**Algorithm:**

```
ALGORITHM: DeleteNode(root, key)

Step 1: IF root == NULL: RETURN NULL

Step 2: Use level order traversal to find:
        a) target_node = node whose data == key
        b) last_node   = deepest rightmost node
        c) parent_of_last = parent of last_node

Step 3: Copy last_node.data into target_node.data

Step 4: Delete last_node:
        IF parent_of_last.right == last_node:
            parent_of_last.right = NULL
        ELSE:
            parent_of_last.left  = NULL

Step 5: RETURN root
```

**Code:**

```python
from collections import deque

def delete_node(root, key):
    if root is None:
        return None

    # Special case: only root node
    if root.left is None and root.right is None:
        if root.data == key:
            return None
        return root

    queue        = deque([root])
    target_node  = None
    last_node    = None
    parent_last  = None

    # Level order to find target and last node
    while queue:
        node = queue.popleft()

        if node.data == key:
            target_node = node

        if node.left:
            parent_last = node
            last_node   = node.left
            queue.append(node.left)

        if node.right:
            parent_last = node
            last_node   = node.right
            queue.append(node.right)

    if target_node:
        # Copy deepest node's value to target
        target_node.data = last_node.data

        # Delete the deepest rightmost node
        if parent_last.right == last_node:
            parent_last.right = None
        else:
            parent_last.left = None

    return root
```

---

### Operation 7 — Mirror / Invert a Binary Tree

**Algorithm:**

```
ALGORITHM: Mirror(root)

Step 1: IF root == NULL: RETURN NULL
Step 2: Mirror(root.left)    ← mirror left subtree
Step 3: Mirror(root.right)   ← mirror right subtree
Step 4: Swap root.left and root.right
Step 5: RETURN root
```

**Code:**

```python
def mirror(root):
    if root is None:
        return None
    mirror(root.left)
    mirror(root.right)
    root.left, root.right = root.right, root.left
    return root
```

---

### Operation 8 — Check if Two Trees are Identical

**Algorithm:**

```
ALGORITHM: IsIdentical(root1, root2)

Step 1: IF root1 == NULL AND root2 == NULL: RETURN True
Step 2: IF root1 == NULL OR  root2 == NULL: RETURN False
Step 3: IF root1.data != root2.data:        RETURN False
Step 4: RETURN IsIdentical(root1.left,  root2.left) AND
               IsIdentical(root1.right, root2.right)
```

**Code:**

```python
def is_identical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.data != root2.data:
        return False
    return (is_identical(root1.left,  root2.left) and
            is_identical(root1.right, root2.right))
```

---

### Operation 9 — Find Width of Tree (Max nodes at any level)

**Algorithm:**

```
ALGORITHM: Width(root)

Step 1: IF root == NULL: RETURN 0
Step 2: Queue Q, Enqueue(Q, root)
Step 3: max_width = 0

Step 4: WHILE Q is not empty:
            level_size = len(Q)        ← nodes at current level
            max_width  = max(max_width, level_size)

            FOR i = 1 to level_size:
                node = Dequeue(Q)
                IF node.left:  Enqueue(Q, node.left)
                IF node.right: Enqueue(Q, node.right)

Step 5: RETURN max_width
```

**Code:**

```python
def width(root):
    if root is None:
        return 0

    queue     = deque([root])
    max_width = 0

    while queue:
        level_size = len(queue)
        max_width  = max(max_width, level_size)

        for _ in range(level_size):
            node = queue.popleft()
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)

    return max_width
```

---

### Operation 10 — Check if Tree is Balanced

A tree is balanced if for every node, the difference in height of left and right subtrees is at most 1.

**Algorithm:**

```
ALGORITHM: IsBalanced(root)

Step 1: IF root == NULL: RETURN True

Step 2: left_h  = Height(root.left)
        right_h = Height(root.right)

Step 3: IF |left_h - right_h| > 1: RETURN False

Step 4: RETURN IsBalanced(root.left) AND IsBalanced(root.right)
```

**Code:**

```python
def is_balanced(root):
    if root is None:
        return True

    left_h  = height(root.left)
    right_h = height(root.right)

    if abs(left_h - right_h) > 1:
        return False

    return is_balanced(root.left) and is_balanced(root.right)
```

---

### Complete Operations Code (All Together)

```python
from collections import deque


# ─────────────────────────────────────────
#  NODE CLASS
# ─────────────────────────────────────────
class Node:
    def __init__(self, data):
        self.data  = data
        self.left  = None
        self.right = None


# ─────────────────────────────────────────
#  ALL OPERATIONS
# ─────────────────────────────────────────

def search(root, key):
    if root is None: return False
    if root.data == key: return True
    return search(root.left, key) or search(root.right, key)


def count_nodes(root):
    if root is None: return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def height(root):
    if root is None: return 0
    return 1 + max(height(root.left), height(root.right))


def find_min(root):
    if root is None: return float('inf')
    return min(root.data, find_min(root.left), find_min(root.right))


def find_max(root):
    if root is None: return float('-inf')
    return max(root.data, find_max(root.left), find_max(root.right))


def count_leaves(root):
    if root is None: return 0
    if root.left is None and root.right is None: return 1
    return count_leaves(root.left) + count_leaves(root.right)


def mirror(root):
    if root is None: return None
    mirror(root.left)
    mirror(root.right)
    root.left, root.right = root.right, root.left
    return root


def is_identical(r1, r2):
    if r1 is None and r2 is None: return True
    if r1 is None or  r2 is None: return False
    if r1.data != r2.data:        return False
    return is_identical(r1.left, r2.left) and is_identical(r1.right, r2.right)


def width(root):
    if root is None: return 0
    queue = deque([root])
    max_w = 0
    while queue:
        level_size = len(queue)
        max_w = max(max_w, level_size)
        for _ in range(level_size):
            node = queue.popleft()
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
    return max_w


def is_balanced(root):
    if root is None: return True
    lh = height(root.left)
    rh = height(root.right)
    if abs(lh - rh) > 1: return False
    return is_balanced(root.left) and is_balanced(root.right)


def delete_node(root, key):
    if root is None: return None
    if root.left is None and root.right is None:
        return None if root.data == key else root

    queue       = deque([root])
    target      = None
    last        = None
    parent_last = None

    while queue:
        node = queue.popleft()
        if node.data == key:
            target = node
        if node.left:
            parent_last = node
            last = node.left
            queue.append(node.left)
        if node.right:
            parent_last = node
            last = node.right
            queue.append(node.right)

    if target:
        target.data = last.data
        if parent_last.right == last:
            parent_last.right = None
        else:
            parent_last.left = None
    return root


def level_order(root):
    if root is None: return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data, end=" → ")
        if node.left:  queue.append(node.left)
        if node.right: queue.append(node.right)


# ─────────────────────────────────────────
#  BUILD TREE AND TEST ALL OPERATIONS
# ─────────────────────────────────────────
root              = Node(1)
root.left         = Node(2)
root.right        = Node(3)
root.left.left    = Node(4)
root.left.right   = Node(5)
root.right.right  = Node(6)

#         1
#        / \
#       2   3
#      / \   \
#     4   5   6

print("── Tree (level order) ──")
level_order(root)
print()

print("── Operations ──")
print("Total nodes    :", count_nodes(root))
print("Height         :", height(root))
print("Leaf nodes     :", count_leaves(root))
print("Minimum value  :", find_min(root))
print("Maximum value  :", find_max(root))
print("Width          :", width(root))
print("Is balanced    :", is_balanced(root))
print("Search 5       :", search(root, 5))
print("Search 99      :", search(root, 99))

print("\n── After deleting node 3 ──")
root = delete_node(root, 3)
level_order(root)
print()

print("\n── Mirror of tree ──")
root = mirror(root)
level_order(root)
print()

# ─── OUTPUT ───
# ── Tree (level order) ──
# 1 → 2 → 3 → 4 → 5 → 6
#
# ── Operations ──
# Total nodes    : 6
# Height         : 3
# Leaf nodes     : 3
# Minimum value  : 1
# Maximum value  : 6
# Width          : 2
# Is balanced    : True
# Search 5       : True
# Search 99      : False
#
# ── After deleting node 3 ──
# 1 → 2 → 6 → 4 → 5
#
# ── Mirror of tree ──
# 1 → 6 → 2 → 5 → 4
```

---

## Summary — All Algorithms and Their Complexities

```
Operation            Algorithm Used          Time       Space
───────────────────  ──────────────────────  ─────────  ──────────
Inorder traversal    Recursive / Stack       O(n)       O(h)
Preorder traversal   Recursive / Stack       O(n)       O(h)
Postorder traversal  Recursive / 2 stacks    O(n)       O(h)
Level order          BFS with Queue          O(n)       O(w)
Search               DFS recursive           O(n)       O(h)
Count nodes          Postorder style         O(n)       O(h)
Height               Postorder style         O(n)       O(h)
Count leaves         DFS recursive           O(n)       O(h)
Find min/max         DFS recursive           O(n)       O(h)
Delete node          Level order + replace   O(n)       O(n)
Mirror tree          Postorder style         O(n)       O(h)
Is identical         DFS recursive           O(n)       O(h)
Width                Level order BFS         O(n)       O(w)
Is balanced          DFS recursive           O(n²)      O(h)
───────────────────────────────────────────────────────────────────
h = height  (O(log n) balanced, O(n) skewed)
w = max width at any level
O(n²) for is_balanced can be optimized to O(n) using height memoization
```