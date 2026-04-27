from collections import deque


# ─────────────────────────────────────────
#  NODE CLASS
# ─────────────────────────────────────────
class Node:
    def __init__(self, data):
        self.data  = data
        self.left  = None
        self.right = None


# ─────────────────────────────────────────
#  BINARY TREE CLASS (LINKED REPRESENTATION)
# ─────────────────────────────────────────
class BinaryTree:
    def __init__(self):
        self.root = None

    # ── Insert node (level order / complete binary tree style) ──
    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            print(data, "inserted as root")
            return

        queue = deque([self.root])

        while queue:
            temp = queue.popleft()

            if temp.left is None:
                temp.left = new_node
                print(data, "inserted as left child of", temp.data)
                return
            else:
                queue.append(temp.left)

            if temp.right is None:
                temp.right = new_node
                print(data, "inserted as right child of", temp.data)
                return
            else:
                queue.append(temp.right)

    # ── Display structure (simple level order print) ──
    def display(self):
        if self.root is None:
            print("Tree is empty")
            return

        queue = deque([self.root])
        print("Binary Tree (level order):")

        while queue:
            temp = queue.popleft()
            left  = temp.left.data  if temp.left  else "NULL"
            right = temp.right.data if temp.right else "NULL"
            print(f"  Node {temp.data} → left: {left}, right: {right}")

            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)


# ─────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────
bt = BinaryTree()
bt.insert(1)
bt.insert(2)
bt.insert(3)
bt.insert(4)
bt.insert(5)
bt.display()

# Output tree:
#         1
#        / \
#       2   3
#      / \
#     4   5