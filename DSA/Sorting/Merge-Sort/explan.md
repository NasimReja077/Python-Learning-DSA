# Complete Line-by-Line Explanation: Merge Sort

I'll provide an extremely detailed explanation with comprehensive diagrams showing every step.

---

## Complete Code with Line Numbers

```python
def Divide(arr, l, r):                      # Line 1
    if (l < r):                             # Line 2
        m = (l + r) // 2                   # Line 3
        Divide(arr, l, m)                   # Line 4
        Divide(arr, m + 1, r)               # Line 5
        merge(arr, l, m, r)                 # Line 6
                                            # Line 7 (blank)
def merge(arr, l, m, r):                    # Line 8
    s1 = m - l + 1                          # Line 9
    s2 = r - m                              # Line 10
                                            # Line 11 (blank)
    L_list = [0] * s1                       # Line 12
    R_list = [0] * s2                       # Line 13
                                            # Line 14 (blank)
    for i in range(s1):                     # Line 15
        L_list[i] = arr[l + i]              # Line 16
                                            # Line 17 (blank)
    for j in range(s2):                     # Line 18
        R_list[j] = arr[m + 1 + j]         # Line 19
                                            # Line 20 (blank)
    i = j = 0                               # Line 21
    k = l                                   # Line 22
                                            # Line 23 (blank)
    while (i < s1 and j < s2):             # Line 24
        if (L_list[i] < R_list[j]):         # Line 25
            arr[k] = L_list[i]              # Line 26
            i = i + 1                       # Line 27
            k = k + 1                       # Line 28
        else:                               # Line 29
            arr[k] = R_list[j]              # Line 30
            j = j + 1                       # Line 31
            k = k + 1                       # Line 32
                                            # Line 33 (blank)
    while (i < s1):                         # Line 34
        arr[k] = L_list[i]                  # Line 35
        i = i + 1                           # Line 36
        k = k + 1                           # Line 37
                                            # Line 38 (blank)
    while (j < s2):                         # Line 39
        arr[k] = R_list[j]                  # Line 40
        j = j + 1                           # Line 41
        k = k + 1                           # Line 42
                                            # Line 43 (blank)
# Driver code                               # Line 44
arr = [21, 45, 24, 89, 7, 5, 10]           # Line 45
Divide(arr, 0, len(arr) - 1)               # Line 46
print(arr)                                  # Line 47
```

---

# OVERVIEW: What is Merge Sort?

```
MERGE SORT = DIVIDE + CONQUER + MERGE

Step 1: DIVIDE array into two halves
Step 2: CONQUER (recursively sort each half)
Step 3: MERGE sorted halves back together

KEY IDEA:
It's easier to merge two SORTED arrays
than to sort one UNSORTED array!
```

---

## LINE 45: Initialize Array

```python
arr = [21, 45, 24, 89, 7, 5, 10]
```

**Visual:**
```
Index:    0    1    2    3   4   5   6
       ┌────┬────┬────┬────┬───┬───┬────┐
arr =  │ 21 │ 45 │ 24 │ 89 │ 7 │ 5 │ 10 │
       └────┴────┴────┴────┴───┴───┴────┘

Total elements: 7
```

---

## LINE 46: First Call to Divide

```python
Divide(arr, 0, len(arr) - 1)
```

**Execution:**
```
len(arr) = 7
len(arr) - 1 = 6

Divide(arr, 0, 6)

Parameters:
• arr = [21, 45, 24, 89, 7, 5, 10]
• l = 0 (left index)
• r = 6 (right index)
```

---

# COMPLETE DIVIDE PHASE

## Big Picture: Full Recursion Tree

```
                    Divide(0, 6)
                    [21,45,24,89,7,5,10]
                   /                   \
          Divide(0,3)              Divide(4,6)
         [21,45,24,89]               [7,5,10]
          /       \                  /      \
    Divide(0,1)  Divide(2,3)   Divide(4,5) Divide(6,6)
    [21,45]      [24,89]        [7,5]        [10]
     /    \       /    \        /    \
 D(0,0) D(1,1) D(2,2) D(3,3) D(4,4) D(5,5)
  [21]   [45]   [24]   [89]   [7]    [5]
  
Then MERGE phase (bottom to top):
[21,45] [24,89] [7,5] merged step by step
```

---

# DIVIDE FUNCTION: LINE BY LINE

## LINE 1: Function Definition

```python
def Divide(arr, l, r):
```

**Parameters:**
```
arr → The array to sort
l   → Left index (start of current portion)
r   → Right index (end of current portion)
```

---

## First Call: Divide(arr, 0, 6)

**State:**
```
arr = [21, 45, 24, 89, 7, 5, 10]
l = 0
r = 6
```

---

## LINE 2: Check Base Case

```python
if (l < r):
```

**What it does:**
- Checks if there are at least 2 elements to sort
- When l == r: only 1 element (already sorted!)
- When l < r: more than 1 element (need to divide)

**In Our Case:**
```
l = 0, r = 6
0 < 6 → TRUE ✓

Continue dividing
```

**Base Case Explained:**
```
┌─────────────────────────────────────┐
│  BASE CASE: l >= r                  │
│  (When array has 0 or 1 element)    │
│                                     │
│  Example: Divide(arr, 3, 3)         │
│  l = 3, r = 3                       │
│  3 < 3 → FALSE                      │
│  → Return immediately (do nothing)  │
│                                     │
│  Single element is always sorted!   │
└─────────────────────────────────────┘
```

---

## LINE 3: Find Middle Point

```python
m = (l + r) // 2
```

**Execution:**
```
m = (0 + 6) // 2
m = 6 // 2
m = 3

Middle index = 3
```

**Visual:**
```
Index:  0   1   2   3   4   5   6
       ┌────┬────┬────┬────┬───┬───┬────┐
arr =  │ 21 │ 45 │ 24 │ 89 │ 7 │ 5 │ 10 │
       └────┴────┴────┴────┴───┴───┴────┘
        ▲              ▲              ▲
        l=0           m=3            r=6
        
Left half: arr[0..3] = [21, 45, 24, 89]
Right half: arr[4..6] = [7, 5, 10]
```

**Why // 2?**
```
// is integer division (floor division)
(0 + 6) // 2 = 3 (not 3.0)
Always gives whole number index
```

---

## LINE 4: Recursive Call - Left Half

```python
Divide(arr, l, m)
```

**Execution:**
```
Divide(arr, 0, 3)

Recursively sort left half:
[21, 45, 24, 89]
```

**Call Stack:**
```
┌─────────────────────────────┐
│  Divide(arr, 0, 3)  ← NEW   │
├─────────────────────────────┤
│ Divide(arr, 0, 6)  ← waiting│
└─────────────────────────────┘
```

---

## Recursive Calls: Dividing Left Half

### **Divide(arr, 0, 3)**

```
l=0, r=3
m = (0+3)//2 = 1

Left:  arr[0..1] = [21, 45]
Right: arr[2..3] = [24, 89]
```

**Visual:**
```
Index:  0   1   2   3
       ┌────┬────┬────┬────┐
       │ 21 │ 45 │ 24 │ 89 │
       └────┴────┴────┴────┘
        ▲    ▲         ▲
        l   m=1        r=3
```

---

### **Divide(arr, 0, 1)**

```
l=0, r=1
m = (0+1)//2 = 0

Left:  arr[0..0] = [21]
Right: arr[1..1] = [45]
```

**Visual:**
```
Index:  0   1
       ┌────┬────┐
       │ 21 │ 45 │
       └────┴────┘
        ▲▲   ▲
       l=m=0 r=1
```

---

### **Divide(arr, 0, 0) → BASE CASE**

```
l=0, r=0
l < r → 0 < 0 → FALSE

Return immediately!
Single element [21] is sorted
```

---

### **Divide(arr, 1, 1) → BASE CASE**

```
l=1, r=1
l < r → 1 < 1 → FALSE

Return immediately!
Single element [45] is sorted
```

---

### **merge(arr, 0, 0, 1) called!**

Now we merge [21] and [45]

---

# MERGE FUNCTION: LINE BY LINE

## merge(arr, l=0, m=0, r=1)

**State:**
```
arr = [21, 45, 24, 89, 7, 5, 10]
l = 0, m = 0, r = 1

Left portion: arr[0..0] = [21]
Right portion: arr[1..1] = [45]
```

---

## LINE 9: Calculate Left Subarray Size

```python
s1 = m - l + 1
```

**Execution:**
```
s1 = m - l + 1
s1 = 0 - 0 + 1
s1 = 1

Left subarray has 1 element
```

**Formula Explained:**
```
Elements from l to m (inclusive):
Indices: l, l+1, l+2, ..., m
Count: m - l + 1

Example: l=0, m=2
Indices: 0, 1, 2 → Count = 3
m - l + 1 = 2 - 0 + 1 = 3 ✓
```

---

## LINE 10: Calculate Right Subarray Size

```python
s2 = r - m
```

**Execution:**
```
s2 = r - m
s2 = 1 - 0
s2 = 1

Right subarray has 1 element
```

**Formula Explained:**
```
Elements from m+1 to r (inclusive):
Indices: m+1, m+2, ..., r
Count: r - m

Example: m=2, r=5
Indices: 3, 4, 5 → Count = 3
r - m = 5 - 2 = 3 ✓
```

---

## LINE 12-13: Create Temporary Arrays

```python
L_list = [0] * s1
R_list = [0] * s2
```

**Execution:**
```
L_list = [0] * 1 = [0]
R_list = [0] * 1 = [0]
```

**Visual:**
```
L_list: ┌───┐
        │ 0 │  ← placeholder
        └───┘

R_list: ┌───┐
        │ 0 │  ← placeholder
        └───┘
```

---

## LINES 15-16: Copy Left Portion to L_list

```python
for i in range(s1):
    L_list[i] = arr[l + i]
```

**Execution:**
```
s1 = 1, range(1) = [0]

i = 0:
    L_list[0] = arr[l + 0]
    L_list[0] = arr[0 + 0]
    L_list[0] = arr[0]
    L_list[0] = 21
```

**Visual:**
```
arr:    ┌────┬────┬────┬────┬───┬───┬────┐
        │ 21 │ 45 │ 24 │ 89 │ 7 │ 5 │ 10 │
        └────┴────┴────┴────┴───┴───┴────┘
          ▲
         arr[0] = 21 (copy to L_list)

L_list: ┌────┐
        │ 21 │  ← Copied!
        └────┘
```

---

## LINES 18-19: Copy Right Portion to R_list

```python
for j in range(s2):
    R_list[j] = arr[m + 1 + j]
```

**Execution:**
```
s2 = 1, range(1) = [0]

j = 0:
    R_list[0] = arr[m + 1 + 0]
    R_list[0] = arr[0 + 1 + 0]
    R_list[0] = arr[1]
    R_list[0] = 45
```

**Visual:**
```
arr:    ┌────┬────┬────┬────┬───┬───┬────┐
        │ 21 │ 45 │ 24 │ 89 │ 7 │ 5 │ 10 │
        └────┴────┴────┴────┴───┴───┴────┘
               ▲
             arr[1] = 45 (copy to R_list)

R_list: ┌────┐
        │ 45 │  ← Copied!
        └────┘
        
Now:
L_list = [21]
R_list = [45]
```

---

## LINE 21: Initialize Pointers

```python
i = j = 0
```

**Execution:**
```
i = 0 (pointer for L_list)
j = 0 (pointer for R_list)
```

---

## LINE 22: Initialize k

```python
k = l
```

**Execution:**
```
k = l = 0

k points to where in arr we write merged elements
```

**Visual:**
```
L_list: ┌────┐     R_list: ┌────┐
        │ 21 │              │ 45 │
        └────┘              └────┘
          ▲i=0                ▲j=0

arr:    ┌────┬────┬────┬────┬───┬───┬────┐
        │ 21 │ 45 │ 24 │ 89 │ 7 │ 5 │ 10 │
        └────┴────┴────┴────┴───┴───┴────┘
          ▲k=0
```

---

## LINE 24-32: Main Merge Loop

```python
while (i < s1 and j < s2):
    if (L_list[i] < R_list[j]):
        arr[k] = L_list[i]
        i = i + 1
        k = k + 1
    else:
        arr[k] = R_list[j]
        j = j + 1
        k = k + 1
```

**Purpose:**
```
Compare elements from L_list and R_list
Place smaller one into arr[k]
```

---

### **Merge Iteration 1: i=0, j=0**

**LINE 24: Check Loop Condition**
```
i < s1 and j < s2
0 < 1 and 0 < 1
TRUE ✓
```

**LINE 25: Compare**
```
L_list[0] < R_list[0]
21 < 45
TRUE ✓
```

**LINE 26-28: Place L_list element**
```
arr[k] = L_list[i]
arr[0] = 21
i = 0 + 1 = 1
k = 0 + 1 = 1
```

**Visual:**
```
L_list: ┌────┐     R_list: ┌────┐
        │ 21 │              │ 45 │
        └────┘              └────┘
          ▲i=0                ▲j=0
          (picked)
          
arr:    ┌────┬────┬────┬────┬───┬───┬────┐
        │ 21 │ 45 │ 24 │ 89 │ 7 │ 5 │ 10 │
        └────┴────┴────┴────┴───┴───┴────┘
          ✓    ▲k=1
          
21 already in correct place!
```

---

### **Check Loop Again: i=1, j=0**

```
i < s1 and j < s2
1 < 1 → FALSE

Exit main merge loop
(i has reached end of L_list)
```

---

## LINE 34-37: Copy Remaining Left Elements

```python
while (i < s1):
    arr[k] = L_list[i]
    i = i + 1
    k = k + 1
```

**Check:**
```
i < s1 → 1 < 1 → FALSE

Nothing to copy from L_list
(already exhausted)
```

---

## LINE 39-42: Copy Remaining Right Elements

```python
while (j < s2):
    arr[k] = R_list[j]
    j = j + 1
    k = k + 1
```

**Iteration: j=0**
```
j < s2 → 0 < 1 → TRUE

arr[k] = R_list[j]
arr[1] = R_list[0]
arr[1] = 45
j = 0 + 1 = 1
k = 1 + 1 = 2
```

**Visual:**
```
R_list: ┌────┐
        │ 45 │
        └────┘
          ▲j=0
          (picked)
          
arr:    ┌────┬────┬────┬────┬───┬───┬────┐
        │ 21 │ 45 │ 24 │ 89 │ 7 │ 5 │ 10 │
        └────┴────┴────┴────┴───┴───┴────┘
          ✓    ✓    ▲k=2
```

**After merge(0, 0, 1):**
```
arr[0..1] = [21, 45] ← SORTED!
```

---

# CONTINUING DIVIDE PHASE

## Divide(arr, 2, 3)

```
l=2, r=3
m = (2+3)//2 = 2

Left:  arr[2..2] = [24]  → base case
Right: arr[3..3] = [89]  → base case
Then:  merge(arr, 2, 2, 3)
```

**merge(arr, 2, 2, 3):**
```
L_list = [24]
R_list = [89]

Compare: 24 < 89 → Place 24 first
Then: Place 89

Result: arr[2..3] = [24, 89] ✓
```

**Array after both merges:**
```
Index:  0   1   2   3   4   5   6
       ┌────┬────┬────┬────┬───┬───┬────┐
arr = │ 21 │ 45 │ 24 │ 89 │ 7 │ 5 │ 10 │
       └────┴────┴────┴────┴───┴───┴────┘
        └──┬──┘  └──┬──┘
         [21,45] [24,89]
         sorted  sorted
```

---

## merge(arr, l=0, m=1, r=3)

**Now merge [21,45] with [24,89]!**

```
s1 = m - l + 1 = 1 - 0 + 1 = 2
s2 = r - m = 3 - 1 = 2

L_list = [21, 45]
R_list = [24, 89]
```

**Copying Phase:**
```
L_list: ┌────┬────┐
        │ 21 │ 45 │  ← copied from arr[0..1]
        └────┴────┘

R_list: ┌────┬────┐
        │ 24 │ 89 │  ← copied from arr[2..3]
        └────┴────┘
```

**Initial state:**
```
L_list: ┌────┬────┐     R_list: ┌────┬────┐
        │ 21 │ 45 │              │ 24 │ 89 │
        └────┴────┘              └────┴────┘
          ▲i=0                     ▲j=0

arr:    ┌────┬────┬────┬────┬───┬───┬────┐
        │ 21 │ 45 │ 24 │ 89 │ 7 │ 5 │ 10 │
        └────┴────┴────┴────┴───┴───┴────┘
          ▲k=0
```

---

### **Merge Iterations for [21,45] vs [24,89]**

**Iteration 1: i=0, j=0**
```
Compare L_list[0] vs R_list[0]:
21 < 24? → TRUE ✓

Place 21 at arr[0]
i=1, k=1
```

**After Iteration 1:**
```
arr:    ┌────┬────┬────┬────┬───┬───┬────┐
        │ 21 │ 45 │ 24 │ 89 │ 7 │ 5 │ 10 │
        └────┴────┴────┴────┴───┴───┴────┘
          ✓    ▲k=1
```

---

**Iteration 2: i=1, j=0**
```
Compare L_list[1] vs R_list[0]:
45 < 24? → FALSE

Place 24 at arr[1]
j=1, k=2
```

**After Iteration 2:**
```
arr:    ┌────┬────┬────┬────┬───┬───┬────┐
        │ 21 │ 24 │ 24 │ 89 │ 7 │ 5 │ 10 │
        └────┴────┴────┴────┴───┴───┴────┘
          ✓    ✓    ▲k=2
```

---

**Iteration 3: i=1, j=1**
```
Compare L_list[1] vs R_list[1]:
45 < 89? → TRUE ✓

Place 45 at arr[2]
i=2, k=3
```

**After Iteration 3:**
```
arr:    ┌────┬────┬────┬────┬───┬───┬────┐
        │ 21 │ 24 │ 45 │ 89 │ 7 │ 5 │ 10 │
        └────┴────┴────┴────┴───┴───┴────┘
          ✓    ✓    ✓    ▲k=3
```

---

**Check Loop: i=2, j=1**
```
i < s1 → 2 < 2 → FALSE
Exit loop
```

**Copy remaining R_list:**
```
j=1 < s2=2 → TRUE
arr[3] = R_list[1] = 89
j=2, k=4
```

**After All Merges:**
```
arr:    ┌────┬────┬────┬────┬───┬───┬────┐
        │ 21 │ 24 │ 45 │ 89 │ 7 │ 5 │ 10 │
        └────┴────┴────┴────┴───┴───┴────┘
          ✓    ✓    ✓    ✓   
          
Left half arr[0..3] = [21, 24, 45, 89] SORTED! ✓
```

---

# DIVIDING RIGHT HALF

## Divide(arr, 4, 6)

```
l=4, r=6
m = (4+6)//2 = 5

Left:  arr[4..5] = [7, 5]
Right: arr[6..6] = [10]
```

**Visual:**
```
Index:  0   1   2   3   4   5   6
       ┌────┬────┬────┬────┬───┬───┬────┐
arr = │ 21 │ 24 │ 45 │ 89 │ 7 │ 5 │ 10 │
       └────┴────┴────┴────┴───┴───┴────┘
                          ▲    ▲       ▲
                         l=4  m=5     r=6
```

---

## Divide(arr, 4, 5)

```
l=4, r=5
m = (4+5)//2 = 4

Left:  arr[4..4] = [7]  → base case
Right: arr[5..5] = [5]  → base case
Then:  merge(arr, 4, 4, 5)
```

---

## merge(arr, l=4, m=4, r=5)

**Merging [7] with [5]:**

```
s1 = 4 - 4 + 1 = 1
s2 = 5 - 4 = 1

L_list = [7]
R_list = [5]

i=0, j=0, k=4
```

**Compare: 7 < 5? FALSE**
```
Place R_list[0] = 5 at arr[4]
j=1, k=5
```

**Copy remaining L_list:**
```
i=0 < s1=1 → TRUE
arr[5] = L_list[0] = 7
i=1, k=6
```

**Result:**
```
arr:    ┌────┬────┬────┬────┬───┬───┬────┐
        │ 21 │ 24 │ 45 │ 89 │ 5 │ 7 │ 10 │
        └────┴────┴────┴────┴───┴───┴────┘
                          ✓   ✓  
                          
arr[4..5] = [5, 7] SORTED! ✓
```

---

## Divide(arr, 6, 6) → BASE CASE

```
l=6, r=6
l < r → 6 < 6 → FALSE

Single element [10] is sorted!
```

---

## merge(arr, l=4, m=5, r=6)

**Merging [5, 7] with [10]:**

```
s1 = 5 - 4 + 1 = 2
s2 = 6 - 5 = 1

L_list = [5, 7]
R_list = [10]

i=0, j=0, k=4
```

**Iteration 1:**
```
5 < 10? YES → arr[4] = 5
i=1, k=5
```

**Iteration 2:**
```
7 < 10? YES → arr[5] = 7
i=2, k=6
```

**Exit loop (i=2, s1=2)**

**Copy remaining R_list:**
```
j=0 < s2=1 → TRUE
arr[6] = R_list[0] = 10
j=1, k=7
```

**Result:**
```
arr:    ┌────┬────┬────┬────┬───┬───┬────┐
        │ 21 │ 24 │ 45 │ 89 │ 5 │ 7 │ 10 │
        └────┴────┴────┴────┴───┴───┴────┘
                          ✓   ✓   ✓
                          
Right half arr[4..6] = [5, 7, 10] SORTED! ✓
```

---

# FINAL MERGE

## merge(arr, l=0, m=3, r=6)

**THE BIG MERGE: [21, 24, 45, 89] with [5, 7, 10]**

```
s1 = 3 - 0 + 1 = 4
s2 = 6 - 3 = 3

L_list = [21, 24, 45, 89]
R_list = [5, 7, 10]
```

**Copy to Temp Arrays:**
```
L_list: ┌────┬────┬────┬────┐
        │ 21 │ 24 │ 45 │ 89 │  ← arr[0..3]
        └────┴────┴────┴────┘

R_list: ┌───┬───┬────┐
        │ 5 │ 7 │ 10 │  ← arr[4..6]
        └───┴───┴────┘
```

**Initial State:**
```
L_list: ┌────┬────┬────┬────┐     R_list: ┌───┬───┬────┐
        │ 21 │ 24 │ 45 │ 89 │              │ 5 │ 7 │ 10 │
        └────┴────┴────┴────┘              └───┴───┴────┘
          ▲i=0                               ▲j=0

arr:    ┌────┬────┬────┬────┬───┬───┬────┐
        │ 21 │ 24 │ 45 │ 89 │ 5 │ 7 │ 10 │
        └────┴────┴────┴────┴───┴───┴────┘
          ▲k=0
```

---

### **Main Merge Loop Iterations**

**Iteration 1: i=0, j=0**
```
L[0]=21 vs R[0]=5
21 < 5? → FALSE

arr[0] = R[0] = 5
j=1, k=1
```

**Iteration 2: i=0, j=1**
```
L[0]=21 vs R[1]=7
21 < 7? → FALSE

arr[1] = R[1] = 7
j=2, k=2
```

**Iteration 3: i=0, j=2**
```
L[0]=21 vs R[2]=10
21 < 10? → FALSE

arr[2] = R[2] = 10
j=3, k=3
```

**Check: j=3 < s2=3 → FALSE**
```
Exit main loop
(R_list exhausted)
```

**Copy remaining L_list (i=0 to 3):**

```
i=0: arr[3] = L[0] = 21, i=1, k=4
i=1: arr[4] = L[1] = 24, i=2, k=5
i=2: arr[5] = L[2] = 45, i=3, k=6
i=3: arr[6] = L[3] = 89, i=4, k=7
```

---

**Step-by-Step Final Merge:**
```
Step 1: Compare 21 vs 5
        5 is smaller → Place 5
        arr: [5, 24, 45, 89, 5, 7, 10]
              ✓

Step 2: Compare 21 vs 7
        7 is smaller → Place 7
        arr: [5, 7, 45, 89, 5, 7, 10]
              ✓  ✓

Step 3: Compare 21 vs 10
        10 is smaller → Place 10
        arr: [5, 7, 10, 89, 5, 7, 10]
              ✓  ✓   ✓

Step 4: R_list exhausted
        Copy remaining L_list: [21, 24, 45, 89]
        arr: [5, 7, 10, 21, 24, 45, 89]
              ✓  ✓   ✓   ✓   ✓   ✓   ✓
              
FULLY SORTED!
```

---

# COMPLETE MERGE TREE

## Full Visualization

```
DIVIDE PHASE (Top to Bottom):
═══════════════════════════════════════════════════

Level 0: [21, 45, 24, 89, 7, 5, 10]
                    │
          ┌─────────┴──────────┐
          │                    │
Level 1: [21,45,24,89]    [7,5,10]
          │                    │
     ┌────┴────┐          ┌────┴────┐
     │         │          │         │
Level 2: [21,45] [24,89] [7,5]   [10]
          │         │       │
     ┌────┴────┐ ┌──┴──┐ ┌──┴──┐
     │         │ │     │ │     │
Level 3: [21][45][24][89][7] [5]

═══════════════════════════════════════════════════
MERGE PHASE (Bottom to Top):
═══════════════════════════════════════════════════

Level 3: [21][45][24][89][7][5]
          │    │   │    │  │  │
Level 2: [21,45] [24,89] [5,7]  [10]
              │       │       │
Level 1:  [21,24,45,89]    [5,7,10]
                   │           │
Level 0:  [5, 7, 10, 21, 24, 45, 89]

═══════════════════════════════════════════════════
FINAL RESULT: [5, 7, 10, 21, 24, 45, 89] ✓
═══════════════════════════════════════════════════
```

---

## LINE 47: Print Final Result

```python
print(arr)
```

**Console Output:**
```
┌────────────────────────────────────────────┐
│  [5, 7, 10, 21, 24, 45, 89]                │
└────────────────────────────────────────────┘
```

---

# CALL STACK VISUALIZATION

```
Order of function calls:

1.  Divide(0,6)
2.    Divide(0,3)
3.      Divide(0,1)
4.        Divide(0,0) ← returns (base)
5.        Divide(1,1) ← returns (base)
6.      merge(0,0,1)  ← [21,45] sorted
7.      Divide(2,3)
8.        Divide(2,2) ← returns (base)
9.        Divide(3,3) ← returns (base)
10.     merge(2,2,3)  ← [24,89] sorted
11.   merge(0,1,3)    ← [21,24,45,89] sorted
12.   Divide(4,6)
13.     Divide(4,5)
14.       Divide(4,4) ← returns (base)
15.       Divide(5,5) ← returns (base)
16.     merge(4,4,5)  ← [5,7] sorted
17.     Divide(6,6)   ← returns (base)
18.   merge(4,5,6)    ← [5,7,10] sorted
19. merge(0,3,6)      ← FINAL SORT COMPLETE!
```

---

## Complexity Analysis

```
TIME COMPLEXITY:
┌──────────────┬─────────────┬──────────┐
│     Case     │    Time     │  Reason  │
├──────────────┼─────────────┼──────────┤
│ Best Case    │  O(n log n) │ Always   │
│ Average Case │  O(n log n) │ divides  │
│ Worst Case   │  O(n log n) │ equally  │
└──────────────┴─────────────┴──────────┘

SPACE COMPLEXITY:
O(n) - Extra arrays L_list and R_list

LOG n LEVELS of division:
n=7: log₂(7) ≈ 3 levels
n=8: log₂(8) = 3 levels
```

---

## 🎉 Complete Understanding!

**You now understand:**
- ✅ Divide function splits array recursively
- ✅ Base case stops recursion (l >= r)
- ✅ Middle point formula `(l+r)//2`
- ✅ Left and right recursive calls
- ✅ Merge function combines sorted halves
- ✅ s1 and s2 calculate subarray sizes
- ✅ L_list and R_list store temp copies
- ✅ Three-pointer merge (i, j, k)
- ✅ Main loop compares and places smaller
- ✅ Leftover loops copy remaining elements
- ✅ Complete recursion tree visualization
- ✅ Time: O(n log n), Space: O(n)

**Key Insight:**
```
Merge Sort is efficient because:
1. Division always splits in half (log n levels)
2. Each merge level processes all n elements
3. Total: n × log n operations!

Divide & Conquer at its best! 🚀
```