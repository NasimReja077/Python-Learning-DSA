Here’s the **better, cleaner, and more exam-friendly** version of your BST algorithm.

This format matches the style of your Kruskal’s, Selection Sort, and Bubble Sort algorithms — clear, structured, numbered steps, with proper indentation, and important points highlighted for viva/exam.

---

# ✅ Algorithm: Binary Search Tree (BST) Operations

**Algorithm Name:** `BST_OPERATIONS(root, value)`

### **Node Structure**
```
Node:
    data
    left ← null
    right ← null
```

---

### **1. INSERT Algorithm**

**INSERT(root, value)**

**Step 1:** Start

**Step 2:** If `root == null`  
   Return new Node(value)

**Step 3:** If `root.data == value`  
   Return root      // Duplicate not inserted

**Step 4:** If `value < root.data`  
   root.left ← INSERT(root.left, value)  
**Else**  
   root.right ← INSERT(root.right, value)

**Step 5:** Return root

**Step 6:** Stop

---

### **2. SEARCH Algorithm**

**SEARCH(root, value)**

**Step 1:** Start

**Step 2:** If `root == null`  
   Print "Element not found"  
   Return

**Step 3:** If `root.data == value`  
   Print "Element Found"  
   Return

**Step 4:** If `value < root.data`  
   SEARCH(root.left, value)  
**Else**  
   SEARCH(root.right, value)

**Step 5:** Stop

---

### **3. DELETE Algorithm**

**DELETE(root, value)**

**Step 1:** Start

**Step 2:** If `root == null`  
   Return null

**Step 3:** If `value < root.data`  
   root.left ← DELETE(root.left, value)

**Step 4:** Else If `value > root.data`  
   root.right ← DELETE(root.right, value)

**Step 5:** Else (Node found)

  **Case 1:** No left child (0 or 1 child)  
    Return root.right

  **Case 2:** No right child  
    Return root.left

  **Case 3:** Two children  
    succ ← GET_SUCCESSOR(root)  
    root.data ← succ.data  
    root.right ← DELETE(root.right, succ.data)

**Step 6:** Return root

**Step 7:** Stop

---

### **4. GET_SUCCESSOR (Helper)**

**GET_SUCCESSOR(node)**

**Step 1:** node ← node.right

**Step 2:** While `node != null` and `node.left != null` do  
   node ← node.left

**Step 3:** Return node

---

### **5. INORDER Traversal**

**INORDER(root)**

**Step 1:** Start

**Step 2:** If `root != null`  
   INORDER(root.left)  
   Print(root.data)  
   INORDER(root.right)

**Step 3:** Stop

---

### **📌 Key Points for Viva / Exam**

- **BST Property**:  
  All nodes in left subtree < root < All nodes in right subtree

- Inorder traversal always gives **sorted order**

- This is a **recursive** implementation

- Duplicates are **not allowed** in this version

---

### **⏱ Time Complexity (Most Important for Exam)**

| Operation      | Average Case     | Worst Case     |
|----------------|------------------|----------------|
| Insert         | O(log n)         | O(n)           |
| Search         | O(log n)         | O(n)           |
| Delete         | O(log n)         | O(n)           |
| Inorder        | O(n)             | O(n)           |

**Space Complexity:** O(h)  (h = height of tree)  
→ Average: O(log n)  
→ Worst: O(n)  (skewed tree)

---

### **Driver Code Summary (What your code does)**

1. Create an empty BST
2. Insert nodes: 20, 15, 30, 40, 12, 18, 25, 50
3. Print Inorder traversal (sorted output)
4. Search for 18 and 100

---

This version is **concise, neat, and examiner-friendly**.  
You can directly write or explain this in exams.

Would you like me to add:
- A single combined "All BST Operations" algorithm in one place?
- Or a short **"How to Write in Exam Sheet"** version (more compact)?

Just tell me which one you prefer.
