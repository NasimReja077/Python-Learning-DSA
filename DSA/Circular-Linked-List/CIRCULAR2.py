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
        temp.next = new_node #  Update Last Node to Point to New Node
        self.head = new_node # Update HEAD to New Node

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
        prev = None
        
        while temp.next != self.head:
            prev = temp
            temp = temp.next

        print(temp.data, "deleted from end")
        prev.next = self.head


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

cll.insert_beginning(5)
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
cll.display()
cll.count_nodes()

cll.delete_value(30)
cll.display()
cll.count_nodes()

cll.delete_end()
cll.display()
cll.count_nodes()



def delete_value(self, key):

    if self.head is None:
        print("List is empty")
        return

    temp = self.head
    prev = None

    # Case 1: If head contains key
    if temp.data == key:

        # Only one node case
        if temp.next == self.head:
            self.head = None
            print(key, "deleted (only node)")
            return

        # More than one node
        last = self.head
        while last.next != self.head:
            last = last.next

        self.head = self.head.next
        last.next = self.head
        print(key, "deleted from circular linked list")
        return

    # Case 2: Deleting non-head node
    prev = temp
    temp = temp.next

    while temp != self.head:
        if temp.data == key:
            prev.next = temp.next
            print(key, "deleted from circular linked list")
            return

        prev = temp
        temp = temp.next

    print(key, "not found")
