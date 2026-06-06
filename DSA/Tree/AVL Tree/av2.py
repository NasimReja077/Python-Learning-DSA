# ════════════════════════════════════════════════════════════
#                   AVL TREE IMPLEMENTATION
# ════════════════════════════════════════════════════════════
# AVL Tree = Self-balancing BST
# Balance Factor (BF) = height(left) - height(right)
# BF must be -1, 0, or +1 at every node
# If |BF| > 1 → perform rotation to rebalance
# ════════════════════════════════════════════════════════════

from collections import deque


# ──────────────────────────────────────────
#  NODE CLASS
# ──────────────────────────────────────────
class Node:
    def __init__(self, value):
        self.data   = value
        self.left   = None
        self.right  = None
        self.height = 1       # new node starts at height 1


# ══════════════════════════════════════════
#  AVL TREE CLASS
# ══════════════════════════════════════════
class AVLTree:

    # ──────────────────────────────────────
    #  UTILITY: GET HEIGHT
    # ──────────────────────────────────────
    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    # ──────────────────────────────────────
    #  UTILITY: GET BALANCE FACTOR
    #  BF = height(left) - height(right)
    #  BF =  1 → left heavy (ok)
    #  BF =  0 → perfectly balanced (ok)
    #  BF = -1 → right heavy (ok)
    #  BF =  2 → left-left or left-right case → rotate
    #  BF = -2 → right-right or right-left case → rotate
    # ──────────────────────────────────────
    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # ──────────────────────────────────────
    #  UTILITY: UPDATE HEIGHT
    # ──────────────────────────────────────
    def update_height(self, node):
        if node is None:
            return
        node.height = 1 + max(
            self.get_height(node.left),
            self.get_height(node.right)
        )

    # ══════════════════════════════════════
    #  ROTATIONS
    # ══════════════════════════════════════

    # ──────────────────────────────────────
    #  RIGHT ROTATION (LL Case)
    #
    #      z                y
    #     / \              / \
    #    y   T4    →     x    z
    #   / \             / \  / \
    #  x  T3           T1 T2 T3 T4
    # / \
    # T1 T2
    # ──────────────────────────────────────
    def rotate_right(self, z):
        y  = z.left        # y is the new root
        T3 = y.right       # T3 is the right subtree of y

        # Perform rotation
        y.right = z        # z becomes right child of y
        z.left  = T3       # T3 becomes left child of z

        # Update heights (z first because it's now lower)
        self.update_height(z)
        self.update_height(y)

        print(f"    Right Rotation on node {z.data} → new subtree root: {y.data}")
        return y            # y is the new root of this subtree

    # ──────────────────────────────────────
    #  LEFT ROTATION (RR Case)
    #
    #   z                  y
    #  / \                / \
    # T1   y      →      z   x
    #     / \           / \ / \
    #    T2   x        T1 T2 T3 T4
    #        / \
    #       T3  T4
    # ──────────────────────────────────────
    def rotate_left(self, z):
        y  = z.right       # y is the new root
        T2 = y.left        # T2 is the left subtree of y

        # Perform rotation
        y.left  = z        # z becomes left child of y
        z.right = T2       # T2 becomes right child of z

        # Update heights
        self.update_height(z)
        self.update_height(y)

        print(f"    Left Rotation on node {z.data} → new subtree root: {y.data}")
        return y            # y is the new root of this subtree

    # ──────────────────────────────────────
    #  REBALANCE: CHECK AND APPLY ROTATION
    #
    #  4 Cases:
    #  1. LL → Right Rotation
    #  2. RR → Left Rotation
    #  3. LR → Left Rotation on left child, then Right Rotation
    #  4. RL → Right Rotation on right child, then Left Rotation
    # ──────────────────────────────────────
    def rebalance(self, node, value=None):
        # Update height of current node
        self.update_height(node)

        # Get balance factor
        balance = self.get_balance(node)

        # ── CASE 1: LL (Left-Left) ──
        # BF = +2 and new node inserted in LEFT subtree of LEFT child
        if balance > 1 and self.get_balance(node.left) >= 0:
            print(f"  LL Case at node {node.data} (BF={balance})")
            return self.rotate_right(node)

        # ── CASE 2: RR (Right-Right) ──
        # BF = -2 and new node inserted in RIGHT subtree of RIGHT child
        if balance < -1 and self.get_balance(node.right) <= 0:
            print(f"  RR Case at node {node.data} (BF={balance})")
            return self.rotate_left(node)

        # ── CASE 3: LR (Left-Right) ──
        # BF = +2 and new node inserted in RIGHT subtree of LEFT child
        if balance > 1 and self.get_balance(node.left) < 0:
            print(f"  LR Case at node {node.data} (BF={balance})")
            node.left = self.rotate_left(node.left)   # Step 1: Left rotate left child
            return self.rotate_right(node)             # Step 2: Right rotate current node

        # ── CASE 4: RL (Right-Left) ──
        # BF = -2 and new node inserted in LEFT subtree of RIGHT child
        if balance < -1 and self.get_balance(node.right) > 0:
            print(f"  RL Case at node {node.data} (BF={balance})")
            node.right = self.rotate_right(node.right) # Step 1: Right rotate right child
            return self.rotate_left(node)               # Step 2: Left rotate current node

        return node  # No imbalance found, return unchanged

    # ══════════════════════════════════════
    #  INSERT
    # ══════════════════════════════════════
    def insert(self, root, value):
        # Step 1: Normal BST insert
        if root is None:
            return Node(value)

        if value < root.data:
            root.left  = self.insert(root.left,  value)
        elif value > root.data:
            root.right = self.insert(root.right, value)
        else:
            print(f"  Duplicate {value} — not inserted")
            return root   # No duplicates

        # Step 2: Rebalance on the way back up
        return self.rebalance(root, value)

    # time complexity: O(log n) always (tree stays balanced)
    # space complexity: O(log n) recursive call stack

    # ══════════════════════════════════════
    #  DELETE
    # ══════════════════════════════════════
    def get_min_node(self, node):
        """Find node with minimum value (leftmost node)."""
        while node.left is not None:
            node = node.left
        return node

    def delete(self, root, value):
        # Step 1: Normal BST delete
        if root is None:
            print(f"  {value} not found in tree")
            return root

        if value < root.data:
            root.left  = self.delete(root.left,  value)
        elif value > root.data:
            root.right = self.delete(root.right, value)
        else:
            # Node found — handle 3 cases

            # Case 1 & 2: No child or one child
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            # Case 3: Two children
            # Find inorder successor (min of right subtree)
            successor       = self.get_min_node(root.right)
            root.data       = successor.data                       # Copy successor value
            root.right      = self.delete(root.right, successor.data)  # Delete successor

        # Step 2: Rebalance on the way back up
        return self.rebalance(root)

    # time complexity: O(log n) always
    # space complexity: O(log n)

    # ══════════════════════════════════════
    #  SEARCH
    # ══════════════════════════════════════
    def search(self, root, value):
        if root is None:
            print(f"  {value} → NOT FOUND")
            return False
        if root.data == value:
            print(f"  {value} → FOUND")
            return True
        if value < root.data:
            return self.search(root.left,  value)
        else:
            return self.search(root.right, value)

    # time complexity: O(log n) always (guaranteed balanced)
    # space complexity: O(log n)

    # ══════════════════════════════════════
    #  TRAVERSALS
    # ══════════════════════════════════════
    def inorder(self, root, result=None):
        if result is None:
            result = []
        if root:
            self.inorder(root.left,  result)
            result.append(root.data)
            self.inorder(root.right, result)
        return result

    def preorder(self, root, result=None):
        if result is None:
            result = []
        if root:
            result.append(root.data)
            self.preorder(root.left,  result)
            self.preorder(root.right, result)
        return result

    def postorder(self, root, result=None):
        if result is None:
            result = []
        if root:
            self.postorder(root.left,  result)
            self.postorder(root.right, result)
            result.append(root.data)
        return result

    def level_order(self, root):
        if root is None:
            return []
        result = []
        queue  = deque([root])
        while queue:
            node = queue.popleft()
            result.append(node.data)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        return result

    # ══════════════════════════════════════
    #  UTILITIES
    # ══════════════════════════════════════
    def find_min(self, root):
        if root is None:
            return None
        while root.left:
            root = root.left
        return root.data

    def find_max(self, root):
        if root is None:
            return None
        while root.right:
            root = root.right
        return root.data

    def get_height_of_tree(self, root):
        return self.get_height(root)

    def get_balance_factor(self, root):
        return self.get_balance(root)

    # ══════════════════════════════════════
    #  PRINT TREE (visual 2D display)
    # ══════════════════════════════════════
    def print_tree(self, root, level=0, prefix="Root: "):
        if root is None:
            return
        print(" " * (level * 6) + prefix + str(root.data) +
              f"  [h={root.height}, bf={self.get_balance(root)}]")
        if root.left or root.right:
            if root.left:
                self.print_tree(root.left,  level + 1, "L── ")
            else:
                print(" " * ((level + 1) * 6) + "L── None")
            if root.right:
                self.print_tree(root.right, level + 1, "R── ")
            else:
                print(" " * ((level + 1) * 6) + "R── None")

    # ══════════════════════════════════════
    #  IS VALID AVL TREE (verify)
    # ══════════════════════════════════════
    def is_valid_avl(self, root):
        """Check if tree satisfies AVL property at every node."""
        if root is None:
            return True
        bf = self.get_balance(root)
        if abs(bf) > 1:
            return False
        return self.is_valid_avl(root.left) and self.is_valid_avl(root.right)


# ════════════════════════════════════════════════════════════
#  DRIVER CODE
# ════════════════════════════════════════════════════════════

avl  = AVLTree()
root = None

# ── Insertions ──────────────────────────────────────────────
print("=" * 55)
print("              AVL TREE — INSERTIONS")
print("=" * 55)

values = [30, 20, 10, 25, 40, 50, 5]

for v in values:
    print(f"\nInserting {v}:")
    root = avl.insert(root, v)

print("\n── Tree after all insertions ──")
avl.print_tree(root)

# ── Traversals ──────────────────────────────────────────────
print("\n" + "=" * 55)
print("              TRAVERSALS")
print("=" * 55)
print("Inorder    (sorted) :", avl.inorder(root))
print("Preorder            :", avl.preorder(root))
print("Postorder           :", avl.postorder(root))
print("Level Order         :", avl.level_order(root))

# ── Properties ──────────────────────────────────────────────
print("\n" + "=" * 55)
print("              PROPERTIES")
print("=" * 55)
print("Minimum value  :", avl.find_min(root))
print("Maximum value  :", avl.find_max(root))
print("Tree height    :", avl.get_height_of_tree(root))
print("Root BF        :", avl.get_balance_factor(root))
print("Valid AVL tree :", avl.is_valid_avl(root))

# ── Search ──────────────────────────────────────────────────
print("\n" + "=" * 55)
print("              SEARCH")
print("=" * 55)
avl.search(root, 25)
avl.search(root, 99)

# ── Deletions ───────────────────────────────────────────────
print("\n" + "=" * 55)
print("              DELETIONS")
print("=" * 55)

print("\nDeleting 20 (node with two children):")
root = avl.delete(root, 20)
avl.print_tree(root)
print("Inorder after deleting 20 :", avl.inorder(root))
print("Valid AVL after delete     :", avl.is_valid_avl(root))

print("\nDeleting 50 (leaf node):")
root = avl.delete(root, 50)
avl.print_tree(root)
print("Inorder after deleting 50 :", avl.inorder(root))
print("Valid AVL after delete     :", avl.is_valid_avl(root))

print("\nDeleting 10 (leaf node):")
root = avl.delete(root, 10)
avl.print_tree(root)
print("Inorder after deleting 10 :", avl.inorder(root))
print("Valid AVL after delete     :", avl.is_valid_avl(root))

# ── Duplicate test ──────────────────────────────────────────
print("\n" + "=" * 55)
print("              DUPLICATE TEST")
print("=" * 55)
print("Inserting 30 again:")
root = avl.insert(root, 30)