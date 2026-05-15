class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t
        self.keys = []
        self.children = []
        self.leaf = leaf
        
        
class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)
        self.t = t

    def traverse(self, node):
        for i in range(len(node.keys)):
            if not node.leaf:
                self.traverse(node.children[i])
                print(node.keys[i], end=" ")
        if not node.leaf:
            self.traverse(node.children[len(node.keys)])

    def search(self, node, k):
        i = 0
        while i < len(node.keys) and k > node.keys[i]:
            i += 1

        if i < len(node.keys) and node.keys[i] == k:
            print("Found:", k)
            return

        if node.leaf:
            print("Not Found:", k)
            return

        self.search(node.children[i], k)
        
def insert(self, k):
        root = self.root

        if len(root.keys) == (2*self.t - 1):
            new_root = BTreeNode(self.t, False)
            new_root.children.append(root)
            self.split_child(new_root, 0)

            i = 0
            if new_root.keys[0] < k:
                i += 1
            self.insert_non_full(new_root.children[i], k)

            self.root = new_root
        else:
            self.insert_non_full(root, k)
     
def insert_non_full(self, node, k):
        i = len(node.keys) - 1

        if node.leaf:
            node.keys.append(0)
            while i >= 0 and k < node.keys[i]:
                node.keys[i+1] = node.keys[i]
                i -= 1
            node.keys[i+1] = k
        else:
            while i >= 0 and k < node.keys[i]:
                i -= 1
            i += 1

            if len(node.children[i].keys) == (2*self.t - 1):
                self.split_child(node, i)
                if k > node.keys[i]:
                    i += 1

            self.insert_non_full(node.children[i], k)
            
def split_child(self, parent, i):
        t = self.t
        node = parent.children[i]

        new_node = BTreeNode(t, node.leaf)

        parent.keys.insert(i, node.keys[t-1])
        parent.children.insert(i+1, new_node)

        new_node.keys = node.keys[t:(2*t-1)]
        node.keys = node.keys[0:(t-1)]

        if not node.leaf:
            new_node.children = node.children[t:(2*t)]
            node.children = node.children[0:t]
            
    def delete(self, node, k):
        t = self.t
        i = 0

        while i < len(node.keys) and k > node.keys[i]:
            i += 1

        # CASE 1: Key found in this node
        if i < len(node.keys) and node.keys[i] == k:

            # CASE 1A: Leaf node
            if node.leaf:
                node.keys.pop(i)

            else:
                # CASE 1B: Internal node
                if len(node.children[i].keys) >= t:
                    pred = self.get_predecessor(node, i)
                    node.keys[i] = pred
                    self.delete(node.children[i], pred)

                elif len(node.children[i+1].keys) >= t:
                    succ = self.get_successor(node, i)
                    node.keys[i] = succ
                    self.delete(node.children[i+1], succ)

                else:
                    self.merge(node, i)
                    self.delete(node.children[i], k)

        else:
            # CASE 2: Key not found here
            if node.leaf:
                return

            flag = (i == len(node.keys))

            if len(node.children[i].keys) < t:
                self.fill(node, i)

            if flag and i > len(node.keys):
                self.delete(node.children[i-1], k)
            else:
                self.delete(node.children[i], k)
                
                
    def get_predecessor(self, node, i):
        cur = node.children[i]
        while not cur.leaf:
            cur = cur.children[-1]
        return cur.keys[-1]
   
       def get_successor(self, node, i):
        cur = node.children[i+1]
        while not cur.leaf:
            cur = cur.children[0]
        return cur.keys[0]
   
       def fill(self, node, i):
        if i != 0 and len(node.children[i-1].keys) >= self.t:
            self.borrow_from_prev(node, i)
        elif i != len(node.keys) and len(node.children[i+1].keys) >= self.t:
            self.borrow_from_next(node, i)
        else:
            if i != len(node.keys):
                self.merge(node, i)
            else:
                self.merge(node, i-1)
                
         def borrow_from_prev(self, node, i):
        child = node.children[i]
        sibling = node.children[i-1]

        child.keys.insert(0, node.keys[i-1])

        if not child.leaf:
            child.children.insert(0, sibling.children.pop())

        node.keys[i-1] = sibling.keys.pop()
        
         def borrow_from_next(self, node, i):
        child = node.children[i]
        sibling = node.children[i+1]

        child.keys.append(node.keys[i])

        if not child.leaf:
            child.children.append(sibling.children.pop(0))

        node.keys[i] = sibling.keys.pop(0)
        
            def merge(self, node, i):
        child = node.children[i]
        sibling = node.children[i+1]

        child.keys.append(node.keys[i])
        child.keys.extend(sibling.keys)

        if not child.leaf:
            child.children.extend(sibling.children)

        node.keys.pop(i)
        node.children.pop(i+1)
        
        bt = BTree(3)

arr = [20, 15, 30, 40, 12, 18, 25, 50]

for x in arr:
    bt.insert(x)

print("Before Deletion:")
bt.traverse(bt.root)

bt.delete(bt.root, 25)

print("\nAfter Deletion:")
bt.traverse(bt.root)