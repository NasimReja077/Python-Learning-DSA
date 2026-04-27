class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Moved the function outside the class scope
def is_full_binary_tree(root):
    # Base case: An empty tree is a full binary tree
    if root is None:
        return True
    
    # if leaf node
    if root.left is None and root.right is None:
        return True

    # if both left and right children exist, check both subtrees
    if root.left is not None and root.right is not None:
        return (is_full_binary_tree(root.left) and 
                is_full_binary_tree(root.right))

    # if only one child exists, it's not a full binary tree
    return False

# Traversal (Inorder)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# Example 1: Full Binary Tree
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.right.left = Node(6)
root1.right.right = Node(7)

print("Is Tree 1 Full Binary Tree?", is_full_binary_tree(root1))   # True

inorder(root1) # Output: 4 2 5 1 6 3 7

print("\n")

# Example 2: Not Full Binary Tree
root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)      # Node 2 has only left child

print("Is Tree 2 Full Binary Tree?", is_full_binary_tree(root2))   # False