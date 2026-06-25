# Complete Algorithm for Bubble Sort

---
```
Algorithm: Bubble Sort (Optimized Version)

Step 1: Start

Step 2: Read array A of size n

Step 3: For i ← 0 to n-2 do
    Step 3.1: swapped ← false

    Step 3.2: For j ← 0 to n-i-2 do
        If A[j] > A[j+1] then
            Swap A[j] ↔ A[j+1]
            swapped ← true

    Step 3.3: If swapped = false then
        Break / Exit the outer loop
        (No more swaps needed → rest of array is already sorted)

Step 4: Stop
```
---

## ALGORITHM 1: Descriptive Step-by-Step

```
ALGORITHM: BubbleSort
INPUT: An array arr of n elements
OUTPUT: Array arr sorted in ascending order

BEGIN
    Step 1: Get the length of array
            n ← length of arr
    
    Step 2: Repeat for each pass (i from 0 to n-2)
            [Outer loop controls number of passes]
            
            Step 2.1: For each adjacent pair in unsorted portion
                      (j from 0 to n-2-i)
                      [Inner loop for comparisons]
                      
                      Step 2.1.1: Compare adjacent elements
                                  IF arr[j] > arr[j+1] THEN
                                      Swap arr[j] and arr[j+1]
                                  END IF
            
            Step 2.2: After this pass, largest element 
                      in unsorted portion is now in correct position
    
    Step 3: Return sorted array arr
END
```

---

## ALGORITHM 2: Pseudocode Format

```pseudocode
ALGORITHM BubbleSort(arr[], n)
// Input: arr[] - array to be sorted, n - size of array
// Output: arr[] - sorted array in ascending order

BEGIN
    // Outer loop: n-1 passes
    FOR i = 0 TO n-2 DO
        
        // Inner loop: compare adjacent elements
        FOR j = 0 TO n-2-i DO
            
            // Compare and swap if needed
            IF arr[j] > arr[j+1] THEN
                SWAP(arr[j], arr[j+1])
            END IF
            
        END FOR
        
    END FOR
    
    RETURN arr
END
```

---

## ALGORITHM 3: Detailed with Variables

```
ALGORITHM: BubbleSort(arr)

INPUT: 
    arr - An unsorted array of comparable elements
    
OUTPUT:
    arr - The same array sorted in ascending order
    
VARIABLES:
    n - Number of elements in array
    i - Outer loop counter (pass number)
    j - Inner loop counter (comparison index)
    temp - Temporary variable for swapping

STEPS:
1. Initialize:
   n ← length(arr)

2. FOR i ← 0 TO n-2 DO
      // Pass i: Move (i+1)th largest element to position
      
      2.1 FOR j ← 0 TO (n-2-i) DO
            // Compare adjacent elements
            
            2.1.1 IF arr[j] > arr[j+1] THEN
                     // Swap elements
                     temp ← arr[j]
                     arr[j] ← arr[j+1]
                     arr[j+1] ← temp
                  END IF
                  
      END FOR
      
   END FOR

3. RETURN arr

END ALGORITHM
```

---

## ALGORITHM 4: Optimized Version (Early Exit)

```pseudocode
ALGORITHM BubbleSortOptimized(arr[], n)
// Optimization: Stop early if array becomes sorted

BEGIN
    FOR i = 0 TO n-2 DO
        swapped ← FALSE
        
        FOR j = 0 TO n-2-i DO
            IF arr[j] > arr[j+1] THEN
                SWAP(arr[j], arr[j+1])
                swapped ← TRUE
            END IF
        END FOR
        
        // If no swaps occurred, array is sorted
        IF swapped = FALSE THEN
            BREAK
        END IF
        
    END FOR
    
    RETURN arr
END
```

---

## ALGORITHM 5: Flowchart Description

```
┌─────────────────────────────────────────┐
│              START                      │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│  Input: Array arr[]                     │
│  Get n = length of arr                  │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│  Initialize: i = 0                      │
└──────────────┬──────────────────────────┘
               │
               ▼
        ┌──────────────┐
        │  i < n-1?    │──────NO────────┐
        └──────┬───────┘                │
               │YES                     │
               ▼                         │
┌─────────────────────────────────────┐  │
│  Initialize: j = 0                  │  │
└──────────────┬──────────────────────┘  │
               │                         │
               ▼                         │
        ┌──────────────┐                 │
        │ j < n-1-i?   │──NO──┐         │
        └──────┬───────┘      │         │
               │YES           │         │
               ▼              │         │
        ┌──────────────┐      │         │
        │ arr[j] >     │      │         │
        │ arr[j+1]?    │      │         │
        └──────┬───────┘      │         │
               │              │         │
         ┌─────┴─────┐        │         │
         │           │        │         │
        YES         NO        │         │
         │           │        │         │
         ▼           │        │         │
    ┌────────┐      │        │         │
    │  SWAP  │      │        │         │
    │arr[j]  │      │        │         │
    │arr[j+1]│      │        │         │
    └────┬───┘      │        │         │
         │          │        │         │
         └──────────┴────┐   │         │
                         │   │         │
                         ▼   │         │
                    ┌────────┴──┐      │
                    │  j = j+1  │      │
                    └────────┬──┘      │
                             │         │
                    ┌────────┴─────────┘
                    │
                    ▼
               ┌─────────┐
               │ i = i+1 │
               └────┬────┘
                    │
                    └──────┐
                           │
                           ▼
                    ┌─────────────┐
                    │ Output:     │
                    │ Sorted arr  │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │     END     │
                    └─────────────┘
```

---

## ALGORITHM 6: Mathematical Notation

```
ALGORITHM BubbleSort(A)

Input: A = {a₁, a₂, a₃, ..., aₙ}
Output: Sorted array A' where A'[i] ≤ A'[i+1] ∀ i ∈ {1, 2, ..., n-1}

1. FOR i ∈ {0, 1, 2, ..., n-2}:
   
   2. FOR j ∈ {0, 1, 2, ..., n-2-i}:
      
      3. IF A[j] > A[j+1]:
            A[j] ⟷ A[j+1]  (swap)
      
   END FOR
   
END FOR

RETURN A
```

---

## ALGORITHM 7: Structured English

```
BUBBLE SORT ALGORITHM

Purpose: Sort an array in ascending order by repeatedly 
         comparing adjacent elements and swapping them 
         if they are in wrong order

Input: Unsorted array

Process:
1. START with the entire array

2. MAKE multiple passes through array:
   - In each pass, compare adjacent elements
   - If left element > right element, SWAP them
   - Continue until end of unsorted portion
   
3. AFTER each pass:
   - One more element is in final position
   - Reduce unsorted portion by 1
   
4. REPEAT passes until array is sorted

5. STOP when no more swaps needed

Output: Sorted array in ascending order
```

---

## ALGORITHM 8: Compact Form

```
Algorithm: Bubble Sort

for i = 0 to n-2:
    for j = 0 to n-2-i:
        if arr[j] > arr[j+1]:
            swap(arr[j], arr[j+1])
```

---

## Key Components Explained

### **1. Loop Structure**
```
Outer Loop: for i = 0 to n-2
    Purpose: Controls number of passes
    Iterations: n-1 passes
    
Inner Loop: for j = 0 to n-2-i
    Purpose: Compares adjacent elements
    Iterations: Decreases each pass
    Formula: (n-1-i) comparisons per pass
```

### **2. Comparison**
```
if arr[j] > arr[j+1]
    Purpose: Check if elements are out of order
    Action: Swap if condition is true
```

### **3. Swap Operation**
```
Method 1 (using temp):
    temp = arr[j]
    arr[j] = arr[j+1]
    arr[j+1] = temp

Method 2 (tuple unpacking - Python):
    arr[j], arr[j+1] = arr[j+1], arr[j]

Method 3 (XOR - for integers):
    arr[j] = arr[j] XOR arr[j+1]
    arr[j+1] = arr[j] XOR arr[j+1]
    arr[j] = arr[j] XOR arr[j+1]
```

---

## Algorithm Complexity

```
TIME COMPLEXITY:
    Best Case:    O(n)     [Optimized version, already sorted]
    Average Case: O(n²)    [Random order]
    Worst Case:   O(n²)    [Reverse sorted]

SPACE COMPLEXITY:
    O(1)    [In-place sorting, only uses constant extra space]

STABILITY:
    Stable    [Maintains relative order of equal elements]
```

---

## Trace Example

```
Input: [5, 2, 8, 1, 9]

Pass 1: [5, 2, 8, 1, 9]
        [2, 5, 8, 1, 9]  (5>2, swap)
        [2, 5, 8, 1, 9]  (5<8, no swap)
        [2, 5, 1, 8, 9]  (8>1, swap)
        [2, 5, 1, 8, 9]  (8<9, no swap)
        Result: Largest (9) in position

Pass 2: [2, 5, 1, 8, 9]
        [2, 5, 1, 8, 9]  (2<5, no swap)
        [2, 1, 5, 8, 9]  (5>1, swap)
        [2, 1, 5, 8, 9]  (5<8, no swap)
        Result: Second largest (8) in position

Pass 3: [2, 1, 5, 8, 9]
        [1, 2, 5, 8, 9]  (2>1, swap)
        [1, 2, 5, 8, 9]  (2<5, no swap)
        Result: Third largest (5) in position

Pass 4: [1, 2, 5, 8, 9]
        [1, 2, 5, 8, 9]  (1<2, no swap)
        Result: Array sorted!

Output: [1, 2, 5, 8, 9]
```

---

## Invariants

```
Loop Invariant (After pass i):
    - Elements at positions [n-1-i, n-1] are sorted
    - Elements at positions [n-1-i, n-1] contain the 
      (i+1) largest elements of the array
    - All elements in positions [0, n-2-i] may still 
      need sorting

Pre-condition:
    - Array arr[] contains comparable elements

Post-condition:
    - Array arr[] is sorted in ascending order
    - arr[i] ≤ arr[i+1] for all 0 ≤ i < n-1
```

---