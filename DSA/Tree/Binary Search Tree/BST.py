class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

def insert(root, value):
    if (root == None):
        return Node(value) #
   
    if (root.data == value): # 
        return root
   
    if (root.data > value): 
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def search(root, value):
    if (root == None):
        print("Element not found", end="\n")
        return
    if (root.data == value):
        print("Element Found", end="\n")
        return
    if (root.data > value):
        search(root.left, value)
    else:
        search(root.right, value)
 
def get_successor(root):
    root = root.right
    while( root != None and root.left != None):
        root = root.left
    return root
       
def delete(root , value):
    if(root == None):
        return root
   # 1. Search for the node
    if(root.data > value):
        root.left = delete(root.left , value)
    elif(root.data < value):
        root.right = delete(root.right , value)       
    else:
         # 2. Node found, handle deletion
         # Case A & B: Node has one child or no children
         if(root.left == None):
              return root.right
         if(root.right == None):
              return root.left
         else:
              # Case C: Node has two children
              succ = get_successor(root)
              root.data = succ.data
              # Delete the successor
              root.right = delete(root.right,succ.data)
              return root

def InOrder(root):
    if (root != None):
        InOrder(root.left)
        print(root.data, end=" ")
        InOrder(root.right)
        
# -------- FIND MIN --------
# -------- FIND MAX --------
# -------- FIND HEIGHT --------

# --- Driver Code ---

root = insert(None, 20)
root = insert(root, 15)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 12)
root = insert(root, 18)
root = insert(root, 25)
root = insert(root, 50)

InOrder(root)

search(root, 18)
search(root, 100)

