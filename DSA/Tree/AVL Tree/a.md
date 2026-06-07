**✅ AVL Tree - All 4 Rotations Algorithms**  
**(Complete & Exam-Ready)**

---

### **1. Right Rotation (LL Rotation)**

```pseudocode
Algorithm: RightRotate(y)
Step 1: Start
Step 2: x ← y.left                  // x is left child of y
Step 3: T2 ← x.right                // T2 is right subtree of x

Step 4: // Perform Rotation
       x.right ← y
       y.left ← T2

Step 5: // Update Heights
       UpdateHeight(y)
       UpdateHeight(x)

Step 6: Return x                    // New root after rotation
Step 7: Stop
```

**Used When:** Left-Left (LL) Imbalance  
**Balance Factor:** `> 1` and left child is left heavy.

---

### **2. Left Rotation (RR Rotation)**

```pseudocode
Algorithm: LeftRotate(x)
Step 1: Start
Step 2: y ← x.right                 // y is right child of x
Step 3: T2 ← y.left                 // T2 is left subtree of y

Step 4: // Perform Rotation
       y.left ← x
       x.right ← T2

Step 5: // Update Heights
       UpdateHeight(x)
       UpdateHeight(y)

Step 6: Return y                    // New root after rotation
Step 7: Stop
```

**Used When:** Right-Right (RR) Imbalance  
**Balance Factor:** `< -1` and right child is right heavy.

---

### **3. Left-Right Rotation (LR Rotation)**

```pseudocode
Algorithm: LeftRightRotate(root)
Step 1: Start
Step 2: // First perform Left Rotation on left child
       root.left ← LeftRotate(root.left)

Step 3: // Then perform Right Rotation on root
       Return RightRotate(root)
Step 4: Stop
```

**Used When:** Left-Right (LR) Imbalance  
**Balance Factor:** `> 1` and left child is right heavy.

---

### **4. Right-Left Rotation (RL Rotation)**

```pseudocode
Algorithm: RightLeftRotate(root)
Step 1: Start
Step 2: // First perform Right Rotation on right child
       root.right ← RightRotate(root.right)

Step 3: // Then perform Left Rotation on root
       Return LeftRotate(root)
Step 4: Stop
```

**Used When:** Right-Left (RL) Imbalance  
**Balance Factor:** `< -1` and right child is left heavy.

---

### **Summary Table (Very Important for Exam)**

| Imbalance Type | Balance Factor Condition                  | Rotation to Perform          | Single/Double |
|----------------|-------------------------------------------|------------------------------|---------------|
| **LL**         | `balance > 1` and `left.balance >= 0`    | Right Rotation               | Single        |
| **RR**         | `balance < -1` and `right.balance <= 0`  | Left Rotation                | Single        |
| **LR**         | `balance > 1` and `left.balance < 0`     | Left-Right Rotation          | Double        |
| **RL**         | `balance < -1` and `right.balance > 0`   | Right-Left Rotation          | Double        |

---

### **Helper Function (Must Write)**

```pseudocode
Algorithm: GetBalance(node)
    Return Height(node.left) - Height(node.right)
```

---

**Exam Tip:**  
Always draw **before and after diagrams** for each rotation. Clearly mention the **imbalance type** (LL, RR, LR, RL) and **balance factor**.

Would you like me to give:
- **Full AVL Tree Python Code** with all rotations?
- **Diagrams** (text-based) for all 4 rotations?
- **Insertion Algorithm** using these rotations?

Just tell me!