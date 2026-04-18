class ArrayBinaryTree:
    def __init__(self, size):
        self.tree = [None] * size
        self.size = size

    # Insert root
    def insert_root(self, value): # 
        if self.tree[0] is None:
            self.tree[0] = value
        else:
            print("Root already exists")

    # Insert left child
    def insert_left(self, parent_index, value):
        left_index = 2 * parent_index + 1

        if left_index < self.size:
            self.tree[left_index] = value
        else:
            print("Index out of range")

    # Insert right child
    def insert_right(self, parent_index, value):
        right_index = 2 * parent_index + 2

        if right_index < self.size:
            self.tree[right_index] = value
        else:
            print("Index out of range")

    def display(self):
        print(self.tree)


# Example
bt = ArrayBinaryTree(10)
bt.insert_root(10)
bt.insert_left(0, 20)
bt.insert_right(0, 30)
bt.insert_left(1, 40)
bt.insert_right(1, 50)

bt.display()