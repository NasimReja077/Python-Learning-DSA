from collections import deque


# ================= NODE =================
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        self.height = 1 # New node has height 1
        
# ================= AVL TREE =================

class AVLTree:
     # Height of node
     def get_height(self, node):
          if node is None:
               return 0
          return node.height
     
     # Balance factor
     def get_balance(self, node):
          if node is None:
               return 0
          return self.get_height(node.left) - self.get_height(node.right)
     
     # ================= UPDATE HEIGHT =================
     def update_height(self, node):
          
          if node is None:
            return
       
          node.height = 1 + max(
               self.get_height(node.left),
               self.get_height(node.right)
          )

          
     
# ================= RIGHT ROTATION =================
# unbalanced_node = z
# new_root = y or left child of z
# t3 = right child of y or transferred subtree - right child of new root

     def right_rotate(self, z):
          # Left child will become new root
          y = z.left
          
          # Store right subtree of new root temporarily
          t3 = y.right
          
          # Rotation
          # Old root becomes right child of new root
          y.right = z
          # Temporary subtree attached back to old root
          z.left = t3
          
          # Update heights
          self.update_height(z)
          self.update_height(y)
          
          # Return new root after rotation
          return y
     
 # ================= LEFT ROTATION =================
 
 # unbalanced_node = z
 # new_root = y or left child of z
 # t2 = left child of y or transferred subtree - left child of new root
 # t3 = right child of y or transferred subtree - right child of new root
 
     def left_rotate(self, z):

        y = z.right
        t2 = y.left

        # Rotation
        y.left = z
        z.right = t2
        
        # Update heights
        self.update_height(y)
        self.update_height(z)

        return y
   
# ================= INSERT =================
     def insert(self, root, value):

        # Normal BST Insert
        if root is None:
            return Node(value)

        if value < root.data:
            root.left = self.insert(root.left, value)

        elif value > root.data:
            root.right = self.insert(root.right, value)

        else:
            return root

        # Update height
        self.update_height(root)

        # Get balance factor
        balance = self.get_balance(root)

        # -------- CASE 1: LL --------
        if balance > 1 and value < root.left.data:
            return self.right_rotate(root)

        # -------- CASE 2: RR --------
        if balance < -1 and value > root.right.data:
            return self.left_rotate(root)

        # -------- CASE 3: LR --------
        if balance > 1 and value > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # -------- CASE 4: RL --------
        if balance < -1 and value < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root


    # ================= DELETE =================
     def delete(self, root, value):

        if root is None:
            return root

        # Normal BST Delete
        # Serch node / Traverse 
        if value < root.data:
            root.left = self.delete(root.left, value)

        elif value > root.data:
            root.right = self.delete(root.right, value)

        else:

            # One child / No child
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            # Two children
            successor = self.get_min_node(root.right)

            root.data = successor.data

            root.right = self.delete(
                root.right,
                successor.data
            )

        # If Tree became empty
        if root is None:
            return root

        # Update height
        self.update_height(root)

        # Check balance
        balance = self.get_balance(root)

        # LL
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # LR
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RR
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # RL
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root
   
   
   # ================= FIND MIN =================
     def get_min_node(self, root):

        current = root

        while current.left:
            current = current.left

        return current
   
    # ================= SEARCH =================
     def search(self, root, value):

        if root is None:
            return False

        if root.data == value:
            return True

        if value < root.data:
            return self.search(root.left, value)

        return self.search(root.right, value)


    # ================= TRAVERSALS =================

     def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)


     def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)


     def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")


    # ================= LEVEL ORDER =================
     def level_order(self, root):

        if root is None:
            return

        queue = deque([root])

        while queue:

            current = queue.popleft()

            bf = self.get_balance(current)

            print(
                f"{current.data}(BF={bf})",
                end=" "
            )

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        print()
        
     # ================= MAX =================
     def find_max(self, root):

        while root.right:
            root = root.right

        return root.data


    # ================= MIN =================
     def find_min(self, root):

        while root.left:
            root = root.left

        return root.data
   
   # ================= DRIVER CODE =================

avl = AVLTree()

root = None

values = [10, 20, 30, 40, 50, 25]

for value in values:
    root = avl.insert(root, value)


print("Inorder:", end=" ")
avl.inorder(root)

print("\nPreorder:", end=" ")
avl.preorder(root)

print("\nPostorder:", end=" ")
avl.postorder(root)

print("\nLevel Order:", end=" ")
avl.level_order(root)


print("\nSearch 25:", avl.search(root, 25))
print("Search 100:", avl.search(root, 100))

print("\nMinimum:", avl.find_min(root))
print("Maximum:", avl.find_max(root))


print("\nDeleting 40...")
root = avl.delete(root, 40)

print("After deletion:")
avl.level_order(root)