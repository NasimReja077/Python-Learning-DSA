**✅ Fixed & Improved Version** (Exam-Ready)

Here is the **corrected and polished** version of your algorithms. I have fixed minor logical issues, improved clarity, consistency, and made them more suitable for MAKAUT exams.

---

### **Stack Operations – Array Implementation (Top Pointer)**

#### **Algorithm 1: PUSH Operation**
**Step 1:** Start  
**Step 2:** If `top == size - 1`, then  
   Print "Stack Overflow!" and Stop  
**Step 3:** `top = top + 1`  
**Step 4:** `stack[top] = value`  
**Step 5:** (Optional) Print "value pushed successfully"  
**Step 6:** Stop  

---

#### **Algorithm 2: POP Operation**
**Step 1:** Start  
**Step 2:** If `top == -1`, then  
   Print "Stack Underflow!"  
   Return None  
**Step 3:** `item = stack[top]`  
**Step 4:** `top = top - 1`  
**Step 5:** (Optional) Print "item popped from stack"  
**Step 6:** Return `item`  
**Step 7:** Stop  

---

#### **Algorithm 3: PEEK Operation**
**Step 1:** Start  
**Step 2:** If `top == -1`, then  
   Print "Stack is Empty"  
   Return None  
**Step 3:** Return `stack[top]`  
**Step 4:** Stop  

---

#### **Algorithm 4: DISPLAY Operation**
**Step 1:** Start  
**Step 2:** If `top == -1`, then  
   Print "Stack is Empty" and Stop  
**Step 3:** Print "Stack elements (Top to Bottom):"  
**Step 4:** For `i = top` downto `0` (step -1):  
   Print `stack[i]`  
**Step 5:** Stop  

---

#### **Algorithm 5: IS_EMPTY**
**Step 1:** Start  
**Step 2:** If `top == -1` then Return **True**  
   Else Return **False**  
**Step 3:** Stop  

---

#### **Algorithm 6: IS_FULL**
**Step 1:** Start  
**Step 2:** If `top == size - 1` then Return **True**  
   Else Return **False**  
**Step 3:** Stop  

---

### **Key Fixes & Improvements Made:**

1. **Consistency** — Used `value` / `item` appropriately.
2. **Return Statements** — Clearly mentioned what is returned (very important in exams).
3. **Error Handling** — Proper messages for Overflow and Underflow.
4. **DISPLAY Loop** — Correctly written as "downto 0".
5. **Removed unnecessary prints** where not needed (kept optional for clarity).
6. **Clean Step Numbering** — Easy to write in exam.

---

### **Bonus: Recommended Class Structure (Python) for Exam**

```python
class Stack:
    def __init__(self, size=10):
        self.stack = [None] * size
        self.top = -1
        self.size = size

    def push(self, value):
        if self.top == self.size - 1:
            print("Stack Overflow!")
        else:
            self.top += 1
            self.stack[self.top] = value

    def pop(self):
        if self.top == -1:
            print("Stack Underflow!")
            return None
        item = self.stack[self.top]
        self.top -= 1
        return item

    def peek(self):
        if self.top == -1:
            print("Stack is Empty")
            return None
        return self.stack[self.top]

    def display(self):
        if self.top == -1:
            print("Stack is Empty")
            return
        print("Stack elements (Top to Bottom):")
        for i in range(self.top, -1, -1):
            print(self.stack[i])
```

---

Would you like me to also give the **Linked List version** of these algorithms?