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

     # i) Create + ii) Insert at Any Position
    def insert_at_position(self, value, position):
        if position < 1:
            print("Invalid Position!")
            return

        new_node = Node(value)
        
        # Case 1: Empty List or Insert at Position 1 (First Position)
        if self.head is None or position == 1:
            # Empty list
            if self.head is None:
                self.head = new_node
                new_node.next = self.head  # <<< Point new node to itself to maintain circular structure
                print(value, "inserted as first node")
                return

            # Find last node
            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            new_node.next = self.head
            temp.next = new_node
            self.head = new_node
            print(value, "inserted at position", position)
            return

        temp = self.head

        # Case 2: Insert at Middle or Last Position
        for _ in range(position - 2):
            temp = temp.next
            if temp.next == self.head:          # Reached end of list
                break

        # Insert the new node
        new_node.next = temp.next
        temp.next = new_node

        print(value, "inserted at position", position)

    # iii) Delete element from any position
    def delete_at_position(self, position):

        if self.head is None:
            print("List is Empty")
            return
        
        if position < 1:
            print("Invalid Position")
            return
        

        # Delete First Node (Position 1)
        if position == 1:
            # Only one node
            if self.head.next == self.head:        # Only one node
                print(self.head.data, "deleted from position 1")
                self.head = None
                return

            # More than one node
            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            print(self.head.data, "deleted from position 1") # <<<
            temp.next = self.head.next # Update last node's next pointer
            self.head = self.head.next # Update head to the next node
            return
        
         # Delete Middle or Last Node
        temp = self.head

        for _ in range(position - 2):
            temp = temp.next # 10 20 30 -> temp =  20 and temp.next = 30 
            
            # Now delete the node
            if temp.next == self.head: # Trying to delete head (invalid case)
                print("Invalid Position")
                return
        
        print(temp.next.data, "deleted from position", position)
        temp.next = temp.next.next # Update the next pointer to skip the deleted node # 10 20 30 40 -> temp.next = 40 (skipping 30) temp.next.next = 40.next = 10 (back to head)
        

   # Display
    def display(self):
        if self.head is None:
            print("List is Empty")
            return

        temp = self.head
        print("Circular Linked List: ", end="")
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to", self.head.data, ")")


# ---------------- MAIN PROGRAM ----------------
cll = CircularLinkedList()

cll.insert_at_position(10, 1)
cll.insert_at_position(20, 2)
cll.insert_at_position(15, 2)
cll.insert_at_position(30, 3)
cll.insert_at_position(25, 3)

print("After Insertion:")
cll.display()

cll.delete_at_position(3)

print("After Deletion:")
cll.display()