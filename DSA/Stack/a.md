**✅ Here are the proper Algorithms for both Stack implementations.**

---

### **1. For First Code (Top Pointer - Fixed Array Implementation)**

This is the **better version** for exams.

#### **Algorithm 1: PUSH Operation**

**Step 1:** Start  
**Step 2:** Check if `top == size - 1`  
   If **True** → Print "Stack Overflow!" and Stop  
**Step 3:** Increment `top` by 1 (`top = top + 1`)  
**Step 4:** Insert value → `stack[top] = value`  
**Step 5:** Print "value pushed into stack"  
**Step 6:** Stop

---

#### **Algorithm 2: POP Operation**

**Step 1:** Start  
**Step 2:** Check if `top == -1`  
   If **True** → Print "Stack Underflow!" and return None  
**Step 3:** Store `item = stack[top]`  
**Step 4:** Decrement `top` by 1 (`top = top - 1`)  
**Step 5:** Print "item popped from stack"  
**Step 6:** Return `item`  
**Step 7:** Stop

---

#### **Algorithm 3: PEEK Operation**

**Step 1:** Start  
**Step 2:** If `top == -1`, Print "Stack is empty." and return None  
**Step 3:** Print "Top element is:" `stack[top]`  
**Step 4:** Return `stack[top]`  
**Step 5:** Stop

---

#### **Algorithm 4: DISPLAY Operation**

**Step 1:** Start  
**Step 2:** If `top == -1`, Print "Stack is empty." and Stop  
**Step 3:** Print "Stack elements (Top to Bottom):"  
**Step 4:** For `i` from `top` down to `0` (decrement by 1):  
   Print `stack[i]`  
**Step 5:** Stop

---

#### **Algorithm 5: IS_EMPTY**

**Step 1:** Start  
**Step 2:** If `top == -1` return **True** else return **False**  
**Step 3:** Stop

---

#### **Algorithm 6: IS_FULL**

**Step 1:** Start  
**Step 2:** If `top == size - 1` return **True** else return **False**  
**Step 3:** Stop

---

---

### **2. For Second Code (Python List Implementation)**

#### **Algorithm 1: PUSH Operation**

**Step 1:** Start  
**Step 2:** Check if `len(stack) == size`  
   If **True** → Print "Stack Overflow!" and Stop  
**Step 3:** Append value → `stack.append(value)`  
**Step 4:** Print "value pushed into stack"  
**Step 5:** Stop

---

#### **Algorithm 2: POP Operation**

**Step 1:** Start  
**Step 2:** Check if `len(stack) == 0`  
   If **True** → Print "Stack Underflow!" and return None  
**Step 3:** Remove and store `item = stack.pop()`  
**Step 4:** Print "item popped from stack"  
**Step 5:** Return `item`  
**Step 6:** Stop

---

#### **Algorithm 3: PEEK Operation**

**Step 1:** Start  
**Step 2:** If `len(stack) == 0`, Print "Stack is empty." and return None  
**Step 3:** Print "Top element is:" `stack[-1]`  
**Step 4:** Return `stack[-1]`  
**Step 5:** Stop

---

#### **Algorithm 4: DISPLAY Operation**

**Step 1:** Start  
**Step 2:** If `len(stack) == 0`, Print "Stack is empty." and Stop  
**Step 3:** Print "Stack elements (Top to Bottom):"  
**Step 4:** For each item in **reversed(stack)**:  
   Print item  
**Step 5:** Stop

---

#### **Algorithm 5: IS_EMPTY**

**Step 1:** Start  
**Step 2:** If `len(stack) == 0` → Print "Stack is empty." and return True  
**Step 3:** Else Print "Stack is not empty." and return False  
**Step 4:** Stop

---

#### **Algorithm 6: IS_FULL**

**Step 1:** Start  
**Step 2:** If `len(stack) == size` → Print "Stack is Full." and return True  
**Step 3:** Else Print "Stack is not Full." and return False  
**Step 4:** Stop

---

### **Recommendation for Exam:**

- Use the **first version** (`self.top = -1`) in exams — it is more conceptual and preferred.
- Always write **Algorithm + Code + Example** when asked to implement Stack.
- Draw diagram of stack while explaining.

Would you like me to give you:
- Full **algorithm + code + complexity** for all operations in one place?
- Linked List implementation with algorithms?

Just tell me what you need next!