# ALGORITHM FOR QUEUE (USING ARRAY)

We consider a **Simple (Linear) Queue** implemented using an array.

---

## VARIABLES USED

* `Q[ ]` → Array to store queue elements
* `front` → Points to first element
* `rear` → Points to last element
* `size` → Maximum size of queue

### Initial Values

```
front = -1
rear  = -1
```

---

## 1️⃣ ALGORITHM: ENQUEUE (INSERT OPERATION)

### Purpose

To insert an element into the queue at the **rear end**.

---

### Algorithm: ENQUEUE(Q, item)

1. **Start**
2. If `rear == size - 1`
   → Print **"Queue Overflow"** and go to Step 6
3. If `front == -1`
   → Set `front = 0`
4. Set `rear = rear + 1`
5. Insert `item` into `Q[rear]`
6. **Stop**

---

## 2️⃣ ALGORITHM: DEQUEUE (DELETE OPERATION)

### Purpose

To remove an element from the queue from the **front end**.

---

### Algorithm: DEQUEUE(Q)

1. **Start**
2. If `front == -1` OR `front > rear`
   → Print **"Queue Underflow"** and go to Step 6
3. Remove element from `Q[front]`
4. Set `front = front + 1`
5. If `front > rear`
   → Set `front = rear = -1`
6. **Stop**

---

## 3️⃣ ALGORITHM: DISPLAY QUEUE

### Purpose

To display all elements of the queue.

---

### Algorithm: DISPLAY(Q)

1. **Start**
2. If `front == -1`
   → Print **"Queue is Empty"** and go to Step 5
3. For `i = front` to `rear`

   * Print `Q[i]`
4. End For
5. **Stop**

---

## QUEUE CONDITIONS (IMPORTANT FOR EXAM)

### Queue Overflow

```
rear == size - 1
```

### Queue Underflow

```
front == -1 OR front > rear
```

---

## TIME COMPLEXITY

| Operation | Time Complexity |
| --------- | --------------- |
| Enqueue   | O(1)            |
| Dequeue   | O(1)            |
| Display   | O(n)            |

---

## SHORT EXAM ANSWER (3–4 Marks)

> A queue is a linear data structure that follows FIFO principle. The enqueue operation inserts an element at the rear end, while the dequeue operation removes an element from the front end. Overflow occurs when the queue is full, and underflow occurs when the queue is empty.

---
---
---

# ALGORITHM FOR CIRCULAR QUEUE (USING ARRAY)

---

## VARIABLES USED

* `CQ[ ]` → Array to store elements
* `front` → Points to first element
* `rear` → Points to last element
* `size` → Maximum size of queue

### Initial Values

```
front = -1
rear  = -1
```

---

## 1️⃣ ALGORITHM: ENQUEUE (CIRCULAR QUEUE)

### Purpose

To insert an element at the **rear end** of the circular queue.

---

### Algorithm: ENQUEUE_CQ(CQ, item)

1. **Start**
2. If `(rear + 1) % size == front`
   → Print **"Queue Overflow"** and go to Step 7
3. If `front == -1`

   * Set `front = 0`
   * Set `rear = 0`
4. Else

   * Set `rear = (rear + 1) % size`
5. Insert `item` into `CQ[rear]`
6. **Stop**

---

## 2️⃣ ALGORITHM: DEQUEUE (CIRCULAR QUEUE)

### Purpose

To delete an element from the **front end** of the circular queue.

---

### Algorithm: DEQUEUE_CQ(CQ)

1. **Start**
2. If `front == -1`
   → Print **"Queue Underflow"** and go to Step 7
3. Remove element from `CQ[front]`
4. If `front == rear`

   * Set `front = -1`
   * Set `rear = -1`
5. Else

   * Set `front = (front + 1) % size`
6. **Stop**

---

## 3️⃣ ALGORITHM: DISPLAY (CIRCULAR QUEUE)

### Purpose

To display all elements of the circular queue.

---

### Algorithm: DISPLAY_CQ(CQ)

1. **Start**
2. If `front == -1`
   → Print **"Queue is Empty"** and go to Step 7
3. Set `i = front`
4. Repeat

   * Print `CQ[i]`
   * `i = (i + 1) % size`
     Until `i == (rear + 1) % size`
5. **Stop**

---

## IMPORTANT CONDITIONS (EXAM POINTS ⭐)

### Queue FULL Condition

```
(rear + 1) % size == front
```

### Queue EMPTY Condition

```
front == -1
```

---

## TIME COMPLEXITY

| Operation | Time Complexity |
| --------- | --------------- |
| Enqueue   | O(1)            |
| Dequeue   | O(1)            |
| Display   | O(n)            |

---

## SHORT EXAM ANSWER (3–4 Marks)

> A circular queue is a linear data structure in which the last position is connected to the first position. Enqueue and dequeue operations are performed using modulo arithmetic. It overcomes the drawback of simple queue by efficiently utilizing memory.

---
---

## 🔹 Sample Output (Exam Friendly)

```
10 inserted
20 inserted
30 inserted
40 inserted
Queue elements:
10 20 30 40
10 removed
20 removed
Queue elements:
30 40
50 inserted
60 inserted
Queue elements:
60 30 40 50
```

---

# 🔹 NUMERICAL EXAMPLES (STEP-BY-STEP)

### Queue Size = 5

Initial:

```
front = -1, rear = -1
```

---

### ▶ Enqueue 10

```
front = 0, rear = 0
[10][ ][ ][ ][ ]
```

---

### ▶ Enqueue 20

```
front = 0, rear = 1
[10][20][ ][ ][ ]
```

---

### ▶ Enqueue 30

```
front = 0, rear = 2
[10][20][30][ ][ ]
```

---

### ▶ Dequeue

```
Removed = 10
front = 1
[ ][20][30][ ][ ]
```

---

### ▶ Enqueue 40

```
rear = 3
[ ][20][30][40][ ]
```

---

### ▶ Enqueue 50

```
rear = 4
[ ][20][30][40][50]
```

---

### ▶ Enqueue 60 (Circular Move)

```
rear = (4 + 1) % 5 = 0
[60][20][30][40][50]
```

---

# 🔹 DIAGRAM-BASED EXPLANATION (FOR EXAM)

### 🔸 Logical Circular Representation

```
        ┌───┐
        │ 0 │ ← rear
        └─▲─┘
          │
┌───┐   ┌─┴─┐   ┌───┐
│ 4 │ ◄ │ 1 │ ◄ │ 2 │
└───┘   └───┘   └───┘
          │
          ▼
         [3]
```

---

### 🔸 Linear Array View

```
Index:  0   1   2   3   4
Queue: [60][20][30][40][50]
          ↑             ↑
        front          rear
```

---

## 🔹 IMPORTANT CONDITIONS (VERY IMPORTANT ⭐)

### Queue FULL

```
(rear + 1) % size == front
```

### Queue EMPTY

```
front == -1
```

---

## 🔹 TIME COMPLEXITY

| Operation | Complexity |
| --------- | ---------- |
| Enqueue   | O(1)       |
| Dequeue   | O(1)       |
| Display   | O(n)       |

---

## 🔹 SHORT EXAM ANSWER (5 Marks)

> A circular queue is a linear data structure in which the last position is connected to the first position, forming a circular structure. It uses modulo arithmetic to efficiently utilize memory and avoids false overflow. Insertion and deletion operations are performed in O(1) time.

---
---

# Why do we use **(rear + 1) % size** in Circular Queue?

## Short Answer (Exam-Friendly)

> The modulo operator `% size` is used in a circular queue to **move the rear or front pointer back to the beginning of the array when it reaches the end**, thus maintaining the circular nature of the queue and efficiently reusing memory.

---

## Detailed Explanation (Step-by-Step)

### Problem Without `% size`

In a **simple queue**, when `rear` reaches the last index:

```
Index:  0   1   2   3   4
Queue: [10][20][30][40][50]
rear = 4
```

If we try:

```
rear = rear + 1  → rear = 5 ❌ (out of array)
```

This causes **overflow**, even though there may be empty spaces at the front.

---

## Solution: Modulo Operator `%`

The modulo operator **wraps the index back to 0**.

### Formula Used

```
rear = (rear + 1) % size
front = (front + 1) % size
```

---

## How `% size` Works

Assume:

```
size = 5
```

| Expression  | Result |
| ----------- | ------ |
| (0 + 1) % 5 | 1      |
| (1 + 1) % 5 | 2      |
| (3 + 1) % 5 | 4      |
| (4 + 1) % 5 | 0 ✅    |

👉 When the index reaches the end, it **automatically returns to 0**.

---

## Circular Queue Example

### Step 1: Queue after some operations

```
Index:  0   1   2   3   4
Queue: [ ][20][30][40][ ]
front = 1
rear  = 3
```

### Step 2: Insert new element

```
rear = (3 + 1) % 5 = 4
```

```
Queue: [ ][20][30][40][50]
```

### Step 3: Insert again (circular move)

```
rear = (4 + 1) % 5 = 0
```

```
Queue: [60][20][30][40][50]
```

✔ Empty space reused
✔ No overflow
✔ Circular behavior maintained

---

## Why `% size` is ESSENTIAL

### 1️⃣ Maintains Circular Nature

It connects:

```
Last index → First index
```

---

### 2️⃣ Prevents False Overflow

Even if rear reaches the end, queue continues if space exists.

---

### 3️⃣ Efficient Memory Utilization

No wasted space at the front.

---

## FULL and EMPTY Conditions Use `% size`

### Queue FULL

```
(rear + 1) % size == front
```

➡ Means **next position of rear is front** → no space left

---

### Queue EMPTY

```
front == -1
```

---

## Diagram Explanation (Exam-Friendly)

```
Index:  0   1   2   3   4
Queue: [ ][20][30][40][ ]
          ↑             ↑
        front          rear

rear moves like:
3 → 4 → 0 → 1 → 2
(using % size)
```

---

## One-Line Exam Answer ⭐

> The modulo operator `% size` is used in circular queue to wrap the front and rear pointers back to the beginning of the array when they reach the end, ensuring circular movement and efficient memory utilization.

---
---
---
---

# ALGORITHM FOR DEQUE (USING ARRAY)

---

## VARIABLES USED

* `DQ[ ]` → Array to store deque elements
* `front` → Points to front end
* `rear` → Points to rear end
* `size` → Maximum size of deque

### Initial Values

```
front = -1
rear  = -1
```

---

## CONDITIONS (VERY IMPORTANT ⭐)

### Deque is EMPTY when:

```
front == -1
```

### Deque is FULL when:

```
(front == 0 and rear == size - 1)
OR
(front == rear + 1)
```

---

# OPERATIONS ON DEQUE

---

## 1️⃣ INSERT AT FRONT

### Algorithm: INSERT_FRONT(DQ, item)

1. **Start**
2. If deque is FULL
   → Print **"Overflow"** and go to Step 7
3. If `front == -1`
   → Set `front = rear = 0`
4. Else if `front == 0`
   → Set `front = size - 1`
5. Else
   → Set `front = front - 1`
6. Insert `item` into `DQ[front]`
7. **Stop**

---

## 2️⃣ INSERT AT REAR

### Algorithm: INSERT_REAR(DQ, item)

1. **Start**
2. If deque is FULL
   → Print **"Overflow"** and go to Step 7
3. If `rear == -1`
   → Set `front = rear = 0`
4. Else if `rear == size - 1`
   → Set `rear = 0`
5. Else
   → Set `rear = rear + 1`
6. Insert `item` into `DQ[rear]`
7. **Stop**

---

## 3️⃣ DELETE FROM FRONT

### Algorithm: DELETE_FRONT(DQ)

1. **Start**
2. If deque is EMPTY
   → Print **"Underflow"** and go to Step 7
3. Remove element from `DQ[front]`
4. If `front == rear`
   → Set `front = rear = -1`
5. Else if `front == size - 1`
   → Set `front = 0`
6. Else
   → Set `front = front + 1`
7. **Stop**

---

## 4️⃣ DELETE FROM REAR

### Algorithm: DELETE_REAR(DQ)

1. **Start**
2. If deque is EMPTY
   → Print **"Underflow"** and go to Step 7
3. Remove element from `DQ[rear]`
4. If `front == rear`
   → Set `front = rear = -1`
5. Else if `rear == 0`
   → Set `rear = size - 1`
6. Else
   → Set `rear = rear - 1`
7. **Stop**

---

## TIME COMPLEXITY

| Operation    | Time Complexity |
| ------------ | --------------- |
| Insert Front | O(1)            |
| Insert Rear  | O(1)            |
| Delete Front | O(1)            |
| Delete Rear  | O(1)            |

---

## SHORT EXAM ANSWER (4–5 Marks)

> A Deque (Double Ended Queue) is a linear data structure in which insertion and deletion can be performed at both the front and rear ends. It provides more flexibility than a simple queue and supports both stack and queue operations. All operations are performed in constant time.

---

## IMPORTANT EXAM POINTS ⭐

✔ Two ends: front and rear
✔ Insertion & deletion at both ends
✔ Two types: Input-restricted & Output-restricted
✔ Can act as stack and queue

---

# 1️⃣ ALGORITHM EXPLANATION – DEQUE

## What is a Deque?

A **Deque (Double Ended Queue)** is a linear data structure in which **insertion and deletion are allowed at both ends** (front and rear).

---

## Variables Used

* `DQ[ ]` → array to store elements
* `front` → index of front element
* `rear` → index of rear element
* `size` → maximum size

### Initial Condition

```
front = -1
rear = -1
```

---

## Conditions

### Deque EMPTY

```
front == -1
```

### Deque FULL

```
(front == 0 and rear == size - 1)
OR
(front == rear + 1)
```

---

## Explanation of Operations

### 🔹 Insert at Front

* Check overflow
* Move `front` backward (circularly)
* Insert element at `front`

---

### 🔹 Insert at Rear

* Check overflow
* Move `rear` forward (circularly)
* Insert element at `rear`

---

### 🔹 Delete from Front

* Check underflow
* Remove element at `front`
* Move `front` forward

---

### 🔹 Delete from Rear

* Check underflow
* Remove element at `rear`
* Move `rear` backward

---
---

# 3️⃣ NUMERICAL EXAMPLES (STEP-BY-STEP)

### Deque Size = 5

#### ▶ Insert Rear: 10

```
[10][ ][ ][ ][ ]
front = 0, rear = 0
```

#### ▶ Insert Rear: 20

```
[10][20][ ][ ][ ]
front = 0, rear = 1
```

#### ▶ Insert Front: 5

```
[10][20][ ][ ][5]
front = 4, rear = 1
```

#### ▶ Delete Rear

```
Deleted: 20
[10][ ][ ][ ][5]
front = 4, rear = 0
```

---

# 4️⃣ DIAGRAM-BASED EXPLANATION

### Logical View

```
Front ↔ [ 5 ][ 10 ] ↔ Rear
```

---

### Circular Array View

```
Index:  0   1   2   3   4
Deque: [10][ ][ ][ ][5]
          ↑           ↑
        rear        front
```

---

# 5️⃣ COMPARISON: DEQUE vs CIRCULAR QUEUE

| Feature       | Deque      | Circular Queue |
| ------------- | ---------- | -------------- |
| Insertion     | Both ends  | Rear only      |
| Deletion      | Both ends  | Front only     |
| FIFO          | Not strict | Strict FIFO    |
| Flexibility   | High       | Moderate       |
| Acts as Stack | Yes        | No             |
| Memory Use    | Efficient  | Efficient      |

---

# ⭐ SHORT EXAM ANSWER (5 Marks)

> A Deque (Double Ended Queue) is a linear data structure in which insertion and deletion can be performed at both the front and rear ends. It provides more flexibility than a circular queue and can behave as both stack and queue. All operations are performed in constant time.

---