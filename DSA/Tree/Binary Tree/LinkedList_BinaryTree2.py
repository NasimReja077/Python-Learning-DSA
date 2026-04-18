class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTreeLinked:
    def __init__(self):
        self.root = None

    # Insert using Level Order (same as array logic)
    def insert(self, data):
        new_node = Node(data)
        
        if self.root is None:
            self.root = new_node
            print(data, "inserted as root")
            return

        # Level order insertion using Queue
        from collections import deque
        queue = deque([self.root])
        
        while queue:
            current = queue.popleft()

            if current.left is None:
                current.left = new_node
                print(data, "inserted as left child of", current.data)
                return
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = new_node
                print(data, "inserted as right child of", current.data)
                return
            else:
                queue.append(current.right)

    # Inorder Traversal
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    # Preorder Traversal
    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # Postorder Traversal
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

    # Level Order Traversal
    def level_order(self):
        if not self.root:
            print("Tree is empty")
            return
        
        from collections import deque
        queue = deque([self.root])
        print("Level Order Traversal:", end=" ")
        
        while queue:
            current = queue.popleft()
            print(current.data, end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print()


# ---------------- Example Usage ----------------
bt_linked = BinaryTreeLinked()

bt_linked.insert(10)
bt_linked.insert(20)
bt_linked.insert(30)
bt_linked.insert(40)
bt_linked.insert(50)
bt_linked.insert(60)

print("\nInorder:", end=" ")
bt_linked.inorder(bt_linked.root)

print("\nPreorder:", end=" ")
bt_linked.preorder(bt_linked.root)

print("\nPostorder:", end=" ")
bt_linked.postorder(bt_linked.root)

print("\nLevel Order:", end=" ")
bt_linked.level_order()