# Write a program to insert a node at any position of an existing circular linked list. Your function should run correctly when you are inserting at the first and the last position of the list and when you are inserting an element when the list is empty. 15mk

# Empty Circular Linked List
# Insert at First Position
# Insert at Middle Position
# Insert at Last Position

# ---------------- NODE CLASS ----------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ---------------- CIRCULAR LINKED LIST ----------------
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert node at any position
    def insert_at_position(self, value, position):
        new_node = Node(value)

        # Case 1: Empty list OR Insert at first position
        if position == 1:

            # Empty list
            if self.head is None:
                self.head = new_node
                new_node.next = self.head
                print(value, "inserted as first node")
                return

            # Find last node
            last = self.head
            while last.next != self.head:
                last = last.next

            new_node.next = self.head
            last.next = new_node
            self.head = new_node

            print(value, "inserted at position", position)
            return

        # Traverse to node before desired position
        temp = self.head

        for i in range(position - 2):
            temp = temp.next

            if temp == self.head:
                print("Invalid Position")
                return

        # Insert new node
        new_node.next = temp.next
        temp.next = new_node

        print(value, "inserted at position", position)

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

# Insert into empty list
cll.insert_at_position(10, 1)

# Insert at last position
cll.insert_at_position(20, 2)
cll.insert_at_position(30, 3)

# Insert in middle
cll.insert_at_position(25, 3)

# Insert at first position
cll.insert_at_position(5, 1)

cll.display()