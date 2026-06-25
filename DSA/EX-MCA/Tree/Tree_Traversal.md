## 🌳 Tree Traversals in Python

**Inorder, Preorder, Postorder**

---

## ✅ Example Tree

```
        1
       / \
      2   3
     / \
    4   5
```

---

## ✅ Step 1: Node Class

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

---

## ✅ Step 2: Create Tree

```python
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
```

---

# 🔹 1. Inorder Traversal (Left → Root → Right)

### 📌 Rule:

```
Left
Visit Root
Right
```

### Code:

```python
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

print("Inorder Traversal:")
inorder(root)
```

### Output:

```
4 2 5 1 3
```

---

# 🔹 2. Preorder Traversal (Root → Left → Right)

### 📌 Rule:

```
Visit Root
Left
Right
```

### Code:

```python
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

print("\nPreorder Traversal:")
preorder(root)
```

### Output:

```
1 2 4 5 3
```

---

# 🔹 3. Postorder Traversal (Left → Right → Root)

### 📌 Rule:

```
Left
Right
Visit Root
```

### Code:

```python
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

print("\nPostorder Traversal:")
postorder(root)
```

### Output:

```
4 5 2 3 1
```

---

# Final Combined Program (All Together)

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

# Create Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder:")
inorder(root)

print("\nPreorder:")
preorder(root)

print("\nPostorder:")
postorder(root)
```

---

# 📚 Time Complexity (Exam Important)

All Traversals → **O(n)**
(Each node visited exactly once)

