# 🌳 Tree Terminology – Proper Theory with Example Diagrams

---

## ✅ Example Tree (Reference Diagram)

Is diagram ko reference ke liye use karenge 👇

```
                A
              /   \
             B     C
            / \     \
           D   E     F
              /
             G
```

---

# 📚 Important Tree Terminologies

---

## 1️⃣ Node

Tree ka basic element **node** kehlata hai.

👉 Example: A, B, C, D, E, F, G sab nodes hain.

---

## 2️⃣ Root Node

Tree ka sabse top wala node **Root** hota hai.
Har tree ka sirf **ek root** hota hai.

👉 Is example me: **A** is the Root.

---

## 3️⃣ Parent Node

Jo node kisi dusre node ko connect karta hai (upar wala node).

👉 Example:

* A is parent of B and C
* B is parent of D and E
* E is parent of G

---

## 4️⃣ Child Node

Jo node kisi parent ke niche hota hai.

👉 Example:

* B and C are children of A
* D and E are children of B

---

## 5️⃣ Sibling

Jo nodes same parent share karte hain unhe siblings kehte hain.

👉 Example:

* B and C are siblings
* D and E are siblings

---

## 6️⃣ Leaf Node (External Node)

Jiske **koi children nahi hote**, use leaf node kehte hain.

👉 Example:

* D
* G
* F

✔ In sab ke niche koi node nahi hai.

---

## 7️⃣ Internal Node (Non-Leaf Node)

Jo node ke paas **at least 1 child** ho.

👉 Example:

* A
* B
* C
* E

---

## 8️⃣ Degree of a Node

Kisi node ke total children ki sankhya.

👉 Example:

* Degree(A) = 2
* Degree(B) = 2
* Degree(C) = 1
* Degree(G) = 0

---

## 9️⃣ Degree of Tree

Tree me kisi bhi node ka **maximum degree**.

👉 Is example me:

* Maximum children = 2
  ✔ So, Degree of Tree = 2

---

## 🔟 Level of Node

Root ka level usually **0 ya 1** maana jata hai (exam me clear karna).

Agar Root level = 0:

| Node    | Level |
| ------- | ----- |
| A       | 0     |
| B, C    | 1     |
| D, E, F | 2     |
| G       | 3     |

---

## 1️⃣1️⃣ Depth of Node

Root se kisi node tak ke edges ki sankhya.

👉 Example:

* Depth(A) = 0
* Depth(B) = 1
* Depth(G) = 3

---

## 1️⃣2️⃣ Height of Node

Node se leaf tak longest path ke edges ki sankhya.

👉 Example:

* Height(G) = 0
* Height(E) = 1
* Height(B) = 2
* Height(A) = 3

---

## 1️⃣3️⃣ Height of Tree

Root node ki height = Height of Tree

✔ Yahan Height of Tree = **3**

---

## 1️⃣4️⃣ Path

Nodes ka sequence jo edges se connected ho.

👉 Example:

* A → B → E → G
* A → C → F

---

## 1️⃣5️⃣ Subtree

Kisi node ke niche ka pura tree structure.

👉 Example:

* B subtree:

```
        B
       / \
      D   E
         /
        G
```

---

# Short Definitions
     ✔ Root → Topmost node
     ✔ Leaf → Node with no children
     ✔ Internal Node → Node with at least one child
     ✔ Degree of Node → Number of  children
     ✔ Height of Tree → Longest path from root to leaf
     ✔ Depth → Distance from root

---

# 🔥 Important Formula

If tree has:

* n nodes
* e edges

Then:

```
e = n - 1
```

---