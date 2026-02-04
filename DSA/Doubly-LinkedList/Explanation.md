
# Line-by-Line Explanation: Insert at Beginning

Let me explain each line of the `insert_beginning` method with detailed diagrams.

---

## Complete Code with Line Numbers

```python
def insert_beginning(self, value):          # Line 1
    new_node = Node(value)                  # Line 2
                                            # Line 3 (blank)
    if self.head is not None:               # Line 4
        self.head.prev = new_node           # Line 5
        new_node.next = self.head           # Line 6
                                            # Line 7 (blank)
    self.head = new_node                    # Line 8
    print(value, "inserted at beginning")   # Line 9
```

---

## Example Scenario

Let's insert value **5** into an existing list: **10 ⇄ 20 ⇄ 30**

### Initial State of List

```
       self.head
           │
           ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘
        ▲                         │                         │
        └─────────────────────────┘                         │
                                  └─────────────────────────┘
```

---

## Line-by-Line Execution

---

### **LINE 1: Function Definition**

```python
def insert_beginning(self, value):
```

**What it does:**
- Defines a method named `insert_beginning`
- Takes two parameters:
  - `self`: Reference to the DoublyLinkedList object
  - `value`: The data to be inserted (in our case, **5**)

**Diagram:**
```
Function Called: insert_beginning(5)
                      │
                      ▼
                  value = 5
```

**Memory State:** No change yet

---

### **LINE 2: Create New Node**

```python
new_node = Node(value)
```

**What it does:**
- Creates a new `Node` object with `data = 5`
- The `Node` constructor automatically sets:
  - `new_node.data = 5`
  - `new_node.prev = None`
  - `new_node.next = None`

**Diagram AFTER Line 2:**

```
                   new_node
                      │
                      ▼
              ┌──────┬────┬──────┐
              │ NULL │ 5  │ NULL │
              │  ←   │    │  →   │
              └──────┴────┴──────┘


       self.head
           │
           ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘
        ▲                         │                         │
        └─────────────────────────┘                         │
                                  └─────────────────────────┘
```

**Memory State:**
- ✅ New node created in memory
- ❌ Not connected to list yet
- ❌ `self.head` still points to node 10

---

### **LINE 4: Check if List is Empty**

```python
if self.head is not None:
```

**What it does:**
- Checks whether the list already has nodes
- `self.head is not None` means the list is **NOT empty**
- In our case: `self.head` points to node 10, so condition is **TRUE**

**Truth Table:**
| Condition | List State | Result |
|-----------|------------|--------|
| `self.head is not None` | Empty list (head = NULL) | **False** → Skip lines 5-6 |
| `self.head is not None` | Has nodes (head ≠ NULL) | **True** → Execute lines 5-6 |

**In Our Case:** `self.head = Node(10)` → **TRUE**, so we execute lines 5-6

**Diagram:** (No change, just checking)

```
       self.head (is NOT None)
           │
           ▼
    ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→ ...
    │  ←   │    │  →   │
    └──────┴────┴──────┘

Condition: self.head is not None → TRUE ✓
```

---

### **LINE 5: Set Old Head's Previous Pointer**

```python
self.head.prev = new_node
```

**What it does:**
- Makes the **current first node** (node 10) point backward to the new node
- `self.head.prev` was `None`, now it points to `new_node`

**Visual Explanation:**

**BEFORE Line 5:**
```
                   new_node
                      │
                      ▼
              ┌──────┬────┬──────┐
              │ NULL │ 5  │ NULL │
              │  ←   │    │  →   │
              └──────┴────┴──────┘


       self.head
           │
           ▼
    ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→ ...
    │  ←   │    │  →   │
    └──────┴────┴──────┘
      ↑
      └─── This is NULL (no previous node)
```

**AFTER Line 5:**
```
                   new_node
                      │
                      ▼
              ┌──────┬────┬──────┐
              │ NULL │ 5  │ NULL │
              │  ←   │    │  →   │
              └──────┴────┴──────┘
                  ▲
                  │
                  │  self.head.prev = new_node
       self.head  │
           │      │
           ▼      │
    ┌──────┬────┬─┼────┐
    │  ●───┼─10 │  ●───┼────→ ...
    │  ←   │    │  →   │
    └──────┴────┴──────┘
```

**Memory State:**
- ✅ Node 10's `prev` now points to new_node (node 5)
- ❌ New node's `next` is still `None` (not connected yet)

---

### **LINE 6: Set New Node's Next Pointer**

```python
new_node.next = self.head
```

**What it does:**
- Makes the **new node** point forward to the current first node
- `new_node.next` was `None`, now it points to `self.head` (node 10)

**Visual Explanation:**

**BEFORE Line 6:**
```
              ┌──────┬────┬──────┐
              │ NULL │ 5  │ NULL │
              │  ←   │    │  →   │
              └──────┴────┴──────┘
                             ↑
                             └─── Still NULL
```

**AFTER Line 6:**
```
                   new_node
                      │
                      ▼
              ┌──────┬────┬──────┐
              │ NULL │ 5  │  ●───┼────┐
              │  ←   │    │  →   │    │
              └──────┴────┴──────┘    │
                  ▲                   │
                  │                   │ new_node.next = self.head
       self.head  │                   │
           │      │                   │
           ▼      │                   ▼
    ┌──────┬────┬─┼────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │  ●───┼─10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘
                                  │                         │
                                  ▼                         │
                            [Points back]                   │
                                                            ▼
                                                      [Points back]
```

**Memory State:**
- ✅ Bidirectional link established between new_node (5) and old head (10)
- ✅ Node 5 ← → Node 10 are now connected
- ❌ `self.head` still points to node 10 (not updated yet)

---

### **LINE 8: Update HEAD Pointer**

```python
self.head = new_node
```

**What it does:**
- Updates the `head` pointer to point to the new node
- Makes the new node the **official first node** of the list

**Visual Explanation:**

**BEFORE Line 8:**
```
                   new_node        self.head (still here)
                      │                 │
                      ▼                 ▼
              ┌──────┬────┬──────┐ ┌──────┬────┬──────┐
              │ NULL │ 5  │  ●───┼→│  ●───┼─10 │  ●───┼────→ ...
              │  ←   │    │  →   │ │  ←   │    │  →   │
              └──────┴────┴──────┘ └──────┴────┴──────┘
                  ▲                     │
                  └─────────────────────┘
```

**AFTER Line 8:**
```
                   self.head (moved here!)
                      │
                      ▼
              ┌──────┬────┬──────┐
              │ NULL │ 5  │  ●───┼────┐
              │  ←   │    │  →   │    │
              └──────┴────┬──────┘    │
                  ▲       │           │
                  │       └───────────┼───────────┐
                  │                   ▼           │
                  │           ┌──────┬────┬──────┐│    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
                  └───────────┤  ●───┼─10 │  ●───┼┼───→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
                              │  ←   │    │  →   ││    │  ←   │    │  →   │     │  ←   │    │  →   │
                              └──────┴────┴──────┘│    └──────┴────┴──────┘     └──────┴────┴──────┘
                                                  │         │                         │
                                                  └─────────┘                         │
                                                            └─────────────────────────┘
```

**Memory State:**
- ✅ `self.head` now points to new_node (node 5)
- ✅ Node 5 is now the first node
- ✅ List is properly updated: **5 ⇄ 10 ⇄ 20 ⇄ 30**

---

### **LINE 9: Print Confirmation**

```python
print(value, "inserted at beginning")
```

**What it does:**
- Prints a confirmation message to the console
- Output: `5 inserted at beginning`

**Diagram:** (No memory change, just output)

```
Console Output:
┌─────────────────────────────────┐
│ 5 inserted at beginning         │
└─────────────────────────────────┘
```

---

## Final State of the List

```
       self.head
           │
           ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 5  │  ●───┼────→│  ●───┼─10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘
        ▲                         │                         │                         │
        └─────────────────────────┘                         │                         │
                                  └─────────────────────────┘                         │
                                                            └─────────────────────────┘

List Order: 5 ⇄ 10 ⇄ 20 ⇄ 30
```

---

## Summary Table: Line-by-Line Changes

| Line | Code | What Happens | Pointers Changed |
|------|------|--------------|------------------|
| **1** | `def insert_beginning(self, value):` | Function starts with `value = 5` | None |
| **2** | `new_node = Node(value)` | Create new node with data=5, prev=None, next=None | `new_node` created |
| **4** | `if self.head is not None:` | Check if list is empty (TRUE in our case) | None |
| **5** | `self.head.prev = new_node` | Old head (10) points back to new node | `node10.prev → node5` |
| **6** | `new_node.next = self.head` | New node points forward to old head | `node5.next → node10` |
| **8** | `self.head = new_node` | Update head to point to new node | `self.head → node5` |
| **9** | `print(value, "inserted...")` | Display confirmation message | None |

---

## Special Case: Empty List

What happens when inserting into an **empty list**?

### Initial State
```
self.head = None

(No nodes exist)
```

### Execution with Empty List

**Line 2:** Create new node
```
new_node created with data=5, prev=None, next=None
```

**Line 4:** Check `if self.head is not None:`
```
self.head is None → FALSE
Skip lines 5-6 (because there's no existing node)
```

**Line 8:** Update head
```
self.head = new_node
```

### Result
```
       self.head
           │
           ▼
    ┌──────┬────┬──────┐
    │ NULL │ 5  │ NULL │
    │  ←   │    │  →   │
    └──────┴────┴──────┘

List: 5 (single node)
```

**Key Point:** When the list is empty, we **skip lines 5-6** because there's no existing head to connect to!

---

## Complete Flow Diagram

```
START
  │
  ▼
Create new_node with value
  │
  ▼
Is list empty?
  │
  ├─── YES → Skip connection steps
  │            │
  │            └─→ Update self.head = new_node
  │                        │
  │                        └─→ Print message → END
  │
  └─── NO  → Connect old head backward (self.head.prev = new_node)
               │
               ▼
           Connect new node forward (new_node.next = self.head)
               │
               ▼
           Update self.head = new_node
               │
               ▼
           Print message
               │
               ▼
              END
```
---
---

# Line-by-Line Explanation: Insert at End

Let me explain each line of the `insert_end` method with detailed diagrams.

---

## Complete Code with Line Numbers

```python
def insert_end(self, value):                # Line 1
    new_node = Node(value)                  # Line 2
                                            # Line 3 (blank)
    if self.head is None:                   # Line 4
        self.head = new_node                # Line 5
        print(value, "inserted at end")     # Line 6
        return                              # Line 7
                                            # Line 8 (blank)
    temp = self.head                        # Line 9
    while temp.next:                        # Line 10
        temp = temp.next                    # Line 11
                                            # Line 12 (blank)
    temp.next = new_node                    # Line 13
    new_node.prev = temp                    # Line 14
    print(value, "inserted at end")         # Line 15
```

---

## Example Scenario

Let's insert value **40** at the end of an existing list: **10 ⇄ 20 ⇄ 30**

### Initial State of List

```
       self.head
           │
           ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘
        ▲                         │                         │
        └─────────────────────────┘                         │
                                  └─────────────────────────┘
```

---

## Line-by-Line Execution

---

### **LINE 1: Function Definition**

```python
def insert_end(self, value):
```

**What it does:**
- Defines a method named `insert_end`
- Takes two parameters:
  - `self`: Reference to the DoublyLinkedList object
  - `value`: The data to be inserted (in our case, **40**)

**Diagram:**
```
Function Called: insert_end(40)
                      │
                      ▼
                  value = 40
```

**Memory State:** No change yet

---

### **LINE 2: Create New Node**

```python
new_node = Node(value)
```

**What it does:**
- Creates a new `Node` object with `data = 40`
- The `Node` constructor automatically sets:
  - `new_node.data = 40`
  - `new_node.prev = None`
  - `new_node.next = None`

**Diagram AFTER Line 2:**

```
                   new_node
                      │
                      ▼
              ┌──────┬────┬──────┐
              │ NULL │ 40 │ NULL │
              │  ←   │    │  →   │
              └──────┴────┴──────┘


       self.head
           │
           ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘
        ▲                         │                         │
        └─────────────────────────┘                         │
                                  └─────────────────────────┘
```

**Memory State:**
- ✅ New node created in memory with value 40
- ❌ Not connected to list yet
- ❌ List remains unchanged: 10 ⇄ 20 ⇄ 30

---

### **LINE 4: Check if List is Empty**

```python
if self.head is None:
```

**What it does:**
- Checks whether the list is empty (no nodes exist)
- `self.head is None` means the list is **empty**
- In our case: `self.head` points to node 10, so condition is **FALSE**

**Truth Table:**
| Condition | List State | Result | Action |
|-----------|------------|--------|--------|
| `self.head is None` | Empty list | **True** | Execute lines 5-7 (special case) |
| `self.head is None` | Has nodes | **False** | Skip lines 5-7, go to line 9 |

**In Our Case:** `self.head = Node(10)` → **FALSE**, so we **skip lines 5-7**

**Diagram:** (Checking only)

```
       self.head (is NOT None)
           │
           ▼
    ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→ ...
    │  ←   │    │  →   │
    └──────┴────┴──────┘

Condition: self.head is None → FALSE ✗
Action: Skip lines 5-7, jump to line 9
```

---

### **LINES 5-7: Handle Empty List Case (SKIPPED in our example)**

```python
self.head = new_node                # Line 5
print(value, "inserted at end")     # Line 6
return                              # Line 7
```

**What it does:**
- **Only executed if the list is EMPTY**
- Makes the new node the first (and only) node
- Prints confirmation and exits the function

**Special Case Diagram (if list was empty):**

```
       self.head
           │
           ▼
    ┌──────┬────┬──────┐
    │ NULL │ 40 │ NULL │
    │  ←   │    │  →   │
    └──────┴────┴──────┘

List: 40 (single node)
Output: "40 inserted at end"
```

**In our example:** Lines 5-7 are **SKIPPED** because list is not empty

---

### **LINE 9: Initialize Traversal Pointer**

```python
temp = self.head
```

**What it does:**
- Creates a temporary pointer `temp` that starts at the **first node**
- `temp` will be used to traverse the list to find the **last node**
- Does NOT change the list, just creates a reference

**Diagram AFTER Line 9:**

```
                   new_node
                      │
                      ▼
              ┌──────┬────┬──────┐
              │ NULL │ 40 │ NULL │
              │  ←   │    │  →   │
              └──────┴────┴──────┘


    self.head
    temp (both pointing here)
        │
        ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘
        ▲                         │                         │
        └─────────────────────────┘                         │
                                  └─────────────────────────┘
```

**Memory State:**
- ✅ `temp` initialized to point to first node (10)
- ❌ Need to move `temp` to the last node

---

### **LINE 10: While Loop - Check for Last Node**

```python
while temp.next:
```

**What it does:**
- Checks if `temp.next` is **not None** (i.e., current node is NOT the last node)
- Continues looping until we reach the **last node** (where `next` is `None`)

**Loop Iterations:**

#### **Iteration 1: temp at Node 10**

```
    self.head
        │     temp
        │      ▼
        ▼      │
    ┌──────┬──┼─┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘
                   │
                   └─── temp.next is NOT None (points to node 20)

Condition: temp.next → TRUE (continue loop)
```

---

### **LINE 11: Move to Next Node**

```python
temp = temp.next
```

**What it does:**
- Moves the `temp` pointer to the **next node**
- This happens inside the while loop

**After First Iteration:**

```
    self.head
        │
        ▼
    ┌──────┬────┬──────┐          temp
    │ NULL │ 10 │  ●───┼────→     ▼
    │  ←   │    │  →   │     ┌────┼─┬────┬──────┐     ┌──────┬────┬──────┐
    └──────┴────┴──────┘     │  ●─┼─┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
                             │  ← │ │    │  →   │     │  ←   │    │  →   │
                             └────┴─┴────┴──────┘     └──────┴────┴──────┘
                                      │
                                      └─── temp.next is NOT None (points to node 30)

Back to Line 10: Check condition again
```

---

#### **Iteration 2: temp at Node 20**

**Line 10:** Check `while temp.next:`
```
Condition: temp.next → TRUE (points to node 30, continue loop)
```

**Line 11:** Move temp forward
```
temp = temp.next  (temp now points to node 30)
```

**After Second Iteration:**

```
    self.head
        │
        ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐          temp
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→     ▼
    │  ←   │    │  →   │     │  ←   │    │  →   │     ┌────┼─┬────┬──────┐
    └──────┴────┴──────┘     └──────┴────┴──────┘     │  ●─┼─┼─30 │ NULL │
                                                       │  ← │ │    │  →   │
                                                       └────┴─┴────┴──────┘
                                                                      │
                                                                      └─── temp.next is None

Back to Line 10: Check condition again
```

---

#### **Iteration 3: temp at Node 30 (Last Node)**

**Line 10:** Check `while temp.next:`
```
Condition: temp.next is None → FALSE (EXIT loop)
```

**Diagram:**

```
    self.head
        │
        ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐ ← temp
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘

temp.next is None → Loop EXITS
temp is now at the LAST NODE (30)
```

**Memory State:**
- ✅ Loop finished
- ✅ `temp` now points to the **last node** (node 30)
- Ready to connect new node

---

### **LINE 13: Connect Last Node to New Node**

```python
temp.next = new_node
```

**What it does:**
- Makes the **current last node** (node 30) point forward to the new node (40)
- Establishes the **forward link**

**Visual Explanation:**

**BEFORE Line 13:**
```
                   new_node
                      │
                      ▼
              ┌──────┬────┬──────┐
              │ NULL │ 40 │ NULL │
              │  ←   │    │  →   │
              └──────┴────┴──────┘


                                                       temp
                                                        ▼
    ... ────→ ┌──────┬────┬──────┐
              │  ●───┼─30 │ NULL │
              │  ←   │    │  →   │
              └──────┴────┴──────┘
                             ↑
                             └─── Currently NULL
```

**AFTER Line 13:**
```
                   new_node
                      │
                      ▼
              ┌──────┬────┬──────┐
              │ NULL │ 40 │ NULL │
              │  ←   │    │  →   │
              └──────┴────┴──────┘
                  ▲
                  │
                  │ temp.next = new_node
       self.head  │              temp
           │      │               ▼
           ▼      │               │
    ┌──────┬────┬──────┐     ┌───┼──┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●┼──┼─20 │  ●───┼────→│  ●───┼─30 │  ●───┼─────┐
    │  ←   │    │  →   │     │  ←│  │    │  →   │     │  ←   │    │  →   │     │
    └──────┴────┴──────┘     └───┴──┴────┴──────┘     └──────┴────┴──────┘     │
                                  │                         │                   │
                                  ▼                         │                   │
                            [Points back]                   │                   │
                                                            ▼                   │
                                                      [Points back]             │
                                                                                │
                                                                                └──→ Points to node 40
```

**Memory State:**
- ✅ Node 30's `next` now points to new_node (40)
- ❌ New node's `prev` is still `None` (backward link not established yet)

---

### **LINE 14: Connect New Node to Last Node**

```python
new_node.prev = temp
```

**What it does:**
- Makes the **new node** point backward to the previous last node (temp = node 30)
- Establishes the **backward link**
- Completes the **bidirectional connection**

**Visual Explanation:**

**BEFORE Line 14:**
```
              ┌──────┬────┬──────┐
              │ NULL │ 40 │ NULL │
              │  ←   │    │  →   │
              └──────┴────┴──────┘
                ↑
                └─── Still NULL (no backward connection)
```

**AFTER Line 14:**
```
       self.head
           │
           ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │  ●───┼────→│  ●───┼─40 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘
        ▲                         │                         │                         │
        └─────────────────────────┘                         │                         │
                                  └─────────────────────────┘                         │
                                                            └─────────────────────────┘
                                                            
                                                   new_node.prev = temp (node 30)
```

**Memory State:**
- ✅ Bidirectional link established: Node 30 ⇄ Node 40
- ✅ List is now: 10 ⇄ 20 ⇄ 30 ⇄ 40
- ✅ Insertion complete!

---

### **LINE 15: Print Confirmation**

```python
print(value, "inserted at end")
```

**What it does:**
- Prints a confirmation message to the console
- Output: `40 inserted at end`

**Diagram:** (No memory change, just output)

```
Console Output:
┌─────────────────────────────────┐
│ 40 inserted at end              │
└─────────────────────────────────┘
```

---

## Final State of the List

```
       self.head
           │
           ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │  ●───┼────→│  ●───┼─40 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘
        ▲                         │                         │                         │
        └─────────────────────────┘                         │                         │
                                  └─────────────────────────┘                         │
                                                            └─────────────────────────┘

List Order: 10 ⇄ 20 ⇄ 30 ⇄ 40
```

---

## Summary Table: Line-by-Line Changes

| Line | Code | What Happens | Key Action |
|------|------|--------------|------------|
| **1** | `def insert_end(self, value):` | Function starts with `value = 40` | None |
| **2** | `new_node = Node(value)` | Create new node: data=40, prev=None, next=None | New node created |
| **4** | `if self.head is None:` | Check if list is empty (FALSE) | Condition check |
| **5-7** | Empty list handling | SKIPPED (list not empty) | Lines skipped |
| **9** | `temp = self.head` | Initialize temp to first node (10) | `temp → node10` |
| **10** | `while temp.next:` | Check if current node has next node | Loop control |
| **11** | `temp = temp.next` | Move temp forward (10→20→30) | Traverse list |
| **10** | (loop exits) | temp.next is None at node 30 | Found last node |
| **13** | `temp.next = new_node` | Last node points to new node | `node30.next → node40` |
| **14** | `new_node.prev = temp` | New node points back to last node | `node40.prev → node30` |
| **15** | `print(value, "inserted...")` | Display confirmation | Console output |

---

## Special Case: Inserting into Empty List

What happens when the list is **empty**?

### Initial State
```
self.head = None

(No nodes exist)
```

### Execution with Empty List

**Line 2:** Create new node
```
new_node created with data=40, prev=None, next=None
```

**Line 4:** Check `if self.head is None:`
```
self.head is None → TRUE
Execute lines 5-7
```

**Line 5:** Update head
```
self.head = new_node
```

**Line 6:** Print confirmation
```
Output: "40 inserted at end"
```

**Line 7:** Return (exit function)
```
Function ends, lines 9-15 are NOT executed
```

### Result
```
       self.head
           │
           ▼
    ┌──────┬────┬──────┐
    │ NULL │ 40 │ NULL │
    │  ←   │    │  →   │
    └──────┴────┴──────┘

List: 40 (single node)
```

---

## Visual Flow of While Loop

```
START at node 10
      │
      ▼
┌─────────────────┐
│  temp at node   │
│      10         │
└─────────────────┘
      │
      ▼
  temp.next? ──YES──→ Move to node 20
      │
      ▼
┌─────────────────┐
│  temp at node   │
│      20         │
└─────────────────┘
      │
      ▼
  temp.next? ──YES──→ Move to node 30
      │
      ▼
┌─────────────────┐
│  temp at node   │
│      30         │
└─────────────────┘
      │
      ▼
  temp.next? ──NO──→ EXIT LOOP
      │
      ▼
  Found last node!
  Connect new node
```

---

## Time & Space Complexity

| Aspect | Complexity | Reason |
|--------|-----------|--------|
| **Time Complexity** | **O(n)** | Must traverse entire list to find last node (where n = number of nodes) |
| **Space Complexity** | **O(1)** | Only one new node created, temp is just a pointer |

**Note:** Unlike insert at beginning O(1), insert at end requires traversal, making it O(n).

---

## Complete Execution Flow Diagram

```
START insert_end(40)
       │
       ▼
Create new_node(40)
       │
       ▼
Is list empty? ────YES───→ self.head = new_node ──→ Print ──→ END
       │
       NO
       ▼
temp = self.head (node 10)
       │
       ▼
┌──────────────────┐
│  While Loop:     │
│  temp.next?      │
└──────────────────┘
       │
       ├──YES──→ temp = temp.next ──┐
       │                            │
       │←───────────────────────────┘
       │
       NO (found last node)
       ▼
temp.next = new_node
       │
       ▼
new_node.prev = temp
       │
       ▼
Print confirmation
       │
       ▼
      END
```

---
---
---
# Line-by-Line Explanation: Insert After a Given Value

Let me explain each line of the `insert_after` method with detailed diagrams.

---

## Complete Code with Line Numbers

```python
def insert_after(self, prev_value, value):      # Line 1
    temp = self.head                            # Line 2
                                                # Line 3 (blank)
    while temp:                                 # Line 4
        if temp.data == prev_value:             # Line 5
            new_node = Node(value)              # Line 6
            new_node.next = temp.next           # Line 7
            new_node.prev = temp                # Line 8
                                                # Line 9 (blank)
            if temp.next:                       # Line 10
                temp.next.prev = new_node       # Line 11
                                                # Line 12 (blank)
            temp.next = new_node                # Line 13
            print(value, "inserted after", prev_value)  # Line 14
            return                              # Line 15
                                                # Line 16 (blank)
        temp = temp.next                        # Line 17
                                                # Line 18 (blank)
    print("Value", prev_value, "not found")     # Line 19
```

---

## Example Scenario

Let's insert value **25** after node with value **20** in the list: **10 ⇄ 20 ⇄ 30**

### Initial State of List

```
       self.head
           │
           ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘
        ▲                         │                         │
        └─────────────────────────┘                         │
                                  └─────────────────────────┘

Goal: Insert 25 after 20
Expected Result: 10 ⇄ 20 ⇄ 25 ⇄ 30
```

---

## Line-by-Line Execution

---

### **LINE 1: Function Definition**

```python
def insert_after(self, prev_value, value):
```

**What it does:**
- Defines a method named `insert_after`
- Takes three parameters:
  - `self`: Reference to the DoublyLinkedList object
  - `prev_value`: The value of the node after which we want to insert (**20**)
  - `value`: The data to be inserted (**25**)

**Diagram:**
```
Function Called: insert_after(20, 25)
                      │       │
                      │       └─── value = 25 (new node data)
                      └─────────── prev_value = 20 (search for this)
```

**Memory State:** No change yet

---

### **LINE 2: Initialize Traversal Pointer**

```python
temp = self.head
```

**What it does:**
- Creates a temporary pointer `temp` that starts at the **first node**
- `temp` will be used to traverse the list to find the node with value `prev_value` (20)

**Diagram AFTER Line 2:**

```
    self.head
    temp (both pointing here)
        │
        ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘
        ▲                         │                         │
        └─────────────────────────┘                         │
                                  └─────────────────────────┘
```

**Memory State:**
- ✅ `temp` initialized to point to first node (10)
- Need to search for node with value 20

---

### **LINE 4: While Loop - Traverse the List**

```python
while temp:
```

**What it does:**
- Checks if `temp` is **not None** (i.e., we haven't reached the end of the list)
- Continues looping until we either:
  - Find the node with `prev_value` (20), OR
  - Reach the end of the list (temp becomes None)

**Loop Control:**
```
while temp:  means  "while temp is not None"
```

---

### **Iteration 1: temp at Node 10**

```
         temp
          ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘

Condition: temp is not None → TRUE (continue)
```

---

### **LINE 5: Check if Current Node Matches**

```python
if temp.data == prev_value:
```

**What it does:**
- Checks if the current node's data equals `prev_value` (20)
- In iteration 1: `temp.data = 10`, `prev_value = 20`
- Condition: `10 == 20` → **FALSE**

**Diagram:**

```
         temp
          ▼
    ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→ ...
    │  ←   │    │  →   │
    └──────┴────┴──────┘

Check: temp.data (10) == prev_value (20)?
Result: FALSE ✗

Action: Skip lines 6-15, go to line 17
```

---

### **LINE 17: Move to Next Node**

```python
temp = temp.next
```

**What it does:**
- Since the condition was false, move `temp` to the next node
- Continue searching

**After Moving:**

```
    self.head
        │
        ▼
    ┌──────┬────┬──────┐          temp
    │ NULL │ 10 │  ●───┼────→     ▼
    │  ←   │    │  →   │     ┌────┼─┬────┬──────┐     ┌──────┬────┬──────┐
    └──────┴────┴──────┘     │  ●─┼─┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
                             │  ← │ │    │  →   │     │  ←   │    │  →   │
                             └────┴─┴────┴──────┘     └──────┴────┴──────┘

Back to Line 4: Check while condition again
```

---

### **Iteration 2: temp at Node 20**

**Line 4:** Check `while temp:`
```
temp is not None → TRUE (continue)
```

**Line 5:** Check `if temp.data == prev_value:`

```
         temp
          ▼
    ┌──────┬────┬──────┐
    │  ●───┼─20 │  ●───┼────→ ...
    │  ←   │    │  →   │
    └──────┴────┴──────┘

Check: temp.data (20) == prev_value (20)?
Result: TRUE ✓

Action: Execute lines 6-15 (insertion logic)
```

**Found the target node! Now we insert after it.**

---

### **LINE 6: Create New Node**

```python
new_node = Node(value)
```

**What it does:**
- Creates a new node with `data = 25`
- `new_node.prev = None`
- `new_node.next = None`

**Diagram AFTER Line 6:**

```
                   new_node
                      │
                      ▼
              ┌──────┬────┬──────┐
              │ NULL │ 25 │ NULL │
              │  ←   │    │  →   │
              └──────┴────┴──────┘


    self.head
        │
        ▼                    temp
    ┌──────┬────┬──────┐     ▼
    │ NULL │ 10 │  ●───┼────→┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │  ←   │    │  →   │     │  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
    └──────┴────┴──────┘     │  ←   │    │  →   │     │  ←   │    │  →   │
                             └──────┴────┴──────┘     └──────┴────┴──────┘
                                                            │
                                                            │
                                                    This will be after new_node
```

**Memory State:**
- ✅ New node (25) created
- ❌ Not connected to list yet
- `temp` is at node 20 (where we want to insert after)

---

### **LINE 7: Connect New Node's Next to temp's Next**

```python
new_node.next = temp.next
```

**What it does:**
- Makes the new node point forward to the node that comes **after temp** (node 30)
- Essentially: "New node's next should point to what temp's next is currently pointing to"

**Visual Explanation:**

**BEFORE Line 7:**
```
              new_node
                 │
                 ▼
         ┌──────┬────┬──────┐
         │ NULL │ 25 │ NULL │
         │  ←   │    │  →   │
         └──────┴────┴──────┘
                        ↑
                        └─── Currently NULL
```

**AFTER Line 7:**
```
                   new_node
                      │
                      ▼
              ┌──────┬────┬──────┐
              │ NULL │ 25 │  ●───┼──────┐
              │  ←   │    │  →   │      │
              └──────┴────┴──────┘      │
                                        │
                                        │ new_node.next = temp.next (points to node 30)
                             temp       │
                              ▼         │
    ... ────→ ┌──────┬────┬──────┐     │   ┌──────┬────┬──────┐
              │  ●───┼─20 │  ●───┼─────┼──→│  ●───┼─30 │ NULL │
              │  ←   │    │  →   │     │   │  ←   │    │  →   │
              └──────┴────┴──────┘     │   └──────┴────┴──────┘
                                       │         ▲
                                       └─────────┘
                                    Both pointing to node 30
```

**Memory State:**
- ✅ New node's next → node 30
- ❌ Node 30 doesn't know about new node yet
- ❌ Node 20 still points to node 30 (not updated yet)

---

### **LINE 8: Connect New Node's Prev to temp**

```python
new_node.prev = temp
```

**What it does:**
- Makes the new node point backward to `temp` (node 20)
- Establishes the backward connection

**AFTER Line 8:**

```
                   new_node
                      │
                      ▼
              ┌──────┬────┬──────┐
              │  ●───┼─25 │  ●───┼──────┐
              │  ←   │    │  →   │      │
              └──────┴────┴──────┘      │
                  ▲                     │
                  │ new_node.prev       │
                  │                     │
                             temp       │
                              ▼         │
    ... ────→ ┌──────┬────┬──────┐     │   ┌──────┬────┬──────┐
              │  ●───┼─20 │  ●───┼─────┼──→│  ●───┼─30 │ NULL │
              │  ←   │    │  →   │     │   │  ←   │    │  →   │
              └──────┴────┴──────┘     │   └──────┴────┴──────┘
                  ▲                    │         ▲
                  └────────────────────┘         │
                                                 └─── Still points to node 20
```

**Memory State:**
- ✅ New node's prev → node 20
- ✅ New node's next → node 30
- ❌ Node 20 still points directly to node 30
- ❌ Node 30 still points back to node 20

---

### **LINE 10: Check if temp.next Exists**

```python
if temp.next:
```

**What it does:**
- Checks if there's a node **after temp** (i.e., we're not at the end of the list)
- This is important because:
  - If `temp.next` exists → We need to update that node's `prev` pointer
  - If `temp.next` is None → temp is the last node, skip line 11

**In Our Case:**
```
temp.next points to node 30 → NOT None → TRUE
Execute line 11
```

**Truth Table:**

| Scenario | temp.next | Result | Action |
|----------|-----------|--------|--------|
| Inserting after middle node | Points to next node | TRUE | Execute line 11 |
| Inserting after last node | None (NULL) | FALSE | Skip line 11 |

---

### **LINE 11: Update Next Node's Prev Pointer**

```python
temp.next.prev = new_node
```

**What it does:**
- Makes the node **after temp** (node 30) point backward to the new node instead of temp
- `temp.next` is node 30
- `temp.next.prev` is node 30's prev pointer
- Change it from pointing to node 20 → pointing to new node (25)

**Visual Explanation:**

**BEFORE Line 11:**
```
              ┌──────┬────┬──────┐
              │  ●───┼─30 │ NULL │
              │  ←   │    │  →   │
              └──────┴────┴──────┘
                  │
                  ├─── Currently points to node 20
                  ▼
            [Node 20]
```

**AFTER Line 11:**
```
                   new_node
                      │
                      ▼
              ┌──────┬────┬──────┐
              │  ●───┼─25 │  ●───┼──────┐
              │  ←   │    │  →   │      │
              └──────┴────┴──────┘      │
                  ▲   ▲                 │
                  │   └─────────────┐   │
                  │                 │   │
                             temp   │   │
                              ▼     │   │
    ... ────→ ┌──────┬────┬──────┐ │   │   ┌──────┬────┬──────┐
              │  ●───┼─20 │  ●───┼─┼───┼──→│  ●───┼─30 │ NULL │
              │  ←   │    │  →   │ │   │   │  ←   │    │  →   │
              └──────┴────┴──────┘ │   │   └──────┴────┴──────┘
                  ▲                │   │       ▲
                  └────────────────┘   └───────┘
                                    temp.next.prev = new_node
```

**Memory State:**
- ✅ Node 30's prev → new node (25)
- ✅ New node is now properly linked backward and forward
- ❌ Node 20 still points to node 30 (final step remaining)

---

### **LINE 13: Update temp's Next Pointer**

```python
temp.next = new_node
```

**What it does:**
- Makes `temp` (node 20) point forward to the new node instead of node 30
- This is the **final connection** that completes the insertion

**Visual Explanation:**

**BEFORE Line 13:**
```
                             temp
                              ▼
    ... ────→ ┌──────┬────┬──────┐
              │  ●───┼─20 │  ●───┼─────────────────┐
              │  ←   │    │  →   │                 │
              └──────┴────┴──────┘                 │
                                                   │
                                          Still points to node 30
                                                   │
                                                   ▼
                                          ┌──────┬────┬──────┐
                                          │  ●───┼─30 │ NULL │
                                          └──────┴────┴──────┘
```

**AFTER Line 13:**
```
       self.head
           │
           ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─25 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘
        ▲                         │                         │                         │
        └─────────────────────────┘                         │                         │
                                  └─────────────────────────┘                         │
                                                            └─────────────────────────┘
                                                            
                                          temp.next = new_node
```

**Memory State:**
- ✅ **Insertion Complete!**
- ✅ All four connections established:
  1. Node 20 → Node 25 (forward)
  2. Node 25 → Node 20 (backward)
  3. Node 25 → Node 30 (forward)
  4. Node 30 → Node 25 (backward)
- List is now: **10 ⇄ 20 ⇄ 25 ⇄ 30**

---

### **LINE 14: Print Confirmation**

```python
print(value, "inserted after", prev_value)
```

**What it does:**
- Prints a success message
- Output: `25 inserted after 20`

**Console Output:**
```
┌─────────────────────────────────┐
│ 25 inserted after 20            │
└─────────────────────────────────┘
```

---

### **LINE 15: Return from Function**

```python
return
```

**What it does:**
- Exits the function immediately
- No need to continue searching (we already found and inserted)
- Lines 17-19 will **NOT** execute

---

## Final State of the List

```
       self.head
           │
           ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─25 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘
        ▲                         │                         │                         │
        └─────────────────────────┘                         │                         │
                                  └─────────────────────────┘                         │
                                                            └─────────────────────────┘

List Order: 10 ⇄ 20 ⇄ 25 ⇄ 30
```

---

## Special Case 1: Inserting After Last Node

What if we insert **40 after 30** (last node)?

### Scenario
```
Initial: 10 ⇄ 20 ⇄ 30
Insert: 40 after 30
```

### Execution Differences

When `temp` reaches node 30:

**Line 5:** `temp.data (30) == prev_value (30)` → TRUE

**Line 7:** `new_node.next = temp.next`
```
temp.next is NULL (30 is last node)
new_node.next = NULL
```

**Line 10:** `if temp.next:`
```
temp.next is None → FALSE
Skip line 11 (no next node to update)
```

**Line 13:** `temp.next = new_node`
```
Node 30 now points to new node 40
```

### Result
```
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │  ●───┼────→│  ●───┼─40 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘

List: 10 ⇄ 20 ⇄ 30 ⇄ 40
```

**Key Difference:** Line 11 is skipped because there's no node after 30 to update.

---

## Special Case 2: Value Not Found

What if we try to insert **25 after 100** (which doesn't exist)?

### Execution Flow

**Line 2:** `temp = self.head` (start at node 10)

**Line 4-17:** Loop through all nodes
- Check node 10: `10 == 100?` → FALSE → Move to next
- Check node 20: `20 == 100?` → FALSE → Move to next
- Check node 30: `30 == 100?` → FALSE → Move to next
- `temp = temp.next` → temp becomes NULL

**Line 4:** `while temp:`
```
temp is None → FALSE (exit loop)
```

**Line 19:** `print("Value", prev_value, "not found")`

### Result
```
Console Output:
┌─────────────────────────────────┐
│ Value 100 not found             │
└─────────────────────────────────┘

List remains unchanged: 10 ⇄ 20 ⇄ 30
```

---

## Summary Table: Line-by-Line Actions

| Line | Code | What Happens | Key Action |
|------|------|--------------|------------|
| **1** | `def insert_after(...)` | Function starts with prev_value=20, value=25 | Initialize parameters |
| **2** | `temp = self.head` | Start at first node (10) | `temp → node10` |
| **4** | `while temp:` | Check if temp exists (loop control) | Search loop |
| **5** | `if temp.data == prev_value:` | Check if current node matches | Found node 20 ✓ |
| **6** | `new_node = Node(value)` | Create new node with data=25 | New node created |
| **7** | `new_node.next = temp.next` | New node points to node 30 | `node25.next → node30` |
| **8** | `new_node.prev = temp` | New node points back to node 20 | `node25.prev → node20` |
| **10** | `if temp.next:` | Check if next node exists (TRUE) | Condition check |
| **11** | `temp.next.prev = new_node` | Node 30 points back to new node | `node30.prev → node25` |
| **13** | `temp.next = new_node` | Node 20 points to new node | `node20.next → node25` |
| **14** | `print(...)` | Display success message | Console output |
| **15** | `return` | Exit function | Insertion complete |

---

## Visual Connection Flow

```
STEP 1: Find target node (20)
┌──────────────────────────────┐
│  Traverse: 10 → 20 (Found!)  │
└──────────────────────────────┘

STEP 2: Create new node (25)
┌──────────────────────────────┐
│  [25] created in memory      │
└──────────────────────────────┘

STEP 3: Forward connections
┌──────────────────────────────┐
│  [25].next → [30]            │
│  [20].next → [25]            │
└──────────────────────────────┘

STEP 4: Backward connections
┌──────────────────────────────┐
│  [25].prev → [20]            │
│  [30].prev → [25]            │
└──────────────────────────────┘

RESULT: 10 ⇄ 20 ⇄ 25 ⇄ 30
```

---

## Four Critical Pointer Updates

When inserting node **B** between nodes **A** and **C**:

```
BEFORE:  A ⇄ C

AFTER:   A ⇄ B ⇄ C

Required Updates:
1. B.next = C     (Line 7)  → B points forward to C
2. B.prev = A     (Line 8)  → B points backward to A
3. C.prev = B     (Line 11) → C points backward to B
4. A.next = B     (Line 13) → A points forward to B
```

**Important:** Line 13 MUST come last! If we update `A.next = B` before setting `B.next = C`, we lose the reference to C.

---

## Complete Execution Flow Diagram

```
START insert_after(20, 25)
       │
       ▼
temp = self.head (node 10)
       │
       ▼
┌──────────────────────────┐
│  While temp exists?      │
└──────────────────────────┘
       │
       ├──YES──→ Is temp.data == 20?
       │              │
       │              ├──NO──→ temp = temp.next ──┐
       │              │                           │
       │              │←──────────────────────────┘
       │              │
       │              └──YES──→ Create new_node(25)
       │                              │
       │                              ▼
       │                   new_node.next = temp.next (node 30)
       │                              │
       │                              ▼
       │                   new_node.prev = temp (node 20)
       │                              │
       │                              ▼
       │                   Is temp.next exists?
       │                              │
       │                              ├──YES──→ temp.next.prev = new_node
       │                              │               │
       │                              │               ▼
       │                              │         temp.next = new_node
       │                              │               │
       │                              │               ▼
       │                              │          Print success
       │                              │               │
       │                              │               ▼
       │                              │            RETURN → END
       │                              │
       │                              └──NO──→ temp.next = new_node
       │                                            │
       │                                            ▼
       │                                       Print success
       │                                            │
       │                                            ▼
       │                                         RETURN → END
       │
       NO (temp is None)
       │
       ▼
Print "Value not found"
       │
       ▼
      END
```

---

## Time & Space Complexity

| Aspect | Complexity | Reason |
|--------|-----------|--------|
| **Time Complexity** | **O(n)** | Must traverse list to find prev_value (worst case: entire list) |
| **Space Complexity** | **O(1)** | Only one new node created, temp is just a pointer |

**Best Case:** O(1) if prev_value is at the first node  
**Worst Case:** O(n) if prev_value is at the last node or not found

---
---
---
# Line-by-Line Explanation: Display, Search, and Count Operations

Let me explain each method with detailed diagrams.

---

## Example List for All Operations

We'll use this list for all demonstrations:

```
       self.head
           │
           ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘
        ▲                         │                         │
        └─────────────────────────┘                         │
                                  └─────────────────────────┘

List: 10 ⇄ 20 ⇄ 30
```

---

# PART 1: DISPLAY METHOD

## Complete Code with Line Numbers

```python
def display(self):                          # Line 1
    if self.head is None:                   # Line 2
        print("Doubly Linked List is empty") # Line 3
        return                              # Line 4
                                            # Line 5 (blank)
    print("Doubly Linked List:")            # Line 6
    temp = self.head                        # Line 7
    while temp:                             # Line 8
        print(temp.data, end=" <-> ")       # Line 9
        temp = temp.next                    # Line 10
    print("NULL")                           # Line 11
```

---

## Line-by-Line Execution: DISPLAY

---

### **LINE 1: Function Definition**

```python
def display(self):
```

**What it does:**
- Defines the `display` method to show all nodes in the list
- Takes only `self` parameter (no additional arguments needed)

---

### **LINE 2: Check if List is Empty**

```python
if self.head is None:
```

**What it does:**
- Checks if the list has any nodes
- `self.head is None` means the list is empty

**Truth Table:**

| Condition | List State | Result | Action |
|-----------|------------|--------|--------|
| `self.head is None` | Empty | TRUE | Execute lines 3-4 |
| `self.head is None` | Has nodes | FALSE | Skip to line 6 |

**In Our Case:** List has nodes → **FALSE** → Skip lines 3-4

```
    self.head (is NOT None)
        │
        ▼
    ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→ ...
    └──────┴────┴──────┘

Condition: FALSE → Skip to line 6
```

---

### **LINES 3-4: Handle Empty List (SKIPPED in our example)**

```python
print("Doubly Linked List is empty")       # Line 3
return                                      # Line 4
```

**What it does:**
- Only executes if list is empty
- Prints message and exits function

**If list was empty:**
```
Console Output:
┌─────────────────────────────────────┐
│ Doubly Linked List is empty         │
└─────────────────────────────────────┘

Function ends (no further execution)
```

---

### **LINE 6: Print Header**

```python
print("Doubly Linked List:")
```

**What it does:**
- Prints a header before displaying the list
- No changes to memory

**Console Output:**
```
┌─────────────────────────────────────┐
│ Doubly Linked List:                 │
└─────────────────────────────────────┘
```

---

### **LINE 7: Initialize Traversal Pointer**

```python
temp = self.head
```

**What it does:**
- Creates `temp` pointer starting at the first node
- Used to traverse the entire list

**Diagram AFTER Line 7:**

```
    self.head
    temp (both pointing here)
        │
        ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘
```

---

### **LINE 8-10: While Loop - Traverse and Print**

```python
while temp:                             # Line 8
    print(temp.data, end=" <-> ")       # Line 9
    temp = temp.next                    # Line 10
```

**What it does:**
- **Line 8:** Checks if `temp` is not None (continue looping)
- **Line 9:** Prints current node's data followed by " <-> "
- **Line 10:** Moves `temp` to the next node

---

#### **Iteration 1: temp at Node 10**

**Line 8:** `while temp:` → temp is not None → **TRUE**

```
         temp
          ▼
    ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→ ...
    │  ←   │    │  →   │
    └──────┴────┴──────┘

Condition: TRUE (enter loop)
```

**Line 9:** Print current node's data
```
print(temp.data, end=" <-> ")
→ Prints: "10 <-> "
```

**Console Output So Far:**
```
Doubly Linked List:
10 <-> 
```

**Line 10:** Move to next node
```
temp = temp.next  (temp now points to node 20)
```

**Diagram After Iteration 1:**
```
    self.head
        │
        ▼
    ┌──────┬────┬──────┐          temp
    │ NULL │ 10 │  ●───┼────→     ▼
    │  ←   │    │  →   │     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    └──────┴────┴──────┘     │  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
                             │  ←   │    │  →   │     │  ←   │    │  →   │
                             └──────┴────┴──────┘     └──────┴────┴──────┘

Back to Line 8
```

---

#### **Iteration 2: temp at Node 20**

**Line 8:** `while temp:` → temp is not None → **TRUE**

```
         temp
          ▼
    ┌──────┬────┬──────┐
    │  ●───┼─20 │  ●───┼────→ ...
    │  ←   │    │  →   │
    └──────┴────┴──────┘
```

**Line 9:** Print current node's data
```
print(temp.data, end=" <-> ")
→ Prints: "20 <-> "
```

**Console Output So Far:**
```
Doubly Linked List:
10 <-> 20 <-> 
```

**Line 10:** Move to next node
```
temp = temp.next  (temp now points to node 30)
```

---

#### **Iteration 3: temp at Node 30**

**Line 8:** `while temp:` → temp is not None → **TRUE**

```
         temp
          ▼
    ┌──────┬────┬──────┐
    │  ●───┼─30 │ NULL │
    │  ←   │    │  →   │
    └──────┴────┴──────┘
```

**Line 9:** Print current node's data
```
print(temp.data, end=" <-> ")
→ Prints: "30 <-> "
```

**Console Output So Far:**
```
Doubly Linked List:
10 <-> 20 <-> 30 <-> 
```

**Line 10:** Move to next node
```
temp = temp.next  (temp becomes None)
```

**Diagram After Iteration 3:**
```
    ┌──────┬────┬──────┐
    │  ●───┼─30 │ NULL │
    │  ←   │    │  →   │
    └──────┴────┴──────┘
                    │
                    └──→ temp = None

Back to Line 8
```

---

#### **Loop Exit Condition**

**Line 8:** `while temp:` → temp is None → **FALSE** → **Exit Loop**

```
temp = None

Condition: FALSE → Exit loop, go to Line 11
```

---

### **LINE 11: Print End Marker**

```python
print("NULL")
```

**What it does:**
- Prints "NULL" to indicate end of list
- Completes the display

**Final Console Output:**
```
┌─────────────────────────────────────┐
│ Doubly Linked List:                 │
│ 10 <-> 20 <-> 30 <-> NULL           │
└─────────────────────────────────────┘
```

---

## Display Method Flow Diagram

```
START display()
      │
      ▼
Is list empty? ──YES──→ Print "empty" → END
      │
      NO
      ▼
Print "Doubly Linked List:"
      │
      ▼
temp = self.head
      │
      ▼
┌─────────────────┐
│  While temp?    │
└─────────────────┘
      │
      ├──YES──→ Print temp.data + " <-> "
      │              │
      │              ▼
      │         temp = temp.next
      │              │
      │←─────────────┘
      │
      NO
      ▼
Print "NULL"
      │
      ▼
     END
```

---

# PART 2: SEARCH METHOD

## Complete Code with Line Numbers

```python
def search(self, key):                      # Line 1
    temp = self.head                        # Line 2
    position = 1                            # Line 3
                                            # Line 4 (blank)
    while temp:                             # Line 5
        if temp.data == key:                # Line 6
            print(key, "found at position", position)  # Line 7
            return                          # Line 8
        temp = temp.next                    # Line 9
        position += 1                       # Line 10
                                            # Line 11 (blank)
    print(key, "not found in the list")     # Line 12
```

---

## Example: Search for Value 20

```
Search for: 20
List: 10 ⇄ 20 ⇄ 30
```

---

## Line-by-Line Execution: SEARCH

---

### **LINE 1: Function Definition**

```python
def search(self, key):
```

**What it does:**
- Defines the `search` method
- Takes `key` parameter (the value to search for)
- In our case: `key = 20`

```
Function Called: search(20)
                    │
                    └─── key = 20 (searching for this value)
```

---

### **LINE 2: Initialize Traversal Pointer**

```python
temp = self.head
```

**What it does:**
- Creates `temp` pointer starting at first node
- Will traverse the list to find `key`

**Diagram:**
```
    self.head
    temp (both pointing here)
        │
        ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘

temp = first node
```

---

### **LINE 3: Initialize Position Counter**

```python
position = 1
```

**What it does:**
- Creates a counter to track node position
- Starts at 1 (first node is position 1)

```
Variables:
temp = first node (10)
position = 1
key = 20 (searching for)
```

---

### **LINE 5-10: While Loop - Search Through List**

```python
while temp:                             # Line 5
    if temp.data == key:                # Line 6
        print(key, "found at position", position)  # Line 7
        return                          # Line 8
    temp = temp.next                    # Line 9
    position += 1                       # Line 10
```

---

#### **Iteration 1: temp at Node 10, position = 1**

**Line 5:** `while temp:` → temp is not None → **TRUE**

```
         temp
          ▼
    ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→ ...
    └──────┴────┴──────┘

position = 1
```

**Line 6:** Check if current node matches
```
if temp.data == key:
→ if 10 == 20:
→ FALSE
```

**Skip lines 7-8, execute lines 9-10:**

**Line 9:** Move to next node
```
temp = temp.next  (temp now points to node 20)
```

**Line 10:** Increment position
```
position += 1  (position now = 2)
```

**State After Iteration 1:**
```
         temp
          ▼
    ┌──────┬────┬──────┐
    │  ●───┼─20 │  ●───┼────→ ...
    └──────┴────┴──────┘

position = 2
Back to Line 5
```

---

#### **Iteration 2: temp at Node 20, position = 2**

**Line 5:** `while temp:` → temp is not None → **TRUE**

```
         temp
          ▼
    ┌──────┬────┬──────┐
    │  ●───┼─20 │  ●───┼────→ ...
    └──────┴────┴──────┘

position = 2
key = 20
```

**Line 6:** Check if current node matches
```
if temp.data == key:
→ if 20 == 20:
→ TRUE ✓
```

**Execute lines 7-8:**

**Line 7:** Print success message
```
print(key, "found at position", position)
→ Prints: "20 found at position 2"
```

**Console Output:**
```
┌─────────────────────────────────────┐
│ 20 found at position 2              │
└─────────────────────────────────────┘
```

**Line 8:** Exit function
```
return
```

**Function ends. Lines 9-12 NOT executed.**

---

## Search Method: Value NOT Found Example

Let's search for **50** (which doesn't exist):

```
Search for: 50
List: 10 ⇄ 20 ⇄ 30
```

### Execution Flow

**Iteration 1:** temp at 10, position 1
- Check: `10 == 50?` → FALSE
- Move: temp → node 20, position → 2

**Iteration 2:** temp at 20, position 2
- Check: `20 == 50?` → FALSE
- Move: temp → node 30, position → 3

**Iteration 3:** temp at 30, position 3
- Check: `30 == 50?` → FALSE
- Move: temp → None, position → 4

**Line 5:** `while temp:` → temp is None → **FALSE** → Exit Loop

**Line 12:** Print not found message
```
print(key, "not found in the list")
→ Prints: "50 not found in the list"
```

**Console Output:**
```
┌─────────────────────────────────────┐
│ 50 not found in the list            │
└─────────────────────────────────────┘
```

---

## Search Method Flow Diagram

```
START search(key)
      │
      ▼
temp = self.head
position = 1
      │
      ▼
┌─────────────────┐
│  While temp?    │
└─────────────────┘
      │
      ├──YES──→ Is temp.data == key?
      │              │
      │              ├──YES──→ Print "found at position" → RETURN → END
      │              │
      │              NO
      │              │
      │              ▼
      │         temp = temp.next
      │         position += 1
      │              │
      │←─────────────┘
      │
      NO
      ▼
Print "not found"
      │
      ▼
     END
```

---

# PART 3: COUNT NODES METHOD

## Complete Code with Line Numbers

```python
def count_nodes(self):                      # Line 1
    count = 0                               # Line 2
    temp = self.head                        # Line 3
                                            # Line 4 (blank)
    while temp:                             # Line 5
        count += 1                          # Line 6
        temp = temp.next                    # Line 7
                                            # Line 8 (blank)
    print("Total number of nodes:", count)  # Line 9
    return count                            # Line 10
```

---

## Line-by-Line Execution: COUNT NODES

Using our list: **10 ⇄ 20 ⇄ 30** (3 nodes)

---

### **LINE 1: Function Definition**

```python
def count_nodes(self):
```

**What it does:**
- Defines the `count_nodes` method
- No additional parameters needed

---

### **LINE 2: Initialize Counter**

```python
count = 0
```

**What it does:**
- Creates a counter variable starting at 0
- Will increment for each node found

```
count = 0
```

---

### **LINE 3: Initialize Traversal Pointer**

```python
temp = self.head
```

**What it does:**
- Creates `temp` pointer starting at first node

**Diagram:**
```
    self.head
    temp (both pointing here)
        │
        ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘

count = 0
temp = first node
```

---

### **LINE 5-7: While Loop - Count Each Node**

```python
while temp:                             # Line 5
    count += 1                          # Line 6
    temp = temp.next                    # Line 7
```

---

#### **Iteration 1: temp at Node 10**

**Line 5:** `while temp:` → temp is not None → **TRUE**

```
         temp
          ▼
    ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→ ...
    └──────┴────┴──────┘

count = 0
```

**Line 6:** Increment counter
```
count += 1  (count becomes 1)
```

**Line 7:** Move to next node
```
temp = temp.next  (temp points to node 20)
```

**State After Iteration 1:**
```
         temp
          ▼
    ┌──────┬────┬──────┐
    │  ●───┼─20 │  ●───┼────→ ...
    └──────┴────┴──────┘

count = 1
```

---

#### **Iteration 2: temp at Node 20**

**Line 5:** `while temp:` → TRUE

**Line 6:** `count += 1` → count = 2

**Line 7:** `temp = temp.next` → temp points to node 30

**State After Iteration 2:**
```
         temp
          ▼
    ┌──────┬────┬──────┐
    │  ●───┼─30 │ NULL │
    └──────┴────┴──────┘

count = 2
```

---

#### **Iteration 3: temp at Node 30**

**Line 5:** `while temp:` → TRUE

**Line 6:** `count += 1` → count = 3

**Line 7:** `temp = temp.next` → temp = None

**State After Iteration 3:**
```
temp = None

count = 3
```

---

#### **Loop Exit**

**Line 5:** `while temp:` → temp is None → **FALSE** → Exit Loop

---

### **LINE 9: Print Result**

```python
print("Total number of nodes:", count)
```

**What it does:**
- Prints the total count of nodes

**Console Output:**
```
┌─────────────────────────────────────┐
│ Total number of nodes: 3            │
└─────────────────────────────────────┘
```

---

### **LINE 10: Return Count**

```python
return count
```

**What it does:**
- Returns the count value (3)
- Allows the caller to use the count in other operations

```
Function returns: 3
```

---

## Count Nodes Visual Progression

```
START: count = 0, temp = node 10

Step 1:
    ┌──────┐
    │  10  │ ← temp
    └──────┘
    count = 0 → 1

Step 2:
    ┌──────┐
    │  20  │ ← temp
    └──────┘
    count = 1 → 2

Step 3:
    ┌──────┐
    │  30  │ ← temp
    └──────┘
    count = 2 → 3

Step 4:
    temp = None
    count = 3 (FINAL)

Output: "Total number of nodes: 3"
Return: 3
```

---

## Count Nodes Flow Diagram

```
START count_nodes()
      │
      ▼
count = 0
temp = self.head
      │
      ▼
┌─────────────────┐
│  While temp?    │
└─────────────────┘
      │
      ├──YES──→ count += 1
      │              │
      │              ▼
      │         temp = temp.next
      │              │
      │←─────────────┘
      │
      NO
      ▼
Print "Total number of nodes: count"
      │
      ▼
Return count
      │
      ▼
     END
```

---

## Summary Table: All Three Methods

| Method | Purpose | Time Complexity | Space Complexity | Returns |
|--------|---------|-----------------|------------------|---------|
| **display()** | Show all nodes | O(n) | O(1) | None (void) |
| **search(key)** | Find node with value | O(n) | O(1) | None (void) |
| **count_nodes()** | Count total nodes | O(n) | O(1) | int (count) |

---

## Comparison Table

| Feature | Display | Search | Count |
|---------|---------|--------|-------|
| **Traversal** | Yes (all nodes) | Yes (until found) | Yes (all nodes) |
| **Extra Variable** | None | `position` | `count` |
| **Early Exit** | No | Yes (when found) | No |
| **Output** | Visual list | Found/Not found | Total count |
| **Best Case** | O(n) | O(1) | O(n) |
| **Worst Case** | O(n) | O(n) | O(n) |

---

## Complete Visual Flow for Empty List

All three methods handle empty lists:

### Display (Empty List)
```
self.head = None
      │
      ▼
Is head None? → YES
      │
      ▼
Print "Doubly Linked List is empty"
      │
      ▼
     END
```

### Search (Empty List)
```
self.head = None
temp = None
      │
      ▼
While temp? → FALSE (skip loop)
      │
      ▼
Print "key not found in the list"
      │
      ▼
     END
```

### Count Nodes (Empty List)
```
self.head = None
count = 0
temp = None
      │
      ▼
While temp? → FALSE (skip loop)
      │
      ▼
Print "Total number of nodes: 0"
      │
      ▼
Return 0
```

---
---
# Line-by-Line Explanation: Delete Operations in Doubly Linked List

Let me explain all three delete methods with detailed diagrams.

---

# PART 1: DELETE FROM BEGINNING

## Complete Code with Line Numbers

```python
def delete_beginning(self):                 # Line 1
    if self.head is None:                   # Line 2
        print("List is empty")              # Line 3
        return                              # Line 4
                                            # Line 5 (blank)
    print(self.head.data, "deleted from beginning")  # Line 6
    self.head = self.head.next              # Line 7
                                            # Line 8 (blank)
    if self.head:                           # Line 9
        self.head.prev = None               # Line 10
```

---

## Example Scenario

Delete first node from the list: **10 ⇄ 20 ⇄ 30**

### Initial State of List

```
       self.head
           │
           ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘
        ▲                         │                         │
        └─────────────────────────┘                         │
                                  └─────────────────────────┘

Goal: Delete node 10 (first node)
Expected Result: 20 ⇄ 30
```

---

## Line-by-Line Execution: DELETE BEGINNING

---

### **LINE 1: Function Definition**

```python
def delete_beginning(self):
```

**What it does:**
- Defines the `delete_beginning` method
- No additional parameters needed (always deletes first node)

---

### **LINE 2: Check if List is Empty**

```python
if self.head is None:
```

**What it does:**
- Checks if the list has any nodes to delete
- `self.head is None` means list is empty, nothing to delete

**Truth Table:**

| Condition | List State | Result | Action |
|-----------|------------|--------|--------|
| `self.head is None` | Empty | TRUE | Execute lines 3-4, exit |
| `self.head is None` | Has nodes | FALSE | Skip to line 6 |

**In Our Case:** List has nodes → **FALSE** → Skip lines 3-4

```
    self.head (is NOT None)
        │
        ▼
    ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→ ...
    └──────┴────┴──────┘

Condition: FALSE → Skip to line 6
```

---

### **LINES 3-4: Handle Empty List (SKIPPED)**

```python
print("List is empty")                  # Line 3
return                                  # Line 4
```

**What it does:**
- Only executed if list is empty
- Prints message and exits

**If list was empty:**
```
Console Output:
┌─────────────────────────────────────┐
│ List is empty                       │
└─────────────────────────────────────┘
```

---

### **LINE 6: Print Deletion Message**

```python
print(self.head.data, "deleted from beginning")
```

**What it does:**
- Prints the value being deleted (node 10)
- Happens BEFORE actual deletion (so we can access the data)

**Console Output:**
```
┌─────────────────────────────────────┐
│ 10 deleted from beginning           │
└─────────────────────────────────────┘
```

**Diagram:** (No change yet)
```
       self.head
           │
           ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘

Message printed, now perform deletion
```

---

### **LINE 7: Move HEAD to Next Node**

```python
self.head = self.head.next
```

**What it does:**
- Updates `self.head` to point to the **second node** (node 20)
- Effectively "removes" the first node from the list
- **Critical:** The old first node (10) is now unreachable from `self.head`

**Visual Explanation:**

**BEFORE Line 7:**
```
       self.head
           │
           ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘
                                  ▲
                                  │
                         self.head.next (node 20)
```

**AFTER Line 7:**
```
                             self.head (moved here!)
                                  │
                                  ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘
        ▲                         │
        │                         │
        └─── Still points back to deleted node (Problem!)
             Need to fix this!
```

**Memory State:**
- ✅ `self.head` now points to node 20
- ❌ Node 20's `prev` still points to old node 10 (dangling pointer)
- ❌ Need to update node 20's `prev` to NULL

---

### **LINE 9: Check if New HEAD Exists**

```python
if self.head:
```

**What it does:**
- Checks if there's still a head node after deletion
- Important for handling deletion of the **only node** in the list

**Why This Check?**
```
Case 1: List had multiple nodes (10 ⇄ 20 ⇄ 30)
→ After deletion: self.head points to node 20 (NOT None)
→ Condition: TRUE → Execute line 10

Case 2: List had only one node (10)
→ After deletion: self.head becomes None
→ Condition: FALSE → Skip line 10 (nothing to fix)
```

**In Our Case:** `self.head` points to node 20 → **TRUE** → Execute line 10

---

### **LINE 10: Fix New HEAD's Previous Pointer**

```python
self.head.prev = None
```

**What it does:**
- Sets the new first node's `prev` pointer to `None`
- Removes the backward link to the deleted node
- Completes the deletion process

**Visual Explanation:**

**BEFORE Line 10:**
```
                             self.head
                                  │
                                  ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘
        ▲                         │
        └─────────────────────────┘
        Dangling pointer (BAD!)
```

**AFTER Line 10:**
```
                             self.head
                                  │
                                  ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│ NULL │ 20 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘
    (Unreachable)                 ▲                         │
    Will be garbage               │                         │
    collected                     └─────────────────────────┘
```

**Memory State:**
- ✅ **Deletion Complete!**
- ✅ Node 20 is now the first node with `prev = None`
- ✅ Old node 10 is unreachable and will be garbage collected
- List is now: **20 ⇄ 30**

---

## Final Result

```
       self.head
           │
           ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 20 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘
        ▲                         │
        └─────────────────────────┘

List: 20 ⇄ 30
Node 10 deleted successfully
```

---

## Special Case: Delete Only Node

What if the list has only **one node** (10)?

### Initial State
```
       self.head
           │
           ▼
    ┌──────┬────┬──────┐
    │ NULL │ 10 │ NULL │
    │  ←   │    │  →   │
    └──────┴────┴──────┘

List: 10
```

### Execution

**Line 6:** Print "10 deleted from beginning"

**Line 7:** `self.head = self.head.next`
```
self.head.next is None
→ self.head = None
```

**Line 9:** `if self.head:`
```
self.head is None → FALSE
Skip line 10 (nothing to fix)
```

### Result
```
self.head = None

List is now empty
```

---

## Delete Beginning Flow Diagram

```
START delete_beginning()
      │
      ▼
Is list empty? ──YES──→ Print "List is empty" → END
      │
      NO
      ▼
Print "data deleted from beginning"
      │
      ▼
self.head = self.head.next
      │
      ▼
Is new head exists? ──YES──→ self.head.prev = None
      │                              │
      NO                             │
      │                              │
      └──────────────────────────────┘
      │
      ▼
     END
```

---

# PART 2: DELETE FROM END

## Complete Code with Line Numbers

```python
def delete_end(self):                       # Line 1
    if self.head is None:                   # Line 2
        print("List is empty")              # Line 3
        return                              # Line 4
                                            # Line 5 (blank)
    if self.head.next is None:              # Line 6
        print(self.head.data, "deleted from end")  # Line 7
        self.head = None                    # Line 8
        return                              # Line 9
                                            # Line 10 (blank)
    temp = self.head                        # Line 11
    while temp.next:                        # Line 12
        temp = temp.next                    # Line 13
                                            # Line 14 (blank)
    print(temp.data, "deleted from end")    # Line 15
    temp.prev.next = None                   # Line 16
```

---

## Example Scenario

Delete last node from the list: **10 ⇄ 20 ⇄ 30**

### Initial State of List

```
       self.head
           │
           ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘
        ▲                         │                         │
        └─────────────────────────┘                         │
                                  └─────────────────────────┘

Goal: Delete node 30 (last node)
Expected Result: 10 ⇄ 20
```

---

## Line-by-Line Execution: DELETE END

---

### **LINE 1: Function Definition**

```python
def delete_end(self):
```

**What it does:**
- Defines the `delete_end` method
- Deletes the last node from the list

---

### **LINE 2-4: Check if List is Empty**

```python
if self.head is None:                   # Line 2
    print("List is empty")              # Line 3
    return                              # Line 4
```

**What it does:**
- Same as delete_beginning: checks if list has nodes

**In Our Case:** List has nodes → **FALSE** → Skip to line 6

---

### **LINE 6: Check if Only One Node Exists**

```python
if self.head.next is None:
```

**What it does:**
- Checks if the list has **only one node**
- `self.head.next is None` means there's no second node
- Special case: Deleting the only node is different from deleting last of many

**Why This Check?**
```
Case 1: List has one node (10)
→ self.head.next is None → TRUE
→ Execute lines 7-9 (special handling)

Case 2: List has multiple nodes (10 ⇄ 20 ⇄ 30)
→ self.head.next points to node 20 → FALSE
→ Skip to line 11 (normal deletion)
```

**In Our Case:** `self.head.next` points to node 20 → **FALSE** → Skip to line 11

```
       self.head
           │
           ▼
    ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→ [Node 20] (exists)
    │  ←   │    │  →   │
    └──────┴────┴──────┘

Condition: self.head.next is None → FALSE
Skip lines 7-9, go to line 11
```

---

### **LINES 7-9: Handle Single Node Case (SKIPPED)**

```python
print(self.head.data, "deleted from end")  # Line 7
self.head = None                           # Line 8
return                                     # Line 9
```

**What it does:**
- Only executed if list has exactly one node
- Sets `self.head = None` (list becomes empty)

**Example (if list was just 10):**
```
BEFORE:
    ┌──────┬────┬──────┐
    │ NULL │ 10 │ NULL │
    └──────┴────┴──────┘

AFTER:
self.head = None
List is empty
```

---

### **LINE 11: Initialize Traversal Pointer**

```python
temp = self.head
```

**What it does:**
- Creates `temp` pointer to traverse to the last node
- Starts at the first node

**Diagram:**
```
    self.head
    temp (both pointing here)
        │
        ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘

temp = first node (need to move to last)
```

---

### **LINE 12-13: While Loop - Find Last Node**

```python
while temp.next:                        # Line 12
    temp = temp.next                    # Line 13
```

**What it does:**
- Traverses to the **last node** (where `next` is `None`)
- Similar to insert_end traversal

---

#### **Iteration 1: temp at Node 10**

**Line 12:** `while temp.next:`
```
temp.next points to node 20 → NOT None → TRUE
```

**Line 13:** Move forward
```
temp = temp.next  (temp now points to node 20)
```

**Diagram:**
```
         temp
          ▼
    ┌──────┬────┬──────┐
    │  ●───┼─20 │  ●───┼────→ [Node 30]
    │  ←   │    │  →   │
    └──────┴────┴──────┘

Back to Line 12
```

---

#### **Iteration 2: temp at Node 20**

**Line 12:** `while temp.next:`
```
temp.next points to node 30 → NOT None → TRUE
```

**Line 13:** Move forward
```
temp = temp.next  (temp now points to node 30)
```

**Diagram:**
```
         temp
          ▼
    ┌──────┬────┬──────┐
    │  ●───┼─30 │ NULL │
    │  ←   │    │  →   │
    └──────┴────┴──────┘

Back to Line 12
```

---

#### **Loop Exit: temp at Node 30 (Last Node)**

**Line 12:** `while temp.next:`
```
temp.next is None → FALSE → Exit loop
```

**Diagram:**
```
                                         temp (at last node)
                                          ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘
                                                            ▲
                                                            └─── temp.next is None
                                                                 (last node found!)
```

---

### **LINE 15: Print Deletion Message**

```python
print(temp.data, "deleted from end")
```

**What it does:**
- Prints the value being deleted (30)

**Console Output:**
```
┌─────────────────────────────────────┐
│ 30 deleted from end                 │
└─────────────────────────────────────┘
```

---

### **LINE 16: Remove Last Node**

```python
temp.prev.next = None
```

**What it does:**
- Makes the **second-to-last node** point to `None` instead of the last node
- `temp.prev` is node 20 (previous node)
- `temp.prev.next` is node 20's next pointer
- Set it to `None` to disconnect the last node

**Visual Explanation:**

**BEFORE Line 16:**
```
                                         temp
                                          ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘
                                  ▲           │
                                  │           └──→ Points to node 30
                                  │                Need to change to None
                                  └─── temp.prev (node 20)
```

**AFTER Line 16:**
```
       self.head
           │
           ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │ NULL │     │  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘
        ▲                         │                    (Unreachable)
        └─────────────────────────┘                    Will be garbage
                                                       collected
        temp.prev.next = None
```

**Memory State:**
- ✅ **Deletion Complete!**
- ✅ Node 20 is now the last node with `next = None`
- ✅ Old node 30 is unreachable and will be garbage collected
- List is now: **10 ⇄ 20**

---

## Final Result

```
       self.head
           │
           ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘
        ▲                         │
        └─────────────────────────┘

List: 10 ⇄ 20
Node 30 deleted successfully
```

---

## Delete End Flow Diagram

```
START delete_end()
      │
      ▼
Is list empty? ──YES──→ Print "List is empty" → END
      │
      NO
      ▼
Is only one node? ──YES──→ Print data → self.head = None → END
      │
      NO
      ▼
temp = self.head
      │
      ▼
┌─────────────────┐
│ While temp.next?│
└─────────────────┘
      │
      ├──YES──→ temp = temp.next ──┐
      │                            │
      │←───────────────────────────┘
      │
      NO (found last node)
      ▼
Print "temp.data deleted from end"
      │
      ▼
temp.prev.next = None
      │
      ▼
     END
```

---

# PART 3: DELETE A GIVEN ELEMENT

## Complete Code with Line Numbers

```python
def delete_element(self, key):              # Line 1
    temp = self.head                        # Line 2
                                            # Line 3 (blank)
    while temp:                             # Line 4
        if temp.data == key:                # Line 5
                                            # Line 6 (blank)
            if temp.prev:                   # Line 7
                temp.prev.next = temp.next  # Line 8
            else:                           # Line 9
                self.head = temp.next       # Line 10 (deleting head)
                                            # Line 11 (blank)
            if temp.next:                   # Line 12
                temp.next.prev = temp.prev  # Line 13
                                            # Line 14 (blank)
            print(key, "deleted from the list")  # Line 15
            return                          # Line 16
                                            # Line 17 (blank)
        temp = temp.next                    # Line 18
                                            # Line 19 (blank)
    print(key, "not found")                 # Line 20
```

---

## Example Scenario

Delete node with value **20** from the list: **10 ⇄ 20 ⇄ 30**

### Initial State of List

```
       self.head
           │
           ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘
        ▲                         │                         │
        └─────────────────────────┘                         │
                                  └─────────────────────────┘

Goal: Delete node 20 (middle node)
Expected Result: 10 ⇄ 30
```

---

## Line-by-Line Execution: DELETE ELEMENT

---

### **LINE 1: Function Definition**

```python
def delete_element(self, key):
```

**What it does:**
- Defines the method to delete a specific element
- `key`: The value to search for and delete (20 in our case)

```
Function Called: delete_element(20)
                      │
                      └─── key = 20 (search and delete this)
```

---

### **LINE 2: Initialize Traversal Pointer**

```python
temp = self.head
```

**What it does:**
- Creates `temp` pointer to search through the list

**Diagram:**
```
    self.head
    temp (both pointing here)
        │
        ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │  ●───┼────→│  ●───┼─30 │ NULL │
    └──────┴────┴──────┘     └──────┴────┴──────┘     └──────┴────┴──────┘

temp = first node, key = 20
```

---

### **LINE 4-18: While Loop - Search and Delete**

```python
while temp:                             # Line 4
    if temp.data == key:                # Line 5
        # deletion logic (lines 7-16)
    temp = temp.next                    # Line 18
```

---

#### **Iteration 1: temp at Node 10**

**Line 4:** `while temp:` → temp is not None → **TRUE**

**Line 5:** Check if matches
```
if temp.data == key:
→ if 10 == 20:
→ FALSE
```

**Skip deletion logic, go to line 18**

**Line 18:** Move to next
```
temp = temp.next  (temp now points to node 20)
```

---

#### **Iteration 2: temp at Node 20**

**Line 4:** `while temp:` → TRUE

**Line 5:** Check if matches
```
         temp
          ▼
    ┌──────┬────┬──────┐
    │  ●───┼─20 │  ●───┼────→ ...
    └──────┴────┴──────┘

if temp.data == key:
→ if 20 == 20:
→ TRUE ✓ (FOUND! Execute deletion logic)
```

---

### **LINE 7: Check if Node Has Previous Node**

```python
if temp.prev:
```

**What it does:**
- Checks if the node to delete is **NOT the first node**
- `temp.prev` exists means there's a node before it

**Why This Check?**
```
Case 1: Deleting middle/last node (temp has prev)
→ temp.prev is NOT None → TRUE
→ Execute line 8 (normal deletion)

Case 2: Deleting first node (head)
→ temp.prev is None → FALSE
→ Execute line 10 (special head deletion)
```

**In Our Case:** Node 20 has prev (node 10) → **TRUE** → Execute line 8

```
         temp
          ▼
    ┌──────┬────┬──────┐
    │  ●───┼─20 │  ●───┼────→ ...
    │  ←   │    │  →   │
    └──────┴────┴──────┘
        ▲
        │
        └─── temp.prev exists (node 10)

Condition: TRUE → Execute line 8
```

---

### **LINE 8: Bypass the Node (Forward Connection)**

```python
temp.prev.next = temp.next
```

**What it does:**
- Makes the **previous node** point to the **next node**, skipping current node
- `temp.prev` is node 10
- `temp.next` is node 30
- Connect node 10 directly to node 30

**Visual Explanation:**

**BEFORE Line 8:**
```
                          temp
                           ▼
    ┌──────┬────┬──────┐ ┌──────┬────┬──────┐ ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼→│  ●───┼─20 │  ●───┼→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │ │  ←   │    │  →   │ │  ←   │    │  →   │
    └──────┴────┴──────┘ └──────┴────┴──────┘ └──────┴────┴──────┘
         │                                   │
         └──→ temp.prev     temp.next ←──────┘
```

**AFTER Line 8:**
```
                          temp
                           ▼
    ┌──────┬────┬──────┐ ┌──────┬────┬──────┐ ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼─┼──────┼─20 │  ●───┼→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │ │  ←   │    │  →   │ │  ←   │    │  →   │
    └──────┴────┴──────┘ └──────┴────┴──────┘ └──────┴────┴──────┘
         │               └──────────────────────────┘│
         └───────────────────┐                       │
                             ▼                       │
                      temp.prev.next = temp.next     │
                      (Node 10 now points to Node 30)│
                                                     │
                                    Node 30 still points back to Node 20!
                                    Need to fix this next
```

**Memory State:**
- ✅ Forward link fixed: Node 10 → Node 30
- ❌ Backward link not fixed yet: Node 30 still points back to Node 20

---

### **LINES 9-10: Handle Head Deletion (SKIPPED)**

```python
else:                               # Line 9
    self.head = temp.next           # Line 10
```

**What it does:**
- Only executed if deleting the **first node** (when `temp.prev` is None)
- Updates `self.head` to point to the second node

**Example (if deleting node 10):**
```
Deleting first node (10):
→ temp.prev is None → Execute line 10
→ self.head = temp.next (points to node 20)
→ Node 20 becomes new head
```

---

### **LINE 12: Check if Node Has Next Node**

```python
if temp.next:
```

**What it does:**
- Checks if the node to delete is **NOT the last node**
- `temp.next` exists means there's a node after it

**Why This Check?**
```
Case 1: Deleting first/middle node (temp has next)
→ temp.next is NOT None → TRUE
→ Execute line 13 (fix backward link)

Case 2: Deleting last node
→ temp.next is None → FALSE
→ Skip line 13 (no next node to fix)
```

**In Our Case:** Node 20 has next (node 30) → **TRUE** → Execute line 13

```
         temp
          ▼
    ┌──────┬────┬──────┐
    │  ●───┼─20 │  ●───┼────→ [Node 30]
    └──────┴────┴──────┘
                    │
                    └─── temp.next exists

Condition: TRUE → Execute line 13
```

---

### **LINE 13: Fix Backward Connection**

```python
temp.next.prev = temp.prev
```

**What it does:**
- Makes the **next node** point backward to the **previous node**, skipping current node
- `temp.next` is node 30
- `temp.prev` is node 10
- Connect node 30 back to node 10

**Visual Explanation:**

**BEFORE Line 13:**
```
                          temp
                           ▼
    ┌──────┬────┬──────┐ ┌──────┬────┬──────┐ ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼─┼──────┼─20 │  ●───┼→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │ │  ←   │    │  →   │ │  ←   │    │  →   │
    └──────┴────┴──────┘ └──────┴────┴──────┘ └──────┴────┴──────┘
         │               └──────────────────────────┘│
         └───────────────────┐                       │
                             ▼                       ▲
                      (Forward link fixed)           │
                                                     │
                                    Node 30 still points to Node 20
```

**AFTER Line 13:**
```
       self.head
           │
           ▼
    ┌──────┬────┬──────┐ ┌──────┬────┬──────┐ ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼─┼──────┼─20 │  ●───┼→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │ │  ←   │    │  →   │ │  ←   │    │  →   │
    └──────┴────┴──────┘ └──────┴────┴──────┘ └──────┴────┴──────┘
         ▲              (Unreachable)              │
         │              Will be garbage            │
         │              collected                  │
         └──────────────────────────────────────────┘
         
         temp.next.prev = temp.prev
         (Node 30 now points back to Node 10)
```

**Memory State:**
- ✅ **Both connections fixed!**
- ✅ Node 10 ⇄ Node 30 are now directly connected
- ✅ Node 20 is completely disconnected and unreachable
- List is now: **10 ⇄ 30**

---

### **LINE 15: Print Success Message**

```python
print(key, "deleted from the list")
```

**Console Output:**
```
┌─────────────────────────────────────┐
│ 20 deleted from the list            │
└─────────────────────────────────────┘
```

---

### **LINE 16: Exit Function**

```python
return
```

**What it does:**
- Exits the function immediately
- No need to continue searching (already found and deleted)
- Line 18 and 20 will NOT execute

---

## Final Result

```
       self.head
           │
           ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘
        ▲                         │
        └─────────────────────────┘

List: 10 ⇄ 30
Node 20 deleted successfully
```

---

## Special Cases for Delete Element

### **Case 1: Delete First Node (Head)**

Deleting **10** from **10 ⇄ 20 ⇄ 30**

**Line 7:** `if temp.prev:` → temp.prev is None → **FALSE**

**Line 10:** Execute `self.head = temp.next`
```
self.head now points to node 20
```

**Line 12:** `if temp.next:` → TRUE

**Line 13:** `temp.next.prev = temp.prev`
```
node 20.prev = None
```

**Result:**
```
       self.head
           │
           ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 20 │  ●───┼────→│  ●───┼─30 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘

List: 20 ⇄ 30
```

---

### **Case 2: Delete Last Node**

Deleting **30** from **10 ⇄ 20 ⇄ 30**

**Line 7:** `if temp.prev:` → TRUE (node 20 exists)

**Line 8:** `temp.prev.next = temp.next`
```
node 20.next = None
```

**Line 12:** `if temp.next:` → temp.next is None → **FALSE**

**Skip line 13** (no next node to fix)

**Result:**
```
       self.head
           │
           ▼
    ┌──────┬────┬──────┐     ┌──────┬────┬──────┐
    │ NULL │ 10 │  ●───┼────→│  ●───┼─20 │ NULL │
    │  ←   │    │  →   │     │  ←   │    │  →   │
    └──────┴────┴──────┘     └──────┴────┴──────┘

List: 10 ⇄ 20
```

---

### **Case 3: Value Not Found**

Deleting **50** from **10 ⇄ 20 ⇄ 30**

**Iterations:**
- Check node 10: `10 == 50?` → FALSE → Move next
- Check node 20: `20 == 50?` → FALSE → Move next
- Check node 30: `30 == 50?` → FALSE → Move next
- temp becomes None → Exit loop

**Line 20:** `print(key, "not found")`

**Console Output:**
```
┌─────────────────────────────────────┐
│ 50 not found                        │
└─────────────────────────────────────┘
```

---

## Delete Element Flow Diagram

```
START delete_element(key)
      │
      ▼
temp = self.head
      │
      ▼
┌─────────────────┐
│  While temp?    │
└─────────────────┘
      │
      ├──YES──→ Is temp.data == key?
      │              │
      │              ├──NO──→ temp = temp.next ──┐
      │              │                           │
      │              │←──────────────────────────┘
      │              │
      │              YES (FOUND!)
      │              │
      │              ▼
      │         Has prev? ──YES──→ temp.prev.next = temp.next
      │              │                      │
      │              NO                     │
      │              │                      │
      │              ▼                      │
      │         self.head = temp.next       │
      │              │                      │
      │              └──────────────────────┘
      │                       │
      │                       ▼
      │              Has next? ──YES──→ temp.next.prev = temp.prev
      │                       │                 │
      │                       NO                │
      │                       │                 │
      │                       └─────────────────┘
      │                                │
      │                                ▼
      │                       Print "deleted"
      │                                │
      │                                ▼
      │                             RETURN → END
      │
      NO (temp is None)
      │
      ▼
Print "not found"
      │
      ▼
     END
```

---

## Summary Table: All Delete Operations

| Operation | Time Complexity | Special Handling | Pointers Updated |
|-----------|----------------|------------------|------------------|
| **Delete Beginning** | O(1) | Empty list, Single node | HEAD, new first.prev |
| **Delete End** | O(n) | Empty list, Single node | last.prev.next |
| **Delete Element** | O(n) | First node, Last node, Not found | prev.next, next.prev (or HEAD) |

---

## Key Deletion Concepts

### **Two Critical Connections to Fix:**

```
When deleting node B from: A ⇄ B ⇄ C

1. Forward Connection: A.next = C  (skip B forward)
2. Backward Connection: C.prev = A (skip B backward)

Result: A ⇄ C (B is unreachable)
```

### **Edge Cases Always Check:**

1. **Empty List:** `self.head is None`
2. **Single Node:** `self.head.next is None`
3. **First Node:** `temp.prev is None` → Update HEAD
4. **Last Node:** `temp.next is None` → Don't fix next.prev
5. **Not Found:** Loop completes without finding

---
