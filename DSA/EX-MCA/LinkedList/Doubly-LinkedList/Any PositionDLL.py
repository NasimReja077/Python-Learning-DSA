# Write a program to insert a node at any position of an existing double linked list. Your function should run correctly when you are inserting at the first and the last position of the list and when you are inserting an element when the list is empty. 15mk

# Empty list insertion
# Insert at first position
# Insert at middle position
# Insert at last position
# Display the list

# Program to Insert a Node at Any Position in a Doubly Linked List


# Write a python program for a Doubly Linked List which can perform following operations 9mk 
# i) create the linked list. 
# ii) insert element in any position. 
# iii) delete the element from any position.


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

        # Case 1: Insert at first position or empty list
        if position == 1:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
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

        # Insert node
        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node

        temp.next = new_node

        print(value, "inserted at position", position)

    # Delete from any position
    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty")
            return

        # Delete first node
        if position == 1:
            print(self.head.data, "deleted")
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return

        temp = self.head

        # Move to the node to be deleted
        for i in range(position - 1):
            if temp is None:
                print("Position out of bounds")
                return
            temp = temp.next

        if temp is None:
            print("Position out of bounds")
            return

        print(temp.data, "deleted")

        if temp.prev is not None:
            temp.prev.next = temp.next

        if temp.next is not None:
            temp.next.prev = temp.prev

    # Display the linked list
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

# Insert at last position
dll.insert_at_position(20, 2)

# Insert at last position
dll.insert_at_position(30, 3)

# Insert in middle
dll.insert_at_position(25, 3)

# Insert at beginning
dll.insert_at_position(5, 1)

print("\nDoubly Linked List after insertion:")
dll.display()

# Delete node at position 3
dll.delete_at_position(3)

print("\nDoubly Linked List after deleting position 3:")
dll.display()