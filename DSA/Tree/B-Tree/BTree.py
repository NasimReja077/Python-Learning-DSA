class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t
        self.leaf = leaf
        self.keys = []
        self.children = []


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)
        self.t = t

    # 🔍 SEARCH
    def search(self, k, x=None):
        if x is None:
            x = self.root

        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1

        if i < len(x.keys) and x.keys[i] == k:
            return True

        if x.leaf:
            return False

        return self.search(k, x.children[i])

    # 🔧 INSERT
    def insert(self, k):
        root = self.root
        if len(root.keys) == (2*self.t - 1):
            new_root = BTreeNode(self.t, False)
            new_root.children.append(root)
            self.split_child(new_root, 0)
            self.root = new_root
            self.insert_non_full(new_root, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        i = len(x.keys) - 1

        if x.leaf:
            x.keys.append(0)
            while i >= 0 and k < x.keys[i]:
                x.keys[i+1] = x.keys[i]
                i -= 1
            x.keys[i+1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1

            if len(x.children[i].keys) == (2*self.t - 1):
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1

            self.insert_non_full(x.children[i], k)

    def split_child(self, parent, i):
        t = self.t
        y = parent.children[i]
        z = BTreeNode(t, y.leaf)

        z.keys = y.keys[t:]
        mid = y.keys[t-1]
        y.keys = y.keys[:t-1]

        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]

        parent.children.insert(i+1, z)
        parent.keys.insert(i, mid)

    # ❌ DELETE
    def delete(self, k, x=None):
        if x is None:
            x = self.root

        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1

        # Case 1: Key found in this node
        if i < len(x.keys) and x.keys[i] == k:
            if x.leaf:
                x.keys.pop(i)   # simple delete
            else:
                # Replace with successor
                succ = self.get_successor(x, i)
                x.keys[i] = succ
                self.delete(succ, x.children[i+1])
        else:
            if x.leaf:
                return  # Not found

            self.delete(k, x.children[i])

        # Adjust root if empty
        if x == self.root and len(x.keys) == 0:
            if not x.leaf:
                self.root = x.children[0]

    def get_successor(self, x, i):
        curr = x.children[i+1]
        while not curr.leaf:
            curr = curr.children[0]
        return curr.keys[0]

    # 📤 TRAVERSAL
    def traverse(self, x=None):
        if x is None:
            x = self.root

        for i in range(len(x.keys)):
            if not x.leaf:
                self.traverse(x.children[i])
            print(x.keys[i], end=" ")

        if not x.leaf:
            self.traverse(x.children[len(x.keys)])
            
            
bt = BTree(2)

values = [20, 15, 30, 40, 12, 18, 25, 50]

for v in values:
    bt.insert(v)

print("Before Deletion:")
bt.traverse()

bt.delete(30)

print("\nAfter Deleting 30:")
bt.traverse()