# 🌳 Types of Trees (Data Structure – Exam Friendly)

Tree ek **non-linear data structure** hai jisme nodes parent-child relation me connected hote hain.

---

## 1️⃣ General Tree

✔ Har node ke **any number of children** ho sakte hain
✔ Koi restriction nahi hota

Example:

```
        A
      / | \
     B  C  D
        |
        E
```

---

## 2️⃣ Binary Tree

✔ Har node ke **maximum 2 children** hote hain
✔ Left child aur Right child

Example:

```
      1
     / \
    2   3
```

---

## 3️⃣ Full Binary Tree

✔ Har node ke **0 ya 2 children** hote hain
✔ Koi node 1 child wala nahi hota

Example:

```
        1
       / \
      2   3
     / \
    4   5
```

---

## 4️⃣ Complete Binary Tree

✔ Sab levels completely filled hote hain
✔ Last level left se fill hota hai

Example:

```
        1
       / \
      2   3
     / \  /
    4  5 6
```

---

## 5️⃣ Perfect Binary Tree

✔ Har internal node ke 2 children
✔ Sab leaf nodes same level par hote hain

Formula:

```
Total Nodes = 2^h - 1
```

Example:

```
        1
       / \
      2   3
     / \ / \
    4  5 6  7
```

---

## 6️⃣ Binary Search Tree (BST)

✔ Left subtree < Root
✔ Right subtree > Root
✔ Searching fast hota hai

Example:

```
        50
       /  \
      30   70
```

---

## 7️⃣ AVL Tree

✔ Self-balancing BST
✔ Height difference ≤ 1
✔ Rotations use karta hai

---

## 8️⃣ Red-Black Tree

✔ Self-balancing BST
✔ Nodes red ya black hote hain
✔ Height balanced rehta hai

---

## 9️⃣ Heap

✔ Complete Binary Tree
✔ Do types:

* Max Heap (Parent > Children)
* Min Heap (Parent < Children)

Used in **Priority Queue**

---

## 🔟 B-Tree

✔ Multi-way tree
✔ Database aur file systems me use hota hai

---

# 🎯 Short Exam Summary Table

| Tree Type            | Key Property           |
| -------------------- | ---------------------- |
| General Tree         | Any number of children |
| Binary Tree          | Max 2 children         |
| Full Binary Tree     | 0 or 2 children        |
| Complete Binary Tree | Filled left to right   |
| Perfect Binary Tree  | All leaves same level  |
| BST                  | Left < Root < Right    |
| AVL                  | Balanced BST           |
| Heap                 | Parent priority rule   |
| B-Tree               | Multi-level indexing   |
# =============================================


# 🌳 Types of Trees – Diagram ke Saath Difference (Exam Ready)



# 1️⃣ Full vs Complete vs Perfect Binary Tree

---

## 🌲 1. Full Binary Tree

✔ Har node ke **0 ya 2 children**
✔ 1 child wala node allowed nahi

### Diagram:

```
        1
       / \
      2   3
     / \
    4   5
```

👉 Node 2 ke 2 children hain
👉 Node 3 ke 0 children
✔ Valid Full Binary Tree

---

## 🌲 2. Complete Binary Tree

✔ Sab levels filled
✔ Last level left se fill hota hai

### Diagram:

```
        1
       / \
      2   3
     / \  /
    4  5 6
```

👉 Last level left se filled
✔ Complete Binary Tree

---

## 🌲 3. Perfect Binary Tree

✔ Har internal node ke 2 children
✔ Sab leaf nodes same level par

### Diagram:

```
        1
       / \
      2   3
     / \ / \
    4  5 6  7
```

✔ All leaves same level
✔ Total Nodes = 2^h - 1

---

## 🔥 Difference Table (Very Important for Exam)

| Feature                | Full          | Complete     | Perfect         |
| ---------------------- | ------------- | ------------ | --------------- |
| 1 child allowed?       | ❌ No          | ✔ Yes        | ❌ No            |
| Last level full?       | Not necessary | Left filled  | Completely full |
| All leaves same level? | Not required  | Not required | ✔ Yes           |
| Strict structure?      | Medium        | High         | Very High       |

---

# 2️⃣ Binary Tree vs Binary Search Tree (BST)

---

## 🌲 Binary Tree

✔ Max 2 children
✔ Koi ordering rule nahi

```
      10
     /  \
    50   20
```

❌ Left > Root allowed
❌ Right < Root allowed

---

## 🌲 Binary Search Tree (BST)

✔ Left < Root
✔ Right > Root

```
        50
       /  \
      30   70
```

✔ Searching fast hota hai

---

## 🔥 Difference Table

| Feature         | Binary Tree | BST      |
| --------------- | ----------- | -------- |
| Ordering Rule   | ❌ No        | ✔ Yes    |
| Searching Speed | O(n)        | O(log n) |
| Structure       | Flexible    | Ordered  |

---

# 3️⃣ AVL Tree vs BST

---

## 🌲 Normal BST (Unbalanced)

```
    10
      \
       20
         \
          30
```

❌ Skewed tree
❌ Search slow (O(n))

---

## 🌲 AVL Tree (Balanced)

```
      20
     /  \
    10   30
```

✔ Height difference ≤ 1
✔ Fast search O(log n)

---

## 🔥 Difference

| Feature      | BST          | AVL             |
| ------------ | ------------ | --------------- |
| Balanced?    | ❌ Not always | ✔ Always        |
| Rotations?   | ❌ No         | ✔ Yes           |
| Search Speed | Can be O(n)  | Always O(log n) |

---

# Quick Revision Trick

Remember:

* Full → 0 or 2 children
* Complete → Left fill
* Perfect → Fully filled
* BST → Ordered
* AVL → Balanced BST

