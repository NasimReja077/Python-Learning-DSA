# ---------------- NODE CLASS ----------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ----------- CIRCULAR LINKED LIST CLASS -----------
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # ---------------- INSERT OPERATIONS ----------------

    # Insert at Beginning
    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            new_node.next = self.head
            temp.next = new_node
            self.head = new_node

        print(data, "inserted at beginning")

    # Insert at End
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head

        print(data, "inserted at end")

    # Insert after a given value
    def insert_after_value(self, key, data):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while True:
            if temp.data == key:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                print(data, "inserted after", key)
                return
            temp = temp.next
            if temp == self.head:
                break

        print("Value not found")

    # Insert at specific position
    def insert_at_position(self, position, data):
        if position <= 0:
            print("Invalid Position")
            return

        if position == 1:
            self.insert_beginning(data)
            return

        new_node = Node(data)
        temp = self.head
        count = 1

        while temp.next != self.head and count < position - 1:
            temp = temp.next
            count += 1

        if count != position - 1:
            print("Position out of range")
            return

        new_node.next = temp.next
        temp.next = new_node
        print(data, "inserted at position", position)

    # ---------------- DELETE OPERATIONS ----------------

    # Delete from Beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            print(self.head.data, "deleted")
            self.head = None
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        print(self.head.data, "deleted from beginning")
        temp.next = self.head.next
        self.head = self.head.next

    # Delete from End
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        prev = None

        if self.head.next == self.head:
            print(self.head.data, "deleted")
            self.head = None
            return

        while temp.next != self.head:
            prev = temp
            temp = temp.next

        print(temp.data, "deleted from end")
        prev.next = self.head

    # Delete a given element
    def delete_value(self, key):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        prev = None

        while True:
            if temp.data == key:
                if prev is None:  # deleting head
                    self.delete_beginning()
                else:
                    prev.next = temp.next
                    print(key, "deleted")
                return

            prev = temp
            temp = temp.next

            if temp == self.head:
                break

        print("Value not found")

    # ---------------- DISPLAY ----------------
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(Back to Head)")

    # ---------------- SEARCH ----------------
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

        print("Value not found")

    # ---------------- COUNT ----------------
    def count(self):
        if self.head is None:
            print("Total nodes: 0")
            return

        temp = self.head
        count = 0

        while True:
            count += 1
            temp = temp.next
            if temp == self.head:
                break

        print("Total nodes:", count)
