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
        if position < 1:
            print("Invalid Position!")
            return

        new_node = Node(value)

        # Case 1: Empty List or Insert at First Position (position == 1)
        if position == 1 or self.head is None:
            new_node.next = self.head
            # If the list is not empty, set the previous head's prev pointer to the new node
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            print(value, "inserted at position", position)
            return
         # Traverse to the node before the desired position
        temp = self.head

        # Move to node before required position
        for _ in range(position - 2): # why not position - 1? because we want to move to the node before the given position, not the node at the given position
            if temp is None:
                print("Position out of bounds")
                return
            # Insert new_node between temp and temp.next
            new_node.next = temp.next
            new_node.prev = temp
            # Update the next node's prev pointer if it exists
            if temp.next:
                temp.next.prev = new_node
        
            # Update the current node's next pointer
            temp.next = new_node
            print(value, "inserted at position", position)

    # Display Doubly Linked List
    def display(self):
        if self.head is None:
            print("Doubly Linked List is Empty")
            return
        
        temp = self.head
        print("Doubly Linked List: ", end="")
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

