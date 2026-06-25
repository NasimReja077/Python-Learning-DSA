from collections import deque

# -------- NODE CLASS --------
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


# -------- BINARY TREE CLASS --------
class BinaryTree:
    def __init__(self):
        self.root = None

    # -------- INSERT (Level Order) --------
    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        queue = deque([self.root])

        while queue:
            temp = queue.popleft()

            if temp.left is None:
                temp.left = new_node
                return
            else:
                queue.append(temp.left)

            if temp.right is None:
                temp.right = new_node
                return
            else:
                queue.append(temp.right)

    # -------- SEARCH --------
    def search(self, key):
        if self.root is None:
            return False

        queue = deque([self.root])

        while queue:
            temp = queue.popleft()

            if temp.data == key:
                return True

            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)

        return False

    # -------- DELETE --------
    def delete(self, key):
        if self.root is None:
            return

        if self.root.left is None and self.root.right is None:
            if self.root.data == key:
                self.root = None
            return

        queue = deque([self.root])
        key_node = None

        while queue:
            temp = queue.popleft()

            if temp.data == key:
                key_node = temp

            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)

        if key_node:
            x = temp.data  # deepest node value
            self._delete_deepest(temp) 
            key_node.data = x

    def _delete_deepest(self, d_node):
        queue = deque([self.root])

        while queue:
            temp = queue.popleft()

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

    # -------- TRAVERSALS --------

    # Preorder (Root → Left → Right)
    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Inorder (Left → Root → Right)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Postorder (Left → Right → Root)
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    # Level Order (BFS)
    def level_order(self):
        if self.root is None:
            return

        queue = deque([self.root])

        while queue:
            temp = queue.popleft()
            print(temp.data, end=" ")

            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)


# -------- MAIN PROGRAM --------
bt = BinaryTree()

# Insert nodes
bt.insert(10)
bt.insert(20)
bt.insert(30)
bt.insert(40)
bt.insert(50)
bt.insert(60)

# Traversals
print("Preorder:", end=" ")
bt.preorder(bt.root)

print("\nInorder:", end=" ")
bt.inorder(bt.root)

print("\nPostorder:", end=" ")
bt.postorder(bt.root)

print("\nLevel Order:", end=" ")
bt.level_order()

# Search
print("\nSearch 30:", bt.search(30))

# Delete
bt.delete(20)

print("After deletion (Level Order):", end=" ")
bt.level_order()
