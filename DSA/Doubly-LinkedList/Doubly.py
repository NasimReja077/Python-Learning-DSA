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
        self.head = None      # i) Create Linked List

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
            temp = temp.next
            
            if temp is None:
                print("Position out of bounds")
                return

        # Insert new_node after temp
            # Insert new_node between temp and temp.next
            new_node.next = temp.next
            new_node.prev = temp
            # Update the next node's prev pointer if it exists
            if temp.next:
                temp.next.prev = new_node
        
            # Update the current node's next pointer
            temp.next = new_node
            print(value, "inserted at position", position)


    # iii) Delete from Any Position
    def delete_at_position(self, position):
        if self.head is None:
            print("List is Empty")
            return

        if position < 1:
            print("Invalid Position")
            return

        # Delete First Node
        if position == 1:
            print(self.head.data, "deleted from position 1")
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return

        # Traverse to the node to be deleted
        temp = self.head
        for _ in range(position - 1):
            if temp is None:
                print("Invalid Position")
                return
            temp = temp.next
            
# Insert at position → Go to previous node → position - 2
# Delete at position → Go to that node itself → position - 1

        if temp is None:
            print("Invalid Position")
            return

        print(temp.data, "deleted from position", position)

        # Update links
        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev

    # Display List
    # def display(self):
    #     temp = self.head

    #     while temp:
    #         print(temp.data, end=" <-> ")
    #         temp = temp.next

    #     print("NULL")
    
    # Display
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

dll.insert_at_position(10, 1)
dll.insert_at_position(20, 2)
dll.insert_at_position(30, 3)
dll.insert_at_position(25, 3)

print("After Insertion:")
dll.display()

dll.delete_at_position(3)

print("After Deletion:")
dll.display()