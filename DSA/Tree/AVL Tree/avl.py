# ════════════════════════════════════════════════════════════
#                   AVL TREE IMPLEMENTATION
# ════════════════════════════════════════════════════════════
# AVL Tree = Self-balancing BST
# Balance Factor (BF) = height(left) - height(right)
# BF must be -1, 0, or +1 at every node
# If |BF| > 1 → perform rotation to rebalance
# ════════════════════════════════════════════════════════════


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

   # ──────────────────────────────────────
    #  RIGHT ROTATION (LL Case)
    #
    #      z                y
    #     / \              / \
    #    y   T4    →     x    z
    #   / \             / \  / \
    #  x  T3           T1 T2 T3 T4
    # / \
    # T1 T2
    # ──────────────────────────────────────
    
     def right_rotate(self, z):
          # Left child will become new root
          y = z.left # y is the new root
          t3 = y.right # T3 is the right subtree of y  # Store right subtree of new root temporarily
          
          # Rotation
          # Old root becomes right child of new root
          y.right = z  # z becomes right child of y
          # Temporary subtree attached back to old root
          z.left = t3  # T3 becomes left child of z
          
          # Update heights (z first because it's now lower)
          self.update_height(z)
          self.update_height(y)
          
          # Step 3: Update heights
          # IMPORTANT: update z FIRST (it is now lower in the tree)
          # z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
          # y.height = 1 + max(self.get_height(y.left),self.get_height(y.right))
          
          print(f"Right Rotation on node {z.data} → new subtree root: {y.data}")
          # Return new root after rotation
          return y
     
 # ================= LEFT ROTATION =================
 
 # unbalanced_node = z
 # new_root = y or left child of z
 # t2 = left child of y or transferred subtree - left child of new root
 # t3 = right child of y or transferred subtree - right child of new root
 
 # ──────────────────────────────────────
    #  LEFT ROTATION (RR Case)
    #
    #   z                  y
    #  / \                / \
    # T1   y      →      z   x
    #     / \           / \ / \
    #    T2   x        T1 T2 T3 T4
    #        / \
    #       T3  T4
    # ──────────────────────────────────────
 
     def left_rotate(self, z):

        y = z.right # y is the new root
        t2 = y.left # T2 is the left subtree of y

        # Rotation
        y.left = z # z becomes left child of y
        z.right = t2 # # T2 becomes right child of z
        
        # Update heights
        self.update_height(y)
        self.update_height(z)
        
        # Step 3: Update heights
        # IMPORTANT: update z FIRST (it is now lower in the tree)
        # z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        # y.height = 1 + max(self.get_height(y.left),self.get_height(y.right))

        print(f"Left Rotation on node {z.data} → new subtree root: {y.data}")
        return y # y is the new root of this subtree
   
# ─── Complexity ─────────────────────────────
# Time  → O(1)
# Space → O(1)
# ────────────────────────────────────────────
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

        # Update height of current node
        self.update_height(root)

        # Get balance factor
        balance = self.get_balance(root)

        # ── CASE 1: LL (Left-Left) ──
        # BF = +2 and new node inserted in LEFT subtree of LEFT child
        
        # optin1 - check value against left child data
        
        if balance > 1 and value < root.left.data:
            # print(f"  LL Case at node {root.data} (BF={balance})")
            return self.right_rotate(root)
        
        
        # option2- more robust and handles duplicates better - check balance of left child
        # if balance > 1 and self.get_balance(root.left) >= 0:
        #     return self.right_rotate(root)
        # We will use option 2 for better handling of duplicates and edge cases
        

         # ── CASE 2: RR (Right-Right) ──
        # BF = -2 and new node inserted in RIGHT subtree of RIGHT child
        
        if balance < -1 and value > root.right.data:
            return self.left_rotate(root)
        

        # # ── CASE 3: LR (Left-Right) ──
        # BF = +2 and new node inserted in RIGHT subtree of LEFT child
        
        if balance > 1 and value > root.left.data:
            root.left = self.left_rotate(root.left) # Step 1: Left rotate left child
            return self.right_rotate(root) # Step 2: Right rotate current node
        

        # ── CASE 4: RL (Right-Left) ──
        # BF = -2 and new node inserted in LEFT subtree of RIGHT child
        
        if balance < -1 and value < root.right.data:
            root.right = self.right_rotate(root.right) # Step 1: Right rotate right child
            return self.left_rotate(root) # Step 2: Left rotate current node

        return root # No imbalance found, return unchanged

# time complexity: O(log n) always (tree stays balanced)
# space complexity: O(log n) recursive call stack

    # ================= DELETE =================
     def delete(self, root, value):

        # Step 1: Normal BST delete
        if root is None:
            # print(f"{value} not found in tree")
            return root

        # Normal BST Delete
        # Serch node / Traverse 
        if value < root.data:
            root.left = self.delete(root.left, value)

        elif value > root.data:
            root.right = self.delete(root.right, value)

        else:
            # Node found — handle 3 cases
            # Case 1 & 2: No child or one child
            
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            # Two children
            # Case 3: Two children
            # Find inorder successor (min of right subtree)
            
            successor = self.get_min_node_succ(root.right)
            root.data = successor.data # Copy successor value # Replace value with successor's value
            root.right = self.delete( root.right, successor.data ) # Delete successor node from right subtree 

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
   
    # time complexity: O(log n) always
    # space complexity: O(log n) recursive call stack
   
   # ================= FIND MIN SUCCESSOR =================
     def get_min_node_succ(self, root): # Used in delete to find successor (smallest node in right subtree)

        # current = root

        # while current.left:
        #     current = current.left

        # return current
    
        current = root
        while current.left is not None:
            current = current.left
        return current
   
    # ================= SEARCH =================
     def search(self, root, value):

        if root is None:
            print("NOT FOUND")
            return False

        if root.data == value:
            print(f" {value} → FOUND")
            return True

        if value < root.data:
            return self.search(root.left, value)

        return self.search(root.right, value)

# time complexity: O(log n) always (guaranteed balanced)
    # space complexity: O(log n) 
    
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
        if root is None:
            return None

        while root.right:
            root = root.right

        return root.data


    # ================= MIN =================
     def find_min(self, root):
        if root is None:
            return None
        
        while root.left:
            root = root.left

        return root.data
    
    # ================
   
     def get_balance_factor(self, root):
        return self.get_balance(root)
     def get_height_of_tree(self, root):
        return self.get_height(root)
    
   # ================= DRIVER CODE =================

avl = AVLTree()

root = None

values = [10, 20, 30, 40, 50, 25, 5, 15, 35]

print("Inserting:", values)

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

print("Tree height :", avl.get_height_of_tree(root))
print("Root BF :", avl.get_balance_factor(root))

print("\nSearch 25:", avl.search(root, 25))
print("Search 100:", avl.search(root, 100))


print("\nMinimum:", avl.find_min(root))
print("Maximum:", avl.find_max(root))


print("\nDeleting 40...")
root = avl.delete(root, 40)

print("After deletion:")
avl.level_order(root)