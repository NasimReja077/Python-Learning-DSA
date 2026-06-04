**✅ Best Exam Answer for Question 8(a)**

**Q. Define Binary Search Tree. Write algorithm to implement insertion and deletion operation in BST.**  
**(8 Marks)**

---

### **Definition of Binary Search Tree (BST)**

A **Binary Search Tree (BST)** is a special type of binary tree in which for every node:

- All nodes in the **left subtree** have values **less than** the node’s value.
- All nodes in the **right subtree** have values **greater than** the node’s value.
- Both left and right subtrees are also Binary Search Trees.
- Usually, duplicate values are not allowed.

**Example:**

```
          50
        /    \
      30      70
     /  \    /  \
   20   40  60   80
```

**Inorder Traversal** of BST always gives nodes in **sorted ascending order**.

---

### **1. Insertion Algorithm in BST**

```pseudocode
Algorithm: BST_Insert(root, value)
Step 1: Start
Step 2: If root == NULL
         Create a new node with value
         Return new node

Step 3: If value < root.data
         root.left = BST_Insert(root.left, value)
         
Step 4: Else If value > root.data
         root.right = BST_Insert(root.right, value)
         
Step 5: Else
         // Duplicate value, ignore or handle as required
         
Step 6: Return root
Step 7: Stop
```

**Time Complexity**:  
- Average Case: **O(log n)**  
- Worst Case: **O(n)** (Skewed Tree)

---

### **2. Deletion Algorithm in BST** (Most Important)

```pseudocode
Algorithm: BST_Delete(root, value)
Step 1: Start
Step 2: If root == NULL
         Return NULL

Step 3: If value < root.data
         root.left = BST_Delete(root.left, value)
         
Else If value > root.data
         root.right = BST_Delete(root.right, value)

Else (Node to be deleted is found)

    // Case 1: Node has No Child (Leaf Node)
    If root.left == NULL and root.right == NULL
        Return NULL

    // Case 2: Node has One Child
    If root.left == NULL
        Return root.right
    If root.right == NULL
        Return root.left

    // Case 3: Node has Two Children
    successor = Find_Minimum(root.right)     // Inorder Successor
    root.data = successor.data
    root.right = BST_Delete(root.right, successor.data)

Step 4: Return root
Step 5: Stop
```

**Helper Function:**

```pseudocode
Algorithm: Find_Minimum(node)
Step 1: Start
Step 2: While node.left != NULL
         node = node.left
Step 3: Return node
Step 4: Stop
```

---

### **Time & Space Complexity**

| Operation     | Average Case     | Worst Case     | Space Complexity     |
|---------------|------------------|----------------|----------------------|
| Insertion     | O(log n)         | O(n)           | O(h)                 |
| Deletion      | O(log n)         | O(n)           | O(h)                 |

---

**Diagram (You must draw in exam):**

**Before Deleting 30 (Node with 2 children):**

```
      50
     /  \
   30    70
  /  \   /
20   40 60
```

**After Deleting 30** (Replaced by inorder successor 40):

```
      50
     /  \
   40    70
  /      /
20      60
```

---

**Key Points to Write in Exam (for full marks):**
- Definition with BST property
- Recursive Insertion Algorithm
- Deletion with all **3 cases** clearly mentioned
- Inorder Successor concept
- Time complexity (Average & Worst)
- One diagram before & after deletion

---