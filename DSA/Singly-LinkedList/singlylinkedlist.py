# ---------------- NODE CLASS ----------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ------------- SINGLY LINKED LIST CLASS -------------
class SinglyLinkedList:
    def __init__(self):
        self.head = None


    # i) Insert a node at the beginning
    def insert_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        print(value, "inserted at beginning")


    # ii) Insert a node at the end
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
        print(value, "inserted at end")


    # iii) Insert a node in between (after a given value)
    def insert_after(self, prev_value, value):
        temp = self.head

        while temp:
            if temp.data == prev_value:
                new_node = Node(value)
                new_node.next = temp.next
                temp.next = new_node
                print(value, "inserted after", prev_value)
                return
            temp = temp.next

        print("Value", prev_value, "not found")


    # iv) Display / Traversing the list
    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return

        temp = self.head
        print("Linked List:")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")


    # v) Search an element
    def search(self, key):
        temp = self.head

        while temp:
            if temp.data == key:
                print(key, "found in the linked list")
                return
            temp = temp.next

        print(key, "not found in the linked list")


    # vi) Count number of nodes
    def count_nodes(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        print("Total number of nodes:", count)


    # vii) Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        print(self.head.data, "deleted from beginning")
        self.head = self.head.next


    # viii) Delete from middle (given element)
    def delete_middle(self, key):
        temp = self.head
        prev = None

        while temp:
            if temp.data == key:
                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next
                print(key, "deleted from linked list")
                return
            prev = temp
            temp = temp.next

        print(key, "not found")


    # ix) Delete from end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            print(self.head.data, "deleted from end")
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next

        print(temp.next.data, "deleted from end")
        temp.next = None


# ---------------- MAIN PROGRAM ----------------
ll = SinglyLinkedList()

ll.insert_beginning(10)
ll.insert_end(20)
ll.insert_end(30)
ll.insert_after(20, 25)

ll.display()

ll.search(25)
ll.count_nodes()

ll.delete_beginning()
ll.delete_middle(25)
ll.delete_end()

ll.display()


# emupedia