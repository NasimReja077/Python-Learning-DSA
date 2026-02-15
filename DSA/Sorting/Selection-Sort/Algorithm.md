# ✅ Selection Sort – Dry Run

Example Array:
A = [64, 25, 12, 22, 11]
n = 5

---

### 🔹 Pass 1 (i = 0)

Minimum element in whole array = 11
Swap 64 and 11

Array becomes:
[11, 25, 12, 22, 64]

---

### 🔹 Pass 2 (i = 1)

Minimum element from index 1 to 4 = 12
Swap 25 and 12

Array becomes:
[11, 12, 25, 22, 64]

---

### 🔹 Pass 3 (i = 2)

Minimum element from index 2 to 4 = 22
Swap 25 and 22

Array becomes:
[11, 12, 22, 25, 64]

---

### 🔹 Pass 4 (i = 3)

Minimum element from index 3 to 4 = 25
Swap 25 and 25 (no change)

Array becomes:
[11, 12, 22, 25, 64]

---

### ✅ Final Sorted Array:

[11, 12, 22, 25, 64]

---

# ✍️ Short 5-Mark Answer (Exam Ready)

### Definition:

Selection Sort is a comparison-based sorting technique that repeatedly selects the smallest element from the unsorted portion and places it at the correct position.

### Algorithm:

1. Start
2. For i = 0 to n−2
   3.  Set min_index = i
   4.  For j = i+1 to n−1
   5.    If A[j] < A[min_index]
   6.      min_index = j
   7.  Swap A[i] and A[min_index]
3. Stop

# ✅ Algorithm: Selection Sort

**Algorithm: SELECTION_SORT(A, n)**
*(Where A is array and n is number of elements)*

---

### Step 1: Start

### Step 2: For i ← 0 to n − 2 do

  Step 2.1: Set min_index ← i

  Step 2.2: For j ← i + 1 to n − 1 do

    If A[j] < A[min_index] then
      Set min_index ← j

  Step 2.3: Swap A[i] and A[min_index]

### Step 3: Stop

---
**Algorithm: SELECTION SORT**  
(Sorts an array in ascending order)

**Step 1:** Start

**Step 2:** Set i = 0

**Step 3:** Repeat while i < (n – 1)  
  → If FALSE, go to Step 10

**Step 4:** Set minIndex = i

**Step 5:** Set j = i + 1

**Step 6:** Repeat while j < n  
  → If FALSE, go to Step 9

**Step 7:** If array[j] < array[minIndex]  
  → If TRUE, set minIndex = j

**Step 8:** Increment j by 1  
  → Go back to Step 6

**Step 9:** If minIndex ≠ i  
  → If TRUE, Swap array[i] with array[minIndex]

**Step 10:** Increment i by 1  
  → Go back to Step 3

**Step 11:** Stop

---

### Slightly more compact version (still same style)

**Algorithm: SELECTION SORT**

**Step 1:** Start

**Step 2:** For i = 0 to n–2 repeat Steps 3 to 7

**Step 3:**   minIndex ← i

**Step 4:**   For j = i+1 to n–1 repeat Steps 5 to 6

**Step 5:**     If array[j] < array[minIndex]  
    → If TRUE, minIndex ← j

**Step 6:**   (end of inner loop)

**Step 7:**   If minIndex ≠ i  
    → If TRUE, Swap array[i] ↔ array[minIndex]

**Step 8:** Stop

---
### Time Complexity:

* Best Case: O(n²)
* Average Case: O(n²)
* Worst Case: O(n²)

### Space Complexity:

O(1) (In-place sorting)