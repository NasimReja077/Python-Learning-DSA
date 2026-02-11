# ---------------- NODE CLASS ----------------
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# -------- DOUBLY CIRCULAR LINKED LIST CLASS --------
class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at Beginning
    def insert_beginning(self, value):
        new_node = Node(value)

        if self.head is None:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            print(f"{value} inserted as first node")
            return

        last = self.head.prev

        new_node.next = self.head
        new_node.prev = last
        last.next = new_node
        self.head.prev = new_node
        self.head = new_node

        print(f"{value} inserted at beginning")

    # Insert at End
    def insert_end(self, value):
        new_node = Node(value)

        if self.head is None:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            print(f"{value} inserted as first node")
            return

        last = self.head.prev

        new_node.next = self.head
        new_node.prev = last
        last.next = new_node
        self.head.prev = new_node

        print(f"{value} inserted at end")

    # Insert After a Given Value
    def insert_after(self, key, value):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while True:
            if temp.data == key:
                new_node = Node(value)
                new_node.next = temp.next
                new_node.prev = temp
                temp.next.prev = new_node
                temp.next = new_node
                print(f"{value} inserted after {key}")
                return

            temp = temp.next
            if temp == self.head:
                break

        print(f"{key} not found")

    # Delete from Beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:  # only one node
            print(f"{self.head.data} deleted (only node)")
            self.head = None
            return

        last = self.head.prev
        print(f"{self.head.data} deleted from beginning")

        self.head = self.head.next
        self.head.prev = last
        last.next = self.head

    # Delete from End
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:  # only one node
            print(f"{self.head.data} deleted (only node)")
            self.head = None
            return

        last = self.head.prev
        second_last = last.prev

        print(f"{last.data} deleted from end")

        second_last.next = self.head
        self.head.prev = second_last

    # Delete Specific Value (FIXED)
    def delete_value(self, key):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:
            if temp.data == key:
                # Case: only one node
                if temp.next == temp:
                    print(f"{key} deleted (only node)")
                    self.head = None
                    return

                # Case: deleting head
                if temp == self.head:
                    self.delete_beginning()
                    return  # Important: stop here

                # Case: middle or last node
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                print(f"{key} deleted from list")
                return

            temp = temp.next
            if temp == self.head:
                break

        print(f"{key} not found")

    # Display Forward
    def display_forward(self):
        if self.head is None:
            print("List is empty")
            return

        print("Forward Traversal:")
        temp = self.head
        while True:
            print(temp.data, end=" <-> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")

    # Display Backward (FIXED)
    def display_backward(self):
        if self.head is None:
            print("List is empty")
            return

        print("Backward Traversal:")
        temp = self.head.prev  # start from last node
        start = temp

        while True:
            print(temp.data, end=" <-> ")
            temp = temp.prev
            if temp == start:
                break
        print("(back to last)")


# ────────────────────────────────────────────────
#                    TEST CODE
# ────────────────────────────────────────────────


dll = DoublyCircularLinkedList()

print("=== Insertions ===")
dll.insert_beginning(20)
dll.insert_beginning(10)
dll.insert_end(30)
dll.insert_end(40)
dll.insert_end(50)
print("\n=== Initial list ===")
dll.display_forward()
dll.display_backward()
print("\n=== Delete 30 (middle) ===")
dll.delete_value(30)
dll.display_forward()
dll.display_backward()
print("\n=== Delete 10 (head) ===")
dll.delete_value(10)
dll.display_forward()
dll.display_backward()
print("\n=== Delete 40 (last) ===")
dll.delete_value(40)
dll.display_forward()
dll.display_backward()
print("\n=== Delete 20 (only node) ===")
dll.delete_value(20)
dll.display_forward()