# 🔹 ALGORITHM: STACK USING ARRAY

---

## 📌 Algorithm 1: PUSH Operation

**Step 1:** Start

**Step 2:** Check if `top == size – 1`

  → If **TRUE**, print **"Stack Overflow"** and go to Step 6

**Step 3:** Increment `top` by 1

**Step 4:** Insert the element at `stack[top]`

**Step 5:** Print **"Element pushed successfully"**

**Step 6:** Stop

---

## 📌 Algorithm 2: POP Operation

**Step 1:** Start

**Step 2:** Check if `top == -1`

  → If **TRUE**, print **"Stack Underflow"** and go to Step 6

**Step 3:** Store `stack[top]` in a variable `item`

**Step 4:** Decrement `top` by 1

**Step 5:** Print **"Popped element is item"**

**Step 6:** Stop

---

## 📌 Algorithm 3: DISPLAY Operation

**Step 1:** Start

**Step 2:** Check if `top == -1`

  → If **TRUE**, print **"Stack is Empty"** and go to Step 5

**Step 3:** For `i = top` down to `0`, print `stack[i]`

**Step 4:** End loop

**Step 5:** Stop

---
# Why use an Array for a Stack?
 **Speed**: Accessing and modifying the top element is $O(1)$ (constant time).

 **Predictability**: Memory is allocated upfront, so there are no surprises with memory usage during execution.

 **Limitation**: The "Overflow" issue exists because arrays have a fixed size. In Python, we often use lists, which grow dynamically, but for learning algorithms, the fixed-size array approach is the most important to master.