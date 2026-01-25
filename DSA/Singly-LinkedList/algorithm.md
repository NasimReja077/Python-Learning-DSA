## 📌 ALGORITHM: SINGLY LINKED LIST

(Each node contains **DATA** and **NEXT** pointer)

---

## 📌 Algorithm 1: INSERT a Node at the BEGINNING

**Step 1:** Start

**Step 2:** Create a new node `new_node`

**Step 3:** Store the value in `new_node.data`

**Step 4:** Set `new_node.next = head`

**Step 5:** Update `head = new_node`

**Step 6:** Stop

---

## 📌 Algorithm 2: INSERT a Node at the END

**Step 1:** Start

**Step 2:** Create a new node `new_node`

**Step 3:** Store value in `new_node.data`

**Step 4:** Set `new_node.next = NULL`

**Step 5:** If `head == NULL`
  → Set `head = new_node` and go to Step 8

**Step 6:** Set `temp = head`

**Step 7:** Traverse while `temp.next != NULL`
     → `temp = temp.next`

**Step 8:** Set `temp.next = new_node`

**Step 9:** Stop

---

## 📌 Algorithm 3: DISPLAY (TRAVERSE) the Linked List

**Step 1:** Start

**Step 2:** If `head == NULL`
  → Print `"Linked List is Empty"` and go to Step 6

**Step 3:** Set `temp = head`

**Step 4:** While `temp != NULL`

  → Print `temp.data`

  → Set `temp = temp.next`

**Step 5:** End loop

**Step 6:** Stop

---

## 📌 Algorithm 4: COUNT Number of Nodes

**Step 1:** Start

**Step 2:** Set `count = 0`

**Step 3:** Set `temp = head`

**Step 4:** While `temp != NULL`

  → `count = count + 1`

  → `temp = temp.next`

**Step 5:** Print `"Total nodes = count"`

**Step 6:** Stop

---

## 📌 Algorithm 5: SEARCH an Element

**Step 1:** Start

**Step 2:** Set `temp = head`

**Step 3:** While `temp != NULL`

  → If `temp.data == key`, print `"Element found"` and go to Step 6

  → Else `temp = temp.next`

**Step 4:** Print `"Element not found"`

**Step 5:** Stop

---

## 📌 Algorithm 6: DELETE a Given Element

**Step 1:** Start

**Step 2:** If `head == NULL`
  → Print `"List is Empty"` and go to Step 8

**Step 3:** If `head.data == key`
  → Set `head = head.next` and go to Step 8

**Step 4:** Set `temp = head`, `prev = NULL`

**Step 5:** While `temp != NULL` and `temp.data != key`

  → `prev = temp`
  → `temp = temp.next`

**Step 6:** If `temp == NULL`

  → Print `"Element not found"`

**Step 7:** Else

  → Set `prev.next = temp.next`

  → Print `"Element deleted"`

**Step 8:** Stop

---

## 🧠 Important Exam Notes

* Singly Linked List uses **one pointer (NEXT)**
* Traversal is **one-directional**
* Dynamic memory allocation
* No index-based access

---




Here is a **clear, exam-ready algorithm** for

### **Insert After a Given Node (Key)**

(also called **middle insertion in a Singly Linked List**)
— written in the **same style used in university exams** ✅

---

## 📌 ALGORITHM: INSERT AFTER A GIVEN NODE (KEY)

*(Singly Linked List)*

---

**Step 1:** Start

**Step 2:** Create a new node `new_node`

**Step 3:** Store the value in `new_node.data`

**Step 4:** Set `temp = head`

**Step 5:** Traverse the list while `temp != NULL`

  **Step 5.1:** If `temp.data == key`
   → Set `new_node.next = temp.next`
   → Set `temp.next = new_node`
   → Print `"Node inserted successfully"`
   → Go to Step 8

  **Step 5.2:** Else
   → Set `temp = temp.next`

**Step 6:** If `temp == NULL`
  → Print `"Key not found"`

**Step 7:** Stop

**Step 8:** Stop

---

## 🧠 Key Exam Notes

* This operation inserts a node **after a given element**
* Used for **middle insertion**
* Time Complexity: **O(n)**
* No insertion if key is not found

---

### 📌 Algorithm 4: INSERT a Node at the MIDDLE

```
Step 1: Start
Step 2: Create a new node new_node
Step 3: Store value in new_node.data
Step 4: If head == NULL
        → Set head = new_node
        → new_node.next = NULL
        → Stop
Step 5: Set slow = head, fast = head
Step 6: While fast != NULL AND fast.next != NULL
        → slow = slow.next
        → fast = fast.next.next
Step 7: Set new_node.next = slow.next
Step 8: Set slow.next = new_node
Step 9: Stop
```

### 🧠 Explanation (1–2 lines for exam)

* `slow` reaches the middle node
* New node is inserted after the middle

**Time Complexity:** `O(n)`
**Space Complexity:** `O(1)`

---