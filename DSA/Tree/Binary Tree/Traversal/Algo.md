470962
---

# 🌳 Binary Tree Traversal Algorithms

---

# ✅ 1. Preorder Traversal (NLR)

👉 **Order:** Root → Left → Right

## 📌 Algorithm

```text
PREORDER(root)
1. If root is NULL, return
2. Visit root node (print root.data)
3. Call PREORDER(root.left)
4. Call PREORDER(root.right)
```

---

# ✅ 2. Inorder Traversal (LNR)

👉 **Order:** Left → Root → Right

## 📌 Algorithm

```text
INORDER(root)
1. If root is NULL, return
2. Call INORDER(root.left)
3. Visit root node (print root.data)
4. Call INORDER(root.right)
```

---

# ✅ 3. Postorder Traversal (LRN)

👉 **Order:** Left → Right → Root

## 📌 Algorithm

```text
POSTORDER(root)
1. If root is NULL, return
2. Call POSTORDER(root.left)
3. Call POSTORDER(root.right)
4. Visit root node (print root.data)
```

---

# ✅ 4. Level Order Traversal (BFS) 🔥

👉 **Order:** Level by Level

## 📌 Algorithm

```text
LEVELORDER(root)
1. If root is NULL, return
2. Create an empty queue Q
3. Insert root into Q
4. While Q is not empty:
   a. Remove node from Q
   b. Visit node (print data)
   c. If left child exists, insert into Q
   d. If right child exists, insert into Q
```

---

# 🎯 Quick Revision Table (Exam Trick 🔥)

| Traversal | Order |
| --------- | ----- |
| Preorder  | NLR   |
| Inorder   | LNR   |
| Postorder | LRN   |
| Level     | BFS   |

---

# 🧠 Important Exam Notes

👉 Always write:

* Base condition (**if root == NULL**)
* Recursive calls clearly
* Order (LNR / NLR / LRN)

---

# 🚀 Bonus (Very Important Viva Question)

👉 Which traversal gives sorted output?
✔ **Inorder (only for BST)**

---