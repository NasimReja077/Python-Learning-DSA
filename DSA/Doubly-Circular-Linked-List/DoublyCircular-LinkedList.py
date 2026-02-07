# ---------------- NODE CLASS ----------------
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# ------------- DOUBLY CIRCULAR LINKED LIST CLASS -------------
class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    # ---------- INSERT OPERATIONS ----------

    # Insert at beginning
    def insert_beginning(self, value):
        new_node = Node(value)

        if self.head is None:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            print(value, "inserted as first node")
            return

        last = self.head.prev

        new_node.next = self.head
        new_node.prev = last

        last.next = new_node
        self.head.prev = new_node

        self.head = new_node
        print(value, "inserted at beginning")


    # Insert at end
    def insert_end(self, value):
        new_node = Node(value)

        if self.head is None:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            print(value, "inserted as first node")
            return

        last = self.head.prev

        new_node.next = self.head
        new_node.prev = last

        last.next = new_node
        self.head.prev = new_node

        print(value, "inserted at end")


    # Insert after a given value
    def insert_after(self, prev_value, value):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:
            if temp.data == prev_value:
                new_node = Node(value)

                new_node.next = temp.next
                new_node.prev = temp

                temp.next.prev = new_node
                temp.next = new_node

                print(value, "inserted after", prev_value)
                return

            temp = temp.next
            if temp == self.head:
                break

        print(prev_value, "not found")


    # ---------- DISPLAY / TRAVERSING ----------

    def display(self):
        if self.head is None:
            print("Doubly Circular Linked List is empty")
            return

        print("Doubly Circular Linked List:")
        temp = self.head

        while True:
            print(temp.data, end=" <-> ")
            temp = temp.next
            if temp == self.head:
                break

        print("(back to head)")


    # ---------- SEARCH ----------

    def search(self, key):
        if self.head is None:
            print("List is empty")
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

        count = 0
        temp = self.head

        while True:
            count += 1
            temp = temp.next
            if temp == self.head:
                break

        print("Total number of nodes:", count)
        return count


    # ---------- DELETE OPERATIONS ----------

    # Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            print(self.head.data, "deleted (only node)")
            self.head = None
            return

        last = self.head.prev

        print(self.head.data, "deleted from beginning")

        self.head = self.head.next
        self.head.prev = last
        last.next = self.head


    # Delete from end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            print(self.head.data, "deleted (only node)")
            self.head = None
            return

        last = self.head.prev
        second_last = last.prev

        print(last.data, "deleted from end")

        second_last.next = self.head
        self.head.prev = second_last


    # Delete a given element
    def delete_element(self, key):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:
            if temp.data == key:

                if temp.next == self.head and temp.prev == self.head:
                    # only one node
                    self.head = None
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev

                    if temp == self.head:
                        self.head = temp.next

                print(key, "deleted from the list")
                return

            temp = temp.next
            if temp == self.head:
                break

        print(key, "not found")

dcll = DoublyCircularLinkedList()

dcll.insert_beginning(10)
dcll.insert_end(20)
dcll.insert_end(30)
dcll.insert_end(40)
dcll.insert_end(50)
dcll.insert_end(60)
dcll.insert_after(30, 25)

dcll.display()

dcll.search(25)
dcll.count_nodes()

dcll.delete_beginning()
dcll.delete_end()
dcll.delete_element(25)

dcll.display()
