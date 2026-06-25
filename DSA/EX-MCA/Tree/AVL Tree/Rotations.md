# AVL Tree — All Rotations: Algorithm + Code

---

## Why Rotations Are Needed

When we insert or delete a node in an AVL Tree, the **Balance Factor (BF)** at some node may become **+2 or −2**, which violates the AVL property. Rotations fix this by **restructuring the tree** without changing the inorder sequence (BST property is preserved).

```
Balance Factor (BF) = Height(Left Subtree) − Height(Right Subtree)

BF =  0 → Perfectly balanced ✓
BF = +1 → Slightly left heavy ✓
BF = -1 → Slightly right heavy ✓
BF = +2 → Left heavy — VIOLATION → Fix with rotation
BF = -2 → Right heavy — VIOLATION → Fix with rotation
```

---

## 4 Rotation Cases — When to Apply Which

```
BF at node     Where new node inserted          Rotation needed
───────────    ─────────────────────────────    ────────────────────────
   +2          LEFT subtree of LEFT child       LL → Single Right Rotate
   -2          RIGHT subtree of RIGHT child     RR → Single Left Rotate
   +2          RIGHT subtree of LEFT child      LR → Left then Right Rotate
   -2          LEFT subtree of RIGHT child      RL → Right then Left Rotate
```

---

## ROTATION 1 — Right Rotation (LL Case)

### When to Apply

When **BF = +2** at a node AND the **left child has BF ≥ 0** (imbalance is in the left subtree of left child).

### Before and After Diagram

```
BEFORE Right Rotation:          AFTER Right Rotation:

        z  ← BF = +2                    y
       / \                             / \
      y   T4   ← BF = +1 or 0        x    z
     / \                             / \  / \
    x   T3                          T1 T2 T3 T4
   / \
  T1  T2

z = unbalanced node (BF = +2)
y = left child of z (new root)
x = left child of y
T1, T2, T3, T4 = subtrees
```

### Algorithm — Right Rotation

```
ALGORITHM: RightRotate(z)

Input  : z = unbalanced node (BF = +2)
Output : y = new root of this subtree (balanced)

Step 1: Start

Step 2: Set y  = z.left          ← y is the new root
        Set T3 = y.right         ← T3 is right subtree of y

Step 3: Perform rotation:
        y.right = z              ← z becomes right child of y
        z.left  = T3             ← T3 becomes left child of z

Step 4: Update heights (update z first because it is now lower):
        z.height = 1 + max(Height(z.left), Height(z.right))
        y.height = 1 + max(Height(y.left), Height(y.right))

Step 5: Return y                 ← y is the new root of this subtree

Step 6: Stop
```

### Code — Right Rotation

```python
def rotate_right(self, z):
    """
    Right Rotation — LL Case
    z = unbalanced node (BF = +2)
    y = left child of z (becomes new root)
    T3 = right subtree of y
    """

    # Step 1: Identify nodes
    y  = z.left     # y will become the new root
    T3 = y.right    # T3 is the subtree between y and z

    # ─── BEFORE ─────────────────────
    #        z  (BF=+2)
    #       / \
    #      y   T4
    #     / \
    #    x   T3
    # ────────────────────────────────

    # Step 2: Perform rotation
    y.right = z     # z becomes right child of y
    z.left  = T3    # T3 becomes left child of z

    # ─── AFTER ──────────────────────
    #      y   (new root)
    #     / \
    #    x    z
    #        / \
    #       T3  T4
    # ────────────────────────────────

    # Step 3: Update heights
    # IMPORTANT: update z FIRST (it is now lower in the tree)
    z.height = 1 + max(self.get_height(z.left),
                       self.get_height(z.right))

    y.height = 1 + max(self.get_height(y.left),
                       self.get_height(y.right))

    # Step 4: Return new root
    return y

# ─── Complexity ─────────────────────────────
# Time  → O(1)  — fixed number of pointer changes
# Space → O(1)  — no extra memory used
# ────────────────────────────────────────────
```

---

## ROTATION 2 — Left Rotation (RR Case)

### When to Apply

When **BF = −2** at a node AND the **right child has BF ≤ 0** (imbalance is in the right subtree of right child).

### Before and After Diagram

```
BEFORE Left Rotation:           AFTER Left Rotation:

    z  ← BF = -2                       y
   / \                                / \
  T1   y   ← BF = -1 or 0           z    x
      / \                           / \  / \
     T2   x                        T1 T2 T3 T4
         / \
        T3  T4

z = unbalanced node (BF = -2)
y = right child of z (new root)
x = right child of y
```

### Algorithm — Left Rotation

```
ALGORITHM: LeftRotate(z)

Input  : z = unbalanced node (BF = -2)
Output : y = new root of this subtree (balanced)

Step 1: Start

Step 2: Set y  = z.right         ← y is the new root
        Set T2 = y.left          ← T2 is left subtree of y

Step 3: Perform rotation:
        y.left  = z              ← z becomes left child of y
        z.right = T2             ← T2 becomes right child of z

Step 4: Update heights (update z first because it is now lower):
        z.height = 1 + max(Height(z.left), Height(z.right))
        y.height = 1 + max(Height(y.left), Height(y.right))

Step 5: Return y                 ← y is the new root of this subtree

Step 6: Stop
```

### Code — Left Rotation

```python
def rotate_left(self, z):
    """
    Left Rotation — RR Case
    z = unbalanced node (BF = -2)
    y = right child of z (becomes new root)
    T2 = left subtree of y
    """

    # Step 1: Identify nodes
    y  = z.right    # y will become the new root
    T2 = y.left     # T2 is the subtree between z and y

    # ─── BEFORE ─────────────────────
    #    z  (BF=-2)
    #   / \
    #  T1   y
    #      / \
    #     T2   x
    # ────────────────────────────────

    # Step 2: Perform rotation
    y.left  = z     # z becomes left child of y
    z.right = T2    # T2 becomes right child of z

    # ─── AFTER ──────────────────────
    #      y  (new root)
    #     / \
    #    z    x
    #   / \
    #  T1  T2
    # ────────────────────────────────

    # Step 3: Update heights
    # IMPORTANT: update z FIRST (it is now lower in the tree)
    z.height = 1 + max(self.get_height(z.left),
                       self.get_height(z.right))

    y.height = 1 + max(self.get_height(y.left),
                       self.get_height(y.right))

    # Step 4: Return new root
    return y

# ─── Complexity ─────────────────────────────
# Time  → O(1)
# Space → O(1)
# ────────────────────────────────────────────
```

---

## ROTATION 3 — Left-Right Rotation (LR Case)

### When to Apply

When **BF = +2** at a node AND the **left child has BF = −1** (imbalance is in the right subtree of left child).

### Before and After Diagram

```
BEFORE:                AFTER LEFT on y:        AFTER RIGHT on z:

      z  (BF=+2)             z  (BF=+2)               x
     / \                    / \                       / \
    y   T4  (BF=-1)        x   T4                   y    z
   / \                    / \                       / \  / \
  T1   x                 y   T3                   T1 T2 T3 T4
      / \               / \
     T2  T3            T1  T2

Step 1: Left Rotate y → get x as new left child of z
Step 2: Right Rotate z → x becomes root
```

### Algorithm — LR Rotation

```
ALGORITHM: LR_Rotate(z)

Input  : z = unbalanced node (BF = +2)
         z.left has BF = -1
Output : balanced subtree

Step 1: Start

Step 2: Perform Left Rotation on z.left (node y):
        z.left = LeftRotate(z.left)
        (This converts LR case into LL case)

Step 3: Perform Right Rotation on z:
        newRoot = RightRotate(z)

Step 4: Return newRoot

Step 5: Stop
```

### Code — LR Rotation

```python
def lr_rotate(self, z):
    """
    LR Rotation — Left-Right Case
    BF = +2 at z AND BF = -1 at z.left

    Step 1: Left Rotate on left child (y) → converts to LL case
    Step 2: Right Rotate on z            → fixes imbalance
    """

    # ─── BEFORE ─────────────────────
    #       z  (BF=+2)
    #      / \
    #     y   T4   (BF=-1)
    #    / \
    #   T1   x
    #       / \
    #      T2  T3
    # ────────────────────────────────

    print(f"    LR Case: Left Rotate on {z.left.data}, "
          f"then Right Rotate on {z.data}")

    # Step 1: Left rotate the left child (y)
    z.left = self.rotate_left(z.left)

    # ─── AFTER LEFT ROTATE ON y ─────
    #       z  (BF=+2)
    #      / \
    #     x   T4      ← now LL case
    #    / \
    #   y   T3
    #  / \
    # T1  T2
    # ────────────────────────────────

    # Step 2: Right rotate z
    return self.rotate_right(z)

    # ─── AFTER RIGHT ROTATE ON z ────
    #        x   (new root)
    #       / \
    #      y    z
    #     / \  / \
    #    T1 T2 T3 T4
    # ────────────────────────────────

# ─── Complexity ─────────────────────────────
# Time  → O(1)  — two rotations, each O(1)
# Space → O(1)
# ────────────────────────────────────────────
```

---

## ROTATION 4 — Right-Left Rotation (RL Case)

### When to Apply

When **BF = −2** at a node AND the **right child has BF = +1** (imbalance is in the left subtree of right child).

### Before and After Diagram

```
BEFORE:                AFTER RIGHT on y:       AFTER LEFT on z:

    z  (BF=-2)              z  (BF=-2)                x
   / \                     / \                       / \
  T1   y  (BF=+1)         T1   x                   z    y
      / \                      / \                 / \  / \
     x   T4                   T2   y              T1 T2 T3 T4
    / \                           / \
   T2  T3                        T3  T4

Step 1: Right Rotate y → get x as new right child of z
Step 2: Left Rotate z  → x becomes root
```

### Algorithm — RL Rotation

```
ALGORITHM: RL_Rotate(z)

Input  : z = unbalanced node (BF = -2)
         z.right has BF = +1
Output : balanced subtree

Step 1: Start

Step 2: Perform Right Rotation on z.right (node y):
        z.right = RightRotate(z.right)
        (This converts RL case into RR case)

Step 3: Perform Left Rotation on z:
        newRoot = LeftRotate(z)

Step 4: Return newRoot

Step 5: Stop
```

### Code — RL Rotation

```python
def rl_rotate(self, z):
    """
    RL Rotation — Right-Left Case
    BF = -2 at z AND BF = +1 at z.right

    Step 1: Right Rotate on right child (y) → converts to RR case
    Step 2: Left Rotate on z               → fixes imbalance
    """

    # ─── BEFORE ─────────────────────
    #    z  (BF=-2)
    #   / \
    #  T1   y   (BF=+1)
    #      / \
    #     x   T4
    #    / \
    #   T2  T3
    # ────────────────────────────────

    print(f"    RL Case: Right Rotate on {z.right.data}, "
          f"then Left Rotate on {z.data}")

    # Step 1: Right rotate the right child (y)
    z.right = self.rotate_right(z.right)

    # ─── AFTER RIGHT ROTATE ON y ────
    #    z  (BF=-2)
    #   / \
    #  T1   x         ← now RR case
    #      / \
    #     T2   y
    #         / \
    #        T3  T4
    # ────────────────────────────────

    # Step 2: Left rotate z
    return self.rotate_left(z)

    # ─── AFTER LEFT ROTATE ON z ─────
    #        x   (new root)
    #       / \
    #      z    y
    #     / \  / \
    #    T1 T2 T3 T4
    # ────────────────────────────────

# ─── Complexity ─────────────────────────────
# Time  → O(1)  — two rotations, each O(1)
# Space → O(1)
# ────────────────────────────────────────────
```

---

## Complete Rotation Module — All 4 Together

```python
# ════════════════════════════════════════════════════════════
#          AVL TREE — ALL 4 ROTATIONS COMPLETE CODE
# ════════════════════════════════════════════════════════════


class Node:
    def __init__(self, data):
        self.data   = data
        self.left   = None
        self.right  = None
        self.height = 1         # every new node starts at height 1


class AVLRotations:

    # ──────────────────────────────────────────
    #  HELPER — GET HEIGHT
    # ──────────────────────────────────────────
    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    # ──────────────────────────────────────────
    #  HELPER — GET BALANCE FACTOR
    # ──────────────────────────────────────────
    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # ──────────────────────────────────────────
    #  HELPER — UPDATE HEIGHT
    # ──────────────────────────────────────────
    def update_height(self, node):
        node.height = 1 + max(
            self.get_height(node.left),
            self.get_height(node.right)
        )

    # ════════════════════════════════════════
    #  ROTATION 1 — RIGHT ROTATE  (LL Case)
    #  Trigger: BF = +2, left child BF >= 0
    # ════════════════════════════════════════
    def rotate_right(self, z):
        y  = z.left     # new root
        T3 = y.right    # middle subtree

        y.right = z     # rotation
        z.left  = T3    # rotation

        self.update_height(z)   # z first (now lower)
        self.update_height(y)   # y second (now higher)

        return y        # new root of this subtree

    # ════════════════════════════════════════
    #  ROTATION 2 — LEFT ROTATE   (RR Case)
    #  Trigger: BF = -2, right child BF <= 0
    # ════════════════════════════════════════
    def rotate_left(self, z):
        y  = z.right    # new root
        T2 = y.left     # middle subtree

        y.left  = z     # rotation
        z.right = T2    # rotation

        self.update_height(z)   # z first (now lower)
        self.update_height(y)   # y second (now higher)

        return y        # new root of this subtree

    # ════════════════════════════════════════
    #  ROTATION 3 — LR ROTATE   (LR Case)
    #  Trigger: BF = +2, left child BF = -1
    #  Step 1: Left Rotate left child
    #  Step 2: Right Rotate z
    # ════════════════════════════════════════
    def lr_rotate(self, z):
        z.left = self.rotate_left(z.left)   # Step 1: make it LL case
        return self.rotate_right(z)         # Step 2: fix LL case

    # ════════════════════════════════════════
    #  ROTATION 4 — RL ROTATE   (RL Case)
    #  Trigger: BF = -2, right child BF = +1
    #  Step 1: Right Rotate right child
    #  Step 2: Left Rotate z
    # ════════════════════════════════════════
    def rl_rotate(self, z):
        z.right = self.rotate_right(z.right) # Step 1: make it RR case
        return self.rotate_left(z)           # Step 2: fix RR case

    # ════════════════════════════════════════
    #  REBALANCE — DETECT CASE & APPLY
    # ════════════════════════════════════════
    def rebalance(self, node):
        self.update_height(node)
        bf = self.get_balance(node)

        # ── LL Case ──
        if bf > 1 and self.get_balance(node.left) >= 0:
            print(f"  LL Case → Right Rotate on {node.data}")
            return self.rotate_right(node)

        # ── RR Case ──
        if bf < -1 and self.get_balance(node.right) <= 0:
            print(f"  RR Case → Left Rotate on {node.data}")
            return self.rotate_left(node)

        # ── LR Case ──
        if bf > 1 and self.get_balance(node.left) < 0:
            print(f"  LR Case → Left Rotate {node.left.data}, "
                  f"Right Rotate {node.data}")
            return self.lr_rotate(node)

        # ── RL Case ──
        if bf < -1 and self.get_balance(node.right) > 0:
            print(f"  RL Case → Right Rotate {node.right.data}, "
                  f"Left Rotate {node.data}")
            return self.rl_rotate(node)

        return node     # already balanced

    # ════════════════════════════════════════
    #  INSERT (uses rebalance after each add)
    # ════════════════════════════════════════
    def insert(self, root, value):
        if root is None:
            return Node(value)
        if value < root.data:
            root.left  = self.insert(root.left,  value)
        elif value > root.data:
            root.right = self.insert(root.right, value)
        else:
            return root     # no duplicates
        return self.rebalance(root)

    # ════════════════════════════════════════
    #  PRINT TREE (with BF shown)
    # ════════════════════════════════════════
    def print_tree(self, root, level=0, tag="Root"):
        if root is None:
            return
        pad = "      " * level
        bf  = self.get_balance(root)
        print(f"{pad}{tag}: {root.data}  "
              f"[h={root.height}, bf={bf}]")
        if root.left or root.right:
            if root.left:
                self.print_tree(root.left,  level+1, "L")
            else:
                print(f"{pad}      L: NULL")
            if root.right:
                self.print_tree(root.right, level+1, "R")
            else:
                print(f"{pad}      R: NULL")


# ════════════════════════════════════════════════════════════
#  DRIVER CODE — Test All 4 Rotation Cases
# ════════════════════════════════════════════════════════════

avl  = AVLRotations()

# ── TEST 1: LL Case (insert 30, 20, 10) ──────────────────────
print("=" * 50)
print("TEST 1: LL Case → Insert 30, 20, 10")
print("=" * 50)
root = None
for v in [30, 20, 10]:
    print(f"Insert {v}:")
    root = avl.insert(root, v)
print("\nTree after LL fix:")
avl.print_tree(root)
# Expected: Right Rotation. Root = 20.

# ── TEST 2: RR Case (insert 10, 20, 30) ──────────────────────
print("\n" + "=" * 50)
print("TEST 2: RR Case → Insert 10, 20, 30")
print("=" * 50)
root = None
for v in [10, 20, 30]:
    print(f"Insert {v}:")
    root = avl.insert(root, v)
print("\nTree after RR fix:")
avl.print_tree(root)
# Expected: Left Rotation. Root = 20.

# ── TEST 3: LR Case (insert 30, 10, 20) ──────────────────────
print("\n" + "=" * 50)
print("TEST 3: LR Case → Insert 30, 10, 20")
print("=" * 50)
root = None
for v in [30, 10, 20]:
    print(f"Insert {v}:")
    root = avl.insert(root, v)
print("\nTree after LR fix:")
avl.print_tree(root)
# Expected: Left Rotate 10, then Right Rotate 30. Root = 20.

# ── TEST 4: RL Case (insert 10, 30, 20) ──────────────────────
print("\n" + "=" * 50)
print("TEST 4: RL Case → Insert 10, 30, 20")
print("=" * 50)
root = None
for v in [10, 30, 20]:
    print(f"Insert {v}:")
    root = avl.insert(root, v)
print("\nTree after RL fix:")
avl.print_tree(root)
# Expected: Right Rotate 30, then Left Rotate 10. Root = 20.
```

---

## Expected Output — All 4 Cases

```
==================================================
TEST 1: LL Case → Insert 30, 20, 10
==================================================
Insert 30:
Insert 20:
Insert 10:
  LL Case → Right Rotate on 30

Tree after LL fix:
Root: 20  [h=2, bf=0]
      L: 10  [h=1, bf=0]
      R: 30  [h=1, bf=0]

==================================================
TEST 2: RR Case → Insert 10, 20, 30
==================================================
Insert 10:
Insert 20:
Insert 30:
  RR Case → Left Rotate on 10

Tree after RR fix:
Root: 20  [h=2, bf=0]
      L: 10  [h=1, bf=0]
      R: 30  [h=1, bf=0]

==================================================
TEST 3: LR Case → Insert 30, 10, 20
==================================================
Insert 30:
Insert 10:
Insert 20:
  LR Case → Left Rotate 10, Right Rotate 30

Tree after LR fix:
Root: 20  [h=2, bf=0]
      L: 10  [h=1, bf=0]
      R: 30  [h=1, bf=0]

==================================================
TEST 4: RL Case → Insert 10, 30, 20
==================================================
Insert 10:
Insert 30:
Insert 20:
  RL Case → Right Rotate 30, Left Rotate 10

Tree after RL fix:
Root: 20  [h=2, bf=0]
      L: 10  [h=1, bf=0]
      R: 30  [h=1, bf=0]
```

---

## All 4 Rotations — One Page Summary

```
Case   BF    Left-child BF   Fix                      Rotations
─────  ────  ──────────────  ───────────────────────  ────────────────────────
LL     +2    BF ≥ 0          Right Rotate(z)          1 rotation
RR     -2    BF ≤ 0          Left Rotate(z)           1 rotation
LR     +2    BF = -1         Left Rotate(left child)  2 rotations
                             then Right Rotate(z)
RL     -2    BF = +1         Right Rotate(right child) 2 rotations
                             then Left Rotate(z)

Time for any rotation  → O(1)    (fixed pointer changes)
Time for insert/delete → O(log n) (height of balanced tree)
```