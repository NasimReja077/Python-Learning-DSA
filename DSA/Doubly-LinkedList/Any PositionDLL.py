# Write a program to insert a node at any position of an existing double linked list. Your function should run correctly when you are inserting at the first and the last position of the list and when you are inserting an element when the list is empty. 15mk

# Empty list insertion
# Insert at first position
# Insert at middle position
# Insert at last position
# Display the list

# Program to Insert a Node at Any Position in a Doubly Linked List

# ---------------- NODE CLASS ----------------
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# ---------------- DOUBLY LINKED LIST ----------------
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at any position
    def insert_at_position(self, value, position):
        new_node = Node(value)

        # Case 1: Empty list or insert at first position
        if position == 1:
            new_node.next = self.head

            if self.head:
                self.head.prev = new_node

            self.head = new_node
            print(value, "inserted at position", position)
            return

        temp = self.head

        # Move to node before required position
        for i in range(position - 2):
            if temp is None:
                print("Position out of bounds")
                return
            temp = temp.next

        if temp is None:
            print("Position out of bounds")
            return

        # Insert node
        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node

        print(value, "inserted at position", position)

    # Display Doubly Linked List
    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("NULL")


# ---------------- MAIN PROGRAM ----------------
dll = DoublyLinkedList()

# Empty list insertion
dll.insert_at_position(10, 1)

# Insert at end
dll.insert_at_position(20, 2)

# Insert at end
dll.insert_at_position(30, 3)

# Insert in middle
dll.insert_at_position(25, 3)

# Insert at beginning
dll.insert_at_position(5, 1)

dll.display()

