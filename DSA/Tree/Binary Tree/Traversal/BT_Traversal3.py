from collections import deque

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


# ---------- Recursive Traversals ----------
def preorder(root):
    if root is None:
        return
    print(root.data, end=" ")      # Root
    preorder(root.left)            # Left
    preorder(root.right)           # Right


def inorder(root):
    if root is None:
        return
    inorder(root.left)             # Left
    print(root.data, end=" ")      # Root
    inorder(root.right)            # Right


def postorder(root):
    if root is None:
        return
    postorder(root.left)           # Left
    postorder(root.right)          # Right
    print(root.data, end=" ")      # Root


def level_order(root):
    if root is None:
        print("Tree is empty")
        return
    queue = deque([root])
    print("Level Order:", end=" ")
    while queue:
        node = queue.popleft()
        print(node.data, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print()


# ---------- Main Program ----------
root = Node(1)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(8)

print("Pre-order: ", end="")
preorder(root)
print()

print("In-order:  ", end="")
inorder(root)
print()

print("Post-order:", end="")
postorder(root)
print()

print("Level-order:", end=" ")
level_order(root)