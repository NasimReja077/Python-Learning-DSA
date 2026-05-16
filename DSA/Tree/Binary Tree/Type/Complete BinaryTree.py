class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


# Count nodes
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# insert using level order 

# Check complete binary tree
def is_complete(root, index, total_nodes):
    if root is None:
        return True

    if index >= total_nodes:
        return False

    return (is_complete(root.left, 2 * index + 1, total_nodes) and
            is_complete(root.right, 2 * index + 2, total_nodes))

# Traversal (Inorder)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
        
        
# Driver
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

total = count_nodes(root)

if is_complete(root, 0, total):
    print("Complete Binary Tree")
else:
    print("Not Complete Binary Tree")
    
inorder(root) # Output: 4 2 5 1 6 3