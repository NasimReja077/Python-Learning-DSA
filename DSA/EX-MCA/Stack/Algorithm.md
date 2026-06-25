# 🔹 Algorithm: Stack Implementation Using Array (Python List)

---

### **Algorithm: STACK**

---

### **Step 1: Start**

---

### **Step 2: Initialize Stack**

1. Create a class `Stack`
2. Define constructor `__init__(size)`

   * Set `self.size = size`
   * Initialize empty list `self.stack = []`

---

## 🔹 **Operation 1: PUSH(value)**

### **Algorithm: PUSH**

1. If `length of stack == stack size`

   * Print **"Stack Overflow! Cannot push."**
2. Else

   * Insert `value` into stack using `append()`
   * Print **"value pushed into stack"**

---

## 🔹 **Operation 2: POP()**

### **Algorithm: POP**

1. If `length of stack == 0`

   * Print **"Stack Underflow! Nothing to pop."**
2. Else

   * Remove top element using `pop()`
   * Store removed value
   * Print **"removed value popped from stack"**

---

## 🔹 **Operation 3: DISPLAY()**

### **Algorithm: DISPLAY**

1. If `length of stack == 0`

   * Print **"Stack is empty."**
2. Else

   * Display stack elements from **top to bottom**
   * Traverse stack in reverse order
   * Print each element

---

### **Step 3: Stop**

---

## 🔹 **One-Line Exam Definition**

> Stack is implemented using array where insertion and deletion are performed at one end called TOP, and overflow/underflow is checked using stack size.

---
