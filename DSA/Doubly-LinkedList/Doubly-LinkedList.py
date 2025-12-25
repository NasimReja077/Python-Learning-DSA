# ---------------- NODE CLASS ----------------
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# ------------- DOUBLY LINKED LIST CLASS -------------
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # ---------- INSERT OPERATIONS ----------

    # Insert at beginning
    def insert_beginning(self, value):
        new_node = Node(value)

        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head

        self.head = new_node
        print(value, "inserted at beginning")

    # Insert at end
    def insert_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print(value, "inserted at end")
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp
        print(value, "inserted at end")

    # Insert after a given value (middle insertion)
    def insert_after(self, prev_value, value):
        temp = self.head

        while temp:
            if temp.data == prev_value:
                new_node = Node(value)
                new_node.next = temp.next
                new_node.prev = temp

                if temp.next:
                    temp.next.prev = new_node

                temp.next = new_node
                print(value, "inserted after", prev_value)
                return

            temp = temp.next

        print("Value", prev_value, "not found")

    # ---------- DISPLAY / TRAVERSING ----------
    def display(self):
        if self.head is None:
            print("Doubly Linked List is empty")
            return

        print("Doubly Linked List:")
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("NULL")

    # ---------- SEARCH ----------
    def search(self, key):
        temp = self.head
        position = 1

        while temp:
            if temp.data == key:
                print(key, "found at position", position)
                return
            temp = temp.next
            position += 1

        print(key, "not found in the list")

    # ---------- COUNT NODES ----------
    def count_nodes(self):
        count = 0
        temp = self.head

        while temp:
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

        print(self.head.data, "deleted from beginning")
        self.head = self.head.next

        if self.head:
            self.head.prev = None

    # Delete from end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            print(self.head.data, "deleted from end")
            self.head = None
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        print(temp.data, "deleted from end")
        temp.prev.next = None

    # Delete a given element (middle deletion)
    def delete_element(self, key):
        temp = self.head

        while temp:
            if temp.data == key:

                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next  # deleting head

                if temp.next:
                    temp.next.prev = temp.prev

                print(key, "deleted from the list")
                return

            temp = temp.next

        print(key, "not found")


# ---------------- MAIN PROGRAM ----------------
dll = DoublyLinkedList()

dll.insert_beginning(10)
dll.insert_end(20)
dll.insert_end(30)
dll.insert_after(20, 25)

dll.display()

dll.search(25)
dll.count_nodes()

dll.delete_beginning()
dll.delete_end()
dll.delete_element(25)

dll.display()
