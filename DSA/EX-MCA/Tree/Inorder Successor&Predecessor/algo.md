**✅ Inorder Successor and Predecessor in BST**  
**(Complete Algorithm + Code)**

---

### **1. Inorder Successor**

**Definition:**  
The **Inorder Successor** of a node is the **next node** that comes after it in **Inorder Traversal** (i.e., the smallest node greater than the given node).

#### **Algorithm: Inorder Successor**

```pseudocode
Algorithm: Inorder_Successor(root, node)
Step 1: Start

Step 2: If node.right != NULL
         Return minimum node in right subtree   // Case 1: Right subtree exists

Step 3: Else
         // Case 2: No right subtree
         successor = NULL
         current = root
         While current != NULL
             If node.data < current.data
                 successor = current
                 current = current.left
             Else If node.data > current.data
                 current = current.right
             Else
                 Break
         Return successor

Step 4: Stop
```

---

### **2. Inorder Predecessor**

**Definition:**  
The **Inorder Predecessor** is the **previous node** in Inorder Traversal (i.e., the largest node smaller than the given node).

#### **Algorithm: Inorder_Predecessor**

```pseudocode
Algorithm: Inorder_Predecessor(root, node)
Step 1: Start

Step 2: If node.left != NULL
         Return maximum node in left subtree     // Case 1: Left subtree exists

Step 3: Else
         // Case 2: No left subtree
         predecessor = NULL
         current = root
         While current != NULL
             If node.data > current.data
                 predecessor = current
                 current = current.right
             Else If node.data < current.data
                 current = current.left
             Else
                 Break
         Return predecessor

Step 4: Stop
```

---

### **3. Python Code Implementation**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Helper: Find Minimum in subtree
def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

# Helper: Find Maximum in subtree
def max_value_node(node):
    current = node
    while current.right:
        current = current.right
    return current

# ==================== INORDER SUCCESSOR ====================
def inorder_successor(root, node):
    if not node:
        return None
    
    # Case 1: Node has right subtree
    if node.right:
        return min_value_node(node.right)
    
    # Case 2: No right subtree - Traverse from root
    successor = None
    current = root
    while current:
        if node.data < current.data:
            successor = current
            current = current.left
        elif node.data > current.data:
            current = current.right
        else:
            break
    return successor

# ==================== INORDER PREDECESSOR ====================
def inorder_predecessor(root, node):
    if not node:
        return None
    
    # Case 1: Node has left subtree
    if node.left:
        return max_value_node(node.left)
    
    # Case 2: No left subtree - Traverse from root
    predecessor = None
    current = root
    while current:
        if node.data > current.data:
            predecessor = current
            current = current.right
        elif node.data < current.data:
            current = current.left
        else:
            break
    return predecessor
```

---

### **Time Complexity**

| Operation              | Time Complexity |
|------------------------|-----------------|
| Inorder Successor      | O(h)            |
| Inorder Predecessor    | O(h)            |

Where `h` = height of tree (O(log n) in balanced tree, O(n) in skewed)

---

**Would you like me to also give:**
- Code to find successor/predecessor using parent pointers?
- Full BST class with these functions?
- Example with a tree diagram?

Just tell me!