from collections import deque
# from logging import root


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


# -------- INSERT --------
def insert(root, value):
    
    # If tree empty, create root
    if root is None:
        return Node(value)
    
    # Duplicate values not allowed
    if root.data == value:
        return root
        
# > means greater than
# < means less than
# 15 > 10 -> True
# 10 < 15 -> True

    # Insert in left subtree
    if value < root.data: # hear value is smaller and root data is big
        root.left = insert(root.left, value)
    # Insert in right subtree
    elif value > root.data:
        root.right = insert(root.right, value)

    return root

# time complexity: 
# - Average Case: O(log n) - when the tree is balanced
# - Worst Case: O(n) - when the tree is skewed (like a linked list)
# space complexity: O(h) where h is the height of the tree 


# -------- SEARCH --------
def search(root, value):
    # Value not found
    if root is None:
        print("Element not found", end="\n")
        return False

    # Value found
    if root.data == value:
        print("Element Found", end="\n")
        return True

    # Search in left subtree
    if value < root.data:
        return search(root.left, value)
    
    else: # Search in right subtree
        return search(root.right, value)

# time complexity: 
# - Average Case: O(log n)
# - Worst Case: O(n) 
# space complexity: O(h)


# -------- GET SUCCESSOR --------
def get_successor(root):
    root = root.right
    while root and root.left is not None:
        root = root.left
    return root



# -------- DELETE --------
def delete(root, value):
    if root is None: #  If Node not found, return None
        return root
    
    # 1. Search for the node
    if value < root.data:
        root.left = delete(root.left, value)
        
    elif value > root.data:
        root.right = delete(root.right, value)

    else:
        # Case 1: Node has No Child (Leaf Node)
        if root.left is None and root.right is None:
            return None
        
        # 2. Node found, handle deletion
        # Case 2A & 2B: Node has one child or no children
        if root.left is None:
            return root.right
        
        if root.right is None:
            return root.left

        # Case 3: Node has two children
        # Find the successor (smallest value in the right subtree)
        succ = get_successor(root)
        root.data = succ.data # Replace nodes value with successor's value
        root.right = delete(root.right, succ.data) # Delete the successor node from right subtree
    return root

# time complexity: 
# - Average Case: O(log n) 
# - Worst Case: O(n)
# space complexity: O(h) 


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
        
# Level Order Traversal
def level_order(root):
    if root is None:
        print("Tree is empty")
        return
    
    queue = deque([root])
    print("Level Order Traversal:", end=" ")
    while queue:
        current = queue.popleft()
        print(current.data, end=" ")
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
            
    print()

# time complexity: 
# - Inorder, Preorder, Postorder: o(n) - we visit each node one time
# - Level Order: O(n) - we visit each node one time
# Space Complexity: O(h) for recursive traversals, O(n) for level order traversal in worst case (when tree is completely unbalanced)

# -------- FIND MIN --------
def find_min(root):
    if root is None:
        print("Tree is empty")
        return None
    while root.left:
        root = root.left
    return root.data


# -------- FIND MAX --------
def find_max(root):
    if root is None:
        print("Tree is empty")
        return None
    while root.right:
        root = root.right
    return root.data


# -------- FIND HEIGHT --------
def height(root):
    if root is None:
        return -1   # height in edges # why -1? empty tree has height -1, single node tree has height 0
    return 1 + max(height(root.left), height(root.right))

# -------- FIND HEIGHT IN NODES --------
def height_in_nodes(root):
    if root is None:
        return 0   # height in nodes
    return 1 + max(height_in_nodes(root.left), height_in_nodes(root.right))

# -------- DRIVER --------
# root = None
# values = [20, 15, 30, 40, 12, 18, 25, 50]

# for v in values:
#     root = insert(root, v)

root = insert(None, 20)
root = insert(root, 15)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 12)
root = insert(root, 18)
root = insert(root, 25)
root = insert(root, 50)


print("Inorder Traversal :", end=" ")
inorder(root)
print()


print("Preorder Traversal :", end=" ")
preorder(root)
print()

print("Postorder Traversal :", end=" ")
postorder(root)
print()

print("Level Order Traversal :", end=" ")
level_order(root)

print("\nMinimum Value :", find_min(root))
print("Maximum Value :", find_max(root))
print("Height (edges) :", height(root))
print("Height (nodes) :", height_in_nodes(root))

search(root, 18)
search(root, 100)

    # Test Deletion
print("\nDeleting 30...")
root = delete(root, 30)
print("Inorder after deletion:", end=" ")
inorder(root)
print()