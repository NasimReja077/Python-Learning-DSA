class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def is_perfect_binary_tree(root):
    # Helper function to calculate height
    def height(node):
        if node is None:
            return 0
        return 1 + max(height(node.left), height(node.right))
    
    # Main function
    def is_perfect(root, h):
        if root is None:
            return True
        
        # If leaf node
        if root.left is None and root.right is None:
            return True
        
        # If node has only one child
        if root.left is None or root.right is None:
            return False
        
        # Check both subtrees are perfect and have same height
        return (is_perfect(root.left, h-1) and 
                is_perfect(root.right, h-1))
    
    if root is None:
        return True
    
    tree_height = height(root)
    return is_perfect(root, tree_height)

# ================== Test Cases ==================

# Example 1: Perfect Binary Tree (Height 2)
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.right.left = Node(6)
root1.right.right = Node(7)

print("Is Tree 1 Perfect?", is_perfect_binary_tree(root1))   # True

# Example 2: Not Perfect (Complete but not Perfect)
root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)
root2.right.left = Node(6)

print("Is Tree 2 Perfect?", is_perfect_binary_tree(root2))   # False