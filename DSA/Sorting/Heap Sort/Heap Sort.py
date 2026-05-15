"""Heap Sort implementation with explanation.

Heap Sort is a comparison-based sorting algorithm that uses a binary heap data
structure. It sorts an array in-place and has O(n log n) time complexity.

Steps:
1. Build a max heap from the input array.
2. Swap the root (maximum element) with the last element in the heap.
3. Reduce the heap size by one and heapify the root to restore the max heap.
4. Repeat until the heap is empty.

This implementation uses a max heap, so the array is sorted in ascending order.
"""

from typing import List


def heapify(arr: List[int], n: int, i: int) -> None:
    """Ensure the subtree rooted at index i is a max heap.

    Args:
        arr: The list representing the heap.
        n: The number of elements in the heap.
        i: The index of the root of the subtree.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Compare root with left child.
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Compare current largest with right child.
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the root is not the largest, swap and continue heapifying.
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr: List[int]) -> None:
    """Sort an array in-place using heap sort."""
    n = len(arr)

    # Build a max heap: start from the last non-leaf node and heapify each node.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements from the heap.
    for end in range(n - 1, 0, -1):
        # Move current max to the end.
        arr[0], arr[end] = arr[end], arr[0]
        # Restore heap property for the reduced heap.
        heapify(arr, end, 0)


def main() -> None:
    sample = [10, 5, 65, 80, 45, 32, 25]
    print("Original List:", sample)
    heap_sort(sample)
    print("Sorted List:", sample)


if __name__ == "__main__":
    main()
