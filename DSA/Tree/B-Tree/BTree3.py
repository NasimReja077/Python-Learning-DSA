# ─────────────────────────────────────────
#  B-TREE NODE
# ─────────────────────────────────────────
class BTreeNode:
    def __init__(self, leaf=False):
        self.keys     = []        # keys stored in this node
        self.children = []        # child node pointers
        self.leaf     = leaf      # is this a leaf node?
        self.n        = 0         # current number of keys


# ─────────────────────────────────────────
#  B-TREE CLASS
# ─────────────────────────────────────────
class BTree:
    def __init__(self, t):
        self.t    = t             # minimum degree (ceil(m/2))
                                  # each node: t-1 <= keys <= 2t-1
        self.root = BTreeNode(leaf=True)

    # ─── SEARCH ───────────────────────────
    def search(self, key, node=None):
        if node is None:
            node = self.root

        i = 0
        while i < node.n and key > node.keys[i]:
            i += 1

        if i < node.n and key == node.keys[i]:
            return (node, i)          # found

        if node.leaf:
            return None               # not found

        return self.search(key, node.children[i])

    # ─── INSERT ───────────────────────────
    def insert(self, key):
        root = self.root

        if root.n == 2 * self.t - 1:   # root is full → must split
            new_root = BTreeNode(leaf=False)
            new_root.children.append(self.root)
            self._split_child(new_root, 0, self.root)
            self.root = new_root
            self._insert_non_full(new_root, key)
        else:
            self._insert_non_full(root, key)

    def _insert_non_full(self, node, key):
        i = node.n - 1

        if node.leaf:
            # Insert key in sorted position
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
            node.n += 1

        else:
            # Find correct child to descend into
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1

            # Split child if full before descending
            if node.children[i].n == 2 * self.t - 1:
                self._split_child(node, i, node.children[i])
                if key > node.keys[i]:
                    i += 1

            self._insert_non_full(node.children[i], key)

    def _split_child(self, parent, i, full_child):
        t          = self.t
        new_node   = BTreeNode(leaf=full_child.leaf)
        new_node.n = t - 1

        # Copy right half of full_child keys to new_node
        new_node.keys = full_child.keys[t:]           # keys after median
        full_child.keys = full_child.keys[:t - 1]     # keys before median

        # Copy right half of children if not leaf
        if not full_child.leaf:
            new_node.children = full_child.children[t:]
            full_child.children = full_child.children[:t]

        # Median key moves up to parent
        median = full_child.keys[t - 1] if len(full_child.keys) >= t else new_node.keys[0]

        # Actually get median before slicing
        all_keys       = full_child.keys[:t - 1]
        median_key     = full_child.keys[t - 1] if False else None

        # Redo cleanly
        t = self.t
        new_node = BTreeNode(leaf=full_child.leaf)
        keys = full_child.keys[:]
        median_key = keys[t - 1]
        new_node.keys = keys[t:]
        new_node.n   = len(new_node.keys)
        full_child.keys   = keys[:t - 1]
        full_child.n   = len(full_child.keys)

        if not full_child.leaf:
            new_node.children   = full_child.children[t:]
            full_child.children = full_child.children[:t]

        # Insert median into parent
        parent.children.insert(i + 1, new_node)
        parent.keys.insert(i, median_key)
        parent.n += 1

    # ─── DISPLAY ──────────────────────────
    def display(self):
        self._display(self.root, level=0)

    def _display(self, node, level):
        indent = "    " * level
        print(f"{indent}Level {level}: {node.keys}")
        if not node.leaf:
            for child in node.children:
                self._display(child, level + 1)

    # ─── TRAVERSE (Inorder) ───────────────
    def traverse(self):
        result = []
        self._traverse(self.root, result)
        print("Sorted keys:", result)
        return result

    def _traverse(self, node, result):
        for i in range(node.n):
            if not node.leaf:
                self._traverse(node.children[i], result)
            result.append(node.keys[i])
        if not node.leaf:
            self._traverse(node.children[node.n], result)

    # ─── HEIGHT ───────────────────────────
    def height(self):
        h = 0
        node = self.root
        while not node.leaf:
            node = node.children[0]
            h += 1
        return h


# ─────────────────────────────────────────
#  MAIN — B-TREE DEMO
# ─────────────────────────────────────────
print("=" * 50)
print("         B-TREE (minimum degree t=2, order=4)")
print("=" * 50)

bt = BTree(t=2)    # t=2 means order 4: max 3 keys, max 4 children

keys_to_insert = [10, 20, 5, 6, 12, 30, 7, 17]

print("\n── Insertions ──")
for key in keys_to_insert:
    bt.insert(key)
    print(f"  Inserted {key}")

print("\n── Tree Structure ──")
bt.display()

print("\n── Traversal (Inorder = Sorted) ──")
bt.traverse()

print(f"\n── Height: {bt.height()} ──")

print("\n── Search ──")
result = bt.search(6)
print(f"  Search 6:  {'FOUND' if result else 'NOT FOUND'}")
result = bt.search(15)
print(f"  Search 15: {'FOUND' if result else 'NOT FOUND'}")