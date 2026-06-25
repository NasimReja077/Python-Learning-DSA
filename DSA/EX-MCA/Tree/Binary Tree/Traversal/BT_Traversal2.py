class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


# Preorder Traversal (Root → Left → Right)
def preOrder(root):
    if root is not None:
        print(root.data, end=" ")
        preOrder(root.left)
        preOrder(root.right)


# Inorder Traversal (Left → Root → Right)
def InOrder(root):
    if root is not None:
        InOrder(root.left)
        print(root.data, end=" ")
        InOrder(root.right)


# Postorder Traversal (Left → Right → Root)
def PostOrder(root):
    if root is not None:
        PostOrder(root.left)
        PostOrder(root.right)
        print(root.data, end=" ")


# Tree Creation
root = Node(1)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(8)


print("Pre-order:", end=" ")
preOrder(root)   # Root Left Right

print("\nIn-order:", end=" ")
InOrder(root)    # Left Root Right

print("\nPost-order:", end=" ")
PostOrder(root)  # Left Right Root


'''
Tree Structure (Your Example)
        1
       / \
      3   5
     / \   \
    2   4   8
'''

'''🔹 Preorder Algorithm (NLR)
1. Visit root node
2. Traverse left subtree
3. Traverse right subtree
🔹 Inorder Algorithm (LNR)
1. Traverse left subtree
2. Visit root node
3. Traverse right subtree
🔹 Postorder Algorithm (LRN)
1. Traverse left subtree
2. Traverse right subtree
3. Visit root node
🔹 Level Order (BFS)
1. Create queue and insert root
2. While queue is not empty:
   a. Remove node from queue
   b. Print node
   c. Insert left child
   d. Insert right child
'''

'''
from collections import deque

# -------- NODE CLASS --------
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


# -------- TRAVERSALS --------

# 1. Preorder Traversal (Root → Left → Right)
def preorder(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


# 2. Inorder Traversal (Left → Root → Right)
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


# 3. Postorder Traversal (Left → Right → Root)
def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")


# 4. Level Order Traversal (BFS) 🔥
def level_order(root):
    if root is None:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.data, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# -------- TREE CREATION --------
root = Node(1)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(8)


# -------- OUTPUT --------
print("Preorder:", end=" ")
preorder(root)

print("\nInorder:", end=" ")
inorder(root)

print("\nPostorder:", end=" ")
postorder(root)

print("\nLevel Order:", end=" ")
level_order(root)'''
