class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create tree manually
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)


# Traversal (Inorder)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


inorder(root)