# Write a program to insert a node at any position of an existing circular linked list. Your function should run correctly when you are inserting at the first and the last position of the list and when you are inserting an element when the list is empty. 15mk

# Empty Circular Linked List
# Insert at First Position
# Insert at Middle Position
# Insert at Last Position

# Write a python program for a circular linked list which can perform following operations 9mk 
# i) create the linked list.
# ii) insert element in any position.
# iii) delete the element from any position.

# ✅ Create Circular Linked List
# ✅ Insert element at any position
# ✅ Delete element from any position

# ---------------- NODE CLASS ----------------
# ---------------- NODE CLASS ----------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ---------------- CIRCULAR LINKED LIST ----------------
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at any position
    def insert_at_position(self, value, position):
        new_node = Node(value)

        # Empty list
        if self.head is None:
            if position != 1:
                print("Position out of bounds")
                return
            self.head = new_node
            new_node.next = self.head
            print(value, "inserted at position", position)
            return

        # Insert at beginning
        if position == 1:
            last = self.head
            while last.next != self.head:
                last = last.next

            new_node.next = self.head
            last.next = new_node
            self.head = new_node

            print(value, "inserted at position", position)
            return

        # Insert at middle or end
        temp = self.head
        for i in range(position - 2):
            if temp.next == self.head:
                break
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

        print(value, "inserted at position", position)

    # Delete from any position
    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty")
            return

        # Delete first node
        if position == 1:
            # Only one node
            if self.head.next == self.head:
                print(self.head.data, "deleted")
                self.head = None
                return

            last = self.head
            while last.next != self.head:
                last = last.next

            print(self.head.data, "deleted")
            last.next = self.head.next
            self.head = self.head.next
            return

        # Delete middle or last node
        temp = self.head
        for i in range(position - 2):
            if temp.next == self.head:
                print("Position out of bounds")
                return
            temp = temp.next

        if temp.next == self.head:
            print("Position out of bounds")
            return

        print(temp.next.data, "deleted")
        temp.next = temp.next.next

    # Display Circular Linked List
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


# ---------------- MAIN PROGRAM ----------------
cll = CircularLinkedList()

# Empty list insertion
cll.insert_at_position(10, 1)

# Insert at last position
cll.insert_at_position(20, 2)

# Insert at last position
cll.insert_at_position(30, 3)

# Insert in middle
cll.insert_at_position(25, 3)

# Insert at beginning
cll.insert_at_position(5, 1)

print("\nCircular Linked List after insertion:")
cll.display()

# Delete node at position 3
cll.delete_at_position(3)

print("\nCircular Linked List after deleting position 3:")
cll.display()