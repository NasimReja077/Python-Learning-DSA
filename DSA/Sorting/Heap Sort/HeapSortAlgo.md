Heap Sort Algorithm (Step-by-step)

1. Build a max heap from the input array.
   - Treat the array as a complete binary tree.
   - Start heapifying from the last non-leaf node at index `n//2 - 1`.
   - Move upward to the root, calling `heapify` on each node.

2. Extract the maximum element from the heap.
   - The largest value is at the root, `arr[0]`.
   - Swap `arr[0]` with `arr[end]`, where `end` is the current last index.

3. Reduce the heap size by one.
   - Exclude the last element from the heap because it is now sorted.
   - Decrease the effective heap size from `n` to `end`.

4. Restore the max heap property.
   - Call `heapify(arr, end, 0)` on the root of the reduced heap.
   - This moves the next largest value to the root.

5. Repeat steps 2–4 until only one element remains.
   - Continue swapping the root with the last unsorted element.
   - Each iteration places the next-largest element into its final sorted position.

Result: The array becomes sorted in ascending order.

Notes:
- `heapify(arr, n, i)` compares the node at index `i` with its children
  at `2*i + 1` and `2*i + 2`.
- If a child is larger, swap and recurse to restore the heap.
- Heap Sort runs in `O(n log n)` time and sorts the array in-place.
