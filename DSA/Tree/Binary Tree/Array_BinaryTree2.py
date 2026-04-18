class BinaryTreeArray:
    def __init__(self, capacity=100):
        self.tree = [None] * capacity   # Fixed size array
        self.size = 0                   # Number of nodes currently in tree

    # Insert node in level order (makes tree complete)
    def insert(self, data):
        if self.size >= len(self.tree) - 1:
            print("Tree is full!")
            return
        
        self.size += 1
        self.tree[self.size] = data
        print(data, "inserted at position", self.size)

    # Get Left Child
    def get_left_child(self, index):
        left = 2 * index
        if left <= self.size:
            return self.tree[left]
        return None

    # Get Right Child
    def get_right_child(self, index):
        right = 2 * index + 1
        if right <= self.size:
            return self.tree[right]
        return None

    # Get Parent
    def get_parent(self, index):
        if index > 1:
            return self.tree[index // 2]
        return None

    # Level Order Traversal (Easiest in Array)
    def level_order(self):
        if self.size == 0:
            print("Tree is empty")
            return
        print("Level Order Traversal:", end=" ")
        for i in range(1, self.size + 1):
            print(self.tree[i], end=" ")
        print()

    # Inorder Traversal (Recursive)
    def inorder(self, index=1):
        if index > self.size or self.tree[index] is None:
            return
        self.inorder(2 * index)          # Left
        print(self.tree[index], end=" ") # Root
        self.inorder(2 * index + 1)      # Right


# ---------------- Example Usage ----------------
bt_array = BinaryTreeArray(20)

bt_array.insert(10)
bt_array.insert(20)
bt_array.insert(30)
bt_array.insert(40)
bt_array.insert(50)
bt_array.insert(60)

print("\nLeft child of 10:", bt_array.get_left_child(1))
print("Right child of 10:", bt_array.get_right_child(1))
print("Parent of 50:", bt_array.get_parent(5))

bt_array.level_order()
print("Inorder Traversal:", end=" ")
bt_array.inorder()