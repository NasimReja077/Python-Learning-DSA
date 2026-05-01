class ArrayBinaryTree:
    def __init__(self, size):
        self.tree = [None] * size # All values initially None ,Example:size = 3 -> [None, None, None]
        # explanation- tree is represented as an array of fixed size , [None] * size creates an array of the specified size filled with None values. This array will be used to store the elements of the binary tree.
        self.size = size # is used to store the maximum number of elements that the binary tree can hold.

    # Insert root
    def insert_root(self, value):
        if self.tree[0] is None: # Root always index 0
            self.tree[0] = value
        else:
            print("Root already exists")
            

    # Insert left child
    def insert_left(self, parent_index, value):
        if parent_index >= self.size or self.tree[parent_index] is None:
            print("Parent does not exist")
            return
        
        left_index = 2 * parent_index + 1
        
        if left_index < self.size: # Check: array ke andar hi insert ho raha hai ya nahi 
            if self.tree[left_index] is None:
                self.tree[left_index] = value # Insert value at the calculated left child index
            else:
                print("Left child already exists")
        else:
            print("Index out of range")

    # Insert right child
    def insert_right(self, parent_index, value):
        if parent_index >= self.size or self.tree[parent_index] is None:
            print("Parent does not exist")
            return
        
        right_index = 2 * parent_index + 2
        
        if right_index < self.size:
            if self.tree[right_index] is None:
                self.tree[right_index] = value
            else:
                print("Right child already exists")
        else:
            print("Index out of range")
            
     # ==================== NEW OPERATIONS ====================

    # Get Parent of a node
    def get_parent(self, index):
        if index <= 0 or index >= self.size:
            print("Invalid index")
            return None
        
        parent_index = (index - 1) // 2
        if self.tree[parent_index] is not None:
            return self.tree[parent_index]
        else:
            return None

    # Get Left Child
    def get_left_child(self, index):
        left_index = 2 * index + 1
        if left_index < self.size and self.tree[left_index] is not None:
            return self.tree[left_index]
        return None

    # Get Right Child
    def get_right_child(self, index):
        right_index = 2 * index + 2
        if right_index < self.size and self.tree[right_index] is not None:
            return self.tree[right_index]
        return None

    # Check if node is Leaf
    def is_leaf(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        return (left >= self.size or self.tree[left] is None) and \
               (right >= self.size or self.tree[right] is None)
               
     # Display Tree
    def display(self):
        print("Array Representation:", self.tree) # / print(self.tree)
        
    # Pretty Display (Better Visualization)
    def display_tree(self):
        print("\nBinary Tree (Level Order):")
        for i in range(self.size):
            if self.tree[i] is not None:
                print(f"Index {i}: {self.tree[i]}", end="   ")
        print()

    # def display(self):
    #     print(self.tree)
    
    
    def preorder(self, index=0):
        if index >= self.size or self.tree[index] is None:
            return
        
        print(self.tree[index], end=" ")
        self.preorder(2 * index + 1)
        self.preorder(2 * index + 2)

    def inorder(self, index=0):
        if index >= self.size or self.tree[index] is None:
            return
        
        self.inorder(2 * index + 1)
        print(self.tree[index], end=" ")
        self.inorder(2 * index + 2)

    def postorder(self, index=0):
        if index >= self.size or self.tree[index] is None:
            return
        
        self.postorder(2 * index + 1)
        self.postorder(2 * index + 2)
        print(self.tree[index], end=" ")

# Example
bt = ArrayBinaryTree(10) # Create object of Tree

bt.insert_root(10) # root 
bt.insert_left(0, 20)
bt.insert_right(0, 30)
bt.insert_left(1, 40)
bt.insert_right(1, 50)
bt.insert_left(2, 60)
bt.insert_right(2, 70)

print("Parent of node at index 3:", bt.get_parent(3))        # Output: 20
print("Left child of node at index 1:", bt.get_left_child(1))    # Output: 40
print("Right child of node at index 1:", bt.get_right_child(1))   # Output: 50
print("Is node at index 3 a leaf?", bt.is_leaf(3))           # Output: True

bt.display()

print("Preorder Traversal:")
bt.preorder()

print("\nInorder Traversal:")
bt.inorder()

print("\nPostorder Traversal:")
bt.postorder()



'''
(0-based Indexing)

Your Python code uses 0-based indexing (starts from index 0):

Root → index 0
Left child → 2*i + 1
Right child → 2*i + 2
Parent → (i - 1) // 2

✔ Example from your code:

Index:   0   1   2   3   4   5
Value:  10  20  30  40  50  60

Tree structure:

        10
       /  \
     20    30
    /  \   /
  40   50 60
  
ALGORITHM: ArrayRepresentation (0-based)

Step 1: Create array A of size n

Step 2: Place root at A[0]

Step 3: FOR each node at index i:
            Left child  = A[2*i + 1]
            Right child = A[2*i + 2]

Step 4: To find parent of node at index i:
            Parent = A[(i - 1) // 2]

Step 5: For level-order traversal:
            Traverse A[0] to A[n-1]
  
'''
