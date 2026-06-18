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

    # i) Create + ii) Insert at Any Position
    def insert_at_position(self, value, position):
        if position < 1:
            print("Invalid Position!")
            return

        new_node = Node(value)

        # Case 1: Insert at First Position or Empty List
        if position == 1 or self.head is None:
            new_node.next = self.head
            self.head = new_node
            print(value, "inserted at position", position)
            return
        # Case 2: Insert at Middle or Last Position 
        # Traverse to the node before the desired position
        temp = self.head
        for _ in range(position - 2):
            if temp is None or temp.next is None:
                print("Position out of bounds")
                return
            temp = temp.next
            
        # Insert the new node
        new_node.next = temp.next
        temp.next = new_node
        print(value, "inserted at position", position)

    # iii) Delete from Any Position
    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty")
            return

        if position < 1:
            print("Invalid Position")
            return

        # Delete First Node
        if position == 1:
            print(self.head.data, "deleted from position", position)
            self.head = self.head.next
            return

        # Traverse to the node BEFORE the node to be deleted
        temp = self.head
        for _ in range(position - 2):
            if temp is None or temp.next is None:
                print("Position", position, "is out of bounds")
                return
            temp = temp.next

        if temp.next is None:
            print("Position", position, "is out of bounds")
            return

        # Delete the node
        print(temp.next.data, "deleted from position", position)
        temp.next = temp.next.next

    # Display Linked List
    def display(self):
        if self.head is None:
            print("List is Empty")
            return

        temp = self.head
        print("Singly Linked List: ", end="")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    ll = SinglyLinkedList()

    # Test Cases
    ll.insert_at_position(10, 1)   # Empty list
    ll.insert_at_position(20, 2)
    ll.insert_at_position(30, 3)
    ll.insert_at_position(25, 3)   # Middle
    ll.insert_at_position(5, 1)    # Beginning

    print("\nAfter Insertion:")
    ll.display()

    ll.delete_at_position(3)       # Delete 25
    ll.delete_at_position(1)       # Delete 5

    print("\nAfter Deletion:")
    ll.display()