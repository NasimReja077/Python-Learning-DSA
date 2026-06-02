# ════════════════════════════════════════════════════════════════════
#
#                    HEAP — COMPLETE IMPLEMENTATION
#
#  Covers:
#   1. MaxHeapify  (Heapify-Down / Sift-Down)
#   2. MinHeapify  (Heapify-Down / Sift-Down)
#   3. Heapify-Up  (Sift-Up / Bubble-Up)
#   4. Build Heap  (Bottom-Up approach)
#   5. Max Heap    (insert, extract_max, delete, search, min, max)
#   6. Min Heap    (insert, extract_min, delete, search, min, max)
#   7. Heap Sort
#   8. Exam Q: Build Max Heap from [80,20,90,40,100,60,120,60,50,70]
#
#  Array Index Formulas (0-based):
#    Parent     =  (i - 1) // 2
#    Left child =   2 * i  + 1
#    Right child=   2 * i  + 2
#
# ════════════════════════════════════════════════════════════════════


# ════════════════════════════════════════════════════════════════════
#  PART 1 — HEAPIFY ALGORITHMS (Standalone Functions)
# ════════════════════════════════════════════════════════════════════

# ────────────────────────────────────────────────────────────────────
#  MAX HEAPIFY  (Heapify-Down for Max Heap)
#
#  Purpose : Fix a single violation at index i.
#            Assumes both left and right subtrees are valid max heaps.
#            Pushes a small root DOWN to its correct position.
#
#  Algorithm:
#   Step 1: Set largest = i  (assume root is largest)
#   Step 2: If left child exists and arr[left] > arr[largest]
#              → update largest = left
#   Step 3: If right child exists and arr[right] > arr[largest]
#              → update largest = right
#   Step 4: If largest != i → swap arr[i] with arr[largest]
#              → recursively heapify at new position (largest)
#   Step 5: If largest == i → heap property satisfied, stop
#
#  Time  : O(log n)
#  Space : O(log n) recursive stack
# ────────────────────────────────────────────────────────────────────
def max_heapify(arr, n, i):
    """
    arr     = the array (heap stored as array)
    n       = current heap size (not total array length)
    i       = index of node that may violate max heap property
    """
    largest = i                 # assume current node is largest
    left    = 2 * i + 1        # left child index
    right   = 2 * i + 2        # right child index

    # Is left child larger than current largest?
    # left < n  → checks left child actually exists inside heap
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Is right child larger than current largest?
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not the current node → violation found
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        max_heapify(arr, n, largest)                  # fix subtree


# ────────────────────────────────────────────────────────────────────
#  MIN HEAPIFY  (Heapify-Down for Min Heap)
#
#  Same logic as MaxHeapify but looks for SMALLEST child instead.
#
#  Time  : O(log n)
#  Space : O(log n)
# ────────────────────────────────────────────────────────────────────
def min_heapify(arr, n, i):
    """
    Fixes min heap violation at index i (downward).
    Assumes both subtrees of i are valid min heaps.
    """
    smallest = i
    left     = 2 * i + 1
    right    = 2 * i + 2

    # Is left child smaller than current smallest?
    if left < n and arr[left] < arr[smallest]:
        smallest = left

    # Is right child smaller?
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)


# ────────────────────────────────────────────────────────────────────
#  HEAPIFY-UP  (Sift-Up / Bubble-Up)
#
#  Purpose : Used after INSERTION.
#            A newly inserted element at the END bubbles UP until
#            the heap property is satisfied.
#
#  Max Heap version → child should be ≤ parent → if child > parent, swap up
#  Min Heap version → child should be ≥ parent → if child < parent, swap up
#
#  Algorithm (Max Heap):
#   Step 1: Start at index i (newly inserted position)
#   Step 2: While i > 0 and arr[parent] < arr[i]:
#               swap arr[i] with arr[parent]
#               i = parent
#   Step 3: Stop when i == 0 OR parent >= child
#
#  Time  : O(log n)
#  Space : O(1)
# ────────────────────────────────────────────────────────────────────
def heapify_up_max(arr, i):
    """Bubble up for Max Heap after insertion at index i."""
    while i > 0:
        parent = (i - 1) // 2              # parent index formula
        if arr[i] > arr[parent]:           # child bigger than parent → swap
            arr[i], arr[parent] = arr[parent], arr[i]
            i = parent                     # move up
        else:
            break                          # heap property satisfied


def heapify_up_min(arr, i):
    """Bubble up for Min Heap after insertion at index i."""
    while i > 0:
        parent = (i - 1) // 2
        if arr[i] < arr[parent]:           # child smaller than parent → swap
            arr[i], arr[parent] = arr[parent], arr[i]
            i = parent
        else:
            break


# ────────────────────────────────────────────────────────────────────
#  BUILD HEAP — Bottom-Up Approach
#
#  Purpose : Convert any unsorted array into a heap in O(n) time.
#
#  Key Insight:
#    → Leaf nodes (from index n//2 to n-1) are already valid heaps.
#    → Only internal nodes (index 0 to n//2 - 1) need heapifying.
#    → Start from LAST INTERNAL NODE and go UP to root.
#    → Bottom-up ensures subtrees are fixed before their parents.
#
#  Why O(n) and not O(n log n)?
#    → Most nodes are near the bottom and only move a little.
#    → Mathematical sum of work converges to O(n).
#
#  Algorithm:
#   Step 1: Find last internal node → index = n//2 - 1
#   Step 2: FOR i FROM n//2-1 DOWN TO 0:
#               heapify(arr, n, i)
#   Step 3: Array is now a valid heap.
#
#  Time  : O(n)  ← proven mathematically
#  Space : O(log n) for recursive heapify calls
# ────────────────────────────────────────────────────────────────────
def build_max_heap(arr):
    n = len(arr)
    # Last internal (parent) node is at index n//2 - 1
    # All nodes from n//2 to n-1 are leaves (no children)
    for i in range(n // 2 - 1, -1, -1):   # n//2-1 down to 0 inclusive
        max_heapify(arr, n, i)


def build_min_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, n, i)


# ════════════════════════════════════════════════════════════════════
#  PART 2 — MAX HEAP CLASS
#  (Full operations: insert, extract, delete, search, min, max)
# ════════════════════════════════════════════════════════════════════
class MaxHeap:
    def __init__(self):
        self.heap = []          # internal array (0-based index)

    def _parent(self, i):   return (i - 1) // 2
    def _left(self, i):     return 2 * i + 1
    def _right(self, i):    return 2 * i + 2
    def size(self):         return len(self.heap)
    def is_empty(self):     return len(self.heap) == 0

    # ── PEEK MAX (O(1)) ──────────────────────────────────────────
    def peek_max(self):
        """Return maximum without removing. Root is always max."""
        if self.is_empty():
            print("  Heap is empty")
            return None
        return self.heap[0]     # root = maximum in max heap

    # ── FIND MIN (O(n)) ──────────────────────────────────────────
    def find_min(self):
        """Min is always a leaf. Must scan all leaf nodes."""
        if self.is_empty():
            return None
        n = self.size()
        # Leaf nodes are from index n//2 to n-1
        return min(self.heap[n // 2:])

    # ── FIND MAX (O(1)) ──────────────────────────────────────────
    def find_max(self):
        return self.peek_max()

    # ── INSERT (O(log n)) ────────────────────────────────────────
    def insert(self, value):
        """
        Step 1: Append value at end of array.
        Step 2: Bubble UP using heapify-up until heap property restored.
        """
        self.heap.append(value)             # place at end
        heapify_up_max(self.heap, self.size() - 1)  # bubble up

    # ── EXTRACT MAX (O(log n)) ───────────────────────────────────
    def extract_max(self):
        """
        Step 1: Save root value (maximum).
        Step 2: Move last element to root.
        Step 3: Remove last element.
        Step 4: Heapify DOWN from root to restore heap.
        Step 5: Return saved maximum.
        """
        if self.is_empty():
            print("  Heap is empty")
            return None

        n         = self.size()
        max_val   = self.heap[0]            # save max (root)
        self.heap[0] = self.heap[n - 1]    # move last to root
        self.heap.pop()                     # remove last element
        if not self.is_empty():
            max_heapify(self.heap, self.size(), 0)  # fix from root down
        return max_val

    # ── SEARCH (O(n)) ────────────────────────────────────────────
    def search(self, value):
        """
        No BST ordering → must scan entire array.
        Can prune if value > current node (it can't be in subtree).
        Simple O(n) linear scan used here.
        """
        for i, v in enumerate(self.heap):
            if v == value:
                print(f"  {value} FOUND at index {i}")
                return i
        print(f"  {value} NOT FOUND")
        return -1

    # ── DELETE ARBITRARY ELEMENT (O(log n)) ──────────────────────
    def delete(self, value):
        """
        Step 1: Find index of value. If not found, return.
        Step 2: Replace value with very large number (+∞).
        Step 3: Bubble UP (it will reach root since it's +∞).
        Step 4: Extract max (removes the +∞ = our target node).
        """
        idx = self.search(value)
        if idx == -1:
            return False

        n = self.size()
        # Replace with +infinity so it bubbles up to root
        self.heap[idx] = float('inf')
        heapify_up_max(self.heap, idx)      # bubble up to root

        # Now extract max (removes our +inf node which is at root)
        self.extract_max()
        print(f"  {value} deleted successfully")
        return True

    # ── HEAP SORT (O(n log n)) ───────────────────────────────────
    def heap_sort(self, arr):
        """
        Sort array in ASCENDING order using max heap.

        Phase 1 — Build Max Heap from arr:   O(n)
        Phase 2 — Extract max n times:       O(n log n)

        Each extraction:
          • Swap root (max) with last element
          • Reduce heap size by 1
          • Heapify root downward
        Result: array sorted ascending (smallest to largest).
        """
        n = len(arr)

        # ── Phase 1: Build Max Heap (Bottom-Up) ──
        for i in range(n // 2 - 1, -1, -1):
            max_heapify(arr, n, i)

        # ── Phase 2: Extract max one by one ──
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]   # move current max to end
            max_heapify(arr, i, 0)             # heapify reduced heap

        return arr

    # ── DISPLAY ──────────────────────────────────────────────────
    def display(self):
        if self.is_empty():
            print("  Heap is empty")
            return
        print(f"  Heap array : {self.heap}")
        print(f"  Max (root) : {self.heap[0]}")
        print(f"  Size       : {self.size()}")
        self._print_tree(0, "", True)

    def _print_tree(self, idx, prefix, is_left):
        if idx >= self.size():
            return
        connector = "L── " if is_left else "R── "
        print(prefix + connector + str(self.heap[idx]))
        new_prefix = prefix + ("│   " if is_left else "    ")
        left  = self._left(idx)
        right = self._right(idx)
        if left < self.size() or right < self.size():
            if left  < self.size():
                self._print_tree(left,  new_prefix, True)
            if right < self.size():
                self._print_tree(right, new_prefix, False)


# ════════════════════════════════════════════════════════════════════
#  PART 3 — MIN HEAP CLASS
# ════════════════════════════════════════════════════════════════════
class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, i):   return (i - 1) // 2
    def _left(self, i):     return 2 * i + 1
    def _right(self, i):    return 2 * i + 2
    def size(self):         return len(self.heap)
    def is_empty(self):     return len(self.heap) == 0

    def peek_min(self):
        if self.is_empty():
            return None
        return self.heap[0]     # root = minimum in min heap

    def find_min(self):
        return self.peek_min()

    def find_max(self):
        """Max is always a leaf. Scan leaf nodes."""
        if self.is_empty():
            return None
        n = self.size()
        return max(self.heap[n // 2:])

    # ── INSERT (O(log n)) ────────────────────────────────────────
    def insert(self, value):
        self.heap.append(value)
        heapify_up_min(self.heap, self.size() - 1)

    # ── EXTRACT MIN (O(log n)) ───────────────────────────────────
    def extract_min(self):
        if self.is_empty():
            print("  Heap is empty")
            return None
        n       = self.size()
        min_val = self.heap[0]
        self.heap[0] = self.heap[n - 1]
        self.heap.pop()
        if not self.is_empty():
            min_heapify(self.heap, self.size(), 0)
        return min_val

    # ── SEARCH (O(n)) ────────────────────────────────────────────
    def search(self, value):
        for i, v in enumerate(self.heap):
            if v == value:
                print(f"  {value} FOUND at index {i}")
                return i
        print(f"  {value} NOT FOUND")
        return -1

    # ── DELETE ARBITRARY ELEMENT (O(log n)) ──────────────────────
    def delete(self, value):
        idx = self.search(value)
        if idx == -1:
            return False
        # Replace with -infinity → bubbles to root
        self.heap[idx] = float('-inf')
        heapify_up_min(self.heap, idx)
        self.extract_min()
        print(f"  {value} deleted successfully")
        return True

    # ── DISPLAY ──────────────────────────────────────────────────
    def display(self):
        if self.is_empty():
            print("  Heap is empty")
            return
        print(f"  Heap array : {self.heap}")
        print(f"  Min (root) : {self.heap[0]}")
        print(f"  Size       : {self.size()}")


# ════════════════════════════════════════════════════════════════════
#  PART 4 — HEAP SORT (Standalone, with step-by-step trace)
# ════════════════════════════════════════════════════════════════════
def heap_sort(arr, verbose=False):
    """
    Heap Sort using Max Heap.

    Step 1: Build Max Heap  — O(n)
        → Start from last internal node (n//2 - 1)
        → Heapify downward to index 0
        → After this loop: arr[0] = maximum element

    Step 2: Sort Phase      — O(n log n)
        → Swap arr[0] (max) with arr[i] (last unsorted)
        → Reduce heap size (i decreases by 1 each time)
        → Heapify root again to get next max at arr[0]
        → Repeat until i = 1

    Final result: Array sorted in ASCENDING order.
    """
    n = len(arr)

    if verbose:
        print(f"  Original      : {arr}")

    # ── PHASE 1: Build Max Heap ──────────────────────────────────
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

    if verbose:
        print(f"  After BuildHeap: {arr}  ← max heap ✓")
        print(f"  Max element at root: {arr[0]}")
        print()

    # ── PHASE 2: Extract elements one by one ─────────────────────
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]          # send max to end
        if verbose:
            print(f"  Swap root({arr[i]}) ↔ index {i}: {arr}")
        max_heapify(arr, i, 0)                   # heapify remaining heap
        if verbose:
            print(f"  After heapify     : {arr}")
            print(f"  Sorted portion    : {arr[i:]}")
            print()

    return arr


# ════════════════════════════════════════════════════════════════════
#  PART 5 — EXAM QUESTION SOLUTION
#  (a) Define Max Heap + Build Algorithm
#  (b) Build Max Heap from: 80, 20, 90, 40, 100, 60, 120, 60, 50, 70
# ════════════════════════════════════════════════════════════════════
def solve_exam_question():
    print("=" * 65)
    print("  EXAM QUESTION (a): DEFINE MAX HEAP + BUILD ALGORITHM")
    print("=" * 65)
    print("""
  Definition:
    A Max Heap is a Complete Binary Tree where every parent node
    is GREATER THAN OR EQUAL TO its children.
    → The MAXIMUM element is always at the ROOT.
    → Stored as an array: left=2i+1, right=2i+2, parent=(i-1)//2

  Algorithm: BuildMaxHeap(arr, n)
    Step 1: Start
    Step 2: Find last internal node index → last = n//2 - 1
    Step 3: FOR i = last DOWNTO 0:
                MaxHeapify(arr, n, i)
    Step 4: Stop
    ↳ Time: O(n)  ← not O(n log n), proven by geometric series

  Algorithm: MaxHeapify(arr, n, i)
    Step 1: largest = i
    Step 2: left = 2*i+1,  right = 2*i+2
    Step 3: IF left < n AND arr[left] > arr[largest]:
                largest = left
    Step 4: IF right < n AND arr[right] > arr[largest]:
                largest = right
    Step 5: IF largest != i:
                swap arr[i] and arr[largest]
                MaxHeapify(arr, n, largest)
    Step 6: Stop
    """)

    print("=" * 65)
    print("  EXAM QUESTION (b): BUILD MAX HEAP FROM")
    print("  Input: [80, 20, 90, 40, 100, 60, 120, 60, 50, 70]")
    print("=" * 65)

    arr = [80, 20, 90, 40, 100, 60, 120, 60, 50, 70]
    n   = len(arr)

    print(f"\n  Input array : {arr}")
    print(f"  n = {n}")
    print(f"  Last internal node = n//2 - 1 = {n}//2 - 1 = {n//2 - 1}")
    print(f"  Leaf nodes (no heapify needed): index {n//2} to {n-1}")
    print()

    print("  Initial Tree:")
    print("""
                  80(0)
               /         \\
           20(1)           90(2)
           /    \\          /    \\
        40(3)  100(4)    60(5)  120(6)
        /   \\   /
     60(7) 50(8) 70(9)
    """)

    print("  ── Step-by-step MaxHeapify (i = 4 down to 0) ──")
    print()

    step = 0
    def verbose_heapify(arr, n, i, step_num):
        largest = i
        left    = 2 * i + 1
        right   = 2 * i + 2

        original = arr[i]
        lv = arr[left]  if left  < n else None
        rv = arr[right] if right < n else None

        if left  < n and arr[left]  > arr[largest]: largest = left
        if right < n and arr[right] > arr[largest]: largest = right

        print(f"  Step {step_num}: i={i}, node={arr[i]}, "
              f"left={lv}(idx {left}), right={rv}(idx {right})")

        if largest != i:
            print(f"    → largest = arr[{largest}] = {arr[largest]} > arr[{i}]={arr[i]}")
            print(f"    → SWAP arr[{i}]({arr[i]}) ↔ arr[{largest}]({arr[largest]})")
            arr[i], arr[largest] = arr[largest], arr[i]
            print(f"    → Array: {arr}")
            verbose_heapify(arr, n, largest, str(step_num)+"b")
        else:
            print(f"    → arr[{i}]={arr[i]} already largest. No swap.")
        print()

    for i in range(n // 2 - 1, -1, -1):
        step += 1
        verbose_heapify(arr, n, i, step)

    print(f"  ✓ Final Max Heap Array : {arr}")
    print(f"  ✓ Maximum (root)       : {arr[0]}")
    print()
    print("  Final Tree:")
    print("""
                 120(0)
              /          \\
           100(1)         90(2)
           /    \\         /    \\
         60(3)  70(4)   60(5)  80(6)
         /   \\   /
       40(7) 50(8) 20(9)
    """)
    print("  Verification (each parent ≥ children):")
    valid = True
    for i in range(n):
        l, r = 2*i+1, 2*i+2
        if l < n and arr[i] < arr[l]:
            valid = False
        if r < n and arr[i] < arr[r]:
            valid = False
    print(f"  Valid Max Heap: {valid} ✓")


# ════════════════════════════════════════════════════════════════════
#  DRIVER CODE
# ════════════════════════════════════════════════════════════════════

# ────────────────────────────────────────────────────────────────────
#  MAX HEAP DEMO
# ────────────────────────────────────────────────────────────────────
print("=" * 55)
print("             MAX HEAP — FULL DEMO")
print("=" * 55)

mh = MaxHeap()

print("\n── Insertions ──")
for v in [50, 30, 70, 10, 40, 60, 80]:
    mh.insert(v)
    print(f"  Inserted {v}  → heap: {mh.heap}")

print("\n── Heap Structure ──")
mh.display()

print("\n── Operations ──")
print(f"  Max (root)  : {mh.find_max()}")
print(f"  Min (leaf)  : {mh.find_min()}")

print("\n── Search ──")
mh.search(40)
mh.search(99)

print("\n── Extract Max ──")
print(f"  Extracted   : {mh.extract_max()}")
print(f"  Heap after  : {mh.heap}")
print(f"  Extracted   : {mh.extract_max()}")
print(f"  Heap after  : {mh.heap}")

print("\n── Delete ──")
mh.delete(30)
print(f"  Heap after  : {mh.heap}")

# ────────────────────────────────────────────────────────────────────
#  MIN HEAP DEMO
# ────────────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("             MIN HEAP — FULL DEMO")
print("=" * 55)

mn = MinHeap()

print("\n── Insertions ──")
for v in [50, 30, 70, 10, 40, 60, 80]:
    mn.insert(v)
    print(f"  Inserted {v}  → heap: {mn.heap}")

print(f"\n  Min (root)  : {mn.find_min()}")
print(f"  Max (leaf)  : {mn.find_max()}")

print("\n── Extract Min ──")
print(f"  Extracted   : {mn.extract_min()}")
print(f"  Heap after  : {mn.heap}")

print("\n── Delete 40 ──")
mn.delete(40)
print(f"  Heap after  : {mn.heap}")

# ────────────────────────────────────────────────────────────────────
#  HEAP SORT DEMO (your code, improved)
# ────────────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("             HEAP SORT — STEP BY STEP")
print("=" * 55)

arr = [64, 32, 25, 12, 22, 11, 90]
print(f"\n  Input  : {arr}")
heap_sort(arr, verbose=True)
print(f"  Sorted : {arr}")

# ────────────────────────────────────────────────────────────────────
#  EXAM QUESTION SOLUTION
# ────────────────────────────────────────────────────────────────────
print("\n")
solve_exam_question()

# ────────────────────────────────────────────────────────────────────
#  BUILD HEAP DEMO (standalone functions)
# ────────────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("       BUILD HEAP — STANDALONE FUNCTIONS")
print("=" * 55)

data = [3, 9, 2, 1, 4, 5, 8, 6, 7]
print(f"\n  Original       : {data}")

max_data = data[:]
build_max_heap(max_data)
print(f"  After build_max: {max_data}  ← root={max_data[0]} (max)")

min_data = data[:]
build_min_heap(min_data)
print(f"  After build_min: {min_data}  ← root={min_data[0]} (min)")