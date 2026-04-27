class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


# -------- INSERT --------
def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.data:
        root.left = insert(root.left, value)
    elif value > root.data:
        root.right = insert(root.right, value)

    return root


# -------- SEARCH --------
def search(root, value):
    if root is None:
        print("Element not found")
        return

    if root.data == value:
        print("Element Found")
        return

    elif value < root.data:
        search(root.left, value)
    else:
        search(root.right, value)


# -------- GET SUCCESSOR --------
def get_successor(root):
    root = root.right
    while root and root.left:
        root = root.left
    return root


# -------- DELETE --------
def delete(root, value):
    if root is None:
        return root

    if value < root.data:
        root.left = delete(root.left, value)

    elif value > root.data:
        root.right = delete(root.right, value)

    else:
        # Case 1 & 2
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        # Case 3
        succ = get_successor(root)
        root.data = succ.data
        root.right = delete(root.right, succ.data)

    return root


# -------- TRAVERSALS --------

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# -------- FIND MIN --------
def find_min(root):
    while root.left:
        root = root.left
    return root.data


# -------- FIND MAX --------
def find_max(root):
    while root.right:
        root = root.right
    return root.data


# -------- FIND HEIGHT --------
def height(root):
    if root is None:
        return -1   # height in edges
    return 1 + max(height(root.left), height(root.right))


# -------- DRIVER --------
root = None
values = [20, 15, 30, 40, 12, 18, 25, 50]

for v in values:
    root = insert(root, v)

print("Inorder:", end=" ")
inorder(root)

print("\nPreorder:", end=" ")
preorder(root)

print("\nPostorder:", end=" ")
postorder(root)

print("\nMin:", find_min(root))
print("Max:", find_max(root))
print("Height:", height(root))

search(root, 18)
search(root, 100)