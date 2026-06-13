# Write a python program for a circular linked list which can perform following operations 9mk 
# i) create the linked list.
# ii) insert element in any position.
# iii) delete the element from any position.

# ✅ Create Circular Linked List
# ✅ Insert element at any position
# ✅ Delete element from any position


# ---------------- NODE CLASS ----------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ---------------- CIRCULAR LINKED LIST ----------------
class CircularLinkedList:
    def __init__(self):
        self.head = None      # i) Create Linked List

    # ii) Insert element at any position
    def insert_at_position(self, value, position):
        new_node = Node(value)

        # Insert at first position
        if position == 1:

            # Empty list
            if self.head is None:
                self.head = new_node
                new_node.next = self.head
                return

            # Find last node
            last = self.head
            while last.next != self.head:
                last = last.next

            new_node.next = self.head
            last.next = new_node
            self.head = new_node
            return

        temp = self.head

        for i in range(position - 2):
            temp = temp.next

            if temp == self.head:
                print("Invalid Position")
                return

        new_node.next = temp.next
        temp.next = new_node

    # iii) Delete element from any position
    def delete_at_position(self, position):

        if self.head is None:
            print("List is Empty")
            return

        # Delete first node
        if position == 1:

            # Only one node
            if self.head.next == self.head:
                self.head = None
                return

            # Find last node
            last = self.head
            while last.next != self.head:
                last = last.next

            last.next = self.head.next
            self.head = self.head.next
            return

        prev = None
        temp = self.head

        for i in range(position - 1):
            prev = temp
            temp = temp.next

            if temp == self.head:
                print("Invalid Position")
                return

        prev.next = temp.next

    # Display Circular Linked List
    def display(self):

        if self.head is None:
            print("List is Empty")
            return

        temp = self.head

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(back to head)")


# ---------------- MAIN PROGRAM ----------------
cll = CircularLinkedList()

cll.insert_at_position(10, 1)
cll.insert_at_position(20, 2)
cll.insert_at_position(30, 3)
cll.insert_at_position(25, 3)

print("After Insertion:")
cll.display()

cll.delete_at_position(3)

print("After Deletion:")
cll.display()