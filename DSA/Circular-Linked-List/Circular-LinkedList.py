# ---------------- NODE CLASS ----------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ------------- CIRCULAR LINKED LIST CLASS -------------
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # ---------- INSERT OPERATIONS ----------

    # Insert at beginning
    def insert_beginning(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node  # Points to itself
            print(value, "inserted at beginning")
            return

        # Find last node
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        new_node.next = self.head
        temp.next = new_node
        self.head = new_node
        print(value, "inserted at beginning")

    # Insert at end
    def insert_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node  # Points to itself
            print(value, "inserted at end")
            return

        # Find last node
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head
        print(value, "inserted at end")

    # Insert after a given value (middle insertion)
    def insert_after(self, prev_value, value):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:
            if temp.data == prev_value:
                new_node = Node(value)
                new_node.next = temp.next
                temp.next = new_node
                print(value, "inserted after", prev_value)
                return

            temp = temp.next
            if temp == self.head:
                break

        print("Value", prev_value, "not found")

    # Insert at specific position
    def insert_at_position(self, value, position):
        if position < 1:
            print("Invalid position")
            return

        new_node = Node(value)

        if position == 1:
            self.insert_beginning(value)
            return

        temp = self.head
        count = 1

        while count < position - 1:
            temp = temp.next
            count += 1
            if temp == self.head:
                print("Position out of range")
                return

        new_node.next = temp.next
        temp.next = new_node
        print(value, "inserted at position", position)

    # ---------- DISPLAY / TRAVERSING ----------
    def display(self):
        if self.head is None:
            print("Circular Linked List is empty")
            return

        print("Circular Linked List:")
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print(f"(HEAD: {self.head.data})")

    # ---------- SEARCH ----------
    def search(self, key):
        if self.head is None:
            print(key, "not found in the list")
            return

        temp = self.head
        position = 1

        while True:
            if temp.data == key:
                print(key, "found at position", position)
                return
            temp = temp.next
            position += 1
            if temp == self.head:
                break

        print(key, "not found in the list")

    # ---------- COUNT NODES ----------
    def count_nodes(self):
        if self.head is None:
            print("Total number of nodes: 0")
            return 0

        count = 1
        temp = self.head

        while temp.next != self.head:
            count += 1
            temp = temp.next

        print("Total number of nodes:", count)
        return count

    # ---------- DELETE OPERATIONS ----------

    # Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        # Only one node
        if self.head.next == self.head:
            print(self.head.data, "deleted from beginning")
            self.head = None
            return

        # Find last node
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        print(self.head.data, "deleted from beginning")
        temp.next = self.head.next
        self.head = self.head.next

    # Delete from end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        # Only one node
        if self.head.next == self.head:
            print(self.head.data, "deleted from end")
            self.head = None
            return

        # Find second-to-last node
        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next

        print(temp.next.data, "deleted from end")
        temp.next = self.head

    # Delete a given element (middle deletion)
    def delete_element(self, key):
        if self.head is None:
            print("List is empty")
            return

        # If head node is to be deleted
        if self.head.data == key:
            # Only one node
            if self.head.next == self.head:
                print(key, "deleted from the list")
                self.head = None
                return

            # Find last node
            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            temp.next = self.head.next
            print(key, "deleted from the list")
            self.head = self.head.next
            return

        # Search for the node to delete
        temp = self.head
        while temp.next != self.head:
            if temp.next.data == key:
                print(key, "deleted from the list")
                temp.next = temp.next.next
                return
            temp = temp.next

        print(key, "not found")


# ---------------- MAIN PROGRAM ----------------
cll = CircularLinkedList()

print("=" * 50)
print("CIRCULAR LINKED LIST OPERATIONS")
print("=" * 50)

print("\n--- INSERT OPERATIONS ---")
cll.insert_beginning(10)
cll.insert_end(20)
cll.insert_end(30)
cll.insert_after(20, 25)
cll.insert_at_position(15, 2)

print("\n--- DISPLAY ---")
cll.display()

print("\n--- SEARCH OPERATIONS ---")
cll.search(25)
cll.search(100)

print("\n--- COUNT NODES ---")
cll.count_nodes()

print("\n--- DELETE OPERATIONS ---")
cll.delete_beginning()
cll.delete_end()
cll.delete_element(25)

print("\n--- FINAL DISPLAY ---")
cll.display()
cll.count_nodes()

print("\n" + "=" * 50)