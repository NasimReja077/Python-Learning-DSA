## 🌳 Basic Tree in Python (Simple Binary Tree)

---

## ✅ 1. Node Class (Basic Structure)

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

---

## ✅ 2. Tree Create Karna (Manually)

Example Tree:

```
        1
       / \
      2   3
     / \
    4   5
```

```python
# Create nodes
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
```

---

## ✅ 3. Tree Traversals

### 🔹 Inorder (Left → Root → Right)

```python
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

print("Inorder:")
inorder(root)
```

---

### 🔹 Preorder (Root → Left → Right)

```python
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

print("\nPreorder:")
preorder(root)
```

---

### 🔹 Postorder (Left → Right → Root)

```python
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

print("\nPostorder:")
postorder(root)
```

---

## 📌 Output

```
Inorder: 4 2 5 1 3
Preorder: 1 2 4 5 3
Postorder: 4 5 2 3 1
```

---

