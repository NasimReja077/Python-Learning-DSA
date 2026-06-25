class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_skewed(root):
    if root is None:
        return True
    
    # If node has both children → Not skewed
    if root.left and root.right:
        return False
    
    # Recur on the only child
    if root.left:
        return is_skewed(root.left)
    if root.right:
        return is_skewed(root.right)
    
    return True   # Leaf node


# Example Usage
root = Node(10)
root.right = Node(20)
root.right.right = Node(30)
root.right.right.right = Node(40)

print("Is Skewed Binary Tree?", is_skewed(root))   # Output: True