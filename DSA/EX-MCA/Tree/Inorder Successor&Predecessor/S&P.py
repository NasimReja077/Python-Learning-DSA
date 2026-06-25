class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Helper: Find Minimum in subtree
def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

# Helper: Find Maximum in subtree
def max_value_node(node):
    current = node
    while current.right:
        current = current.right
    return current

# ==================== INORDER SUCCESSOR ====================
def inorder_successor(root, node):
    if not node:
        return None
    
    # Case 1: Node has right subtree
    if node.right:
        return min_value_node(node.right)
    
    # Case 2: No right subtree - Traverse from root
    successor = None
    current = root
    while current:
        if node.data < current.data:
            successor = current
            current = current.left
        elif node.data > current.data:
            current = current.right
        else:
            break
    return successor

# ==================== INORDER PREDECESSOR ====================
def inorder_predecessor(root, node):
    if not node:
        return None
    
    # Case 1: Node has left subtree
    if node.left:
        return max_value_node(node.left)
    
    # Case 2: No left subtree - Traverse from root
    predecessor = None
    current = root
    while current:
        if node.data > current.data:
            predecessor = current
            current = current.right
        elif node.data < current.data:
            current = current.left
        else:
            break
    return predecessor

# -------- SEARCH --------
def search(root, value):
    if root is None or root.data == value:
        return root
    
    if value < root.data: # Search in left subtree
        return search(root.left, value)
    else:
        return search(root.right, value)
   
def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

values = [2, 30, 6, 5, 10, 25, 15, 35, 50, 40, 7, 8, 9]
root = None
for val in values:
    root = insert(root, val)
    
# Test Inorder Successor
node = search(root, 15)    
   
successor = inorder_successor(root, node)

if successor:
     print(f"Inorder Successor of {node.data} is {successor.data}")
else:     
     print(f"Inorder Successor of {node.data} does not exist")  
      
# Test Inorder Predecessor
predecessor = inorder_predecessor(root, node)
if predecessor:     
     print(f"Inorder Predecessor of {node.data} is {predecessor.data}")
else:    
     print(f"Inorder Predecessor of {node.data} does not exist")
     

