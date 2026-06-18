# ---------------- NODE CLASS ----------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ---------------- SORTED SINGLY LINKED LIST ----------------
class SortedLinkedList:
    def __init__(self):
        self.head = None

    # Insert in Sorted Order
    def insert_sorted(self, value):
        new_node = Node(value)

        # Case 1: Empty list or insert at beginning
        if self.head is None or self.head.data >= value:
            new_node.next = self.head
            self.head = new_node
            return

        # Traverse to find correct position
        temp = self.head
        while temp.next is not None and temp.next.data < value:
            temp = temp.next

        # Insert the new node
        new_node.next = temp.next
        temp.next = new_node

    # Display
    def display(self):
        if self.head is None:
            print("List is Empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")
        
        
    # Merge two sorted linked lists
    def merge(self, list1, list2):
        # Dummy node to simplify code
        dummy = Node(0)
        tail = dummy

        while list1.head is not None and list2.head is not None:
            if list1.head.data <= list2.head.data:
                tail.next = list1.head
                list1.head = list1.head.next
            else:
                tail.next = list2.head
                list2.head = list2.head.next
            tail = tail.next

        # Attach remaining nodes
        if list1.head is not None:
            tail.next = list1.head
        else:
            tail.next = list2.head

        # Create new merged list
        merged = SortedLinkedList()
        merged.head = dummy.next
        return merged
   
   
   # ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    # Create two sorted lists
    l1 = SortedLinkedList()
    l1.insert_sorted(10)
    l1.insert_sorted(30)
    l1.insert_sorted(50)
    l1.insert_sorted(70)

    l2 = SortedLinkedList()
    l2.insert_sorted(20)
    l2.insert_sorted(40)
    l2.insert_sorted(60)

    print("List 1:")
    l1.display()

    print("List 2:")
    l2.display()

    # Merge both lists
    merged_list = l1.merge(l1, l2)

    print("\nMerged Sorted List:")
    merged_list.display()