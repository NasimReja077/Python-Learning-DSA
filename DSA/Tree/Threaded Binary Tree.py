class ThreadedNode:
    def __init__(self, data):
        self.data    = data
        self.left    = None
        self.right   = None
        self.lthread = False   # False = real child, True = thread
        self.rthread = False

def leftmost(node):
    """Go to the leftmost node of a subtree (used during traversal)."""
    while node is not None and node.lthread == False:
        node = node.left
    return node

def construct_threaded_tree():
    # Step 1: Create all nodes
    header = ThreadedNode(-1)   # dummy header node
    n1 = ThreadedNode(1)        # root
    n2 = ThreadedNode(2)
    n3 = ThreadedNode(3)
    n4 = ThreadedNode(4)
    n5 = ThreadedNode(5)

    # Step 2: Set up header
    header.left    = n1       # header's left → root (real link)
    header.lthread = False
    header.right   = header   # header's right → itself (thread)
    header.rthread = True

    # Step 3: Build real tree links (node 1 and node 2)
    n1.left  = n2;  n1.lthread = False   # real left child
    n1.right = n3;  n1.rthread = False   # real right child

    n2.left  = n4;  n2.lthread = False   # real left child
    n2.right = n5;  n2.rthread = False   # real right child

    # Step 4: Thread node 4 (leaf)
    # Inorder: no predecessor → header, successor → n2
    n4.left    = header;  n4.lthread = True   # thread to header
    n4.right   = n2;      n4.rthread = True   # thread to inorder successor

    # Step 5: Thread node 5 (leaf)
    # Inorder: predecessor → n2, successor → n1
    n5.left    = n2;   n5.lthread = True   # thread to inorder predecessor
    n5.right   = n1;   n5.rthread = True   # thread to inorder successor

    # Step 6: Thread node 3 (leaf)
    # Inorder: predecessor → n1, no successor → header
    n3.left    = n1;     n3.lthread = True   # thread to inorder predecessor
    n3.right   = header; n3.rthread = True   # thread to header (no successor)

    return header

# Inorder traversal using threads
def inorder(header):
    cur = leftmost(header.left)    # go to leftmost of root
    while cur != header:
        print(cur.data, end=" → ")
        if cur.rthread:
            cur = cur.right        # follow thread
        else:
            cur = leftmost(cur.right)  # go right, find leftmost

header = construct_threaded_tree()
inorder(header)
# Output: 4 → 2 → 5 → 1 → 3