# Complete Line-by-Line Explanation: Singly Linked List

---

# PART 1: INSERT AT BEGINNING

## Complete Code with Line Numbers

```python
def insert_beginning(self, value):          # Line 1
    new_node = Node(value)                  # Line 2
    new_node.next = self.head               # Line 3
    self.head = new_node                    # Line 4
    print(value, "inserted at beginning")   # Line 5
```

---

## Example Scenario

Insert value **5** at the beginning of the list: **10 → 20 → 30 → NULL**

### Initial State of List

```
       self.head
           │
           ▼
    ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
    │ 10 │ ●──┼────→│ 20 │ ●──┼────→│ 30 │NULL│
    │    │ →  │     │    │ →  │     │    │ →  │
    └────┴────┘     └────┴────┘     └────┴────┘

Goal: Insert 5 at beginning
Expected Result: 5 → 10 → 20 → 30 → NULL
```

---

## Line-by-Line Execution

---

### **LINE 1: Function Definition**

```python
def insert_beginning(self, value):
```

**What it does:**
- Defines the method to insert a node at the beginning
- `value`: The data to insert (5 in our case)

```
Function Called: insert_beginning(5)
                      │
                      └─── value = 5
```

---

### **LINE 2: Create New Node**

```python
new_node = Node(value)
```

**What it does:**
- Creates a new node with `data = 5`
- The `Node` constructor sets:
  - `new_node.data = 5`
  - `new_node.next = None`

**Diagram AFTER Line 2:**

```
                   new_node
                      │
                      ▼
                  ┌────┬────┐
                  │ 5  │NULL│
                  │    │ →  │
                  └────┴────┘


       self.head
           │
           ▼
    ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
    │ 10 │ ●──┼────→│ 20 │ ●──┼────→│ 30 │NULL│
    │    │ →  │     │    │ →  │     │    │ →  │
    └────┴────┘     └────┴────┘     └────┴────┘
```

**Memory State:**
- ✅ New node created with value 5
- ❌ Not connected to list yet
- `new_node.next = None`

---

### **LINE 3: Connect New Node to Current Head**

```python
new_node.next = self.head
```

**What it does:**
- Makes the new node point to the current first node (10)
- Links the new node into the existing list

**Visual Explanation:**

**BEFORE Line 3:**
```
                   new_node
                      │
                      ▼
                  ┌────┬────┐
                  │ 5  │NULL│
                  └────┴────┘
                        ↑
                        └─── Currently NULL
```

**AFTER Line 3:**
```
                   new_node
                      │
                      ▼
                  ┌────┬────┐
                  │ 5  │ ●──┼────┐
                  │    │ →  │    │
                  └────┴────┘    │
                                 │ new_node.next = self.head
       self.head                 │
           │                     │
           ▼                     │
    ┌────┬────┐     ┌────┬────┐ ▼    ┌────┬────┐
    │ 10 │ ●──┼────→│ 20 │ ●──┼────→│ 30 │NULL│
    │    │ →  │     │    │ →  │     │    │ →  │
    └────┴────┘     └────┴────┘     └────┴────┘
```

**Memory State:**
- ✅ New node points to current head (node 10)
- ❌ HEAD still points to node 10 (not updated yet)

---

### **LINE 4: Update HEAD to New Node**

```python
self.head = new_node
```

**What it does:**
- Updates `self.head` to point to the new node
- Makes the new node the official first node of the list

**Visual Explanation:**

**BEFORE Line 4:**
```
       self.head (still here)
           │
           ▼
       [Node 10]
```

**AFTER Line 4:**
```
                   self.head (moved here!)
                      │
                      ▼
                  ┌────┬────┐
                  │ 5  │ ●──┼────┐
                  │    │ →  │    │
                  └────┴────┘    │
                                 │
                                 ▼
                  ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
                  │ 10 │ ●──┼────→│ 20 │ ●──┼────→│ 30 │NULL│
                  │    │ →  │     │    │ →  │     │    │ →  │
                  └────┴────┘     └────┴────┘     └────┴────┘
```

**Memory State:**
- ✅ **Insertion Complete!**
- ✅ HEAD points to new node (5)
- ✅ List is now: 5 → 10 → 20 → 30 → NULL

---

### **LINE 5: Print Confirmation**

```python
print(value, "inserted at beginning")
```

**Console Output:**
```
┌─────────────────────────────────────┐
│ 5 inserted at beginning             │
└─────────────────────────────────────┘
```

---

## Final State

```
       self.head
           │
           ▼
    ┌────┬────┐     ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
    │ 5  │ ●──┼────→│ 10 │ ●──┼────→│ 20 │ ●──┼────→│ 30 │NULL│
    │    │ →  │     │    │ →  │     │    │ →  │     │    │ →  │
    └────┴────┘     └────┴────┘     └────┴────┘     └────┴────┘

List: 5 → 10 → 20 → 30 → NULL
```

---

## Special Case: Empty List

What if the list is **empty**?

### Initial State
```
self.head = None
```

### Execution

**Line 2:** Create new_node with value 5

**Line 3:** `new_node.next = self.head`
```
new_node.next = None
(Points to nothing - list is empty)
```

**Line 4:** `self.head = new_node`
```
       self.head
           │
           ▼
       ┌────┬────┐
       │ 5  │NULL│
       └────┴────┘

List: 5 → NULL
```

---

## Insert Beginning Flow Diagram

```
START insert_beginning(value)
      │
      ▼
Create new_node(value)
      │
      ▼
new_node.next = self.head
      │
      ▼
self.head = new_node
      │
      ▼
Print message
      │
      ▼
     END
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
        print(value, "inserted at end")     # Line 6
        return                              # Line 7
                                            # Line 8 (blank)
    temp = self.head                        # Line 9
    while temp.next:                        # Line 10
        temp = temp.next                    # Line 11
                                            # Line 12 (blank)
    temp.next = new_node                    # Line 13
    print(value, "inserted at end")         # Line 14
```

---

## Example Scenario

Insert value **40** at the end of: **10 → 20 → 30 → NULL**

### Initial State

```
       self.head
           │
           ▼
    ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
    │ 10 │ ●──┼────→│ 20 │ ●──┼────→│ 30 │NULL│
    │    │ →  │     │    │ →  │     │    │ →  │
    └────┴────┘     └────┴────┘     └────┴────┘

Goal: Insert 40 at end
Expected: 10 → 20 → 30 → 40 → NULL
```

---

## Line-by-Line Execution

---

### **LINES 1-2: Function & Create Node**

```python
def insert_end(self, value):            # Line 1
    new_node = Node(value)              # Line 2
```

**Creates new node with value 40:**

```
                   new_node
                      │
                      ▼
                  ┌────┬────┐
                  │ 40 │NULL│
                  └────┴────┘
```

---

### **LINE 4: Check if List is Empty**

```python
if self.head is None:
```

**What it does:**
- Checks if this is the first node being inserted
- Empty list is a special case

**In Our Case:** List has nodes → **FALSE** → Skip lines 5-7

```
    self.head (is NOT None)
        │
        ▼
    ┌────┬────┐
    │ 10 │ ●──┼────→ ...
    └────┴────┘

Condition: FALSE → Skip to line 9
```

---

### **LINES 5-7: Handle Empty List (SKIPPED)**

```python
self.head = new_node                # Line 5
print(value, "inserted at end")     # Line 6
return                              # Line 7
```

**What it does:**
- Only executed if list is empty
- Makes new node the head

**Example (if list was empty):**
```
       self.head
           │
           ▼
       ┌────┬────┐
       │ 40 │NULL│
       └────┴────┘

List: 40 → NULL
```

---

### **LINE 9: Initialize Traversal Pointer**

```python
temp = self.head
```

**What it does:**
- Creates `temp` pointer to find the last node
- Starts at the first node

**Diagram:**
```
    self.head
    temp (both here)
        │
        ▼
    ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
    │ 10 │ ●──┼────→│ 20 │ ●──┼────→│ 30 │NULL│
    │    │ →  │     │    │ →  │     │    │ →  │
    └────┴────┘     └────┴────┘     └────┴────┘
```

---

### **LINES 10-11: While Loop - Find Last Node**

```python
while temp.next:                    # Line 10
    temp = temp.next                # Line 11
```

**What it does:**
- Traverses until `temp.next` is `None` (last node)
- Last node is the one whose `next` is NULL

---

#### **Iteration 1: temp at Node 10**

**LINE 10:** Check condition
```
         temp
          ▼
    ┌────┬────┐
    │ 10 │ ●──┼────→ [Node 20]
    └────┴────┘
         │
         └─── temp.next is NOT None → TRUE (continue)
```

**LINE 11:** Move forward
```
temp = temp.next  (temp now at node 20)
```

---

#### **Iteration 2: temp at Node 20**

**LINE 10:** Check condition
```
         temp
          ▼
    ┌────┬────┐
    │ 20 │ ●──┼────→ [Node 30]
    └────┴────┘

temp.next is NOT None → TRUE (continue)
```

**LINE 11:** Move forward
```
temp = temp.next  (temp now at node 30)
```

---

#### **Iteration 3: temp at Node 30 (Last Node)**

**LINE 10:** Check condition
```
         temp
          ▼
    ┌────┬────┐
    │ 30 │NULL│
    └────┴────┘
         │
         └─── temp.next is None → FALSE (EXIT LOOP)
```

**Diagram:**
```
    self.head
        │
        ▼
    ┌────┬────┐     ┌────┬────┐     ┌────┬────┐ ← temp (last node found!)
    │ 10 │ ●──┼────→│ 20 │ ●──┼────→│ 30 │NULL│
    │    │ →  │     │    │ →  │     │    │ →  │
    └────┴────┘     └────┴────┘     └────┴────┘
```

**Memory State:**
- ✅ `temp` now points to the last node (30)
- Ready to attach new node

---

### **LINE 13: Connect Last Node to New Node**

```python
temp.next = new_node
```

**What it does:**
- Makes the current last node (30) point to the new node (40)

**Visual Explanation:**

**BEFORE Line 13:**
```
                                         ┌────┬────┐
                                         │ 30 │NULL│
                                         └────┴────┘
                                              ▲
                                             temp
```

**AFTER Line 13:**
```
                   new_node
                      │
                      ▼
                  ┌────┬────┐
                  │ 40 │NULL│
                  └────┴────┘
                       ▲
                       │
                       │ temp.next = new_node
       self.head       │
           │           │
           ▼           │
    ┌────┬────┐     ┌─┼──┬────┐     ┌────┬────┐
    │ 10 │ ●──┼────→│ 20 │ ●──┼────→│ 30 │ ●──┼────┐
    │    │ →  │     │    │ →  │     │    │ →  │    │
    └────┴────┘     └────┴────┘     └────┴────┘    │
                                          ▲  temp   │
                                          │         │
                                          └─────────┘
```

**Memory State:**
- ✅ **Insertion Complete!**
- ✅ Node 30 points to new node (40)
- ✅ List is now: 10 → 20 → 30 → 40 → NULL

---

### **LINE 14: Print Confirmation**

```python
print(value, "inserted at end")
```

**Console Output:**
```
┌─────────────────────────────────────┐
│ 40 inserted at end                  │
└─────────────────────────────────────┘
```

---

## Final State

```
       self.head
           │
           ▼
    ┌────┬────┐     ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
    │ 10 │ ●──┼────→│ 20 │ ●──┼────→│ 30 │ ●──┼────→│ 40 │NULL│
    │    │ →  │     │    │ →  │     │    │ →  │     │    │ →  │
    └────┴────┘     └────┴────┘     └────┴────┘     └────┴────┘

List: 10 → 20 → 30 → 40 → NULL
```

---

# PART 3: INSERT AFTER A GIVEN VALUE

## Complete Code with Line Numbers

```python
def insert_after(self, prev_value, value):  # Line 1
    temp = self.head                        # Line 2
                                            # Line 3 (blank)
    while temp:                             # Line 4
        if temp.data == prev_value:         # Line 5
            new_node = Node(value)          # Line 6
            new_node.next = temp.next       # Line 7
            temp.next = new_node            # Line 8
            print(value, "inserted after", prev_value)  # Line 9
            return                          # Line 10
        temp = temp.next                    # Line 11
                                            # Line 12 (blank)
    print("Value", prev_value, "not found") # Line 13
```

---

## Example Scenario

Insert **25** after **20** in: **10 → 20 → 30 → NULL**

### Initial State

```
       self.head
           │
           ▼
    ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
    │ 10 │ ●──┼────→│ 20 │ ●──┼────→│ 30 │NULL│
    │    │ →  │     │    │ →  │     │    │ →  │
    └────┴────┘     └────┴────┘     └────┴────┘

Goal: Insert 25 after 20
Expected: 10 → 20 → 25 → 30 → NULL
```

---

## Line-by-Line Execution

---

### **LINE 1: Function Definition**

```python
def insert_after(self, prev_value, value):
```

**What it does:**
- `prev_value`: Node value after which to insert (20)
- `value`: New value to insert (25)

```
Function Called: insert_after(20, 25)
                      │       │
                      │       └─── value = 25
                      └─────────── prev_value = 20
```

---

### **LINE 2: Initialize Traversal**

```python
temp = self.head
```

**Diagram:**
```
    self.head
    temp
        │
        ▼
    ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
    │ 10 │ ●──┼────→│ 20 │ ●──┼────→│ 30 │NULL│
    │    │ →  │     │    │ →  │     │    │ →  │
    └────┴────┘     └────┴────┘     └────┴────┘

Searching for value 20...
```

---

### **LINES 4-11: While Loop - Search and Insert**

```python
while temp:                             # Line 4
    if temp.data == prev_value:         # Line 5
        # insertion logic (lines 6-10)
    temp = temp.next                    # Line 11
```

---

#### **Iteration 1: temp at Node 10**

**LINE 4:** `while temp:` → temp is not None → **TRUE**

**LINE 5:** Check if matches
```
         temp
          ▼
    ┌────┬────┐
    │ 10 │ ●──┼────→ ...
    └────┴────┘

if temp.data == prev_value:
→ if 10 == 20:
→ FALSE

Skip lines 6-10
```

**LINE 11:** Move to next
```
temp = temp.next  (temp now at node 20)
```

---

#### **Iteration 2: temp at Node 20**

**LINE 4:** `while temp:` → TRUE

**LINE 5:** Check if matches
```
         temp
          ▼
    ┌────┬────┐
    │ 20 │ ●──┼────→ ...
    └────┴────┘

if temp.data == prev_value:
→ if 20 == 20:
→ TRUE ✓ (FOUND!)

Execute insertion logic (lines 6-10)
```

---

### **LINE 6: Create New Node**

```python
new_node = Node(value)
```

**Diagram:**
```
                   new_node
                      │
                      ▼
                  ┌────┬────┐
                  │ 25 │NULL│
                  └────┴────┘


                   temp
                    ▼
    ... ────→ ┌────┬────┐     ┌────┬────┐
              │ 20 │ ●──┼────→│ 30 │NULL│
              └────┴────┘     └────┴────┘
```

---

### **LINE 7: Connect New Node to Next Node**

```python
new_node.next = temp.next
```

**What it does:**
- Makes new node point to what temp is currently pointing to (node 30)

**Visual Explanation:**

**BEFORE Line 7:**
```
                  ┌────┬────┐
                  │ 25 │NULL│
                  └────┴────┘
                        ↑
                        └─── Still NULL
```

**AFTER Line 7:**
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
    ... ────→ ┌────┬────┐     ┌─┼──┬────┐
              │ 20 │ ●──┼─────┼→│ 30│NULL│
              │    │ →  │     │ │   │ →  │
              └────┴────┘     │ └───┴────┘
                   │          │      ▲
                   └──────────┘      │
                    Both point to node 30
```

**Memory State:**
- ✅ New node points to node 30
- ❌ Node 20 still points to node 30 (bypasses new node)

---

### **LINE 8: Connect Previous Node to New Node**

```python
temp.next = new_node
```

**What it does:**
- Makes node 20 point to the new node (25)
- Inserts the new node into the chain

**Visual Explanation:**

**BEFORE Line 8:**
```
                   temp
                    ▼
              ┌────┬────┐
              │ 20 │ ●──┼─────────→ [Node 30]
              └────┴────┘
```

**AFTER Line 8:**
```
       self.head
           │
           ▼
    ┌────┬────┐     ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
    │ 10 │ ●──┼────→│ 20 │ ●──┼────→│ 25 │ ●──┼────→│ 30 │NULL│
    │    │ →  │     │    │ →  │     │    │ →  │     │    │ →  │
    └────┴────┘     └────┴────┘     └────┴────┘     └────┴────┘

temp.next = new_node (Insertion complete!)
```

**Memory State:**
- ✅ **Insertion Complete!**
- ✅ Node 20 → 25 → 30
- ✅ List is now: 10 → 20 → 25 → 30 → NULL

---

### **LINES 9-10: Print and Exit**

```python
print(value, "inserted after", prev_value)  # Line 9
return                                      # Line 10
```

**Console Output:**
```
┌─────────────────────────────────────┐
│ 25 inserted after 20                │
└─────────────────────────────────────┘
```

**Function exits** - Lines 11-13 NOT executed

---

## Final State

```
       self.head
           │
           ▼
    ┌────┬────┐     ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
    │ 10 │ ●──┼────→│ 20 │ ●──┼────→│ 25 │ ●──┼────→│ 30 │NULL│
    │    │ →  │     │    │ →  │     │    │ →  │     │    │ →  │
    └────┴────┘     └────┴────┘     └────┴────┘     └────┴────┘

List: 10 → 20 → 25 → 30 → NULL
```

---

# PART 4: DISPLAY METHOD

## Complete Code with Line Numbers

```python
def display(self):                          # Line 1
    if self.head is None:                   # Line 2
        print("Linked List is empty")       # Line 3
        return                              # Line 4
                                            # Line 5 (blank)
    temp = self.head                        # Line 6
    print("Linked List:")                   # Line 7
    while temp:                             # Line 8
        print(temp.data, end=" -> ")        # Line 9
        temp = temp.next                    # Line 10
    print("NULL")                           # Line 11
```

---

## Example: Display List 10 → 20 → 30

---

### **LINES 2-4: Check Empty**

```python
if self.head is None:
```

**In Our Case:** List has nodes → **FALSE** → Skip

---

### **LINE 6: Initialize**

```python
temp = self.head
```

**Diagram:**
```
    self.head
    temp
        │
        ▼
    ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
    │ 10 │ ●──┼────→│ 20 │ ●──┼────→│ 30 │NULL│
    └────┴────┘     └────┴────┘     └────┴────┘
```

---

### **LINE 7: Print Header**

```python
print("Linked List:")
```

**Output:**
```
Linked List:
```

---

### **LINES 8-10: Traverse and Print**

```python
while temp:                             # Line 8
    print(temp.data, end=" -> ")        # Line 9
    temp = temp.next                    # Line 10
```

**Iteration 1:** temp at 10
- Print "10 -> "
- Move to node 20
- Check: temp is not None? YES, continue

**Iteration 2:** temp at 20
- Print "20 -> "
- Move to node 30
- Check: temp is not None? YES, continue

**Iteration 3:** temp at 30
- Print "30 -> "
- Move to None
- Check: temp is not None? NO, **exit loop**

**Output so far:**
```
Linked List:
10 -> 20 -> 30 -> 
```

---

### **LINE 11: Print NULL**

```python
print("NULL")
```

**Final Output:**
```
Linked List:
10 -> 20 -> 30 -> NULL
```

---

# PART 5: SEARCH METHOD

## Complete Code with Line Numbers

```python
def search(self, key):                      # Line 1
    temp = self.head                        # Line 2
                                            # Line 3 (blank)
    while temp:                             # Line 4
        if temp.data == key:                # Line 5
            print(key, "found in the linked list")  # Line 6
            return                          # Line 7
        temp = temp.next                    # Line 8
                                            # Line 9 (blank)
    print(key, "not found in the linked list")  # Line 10
```

---

## Example: Search for 25

Search for **25** in: **10 → 20 → 25 → 30 → NULL**

---

### **Execution:**

**LINE 2:** `temp = self.head` (node 10)

**Iteration 1:** temp at 10
- Check: 10 == 25? NO
- Move to node 20

**Iteration 2:** temp at 20
- Check: 20 == 25? NO
- Move to node 25

**Iteration 3:** temp at 25
- Check: 25 == 25? **YES** ✓
- Print "25 found in the linked list"
- Return (exit function)

**Output:**
```
25 found in the linked list
```

---

## Search Not Found Example

Search for **100** (doesn't exist):

**Iterations:**
- Check 10: NO → Move next
- Check 20: NO → Move next
- Check 25: NO → Move next
- Check 30: NO → Move next
- temp becomes None → Exit loop

**LINE 10:** Print "100 not found in the linked list"

---

# PART 6: COUNT NODES METHOD

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
```

---

## Example: Count nodes in 10 → 20 → 30

---

### **Execution:**

**LINE 2:** `count = 0`

**LINE 3:** `temp = self.head`

**Iteration 1:** temp at 10
- count = 1
- Move to node 20

**Iteration 2:** temp at 20
- count = 2
- Move to node 30

**Iteration 3:** temp at 30
- count = 3
- Move to None

**LINE 5:** temp is None → Exit loop

**LINE 9:** Print "Total number of nodes: 3"

---

# PART 7: DELETE FROM BEGINNING

## Complete Code with Line Numbers

```python
def delete_beginning(self):                 # Line 1
    if self.head is None:                   # Line 2
        print("List is empty")              # Line 3
        return                              # Line 4
                                            # Line 5 (blank)
    print(self.head.data, "deleted from beginning")  # Line 6
    self.head = self.head.next              # Line 7
```

---

## Example Scenario

Delete first node from: **10 → 20 → 30 → NULL**

### Initial State

```
       self.head
           │
           ▼
    ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
    │ 10 │ ●──┼────→│ 20 │ ●──┼────→│ 30 │NULL│
    │    │ →  │     │    │ →  │     │    │ →  │
    └────┴────┘     └────┴────┘     └────┴────┘

Goal: Delete node 10
Expected: 20 → 30 → NULL
```

---

## Line-by-Line Execution

---

### **LINES 2-4: Check Empty List**

```python
if self.head is None:
```

**In Our Case:** List has nodes → **FALSE** → Skip

---

### **LINE 6: Print Deletion Message**

```python
print(self.head.data, "deleted from beginning")
```

**What it does:**
- Prints the value being deleted (10)
- Done BEFORE actual deletion so we can access the data

**Output:**
```
10 deleted from beginning
```

---

### **LINE 7: Move HEAD to Next Node**

```python
self.head = self.head.next
```

**What it does:**
- Updates `self.head` to point to the second node (20)
- First node becomes unreachable and will be garbage collected

**Visual Explanation:**

**BEFORE Line 7:**
```
       self.head
           │
           ▼
    ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
    │ 10 │ ●──┼────→│ 20 │ ●──┼────→│ 30 │NULL│
    │    │ →  │     │    │ →  │     │    │ →  │
    └────┴────┘     └────┴────┘     └────┴────┘
                         ▲
                         │
                  self.head.next
```

**AFTER Line 7:**
```
                   self.head (moved here!)
                        │
                        ▼
    ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
    │ 10 │ ●──┼────→│ 20 │ ●──┼────→│ 30 │NULL│
    │    │ →  │     │    │ →  │     │    │ →  │
    └────┴────┘     └────┴────┘     └────┴────┘
   (Unreachable)
   Will be garbage
   collected
```

**Memory State:**
- ✅ **Deletion Complete!**
- ✅ HEAD points to node 20
- ✅ List is now: 20 → 30 → NULL
- ✅ Node 10 unreachable and will be garbage collected

---

## Final State

```
       self.head
           │
           ▼
    ┌────┬────┐     ┌────┬────┐
    │ 20 │ ●──┼────→│ 30 │NULL│
    │    │ →  │     │    │ →  │
    └────┴────┘     └────┴────┘

List: 20 → 30 → NULL
```

---

# PART 8: DELETE FROM MIDDLE (GIVEN ELEMENT)

## Complete Code with Line Numbers

```python
def delete_middle(self, key):               # Line 1
    temp = self.head                        # Line 2
    prev = None                             # Line 3
                                            # Line 4 (blank)
    while temp:                             # Line 5
        if temp.data == key:                # Line 6
            if prev is None:                # Line 7
                self.head = temp.next       # Line 8
            else:                           # Line 9
                prev.next = temp.next       # Line 10
            print(key, "deleted from linked list")  # Line 11
            return                          # Line 12
        prev = temp                         # Line 13
        temp = temp.next                    # Line 14
                                            # Line 15 (blank)
    print(key, "not found")                 # Line 16
```

---

## Example Scenario

Delete node with value **25** from: **10 → 20 → 25 → 30 → NULL**

### Initial State

```
       self.head
           │
           ▼
    ┌────┬────┐     ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
    │ 10 │ ●──┼────→│ 20 │ ●──┼────→│ 25 │ ●──┼────→│ 30 │NULL│
    │    │ →  │     │    │ →  │     │    │ →  │     │    │ →  │
    └────┴────┘     └────┴────┘     └────┴────┘     └────┴────┘

Goal: Delete node 25
Expected: 10 → 20 → 30 → NULL
```

---

## Line-by-Line Execution

---

### **LINES 2-3: Initialize Pointers**

```python
temp = self.head                        # Line 2
prev = None                             # Line 3
```

**What it does:**
- `temp`: Points to current node being checked
- `prev`: Points to previous node (used to bypass the deleted node)

**Diagram:**
```
    prev = None

    self.head
    temp
        │
        ▼
    ┌────┬────┐     ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
    │ 10 │ ●──┼────→│ 20 │ ●──┼────→│ 25 │ ●──┼────→│ 30 │NULL│
    └────┴────┘     └────┴────┘     └────┴────┘     └────┴────┘

Searching for value 25...
```

---

### **LINES 5-14: While Loop - Search and Delete**

```python
while temp:                             # Line 5
    if temp.data == key:                # Line 6
        # deletion logic (lines 7-12)
    prev = temp                         # Line 13
    temp = temp.next                    # Line 14
```

---

#### **Iteration 1: temp at Node 10**

**LINE 5:** `while temp:` → TRUE

**LINE 6:** Check if matches
```
    prev = None
    
         temp
          ▼
    ┌────┬────┐
    │ 10 │ ●──┼────→ ...
    └────┴────┘

if temp.data == key:
→ if 10 == 25:
→ FALSE

Skip lines 7-12
```

**LINE 13:** Update prev
```
prev = temp  (prev now points to node 10)
```

**LINE 14:** Move temp
```
temp = temp.next  (temp now points to node 20)
```

**State After Iteration 1:**
```
         prev     temp
          ▼        ▼
    ┌────┬────┐ ┌────┬────┐
    │ 10 │ ●──┼→│ 20 │ ●──┼────→ ...
    └────┴────┘ └────┴────┘
```

---

#### **Iteration 2: temp at Node 20**

**LINE 6:** Check if matches
```
if 20 == 25:
→ FALSE
```

**LINE 13-14:** Update pointers
```
prev = temp  (prev now at node 20)
temp = temp.next  (temp now at node 25)
```

**State After Iteration 2:**
```
                   prev     temp
                    ▼        ▼
    ... ────→ ┌────┬────┐ ┌────┬────┐
              │ 20 │ ●──┼→│ 25 │ ●──┼────→ ...
              └────┴────┘ └────┴────┘
```

---

#### **Iteration 3: temp at Node 25**

**LINE 6:** Check if matches
```
         prev     temp
          ▼        ▼
    ┌────┬────┐ ┌────┬────┐
    │ 20 │ ●──┼→│ 25 │ ●──┼────→ ...
    └────┴────┘ └────┴────┘

if temp.data == key:
→ if 25 == 25:
→ TRUE ✓ (FOUND!)

Execute deletion logic (lines 7-12)
```

---

### **LINE 7: Check if Deleting Head**

```python
if prev is None:
```

**What it does:**
- Checks if we're deleting the **first node**
- `prev is None` means we haven't moved from the start

**In Our Case:**
```
prev = Node 20 (NOT None)
→ FALSE

Skip line 8, execute line 10
```

---

### **LINES 8-10: Delete Node**

```python
if prev is None:                # Line 7
    self.head = temp.next       # Line 8 (SKIPPED)
else:                           # Line 9
    prev.next = temp.next       # Line 10 (EXECUTED)
```

---

### **LINE 10: Bypass the Node**

```python
prev.next = temp.next
```

**What it does:**
- Makes the previous node (20) point to the next node (30)
- Bypasses the current node (25)

**Visual Explanation:**

**BEFORE Line 10:**
```
                   prev     temp
                    ▼        ▼
    ... ────→ ┌────┬────┐ ┌────┬────┐     ┌────┬────┐
              │ 20 │ ●──┼→│ 25 │ ●──┼────→│ 30 │NULL│
              │    │ →  │ │    │ →  │     │    │ →  │
              └────┴────┘ └────┴────┘     └────┴────┘
                   │                           ▲
                   │                           │
                   └──────→ temp.next ─────────┘
```

**AFTER Line 10:**
```
       self.head
           │
           ▼
    ┌────┬────┐     ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
    │ 10 │ ●──┼────→│ 20 │ ●──┼──┐  │ 25 │ ●──┼────→│ 30 │NULL│
    │    │ →  │     │    │ →  │  │  │    │ →  │     │    │ →  │
    └────┴────┘     └────┴────┘  │  └────┴────┘     └────┴────┘
                                  │  (Unreachable)        ▲
                                  │   Will be             │
                                  │   garbage             │
                                  │   collected           │
                                  └───────────────────────┘
                                  
                                  prev.next = temp.next
```

**Memory State:**
- ✅ **Deletion Complete!**
- ✅ Node 20 directly points to node 30
- ✅ List is now: 10 → 20 → 30 → NULL
- ✅ Node 25 unreachable and will be garbage collected

---

### **LINES 11-12: Print and Exit**

```python
print(key, "deleted from linked list")  # Line 11
return                                  # Line 12
```

**Output:**
```
25 deleted from linked list
```

Function exits - Lines 13-16 NOT executed

---

## Final State

```
       self.head
           │
           ▼
    ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
    │ 10 │ ●──┼────→│ 20 │ ●──┼────→│ 30 │NULL│
    │    │ →  │     │    │ →  │     │    │ →  │
    └────┴────┘     └────┴────┘     └────┴────┘

List: 10 → 20 → 30 → NULL
```

---

## Special Case: Deleting First Node

What if we delete **10** (first node)?

**Execution:**

**Initial:**
```
prev = None
temp = self.head (node 10)
```

**Check:** `10 == 10?` → **TRUE**

**LINE 7:** `if prev is None:` → **TRUE**

**LINE 8:** `self.head = temp.next`
```
       self.head (moved to node 20)
           │
           ▼
    ┌────┬────┐     ┌────┬────┐
    │ 20 │ ●──┼────→│ 30 │NULL│
    └────┴────┘     └────┴────┘

List: 20 → 30 → NULL
```

---

# PART 9: DELETE FROM END

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
    while temp.next.next:                   # Line 12
        temp = temp.next                    # Line 13
                                            # Line 14 (blank)
    print(temp.next.data, "deleted from end")  # Line 15
    temp.next = None                        # Line 16
```

---

## Example Scenario

Delete last node from: **10 → 20 → 30 → NULL**

### Initial State

```
       self.head
           │
           ▼
    ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
    │ 10 │ ●──┼────→│ 20 │ ●──┼────→│ 30 │NULL│
    │    │ →  │     │    │ →  │     │    │ →  │
    └────┴────┘     └────┴────┘     └────┴────┘

Goal: Delete node 30 (last node)
Expected: 10 → 20 → NULL
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

### **LINE 6: Check Single Node**

```python
if self.head.next is None:
```

**What it does:**
- Checks if there's only one node in the list
- Single node: `self.head.next` is None

**In Our Case:**
```
    self.head
        │
        ▼
    ┌────┬────┐
    │ 10 │ ●──┼────→ [Node 20] (exists)
    └────┴────┘

self.head.next is NOT None → FALSE
Skip lines 7-9
```

---

### **LINES 7-9: Handle Single Node (SKIPPED)**

**Would execute if list had only one node:**

```python
print(self.head.data, "deleted from end")  # Line 7
self.head = None                           # Line 8
return                                     # Line 9
```

**Result:**
```
List becomes empty
```

---

### **LINE 11: Initialize Traversal**

```python
temp = self.head
```

**Diagram:**
```
    self.head
    temp
        │
        ▼
    ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
    │ 10 │ ●──┼────→│ 20 │ ●──┼────→│ 30 │NULL│
    └────┴────┘     └────┴────┘     └────┴────┘
```

---

### **LINES 12-13: Find Second-to-Last Node**

```python
while temp.next.next:                   # Line 12
    temp = temp.next                    # Line 13
```

**What it does:**
- Finds the node **before** the last node
- `temp.next.next` checks two nodes ahead

**Critical Pattern:**
```
temp.next        → Last node
temp.next.next   → NULL (if temp.next is last)

while temp.next.next: → Stop when next node is last
```

---

#### **Iteration 1: temp at Node 10**

**LINE 12:** Check condition
```
         temp
          ▼
    ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
    │ 10 │ ●──┼────→│ 20 │ ●──┼────→│ 30 │NULL│
    └────┴────┘     └────┴────┘     └────┴────┘
         │              │               │
         │              └── temp.next   │
         └── temp                       │
                                temp.next.next

temp.next = node 20
temp.next.next = node 30 (NOT None)
→ TRUE (continue)
```

**LINE 13:** Move forward
```
temp = temp.next  (temp now at node 20)
```

---

#### **Iteration 2: temp at Node 20**

**LINE 12:** Check condition
```
                   temp
                    ▼
    ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
    │ 10 │ ●──┼────→│ 20 │ ●──┼────→│ 30 │NULL│
    └────┴────┘     └────┴────┘     └────┴────┘
                         │               │
                         └── temp.next   │
                                         │
                                 temp.next.next = NULL

temp.next = node 30
temp.next.next = None
→ FALSE (EXIT LOOP)
```

**Result:**
```
    self.head
        │
        ▼
    ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
    │ 10 │ ●──┼────→│ 20 │ ●──┼────→│ 30 │NULL│
    │    │ →  │     │    │ →  │     │    │ →  │
    └────┴────┘     └────┴────┘     └────┴────┘
                         ▲  temp          ▲
                         │                │
                         │        temp.next (last node)
                         └── Second-to-last node found!
```

---

### **LINE 15: Print Deletion Message**

```python
print(temp.next.data, "deleted from end")
```

**What it does:**
- `temp.next` is the last node (30)
- Print its data before deleting

**Output:**
```
30 deleted from end
```

---

### **LINE 16: Remove Last Node**

```python
temp.next = None
```

**What it does:**
- Makes the second-to-last node (20) point to NULL
- Last node (30) becomes unreachable

**Visual Explanation:**

**BEFORE Line 16:**
```
                   temp
                    ▼
              ┌────┬────┐     ┌────┬────┐
              │ 20 │ ●──┼────→│ 30 │NULL│
              └────┴────┘     └────┴────┘
```

**AFTER Line 16:**
```
       self.head
           │
           ▼
    ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
    │ 10 │ ●──┼────→│ 20 │NULL│     │ 30 │NULL│
    │    │ →  │     │    │ →  │     │    │ →  │
    └────┴────┘     └────┴────┘     └────┴────┘
                                    (Unreachable)
                                    Will be garbage
                                    collected

temp.next = None
```

**Memory State:**
- ✅ **Deletion Complete!**
- ✅ Node 20 is now the last node (points to NULL)
- ✅ List is now: 10 → 20 → NULL
- ✅ Node 30 unreachable and will be garbage collected

---

## Final State

```
       self.head
           │
           ▼
    ┌────┬────┐     ┌────┬────┐
    │ 10 │ ●──┼────→│ 20 │NULL│
    │    │ →  │     │    │ →  │
    └────┴────┘     └────┴────┘

List: 10 → 20 → NULL
```

---

## Summary: All Operations

### **Insertion Operations**

| Operation | Time | Key Steps |
|-----------|------|-----------|
| **insert_beginning** | O(1) | 1. new_node.next = head<br>2. head = new_node |
| **insert_end** | O(n) | 1. Traverse to last<br>2. last.next = new_node |
| **insert_after** | O(n) | 1. Find prev_value<br>2. new_node.next = temp.next<br>3. temp.next = new_node |

### **Display & Search Operations**

| Operation | Time | Pattern |
|-----------|------|---------|
| **display** | O(n) | while temp: print → temp = temp.next |
| **search** | O(n) | while temp: check → temp = temp.next |
| **count_nodes** | O(n) | while temp: count++ → temp = temp.next |

### **Deletion Operations**

| Operation | Time | Key Steps |
|-----------|------|-----------|
| **delete_beginning** | O(1) | head = head.next |
| **delete_middle** | O(n) | 1. Find node (track prev)<br>2. prev.next = temp.next |
| **delete_end** | O(n) | 1. Find second-to-last<br>2. temp.next = None |

---

## Key Singly Linked List Patterns

### **1. Find Last Node:**
```python
temp = self.head
while temp.next:  # While temp has a next
    temp = temp.next
# temp is now last node
```

### **2. Find Second-to-Last Node:**
```python
temp = self.head
while temp.next.next:  # While next has a next
    temp = temp.next
# temp is now second-to-last
```

### **3. Traverse with Previous Pointer:**
```python
temp = self.head
prev = None
while temp:
    # Process
    prev = temp
    temp = temp.next
```

### **4. Empty List Check:**
```python
if self.head is None:
    # List is empty
```

### **5. Single Node Check:**
```python
if self.head.next is None:
    # Only one node
```

---

## Complete Execution Flow

### **Main Program Output:**

```python
ll = SinglyLinkedList()

ll.insert_beginning(10)    # 10 inserted at beginning
ll.insert_end(20)          # 20 inserted at end
ll.insert_end(30)          # 30 inserted at end
ll.insert_after(20, 25)    # 25 inserted after 20

ll.display()               # Linked List:
                          # 10 -> 20 -> 25 -> 30 -> NULL

ll.search(25)             # 25 found in the linked list
ll.count_nodes()          # Total number of nodes: 4

ll.delete_beginning()     # 10 deleted from beginning
ll.delete_middle(25)      # 25 deleted from linked list
ll.delete_end()           # 30 deleted from end

ll.display()              # Linked List:
                          # 20 -> NULL
```

---

## Visual Progression

### **After Insertions:**
```
       HEAD
         │
         ▼
    ┌────┬────┐     ┌────┬────┐     ┌────┬────┐     ┌────┬────┐
    │ 10 │ ●──┼────→│ 20 │ ●──┼────→│ 25 │ ●──┼────→│ 30 │NULL│
    └────┴────┘     └────┴────┘     └────┴────┘     └────┴────┘

List: 10 → 20 → 25 → 30 → NULL
```

### **After Deletions:**
```
       HEAD
         │
         ▼
    ┌────┬────┐
    │ 20 │NULL│
    └────┴────┘

List: 20 → NULL
```

---

## 🎉 Complete Singly Linked List Explained!

Now understand every line of the **Singly Linked List** implementation with detailed diagrams showing exactly how pointers are manipulated!

**Key Takeaways:**
- ✅ Each node points to the **next** node only (one direction)
- ✅ Last node points to **NULL**
- ✅ Traversal only in **forward** direction
- ✅ Use `temp` for traversal, `prev` for deletion
- ✅ Always check for **empty list** and **single node** cases
- ✅ Garbage collection handles unreachable nodes automatically
