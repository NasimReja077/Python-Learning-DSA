# 

from collections import deque
import queue

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
                
    def search(self, key):
        if self.root is None:
            print("Tree is empty")
            return False
        
        queue = deque([self.root])

        while queue:
            temp = queue.popleft()
            
            if temp.data == key:
                print(key, "found in the tree")
                return True

            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)
        print(key, "not found in the tree")
        return False
                
    def delete(self, data):
         if self.root is None:
             print("Tree is empty")
             return
         
         # Special case: only root node
         if self.root.left is None and self.root.right is None:
             if self.root.data == data:
                 self.root = None
                 print(data, "deleted from the tree")
             else:
                 print(data, "not found in the tree")
                 return
             
        # BFS - traverse full tree to find node_to_delete AND last_node
         queue = deque([self.root]) # Start BFS (level order traversal)
         node_to_delete = None # Will store the node we want to delete
         Last_node = None # Will store deepest (last visited) node
         
         while queue:                        # Complete BFS - don't break early
            current = queue.popleft() # Visit node
            if current.data == data:
                node_to_delete = current    # Mark node to delete
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
                
            last_node = current  # Track last visited node (deepest rightmost)
            
            # After full traversal
            if node_to_delete is None:
                print(data, "not found in the tree")
                return
            # Replace target node's data with deepest node's data
            node_to_delete.data = last_node.data # Copy deepest node value

            # Remove the deepest node
            self._delete_deepest(last_node)
            print(data, "deleted from the tree")
            
    def _delete_deepest(self, node):
        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            if current is node:
                current = None
                return
            if current.left:
                if current.left is node:
                    current.left = None
                    return
                else:
                    queue.append(current.left)
                    
                if current.right:
                    if current.right is node:
                        current.right = None
                        return
                    else:
                        queue.append(current.right)
                            
        
    # Maximum/Minimum
    
     # ====================== NEW: MAXIMUM & MINIMUM ======================
    
    def find_maximum(self):
        if self.root is None:
            print("Tree is empty")
            return None
        return self._find_max(self.root)    # Call private helper

    def _find_max(self, node):              # Private recursive helper
        if node is None:
            return float('-inf')            # Base case: return very small number
        left_max  = self._find_max(node.left)
        right_max = self._find_max(node.right)
        return max(node.data, left_max, right_max)

    def find_minimum(self):
        if self.root is None:
            print("Tree is empty")
            return None
        return self._find_min(self.root)

    def _find_min(self, node):
        if node is None:
            return float('inf')             # Base case: return very large number
        left_min  = self._find_min(node.left)
        right_min = self._find_min(node.right)
        return min(node.data, left_min, right_min)
    
    # ====================== HEIGHT & COUNT ======================
    def height_of_tree(self, node):
        if node is None:
            # print("Tree is empty")
            return -1 # base case: height of empty tree is -1, height of leaf node is 0
        else:
            Left_height = self.height_of_tree(node.left)
            Right_height = self.height_of_tree(node.right)
            return max(Left_height, Right_height) + 1
        '''
        Definition	                    Base Case
        Height = number of edges	    return -1
        Height = number of nodes	    return 0
        '''
        
    def count_nodes(self, node):
        if node is None:
            # print("Tree is empty")
            return 0
        else:
            Left_count = self.count_nodes(node.left)
            Right_count = self.count_nodes(node.right)
            return Left_count + Right_count + 1 # return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)
    
    def count_leaves(self, node):
        if node is None:
            print("Tree is empty")
            return 0
        if node.left is None and node.right is None:
            return 1
        else:
            Left_leaves = self.count_leaves(node.left)
            Right_leaves = self.count_leaves(node.right)
            return Left_leaves + Right_leaves # return self.count_leaves(node.left) + self.count_leaves(node.right)
        

        # Display (Tree Structure)
    # def display(self):
    #     if not self.root:
    #         print("Tree is empty")
    #         return
    #     queue = deque([self.root])
    #     print("\nTree Structure:")
        
    #     while queue:
    #         current = queue.popleft()
    #         left = current.left.data if current.left else "NULL"
    #         right = current.right.data if current.right else "NULL"
            
    #         print(f"{current.data} → L:{left} R:{right}")

    #         if current.left:
    #             queue.append(current.left)
    #         if current.right:
    #             queue.append(current.right)
                
    #         print()  # Newline after each level
    
    
    def display(self):
     queue = deque([self.root])
     while queue:
        node = queue.popleft()
        print(node.data, end=" → ")
        if node.left:
            print(node.left.data, end=" ")
            queue.append(node.left)
        if node.right:
            print(node.right.data, end=" ")
            queue.append(node.right)
        print()
    
    
    # def display(self):
    #     if not self.root:
    #         print("Tree is empty")
    #         return
    #     queue = deque([self.root])
        
    #     while queue:
    #         current = queue.popleft()
    #         print(current.data, end=" ")
            
    #         if current.left:
    #             queue.append(current.left)
    #         if current.right:
    #             queue.append(current.right)
    #         print()  # Newline after each level



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

print("\nTree Structure:")
bt_linked.display()

print("\nInorder:", end=" ")
bt_linked.inorder(bt_linked.root)

print("\nPreorder:", end=" ")
bt_linked.preorder(bt_linked.root)

print("\nPostorder:", end=" ")
bt_linked.postorder(bt_linked.root)

print("\nLevel Order:", end=" ")
bt_linked.level_order()

bt_linked.search(30) 
bt_linked.search(100)

bt_linked.delete(20)

bt_linked.display()

bt_linked.delete(100)

print("\nMaximum value:", bt_linked.find_maximum())
print("Minimum value:", bt_linked.find_minimum())
print("Height of tree:", bt_linked.height_of_tree(bt_linked.root))
print("Total nodes:", bt_linked.count_nodes(bt_linked.root))
print("Total leaves:", bt_linked.count_leaves(bt_linked.root))
