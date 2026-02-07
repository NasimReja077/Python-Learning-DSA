# ---------------- NODE CLASS ----------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ------------- CIRCULAR LINKED LIST CLASS -------------
class CircularLinkedList:
    def __init__(self):
        self.head = None


    # i) Insert at Beginning
    def insert_beginning(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            print(value, "inserted as first node")
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

        print(value, "inserted at beginning")


    # ii) Insert at End
    def insert_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            print(value, "inserted as first node")
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

        print(value, "inserted at end")


    # iii) Insert after a given value
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

        print(prev_value, "not found")


    # iv) Display
    def display(self):
        if self.head is None:
            print("Circular Linked List is empty")
            return

        temp = self.head
        print("Circular Linked List:")

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break

        print("(back to head)")


    # v) Search
    def search(self, key):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while True:
            if temp.data == key:
                print(key, "found in circular linked list")
                return
            temp = temp.next
            if temp == self.head:
                break

        print(key, "not found")


    # vi) Count nodes
    def count_nodes(self):
        if self.head is None:
            print("Total nodes: 0")
            return

        count = 0
        temp = self.head
        while True:
            count += 1
            temp = temp.next
            if temp == self.head:
                break

        print("Total number of nodes:", count)


    # vii) Delete from Beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            print(self.head.data, "deleted (only node)")
            self.head = None
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        print(self.head.data, "deleted from beginning")
        temp.next = self.head.next
        self.head = self.head.next


    # viii) Delete from End
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            print(self.head.data, "deleted (only node)")
            self.head = None
            return

        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next

        print(temp.next.data, "deleted from end")
        temp.next = self.head


    # ix) Delete a given element
    def delete_value(self, key):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        prev = None

        while True:
            if temp.data == key:
                if prev is None:
                    # deleting head
                    self.delete_beginning()
                else:
                    prev.next = temp.next
                    print(key, "deleted from circular linked list")
                return

            prev = temp
            temp = temp.next

            if temp == self.head:
                break

        print(key, "not found")

cll = CircularLinkedList()

cll.insert_beginning(10)
cll.insert_end(20)
cll.insert_end(30)
cll.insert_end(40)
cll.insert_end(50)
cll.insert_after(20, 25)

cll.display()

cll.search(25)
cll.count_nodes()

cll.delete_beginning()
cll.delete_value(25)
cll.delete_end()

cll.display()