# Complete Line-by-Line Explanation: Circular Linked List

I'll explain each method with detailed diagrams.

---

# PART 1: INSERT AT BEGINNING

## Complete Code with Line Numbers

```python
def insert_beginning(self, value):          # Line 1
    new_node = Node(value)                  # Line 2
                                            # Line 3 (blank)
    if self.head is None:                   # Line 4
        self.head = new_node                # Line 5
        new_node.next = self.head           # Line 6
        print(value, "inserted as first node")  # Line 7
        return                              # Line 8
                                            # Line 9 (blank)
    temp = self.head                        # Line 10
    while temp.next != self.head:           # Line 11
        temp = temp.next                    # Line 12
                                            # Line 13 (blank)
    new_node.next = self.head               # Line 14
    temp.next = new_node                    # Line 15
    self.head = new_node                    # Line 16
                                            # Line 17 (blank)
    print(value, "inserted at beginning")   # Line 18
```

---

## Example Scenario 1: Insert into Empty List

Insert value **5** into an empty list.

### Initial State
```
self.head = None
(No nodes exist)
```

---

## Line-by-Line Execution (Empty List)

---

### **LINE 1: Function Definition**

```python
def insert_beginning(self, value):
```

**Function Called:** `insert_beginning(5)`

---

### **LINE 2: Create New Node**

```python
new_node = Node(value)
```

**Creates new node:**
```
                   new_node
                      │
                      ▼
                  ┌────┬────┐
                  │ 5  │NULL│
                  └────┴────┘

self.head = None
```

---

### **LINE 4: Check if List is Empty**

```python
if self.head is None:
```

**What it does:**
- Checks if this is the first node

**In This Case:** `self.head is None` → **TRUE** → Execute lines 5-8

---

### **LINE 5: Set HEAD to New Node**

```python
self.head = new_node
```

**After Line 5:**
```
       self.head
           │
           ▼
       ┌────┬────┐
       │ 5  │NULL│
       └────┴────┘
```

---

### **LINE 6: Make it Circular (Point to Itself)**

```python
new_node.next = self.head
```

**What it does:**
- Makes the single node point to itself
- Creates circular structure

**Visual Explanation:**

**BEFORE Line 6:**
```
       self.head
           │
           ▼
       ┌────┬────┐
       │ 5  │NULL│
       └────┴────┘
```

**AFTER Line 6:**
```
       self.head
           │
           ▼
       ┌────┬────┐
       │ 5  │ ●──┼──┐
       │    │ →  │  │
       └────┴────┘  │
            ▲       │
            └───────┘
       (Points to itself - CIRCULAR!)
```

**Memory State:**
- ✅ Node 5 points to itself
- ✅ Circular structure created
- ✅ List: 5 → (back to 5)

---

### **LINE 7-8: Print and Exit**

```python
print(value, "inserted as first node")  # Line 7
return                                  # Line 8
```

**Output:**
```
5 inserted as first node
```

**Function exits** - Lines 10-18 NOT executed

---

## Final State (First Node)

```
       self.head
           │
           ▼
       ┌────┬────┐
       │ 5  │ ●──┼──┐
       │    │ →  │  │
       └────┴────┘  │
            ▲       │
            └───────┘

List: 5 → (back to 5)
```

---

## Example Scenario 2: Insert into Non-Empty List

Now insert **10** at the beginning of: **5 → (back to 5)**

### Initial State

```
       self.head
           │
           ▼
       ┌────┬────┐
       │ 5  │ ●──┼──┐
       │    │ →  │  │
       └────┴────┘  │
            ▲       │
            └───────┘

Goal: Insert 10 at beginning
Expected: 10 → 5 → (back to 10)
```

---

## Line-by-Line Execution (Non-Empty List)

---

### **LINE 2: Create New Node**

```python
new_node = Node(value)
```

```
                   new_node
                      │
                      ▼
                  ┌────┬────┐
                  │ 10 │NULL│
                  └────┴────┘
```

---

### **LINE 4: Check if Empty**

```python
if self.head is None:
```

**In This Case:** `self.head` points to node 5 → **FALSE** → Skip to line 10

---

### **LINE 10: Initialize Traversal**

```python
temp = self.head
```

**Diagram:**
```
    self.head
    temp
        │
        ▼
    ┌────┬────┐
    │ 5  │ ●──┼──┐
    │    │ →  │  │
    └────┴────┘  │
         ▲       │
         └───────┘
```

---

### **LINE 11-12: Find Last Node**

```python
while temp.next != self.head:           # Line 11
    temp = temp.next                    # Line 12
```

**What it does:**
- Finds the last node (whose `next` points back to `head`)

**In This Case:**
```
temp = node 5
temp.next = node 5 (self.head)
temp.next != self.head → 5 != 5 → FALSE

Exit loop immediately (already at last node)
```

**After Loop:**
```
    self.head
        │
        ▼
    ┌────┬────┐ ← temp (last node)
    │ 5  │ ●──┼──┐
    │    │ →  │  │
    └────┴────┘  │
         ▲       │
         └───────┘
```

---

### **LINE 14: Connect New Node to Current Head**

```python
new_node.next = self.head
```

**Visual Explanation:**

**BEFORE Line 14:**
```
                   new_node
                      │
                      ▼
                  ┌────┬────┐
                  │ 10 │NULL│
                  └────┴────┘
```

**AFTER Line 14:**
```
                   new_node
                      │
                      ▼
                  ┌────┬────┐
                  │ 10 │ ●──┼────┐
                  │    │ →  │    │
                  └────┴────┘    │
                                 │ new_node.next = self.head
       self.head                 │
           │                     │
           ▼                     │
       ┌────┬────┐               │
       │ 5  │ ●──┼──┐            │
       │    │ →  │  │            │
       └────┴────┘  │            │
            ▲       │            │
            └───────┘            │
                                 ▼
                            [Points to node 5]
```

---

### **LINE 15: Update Last Node to Point to New Node**

```python
temp.next = new_node
```

**What it does:**
- Makes the last node (5) point to the new node (10)
- Maintains circular structure

**Visual Explanation:**

**BEFORE Line 15:**
```
       ┌────┬────┐
       │ 5  │ ●──┼──┐
       └────┴────┘  │
            ▲       │
            └───────┘
         Points to itself
```

**AFTER Line 15:**
```
                   new_node
                      │
                      ▼
                  ┌────┬────┐
                  │ 10 │ ●──┼────┐
                  │    │ →  │    │
                  └────┴────┘    │
                       ▲         │
                       │         │
       self.head       │         │
           │           │         ▼
           ▼           │     ┌────┬────┐
       ┌────┬────┐    └─────┤ 5  │ ●──┼──┐
       │ 5  │ ●──┼──────────→    │ →  │  │
       │    │ →  │          └────┴────┘  │
       └────┴────┘               ▲  temp │
            │                    │        │
            └────────────────────┘        │
                                          └──→ Points to new_node (10)
```

---

### **LINE 16: Update HEAD to New Node**

```python
self.head = new_node
```

**What it does:**
- Makes new node (10) the official first node

**Visual Explanation:**

**BEFORE Line 16:**
```
       self.head (still at node 5)
           │
           ▼
       [Node 5]
```

**AFTER Line 16:**
```
                   self.head (moved here!)
                      │
                      ▼
                  ┌────┬────┐
                  │ 10 │ ●──┼────┐
                  │    │ →  │    │
                  └────┴────┘    │
                       ▲         │
                       │         ▼
                       │     ┌────┬────┐
                       └─────┤ 5  │ ●──┼──┐
                             │    │ →  │  │
                             └────┴────┘  │
                                  ▲       │
                                  └───────┘
```

**Memory State:**
- ✅ **Insertion Complete!**
- ✅ HEAD points to new node (10)
- ✅ Circular structure maintained: 10 → 5 → (back to 10)

---

### **LINE 18: Print Confirmation**

```python
print(value, "inserted at beginning")
```

**Output:**
```
10 inserted at beginning
```

---

## Final State (After Inserting 10)

```
       self.head
           │
           ▼
       ┌────┬────┐
       │ 10 │ ●──┼────┐
       │    │ →  │    │
       └────┴────┘    │
            ▲         │
            │         ▼
            │     ┌────┬────┐
            └─────┤ 5  │ ●──┼──┐
                  │    │ →  │  │
                  └────┴────┘  │
                       ▲       │
                       └───────┘

List: 10 → 5 → (back to 10)
```

---

# PART 2: INSERT AT END

## Complete Code with Line Numbers

```python
def insert_end(self, value):                # Line 1
    new_node = Node(value)                  # Line 2
                                            # Line 3 (blank)
    if self.head is None:                   # Line 4
        self.head = new_node                # Line 5
        new_node.next = self.head           # Line 6
        print(value, "inserted as first node")  # Line 7
        return                              # Line 8
                                            # Line 9 (blank)
    temp = self.head                        # Line 10
    while temp.next != self.head:           # Line 11
        temp = temp.next                    # Line 12
                                            # Line 13 (blank)
    temp.next = new_node                    # Line 14
    new_node.next = self.head               # Line 15
                                            # Line 16 (blank)
    print(value, "inserted at end")         # Line 17
```

---

## Example Scenario

Insert **20** at the end of: **10 → 5 → (back to 10)**

### Initial State

```
       self.head
           │
           ▼
       ┌────┬────┐
       │ 10 │ ●──┼────┐
       │    │ →  │    │
       └────┴────┘    │
            ▲         │
            │         ▼
            │     ┌────┬────┐
            └─────┤ 5  │ ●──┼──┐
                  │    │ →  │  │
                  └────┴────┘  │
                       ▲       │
                       └───────┘

Goal: Insert 20 at end
Expected: 10 → 5 → 20 → (back to 10)
```

---

## Line-by-Line Execution

---

### **LINES 2-8: Create Node & Handle Empty List**

Same as insert_beginning - handles empty list case.

**In Our Case:** List has nodes → Skip to line 10

---

### **LINES 10-12: Find Last Node**

```python
temp = self.head                        # Line 10
while temp.next != self.head:           # Line 11
    temp = temp.next                    # Line 12
```

**Process:**

**Start:** temp at node 10
```
         temp
          ▼
    ┌────┬────┐
    │ 10 │ ●──┼────→ [Node 5]
    └────┴────┘

temp.next = node 5
temp.next != self.head → 5 != 10 → TRUE (continue)
```

**Move:** temp to node 5
```
         temp
          ▼
    ┌────┬────┐
    │ 5  │ ●──┼────→ [Node 10 - head]
    └────┴────┘

temp.next = node 10 (self.head)
temp.next != self.head → 10 != 10 → FALSE (EXIT)
```

**After Loop:**
```
    self.head
        │
        ▼
    ┌────┬────┐     ┌────┬────┐ ← temp (last node)
    │ 10 │ ●──┼────→│ 5  │ ●──┼──┐
    │    │ →  │     │    │ →  │  │
    └────┴────┘     └────┴────┘  │
         ▲                        │
         └────────────────────────┘
```

---

### **LINE 14: Connect Last Node to New Node**

```python
temp.next = new_node
```

**Visual Explanation:**

**BEFORE Line 14:**
```
                                    new_node
                                       │
                                       ▼
                                   ┌────┬────┐
                                   │ 20 │NULL│
                                   └────┴────┘


                                    temp
                                     ▼
                                ┌────┬────┐
                                │ 5  │ ●──┼──┐
                                └────┴────┘  │
                                     ▲       │
                                     └───────┘
                                Points to head (10)
```

**AFTER Line 14:**
```
                                    new_node
                                       │
                                       ▼
                                   ┌────┬────┐
                                   │ 20 │NULL│
                                   └────┴────┘
                                        ▲
                                        │
                                        │ temp.next = new_node
    ┌────┬────┐     ┌────┬────┐        │
    │ 10 │ ●──┼────→│ 5  │ ●──┼────────┘
    │    │ →  │     │    │ →  │
    └────┴────┘     └────┴────┘
                         ▲  temp
```

---

### **LINE 15: Complete the Circle**

```python
new_node.next = self.head
```

**What it does:**
- Makes new node point back to HEAD
- Completes circular structure

**Visual Explanation:**

**BEFORE Line 15:**
```
                   ┌────┬────┐
                   │ 20 │NULL│ ← Still NULL!
                   └────┴────┘
```

**AFTER Line 15:**
```
       self.head
           │
           ▼
       ┌────┬────┐
       │ 10 │ ●──┼────┐
       │    │ →  │    │
       └────┴────┘    │
            ▲         │
            │         ▼
            │     ┌────┬────┐     ┌────┬────┐
            │     │ 5  │ ●──┼────→│ 20 │ ●──┼──┐
            │     │    │ →  │     │    │ →  │  │
            │     └────┴────┘     └────┴────┘  │
            │                          ▲        │
            └──────────────────────────┘        │
                                                │
                                new_node.next = self.head
                                (Circle complete!)
```

**Memory State:**
- ✅ **Insertion Complete!**
- ✅ Circular structure maintained
- ✅ List: 10 → 5 → 20 → (back to 10)

---

### **LINE 17: Print Confirmation**

```python
print(value, "inserted at end")
```

**Output:**
```
20 inserted at end
```

---

## Final State

```
       self.head
           │
           ▼
       ┌────┬────┐
       │ 10 │ ●──┼────┐
       │    │ →  │    │
       └────┴────┘    │
            ▲         │
            │         ▼
            │     ┌────┬────┐     ┌────┬────┐
            │     │ 5  │ ●──┼────→│ 20 │ ●──┼──┐
            │     │    │ →  │     │    │ →  │  │
            │     └────┴────┘     └────┴────┘  │
            │                          ▲        │
            └──────────────────────────┘        │
                                                └──→ back to head

List: 10 → 5 → 20 → (back to 10)
```

---

# PART 3: INSERT AFTER A GIVEN VALUE

## Complete Code with Line Numbers

```python
def insert_after(self, prev_value, value):  # Line 1
    if self.head is None:                   # Line 2
        print("List is empty")              # Line 3
        return                              # Line 4
                                            # Line 5 (blank)
    temp = self.head                        # Line 6
    while True:                             # Line 7
        if temp.data == prev_value:         # Line 8
            new_node = Node(value)          # Line 9
            new_node.next = temp.next       # Line 10
            temp.next = new_node            # Line 11
            print(value, "inserted after", prev_value)  # Line 12
            return                          # Line 13
                                            # Line 14 (blank)
        temp = temp.next                    # Line 15
        if temp == self.head:               # Line 16
            break                           # Line 17
                                            # Line 18 (blank)
    print(prev_value, "not found")          # Line 19
```

---

## Example Scenario

Insert **25** after **20** in: **10 → 5 → 20 → (back to 10)**

### Initial State

```
       self.head
           │
           ▼
       ┌────┬────┐
       │ 10 │ ●──┼────┐
       │    │ →  │    │
       └────┴────┘    │
            ▲         │
            │         ▼
            │     ┌────┬────┐     ┌────┬────┐
            │     │ 5  │ ●──┼────→│ 20 │ ●──┼──┐
            │     │    │ →  │     │    │ →  │  │
            │     └────┴────┘     └────┴────┘  │
            │                          ▲        │
            └──────────────────────────┘        │
                                                └──→

Goal: Insert 25 after 20
Expected: 10 → 5 → 20 → 25 → (back to 10)
```

---

## Line-by-Line Execution

---

### **LINES 2-4: Check Empty List**

```python
if self.head is None:
```

**In Our Case:** FALSE → Skip

---

### **LINE 6: Initialize Traversal**

```python
temp = self.head
```

```
    self.head
    temp
        │
        ▼
    ┌────┬────┐
    │ 10 │ ●──┼────→ ...
    └────┴────┘

Searching for value 20...
```

---

### **LINES 7-17: While Loop - Search and Insert**

```python
while True:                             # Line 7
    if temp.data == prev_value:         # Line 8
        # insertion logic
    temp = temp.next                    # Line 15
    if temp == self.head:               # Line 16
        break                           # Line 17
```

**Iteration 1:** temp at node 10
- Check: 10 == 20? NO
- Move to node 5
- Check: 5 == head? NO, continue

**Iteration 2:** temp at node 5
- Check: 5 == 20? NO
- Move to node 20
- Check: 20 == head? NO, continue

**Iteration 3:** temp at node 20
- Check: 20 == 20? **YES** ✓
- Execute insertion (lines 9-13)

---

### **LINE 9: Create New Node**

```python
new_node = Node(value)
```

```
                   new_node
                      │
                      ▼
                  ┌────┬────┐
                  │ 25 │NULL│
                  └────┴────┘
```

---

### **LINE 10: Connect New Node Forward**

```python
new_node.next = temp.next
```

**Visual Explanation:**

**BEFORE Line 10:**
```
                   new_node
                      │
                      ▼
                  ┌────┬────┐
                  │ 25 │NULL│
                  └────┴────┘


                   temp
                    ▼
    ... ────→ ┌────┬────┐
              │ 20 │ ●──┼────→ [Node 10 - head]
              └────┴────┘
```

**AFTER Line 10:**
```
                   new_node
                      │
                      ▼
                  ┌────┬────┐
                  │ 25 │ ●──┼────┐
                  │    │ →  │    │
                  └────┴────┘    │
                                 │ new_node.next = temp.next
                   temp          │
                    ▼            │
    ... ────→ ┌────┬────┐       │
              │ 20 │ ●──┼───────┼──→ [Node 10]
              │    │ →  │       │
              └────┴────┘       │
                   │            │
                   └────────────┘
                Both point to node 10 (head)
```

---

### **LINE 11: Connect Previous Node to New Node**

```python
temp.next = new_node
```

**Visual Explanation:**

**AFTER Line 11:**
```
       self.head
           │
           ▼
       ┌────┬────┐
       │ 10 │ ●──┼────┐
       │    │ →  │    │
       └────┴────┘    │
            ▲         │
            │         ▼
            │     ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
            │     │ 5  │ ●──┼────→│ 20 │ ●──┼────→│ 25 │ ●──┼──┐
            │     │    │ →  │     │    │ →  │     │    │ →  │  │
            │     └────┴────┘     └────┴────┘     └────┴────┘  │
            │                                          ▲        │
            └──────────────────────────────────────────┘        │
                                                                └──→

temp.next = new_node (Insertion complete!)
```

**Memory State:**
- ✅ **Insertion Complete!**
- ✅ Node 20 → 25 → 10 (head)
- ✅ Circular structure maintained

---

### **LINES 12-13: Print and Exit**

```python
print(value, "inserted after", prev_value)  # Line 12
return                                      # Line 13
```

**Output:**
```
25 inserted after 20
```

---

## Final State

```
       self.head
           │
           ▼
       ┌────┬────┐
       │ 10 │ ●──┼────┐
       │    │ →  │    │
       └────┴────┘    │
            ▲         │
            │         ▼
            │     ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
            │     │ 5  │ ●──┼────→│ 20 │ ●──┼────→│ 25 │ ●──┼──┐
            │     │    │ →  │     │    │ →  │     │    │ →  │  │
            │     └────┴────┘     └────┴────┘     └────┴────┘  │
            │                                          ▲        │
            └──────────────────────────────────────────┘        │
                                                                └──→

List: 10 → 5 → 20 → 25 → (back to 10)
```

---

# PART 4: DISPLAY METHOD

## Complete Code with Line Numbers

```python
def display(self):                          # Line 1
    if self.head is None:                   # Line 2
        print("Circular Linked List is empty")  # Line 3
        return                              # Line 4
                                            # Line 5 (blank)
    temp = self.head                        # Line 6
    print("Circular Linked List:")          # Line 7
                                            # Line 8 (blank)
    while True:                             # Line 9
        print(temp.data, end=" -> ")        # Line 10
        temp = temp.next                    # Line 11
        if temp == self.head:               # Line 12
            break                           # Line 13
                                            # Line 14 (blank)
    print("(back to head)")                 # Line 15
```

---

## Example: Display List 10 → 5 → 20

---

### **LINES 2-4: Check Empty**

Skip if list has nodes

---

### **LINE 6-7: Initialize & Print Header**

```python
temp = self.head
print("Circular Linked List:")
```

**Output:**
```
Circular Linked List:
```

---

### **LINES 9-13: Traverse and Print**

```python
while True:                             # Line 9
    print(temp.data, end=" -> ")        # Line 10
    temp = temp.next                    # Line 11
    if temp == self.head:               # Line 12
        break                           # Line 13
```

**Iteration 1:** temp at 10
- Print "10 -> "
- Move to node 5
- Check: 5 == head? NO, continue

**Iteration 2:** temp at 5
- Print "5 -> "
- Move to node 20
- Check: 20 == head? NO, continue

**Iteration 3:** temp at 20
- Print "20 -> "
- Move to node 10 (back to head!)
- Check: 10 == head? YES, **break**

**Output so far:**
```
Circular Linked List:
10 -> 5 -> 20 -> 
```

---

### **LINE 15: Print Completion**

```python
print("(back to head)")
```

**Final Output:**
```
Circular Linked List:
10 -> 5 -> 20 -> (back to head)
```

---

# PART 5: SEARCH METHOD

## Complete Code with Line Numbers

```python
def search(self, key):                      # Line 1
    if self.head is None:                   # Line 2
        print("List is empty")              # Line 3
        return                              # Line 4
                                            # Line 5 (blank)
    temp = self.head                        # Line 6
    while True:                             # Line 7
        if temp.data == key:                # Line 8
            print(key, "found in circular linked list")  # Line 9
            return                          # Line 10
        temp = temp.next                    # Line 11
        if temp == self.head:               # Line 12
            break                           # Line 13
                                            # Line 14 (blank)
    print(key, "not found")                 # Line 15
```

---

## Example: Search for 25

**Execution:**

**Initialize:** temp = head (node 10)

**Iteration 1:** temp at 10
- Check: 10 == 25? NO
- Move to node 5

**Iteration 2:** temp at 5
- Check: 5 == 25? NO
- Move to node 20

**Iteration 3:** temp at 20
- Check: 20 == 25? NO
- Move to node 25

**Iteration 4:** temp at 25
- Check: 25 == 25? **YES** ✓
- Print "25 found in circular linked list"
- Return (exit)

**Output:**
```
25 found in circular linked list
```

---

# PART 6: COUNT NODES METHOD

## Complete Code with Line Numbers

```python
def count_nodes(self):                      # Line 1
    if self.head is None:                   # Line 2
        print("Total nodes: 0")             # Line 3
        return                              # Line 4
                                            # Line 5 (blank)
    count = 0                               # Line 6
    temp = self.head                        # Line 7
    while True:                             # Line 8
        count += 1                          # Line 9
        temp = temp.next                    # Line 10
        if temp == self.head:               # Line 11
            break                           # Line 12
                                            # Line 13 (blank)
    print("Total number of nodes:", count)  # Line 14
```

---

## Example: Count nodes in 10 → 5 → 20 → 25

**Execution:**

**LINE 6:** count = 0
**LINE 7:** temp = head

**Iteration 1:** temp at 10
- count = 1
- Move to node 5
- Check: 5 == head? NO

**Iteration 2:** temp at 5
- count = 2
- Move to node 20
- Check: 20 == head? NO

**Iteration 3:** temp at 20
- count = 3
- Move to node 25
- Check: 25 == head? NO

**Iteration 4:** temp at 25
- count = 4
- Move to node 10 (head)
- Check: 10 == head? YES, **break**

**Output:**
```
Total number of nodes: 4
```

---

# PART 7: DELETE FROM BEGINNING

## Complete Code with Line Numbers

```python
def delete_beginning(self):                 # Line 1
    if self.head is None:                   # Line 2
        print("List is empty")              # Line 3
        return                              # Line 4
                                            # Line 5 (blank)
    if self.head.next == self.head:         # Line 6
        print(self.head.data, "deleted (only node)")  # Line 7
        self.head = None                    # Line 8
        return                              # Line 9
                                            # Line 10 (blank)
    temp = self.head                        # Line 11
    while temp.next != self.head:           # Line 12
        temp = temp.next                    # Line 13
                                            # Line 14 (blank)
    print(self.head.data, "deleted from beginning")  # Line 15
    temp.next = self.head.next              # Line 16
    self.head = self.head.next              # Line 17
```

---

## Example Scenario

Delete first node from: **10 → 5 → 20 → 25 → (back to 10)**

### Initial State

```
       self.head
           │
           ▼
       ┌────┬────┐
       │ 10 │ ●──┼────┐
       │    │ →  │    │
       └────┴────┘    │
            ▲         │
            │         ▼
            │     ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
            │     │ 5  │ ●──┼────→│ 20 │ ●──┼────→│ 25 │ ●──┼──┐
            │     │    │ →  │     │    │ →  │     │    │ →  │  │
            │     └────┴────┘     └────┴────┘     └────┴────┘  │
            │                                          ▲        │
            └──────────────────────────────────────────┘        │
                                                                └──→

Goal: Delete node 10
Expected: 5 → 20 → 25 → (back to 5)
```

---

## Line-by-Line Execution

---

### **LINES 2-4: Check Empty List**

Skip if list has nodes

---

### **LINE 6: Check Single Node**

```python
if self.head.next == self.head:
```

**What it does:**
- Checks if only one node exists
- Single node points to itself

**In Our Case:**
```
self.head.next = node 5 (NOT self)
→ FALSE
Skip lines 7-9
```

---

### **LINES 11-13: Find Last Node**

```python
temp = self.head                        # Line 11
while temp.next != self.head:           # Line 12
    temp = temp.next                    # Line 13
```

**Process:**
- Start at node 10
- Move through: 10 → 5 → 20 → 25
- Stop when temp.next == head

**After Loop:**
```
    self.head
        │
        ▼
    ┌────┬────┐     ...     ┌────┬────┐ ← temp (last node)
    │ 10 │ ●──┼────→  ...   │ 25 │ ●──┼──┐
    │    │ →  │             │    │ →  │  │
    └────┴────┘             └────┴────┘  │
         ▲                       ▲        │
         └───────────────────────┘        │
                                          └──→ Points back to head
```

---

### **LINE 15: Print Deletion Message**

```python
print(self.head.data, "deleted from beginning")
```

**Output:**
```
10 deleted from beginning
```

---

### **LINE 16: Update Last Node to Point to Second Node**

```python
temp.next = self.head.next
```

**What it does:**
- Makes last node (25) point to second node (5) instead of first

**Visual Explanation:**

**BEFORE Line 16:**
```
    self.head
        │
        ▼
    ┌────┬────┐     ┌────┬────┐
    │ 10 │ ●──┼────→│ 5  │ ...
    │    │ →  │     │    │
    └────┴────┘     └────┴────┘
         ▲              ▲
         │              │
         │              └─── self.head.next
         │
    ┌────┬────┐
    │ 25 │ ●──┼──┐
    └────┴────┘  │
         ▲  temp │
         └───────┘
      Currently points to node 10
```

**AFTER Line 16:**
```
    self.head
        │
        ▼
    ┌────┬────┐     ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
    │ 10 │ ●──┼────→│ 5  │ ●──┼────→│ 20 │ ●──┼────→│ 25 │ ●──┼──┐
    │    │ →  │     │    │ →  │     │    │ →  │     │    │ →  │  │
    └────┴────┘     └────┴────┘     └────┴────┘     └────┴────┘  │
   (Will be              ▲                               ▲        │
   unreachable)          └───────────────────────────────┘        │
                                                                  └──→
                         temp.next = self.head.next
                         (Last now points to node 5)
```

---

### **LINE 17: Update HEAD**

```python
self.head = self.head.next
```

**What it does:**
- Moves HEAD to the second node (5)

**Visual Explanation:**

**AFTER Line 17:**
```
                   self.head (moved here!)
                        │
                        ▼
    ┌────┬────┐     ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
    │ 10 │ ●──┼────→│ 5  │ ●──┼────→│ 20 │ ●──┼────→│ 25 │ ●──┼──┐
    │    │ →  │     │    │ →  │     │    │ →  │     │    │ →  │  │
    └────┴────┘     └────┴────┘     └────┴────┘     └────┴────┘  │
   (Unreachable)         ▲                               ▲        │
   Will be garbage       └───────────────────────────────┘        │
   collected                                                      └──→
```

**Memory State:**
- ✅ **Deletion Complete!**
- ✅ HEAD points to node 5
- ✅ Circular structure maintained: 5 → 20 → 25 → (back to 5)

---

## Final State

```
       self.head
           │
           ▼
       ┌────┬────┐
       │ 5  │ ●──┼────┐
       │    │ →  │    │
       └────┴────┘    │
            ▲         │
            │         ▼
            │     ┌────┬────┐     ┌────┬────┐
            │     │ 20 │ ●──┼────→│ 25 │ ●──┼──┐
            │     │    │ →  │     │    │ →  │  │
            │     └────┴────┘     └────┴────┘  │
            │                          ▲        │
            └──────────────────────────┘        │
                                                └──→

List: 5 → 20 → 25 → (back to 5)
```

---

# PART 8: DELETE FROM END

## Complete Code with Line Numbers

```python
def delete_end(self):                       # Line 1
    if self.head is None:                   # Line 2
        print("List is empty")              # Line 3
        return                              # Line 4
                                            # Line 5 (blank)
    if self.head.next == self.head:         # Line 6
        print(self.head.data, "deleted (only node)")  # Line 7
        self.head = None                    # Line 8
        return                              # Line 9
                                            # Line 10 (blank)
    temp = self.head                        # Line 11
    prev = None                             # Line 12
                                            # Line 13 (blank)
    while temp.next != self.head:           # Line 14
        prev = temp                         # Line 15
        temp = temp.next                    # Line 16
                                            # Line 17 (blank)
    print(temp.data, "deleted from end")    # Line 18
    prev.next = self.head                   # Line 19
```

---

## Example Scenario

Delete last node from: **5 → 20 → 25 → (back to 5)**

### Initial State

```
       self.head
           │
           ▼
       ┌────┬────┐
       │ 5  │ ●──┼────┐
       │    │ →  │    │
       └────┴────┘    │
            ▲         │
            │         ▼
            │     ┌────┬────┐     ┌────┬────┐
            │     │ 20 │ ●──┼────→│ 25 │ ●──┼──┐
            │     │    │ →  │     │    │ →  │  │
            │     └────┴────┘     └────┴────┘  │
            │                          ▲        │
            └──────────────────────────┘        │
                                                └──→

Goal: Delete node 25 (last node)
Expected: 5 → 20 → (back to 5)
```

---

## Line-by-Line Execution

---

### **LINES 2-9: Check Empty & Single Node**

Skip if list has multiple nodes

---

### **LINES 11-12: Initialize Pointers**

```python
temp = self.head                        # Line 11
prev = None                             # Line 12
```

**What it does:**
- `temp`: Traverses to find last node
- `prev`: Tracks the second-to-last node

---

### **LINES 14-16: Find Last Node**

```python
while temp.next != self.head:           # Line 14
    prev = temp                         # Line 15
    temp = temp.next                    # Line 16
```

**Iteration 1:** temp at 5, prev = None
```
prev = None    temp
                ▼
            ┌────┬────┐
            │ 5  │ ●──┼────→ [Node 20]
            └────┴────┘

temp.next != self.head → 20 != 5 → TRUE

Update: prev = temp (node 5)
        temp = temp.next (node 20)
```

**Iteration 2:** temp at 20, prev = 5
```
         prev     temp
          ▼        ▼
    ┌────┬────┐ ┌────┬────┐
    │ 5  │ ●──┼→│ 20 │ ●──┼────→ [Node 25]
    └────┴────┘ └────┴────┘

temp.next != self.head → 25 != 5 → TRUE

Update: prev = temp (node 20)
        temp = temp.next (node 25)
```

**Iteration 3:** temp at 25, prev = 20
```
                   prev     temp
                    ▼        ▼
    ... ────→ ┌────┬────┐ ┌────┬────┐
              │ 20 │ ●──┼→│ 25 │ ●──┼──┐
              └────┴────┘ └────┴────┘  │
                               ▲       │
                               └───────┘
                          Points to head (5)

temp.next != self.head → 5 != 5 → FALSE (EXIT)
```

**After Loop:**
```
    self.head
        │
        ▼
    ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
    │ 5  │ ●──┼────→│ 20 │ ●──┼────→│ 25 │ ●──┼──┐
    │    │ →  │     │    │ →  │     │    │ →  │  │
    └────┴────┘     └────┴────┘     └────┴────┘  │
                         ▲  prev          ▲  temp │
                         │                │        │
                         │                └────────┘
                         └── Second-to-last    Last node
```

---

### **LINE 18: Print Deletion Message**

```python
print(temp.data, "deleted from end")
```

**Output:**
```
25 deleted from end
```

---

### **LINE 19: Remove Last Node**

```python
prev.next = self.head
```

**What it does:**
- Makes second-to-last node (20) point back to HEAD (5)
- Bypasses and removes last node (25)

**Visual Explanation:**

**BEFORE Line 19:**
```
                   prev     temp
                    ▼        ▼
              ┌────┬────┐ ┌────┬────┐
              │ 20 │ ●──┼→│ 25 │ ●──┼──→ back to head
              └────┴────┘ └────┴────┘
```

**AFTER Line 19:**
```
       self.head
           │
           ▼
       ┌────┬────┐
       │ 5  │ ●──┼────┐
       │    │ →  │    │
       └────┴────┘    │
            ▲         │
            │         ▼
            │     ┌────┬────┐     ┌────┬────┐
            │     │ 20 │ ●──┼──┐  │ 25 │ ●──┼──┐
            │     │    │ →  │  │  │    │ →  │  │
            │     └────┴────┘  │  └────┴────┘  │
            │          ▲  prev  │  (Unreachable)│
            └──────────┘        │   Will be     │
                                │   garbage     │
                                │   collected   │
                                └──────────────→│
                                                └──→ (broken link)

prev.next = self.head (Circle restored!)
```

**Memory State:**
- ✅ **Deletion Complete!**
- ✅ Node 20 points back to HEAD (5)
- ✅ Circular structure maintained: 5 → 20 → (back to 5)

---

## Final State

```
       self.head
           │
           ▼
       ┌────┬────┐
       │ 5  │ ●──┼────┐
       │    │ →  │    │
       └────┴────┘    │
            ▲         │
            │         ▼
            │     ┌────┬────┐
            │     │ 20 │ ●──┼──┐
            │     │    │ →  │  │
            │     └────┴────┘  │
            │          ▲        │
            └──────────┘        │
                                └──→

List: 5 → 20 → (back to 5)
```

---

# PART 9: DELETE A GIVEN ELEMENT

## Complete Code with Line Numbers

```python
def delete_value(self, key):                # Line 1
    if self.head is None:                   # Line 2
        print("List is empty")              # Line 3
        return                              # Line 4
                                            # Line 5 (blank)
    temp = self.head                        # Line 6
    prev = None                             # Line 7
                                            # Line 8 (blank)
    while True:                             # Line 9
        if temp.data == key:                # Line 10
            if prev is None:                # Line 11
                # deleting head              # Line 12 (comment)
                self.delete_beginning()     # Line 13
            else:                           # Line 14
                prev.next = temp.next       # Line 15
                print(key, "deleted from circular linked list")  # Line 16
            return                          # Line 17
                                            # Line 18 (blank)
        prev = temp                         # Line 19
        temp = temp.next                    # Line 20
                                            # Line 21 (blank)
        if temp == self.head:               # Line 22
            break                           # Line 23
                                            # Line 24 (blank)
    print(key, "not found")                 # Line 25
```

---

## Example Scenario

Delete node with value **30** from the main program execution.

Let me trace through the **actual main program** to show the complete flow:

---

## Main Program Execution

```python
cll = CircularLinkedList()

cll.insert_beginning(5)     # List: 5 → (back to 5)
cll.insert_beginning(10)    # List: 10 → 5 → (back to 10)
cll.insert_end(20)          # List: 10 → 5 → 20 → (back to 10)
cll.insert_end(30)          # List: 10 → 5 → 20 → 30 → (back to 10)
cll.insert_end(40)          # List: 10 → 5 → 20 → 30 → 40 → (back to 10)
cll.insert_end(50)          # List: 10 → 5 → 20 → 30 → 40 → 50 → (back to 10)
cll.insert_after(20, 25)    # List: 10 → 5 → 20 → 25 → 30 → 40 → 50 → (back to 10)
```

### State Before delete_value(30)

```
       self.head
           │
           ▼
       ┌────┬────┐
       │ 10 │ ●──┼────┐
       │    │ →  │    │
       └────┴────┘    │
            ▲         │
            │         ▼
            │     ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
            │     │ 5  │ ●──┼────→│ 20 │ ●──┼────→│ 25 │ ●──┼────┐
            │     │    │ →  │     │    │ →  │     │    │ →  │    │
            │     └────┴────┘     └────┴────┘     └────┴────┘    │
            │                                                      │
            │                                                      ▼
            │     ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
            │     │ 50 │ ●──┼────→│ 40 │ ●──┼────→│ 30 │ ●──┼────┘
            │     │    │ →  │     │    │ →  │     │    │ →  │
            │     └────┴────┘     └────┴────┘     └────┴────┘
            │          ▲
            └──────────┘

Goal: Delete node 30
```

---

## Line-by-Line Execution: delete_value(30)

---

### **LINES 2-4: Check Empty**

Skip if list has nodes

---

### **LINES 6-7: Initialize Pointers**

```python
temp = self.head                        # Line 6
prev = None                             # Line 7
```

```
prev = None

    self.head
    temp
        │
        ▼
    ┌────┬────┐
    │ 10 │ ●──┼────→ ...
    └────┴────┘
```

---

### **LINES 9-23: While Loop - Search and Delete**

```python
while True:                             # Line 9
    if temp.data == key:                # Line 10
        # deletion logic
    prev = temp                         # Line 19
    temp = temp.next                    # Line 20
    if temp == self.head:               # Line 22
        break                           # Line 23
```

**Iterations:**

1. temp at 10: Check 10 == 30? NO → prev=10, temp=5
2. temp at 5: Check 5 == 30? NO → prev=5, temp=20
3. temp at 20: Check 20 == 30? NO → prev=20, temp=25
4. temp at 25: Check 25 == 30? NO → prev=25, temp=30
5. temp at 30: Check 30 == 30? **YES** ✓

---

### **At Node 30 (FOUND):**

```
                   prev     temp
                    ▼        ▼
    ... ────→ ┌────┬────┐ ┌────┬────┐
              │ 25 │ ●──┼→│ 30 │ ●──┼────→ [Node 40]
              └────┴────┘ └────┴────┘
```

---

### **LINE 11: Check if Deleting Head**

```python
if prev is None:
```

**In Our Case:**
```
prev = Node 25 (NOT None)
→ FALSE
Skip line 13, execute line 15
```

---

### **LINE 15: Bypass the Node**

```python
prev.next = temp.next
```

**What it does:**
- Makes node 25 point to node 40 (skipping node 30)

**Visual Explanation:**

**BEFORE Line 15:**
```
                   prev     temp
                    ▼        ▼
    ... ────→ ┌────┬────┐ ┌────┬────┐     ┌────┬────┐
              │ 25 │ ●──┼→│ 30 │ ●──┼────→│ 40 │ ...
              └────┴────┘ └────┴────┘     └────┴────┘
                   │                           ▲
                   │                           │
                   └──────→ temp.next ─────────┘
```

**AFTER Line 15:**
```
       self.head
           │
           ▼
       ┌────┬────┐
       │ 10 │ ●──┼────┐
       │    │ →  │    │
       └────┴────┘    │
            ▲         │
            │         ▼
            │     ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
            │     │ 5  │ ●──┼────→│ 20 │ ●──┼────→│ 25 │ ●──┼────┐
            │     │    │ →  │     │    │ →  │     │    │ →  │    │
            │     └────┴────┘     └────┴────┘     └────┴────┘    │
            │                                                      │
            │                                                      │
            │     ┌────┬────┐     ┌────┬────┐     ┌────┬────┐    │
            │     │ 50 │ ●──┼────→│ 40 │ ●──┼──┐  │ 30 │ ●──┼────┘
            │     │    │ →  │     │    │ →  │  │  │    │ →  │
            │     └────┴────┘     └────┴────┘  │  └────┴────┘
            │          ▲               ▲       │  (Unreachable)
            └──────────┘               └───────┘
                                       
                                prev.next = temp.next
```

**Memory State:**
- ✅ **Deletion Complete!**
- ✅ Node 25 directly points to node 40
- ✅ Circular structure maintained
- ✅ Node 30 unreachable

---

### **LINES 16-17: Print and Exit**

```python
print(key, "deleted from circular linked list")  # Line 16
return                                           # Line 17
```

**Output:**
```
30 deleted from circular linked list
```

---

## Final State After delete_value(30)

```
       self.head
           │
           ▼
       ┌────┬────┐
       │ 10 │ ●──┼────┐
       │    │ →  │    │
       └────┴────┘    │
            ▲         │
            │         ▼
            │     ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
            │     │ 5  │ ●──┼────→│ 20 │ ●──┼────→│ 25 │ ●──┼────┐
            │     │    │ →  │     │    │ →  │     │    │ →  │    │
            │     └────┴────┘     └────┴────┘     └────┴────┘    │
            │                                                      │
            │                                                      ▼
            │     ┌────┬────┐     ┌────┬────┐
            │     │ 50 │ ●──┼────→│ 40 │ ●──┼──────────────────────┘
            │     │    │ →  │     │    │ →  │
            │     └────┴────┘     └────┴────┘
            │          ▲
            └──────────┘

List: 10 → 5 → 20 → 25 → 40 → 50 → (back to 10)
```

---

## Special Case: Deleting Head Node

If we delete the **first node** (prev is None):

**LINE 11:** `if prev is None:` → **TRUE**

**LINE 13:** `self.delete_beginning()`
```
Calls the delete_beginning() method
(which we already explained in Part 7)
```

This reuses existing logic instead of duplicating code!

---

## Complete Main Program Output

```
5 inserted as first node
10 inserted at beginning
20 inserted at end
30 inserted at end
40 inserted at end
50 inserted at end
25 inserted after 20
Circular Linked List:
10 -> 5 -> 20 -> 25 -> 30 -> 40 -> 50 -> (back to head)
25 found in circular linked list
Total number of nodes: 7
10 deleted from beginning
Circular Linked List:
5 -> 20 -> 25 -> 30 -> 40 -> 50 -> (back to head)
Total number of nodes: 6
30 deleted from circular linked list
Circular Linked List:
5 -> 20 -> 25 -> 40 -> 50 -> (back to head)
Total number of nodes: 5
50 deleted from end
Circular Linked List:
5 -> 20 -> 25 -> 40 -> (back to head)
Total number of nodes: 4
```

---

## Summary: All Operations

### **Insertion Operations**

| Operation | Time | Key Pattern |
|-----------|------|-------------|
| **insert_beginning** | O(n) | Find last → Update last.next → Update head |
| **insert_end** | O(n) | Find last → Update last.next → Update new.next |
| **insert_after** | O(n) | Search → new.next = temp.next → temp.next = new |

### **Display & Search Operations**

| Operation | Time | Key Pattern |
|-----------|------|-------------|
| **display** | O(n) | while True: print → break when back to head |
| **search** | O(n) | while True: check → break when back to head |
| **count_nodes** | O(n) | while True: count++ → break when back to head |

### **Deletion Operations**

| Operation | Time | Key Pattern |
|-----------|------|-------------|
| **delete_beginning** | O(n) | Find last → Update last.next → Update head |
| **delete_end** | O(n) | Find second-to-last → Update prev.next |
| **delete_value** | O(n) | Search (track prev) → Update prev.next |

---

## Key Circular List Patterns

### **1. Check if Back at Head:**
```python
if temp == self.head:
    break
```

### **2. Find Last Node:**
```python
temp = self.head
while temp.next != self.head:
    temp = temp.next
# temp is now last node
```

### **3. Circular Traversal:**
```python
temp = self.head
while True:
    # Process temp
    temp = temp.next
    if temp == self.head:
        break
```

### **4. Single Node Check:**
```python
if self.head.next == self.head:
    # Only one node (points to itself)
```

### **5. Maintain Circular Structure:**
```python
# Always ensure last node points to head
last_node.next = self.head
```

---

## 🎉 Complete Circular Linked List Explained!

**Key Takeaways:**
- ✅ Last node always points back to HEAD (circular)
- ✅ Use `while True` with manual break for traversal
- ✅ Check `temp == self.head` to detect full circle
- ✅ Single node points to itself
- ✅ Always maintain circular structure in all operations
- ✅ No NULL pointers (every node points somewhere)

**Perfect for:**
- Round-robin scheduling
- Music playlists
- Game turn systems
- Circular buffers

**All operations fully explained with detailed diagrams! 🚀**