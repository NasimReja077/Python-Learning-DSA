# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# ---------------- INSERTION ----------------
def insert(root, value):
    new_node = Node(value)
    
    if root is None:
        return new_node
    
    queue = [root]
    
    while queue:
        temp = queue.pop(0)
        
        if temp.left is None:
            temp.left = new_node
            return root
        else:
            queue.append(temp.left)
        
        if temp.right is None:
            temp.right = new_node
            return root
        else:
            queue.append(temp.right)


# ---------------- TRAVERSALS ----------------
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


# ---------------- LEVEL ORDER ----------------
def level_order(root):
    if root is None:
        return
    
    queue = [root]
    
    while queue:
        temp = queue.pop(0)
        print(temp.data, end=" ")
        
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)


# ---------------- SEARCH ----------------
def search(root, key):
    if root is None:
        return False
    
    if root.data == key:
        return True
    
    return search(root.left, key) or search(root.right, key)


# ---------------- HEIGHT ----------------
def height(root):
    if root is None:
        return -1
    
    return 1 + max(height(root.left), height(root.right))


# ---------------- DELETION ----------------
def delete(root, key):
    if root is None:
        return None
    
    queue = [root]
    key_node = None
    
    while queue:
        temp = queue.pop(0)
        
        if temp.data == key:
            key_node = temp
        
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)
    
    if key_node:
        deepest = temp
        key_node.data = deepest.data
        delete_deepest(root, deepest)
    
    return root


def delete_deepest(root, d_node):
    queue = [root]
    
    while queue:
        temp = queue.pop(0)
        
        if temp.left:
            if temp.left == d_node:
                temp.left = None
                return
            else:
                queue.append(temp.left)
        
        if temp.right:
            if temp.right == d_node:
                temp.right = None
                return
            else:
                queue.append(temp.right)


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    root = None
    
    # Insert nodes
    root = insert(root, "A")
    root = insert(root, "B")
    root = insert(root, "C")
    root = insert(root, "D")
    root = insert(root, "E")
    root = insert(root, "F")
    
    print("Inorder Traversal:")
    inorder(root)
    
    print("\nPreorder Traversal:")
    preorder(root)
    
    print("\nPostorder Traversal:")
    postorder(root)
    
    print("\nLevel Order Traversal:")
    level_order(root)
    
    print("\nSearch for E:", search(root, "E"))
    
    print("Height of Tree:", height(root))
    
    print("\nDeleting node B...")
    root = delete(root, "B")
    
    print("Level Order after deletion:")
    level_order(root)