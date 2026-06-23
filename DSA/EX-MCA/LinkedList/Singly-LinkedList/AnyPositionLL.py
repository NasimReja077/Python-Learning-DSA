# Write a program to insert a node at any position of an existing singly linked list. Your function should run correctly when you are inserting at the first and the last position of the list and when you are inserting an element when the list is empty. 15mk

# Program to Insert a Node at Any Position in a Singly Linked List

# Empty list insertion
# Insert at first position
# Insert at middle position
# Insert at last position
# Display the linked list

# -----------
# Write a python program for a singly linked list which can perform following operations 9mk
# i) create the linked list.
# ii) insert element in any position.
# iii) delete the element from any position.


# ---------------- NODE CLASS ----------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# ---------------- SINGLY LINKED LIST ----------------
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at any position
    def insert_at_position(self, value, position):
        new_node = Node(value)

        # Case 1: Empty list or insert at first position
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            print(value, "inserted at position", position)
            return

        temp = self.head

        # Move to the node before required position
        for i in range(position - 2):
            if temp is None:
                print("Position out of bounds")
                return
            temp = temp.next

        if temp is None:
            print("Position out of bounds")
            return

        # Insert the node
        new_node.next = temp.next
        temp.next = new_node

        print(value, "inserted at position", position)

    # Display linked list
    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("NULL")

    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty")
            return

        if position == 1:
            print(self.head.data, "deleted")
            self.head = self.head.next
            return

        temp = self.head

        for i in range(position - 2):
            if temp is None or temp.next is None:
                print("Position out of bounds")
                return
        temp = temp.next

        if temp.next is None:
            print("Position out of bounds")
            return

        print(temp.next.data, "deleted")
        temp.next = temp.next.next

# ---------------- MAIN PROGRAM ----------------
ll = SinglyLinkedList()

# Empty list insertion
ll.insert_at_position(10, 1)

# Insert at last position
ll.insert_at_position(20, 2)

# Insert at last position
ll.insert_at_position(30, 3)

# Insert in middle
ll.insert_at_position(25, 3)

# Insert at beginning
ll.insert_at_position(5, 1)

print("\nLinked List after insertion:")
ll.display()

# Delete node at position 3
ll.delete_at_position(3)

print("\nLinked List after deleting position 3:")
ll.display()