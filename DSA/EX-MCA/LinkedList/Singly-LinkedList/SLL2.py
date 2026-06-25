# Question:
# Write a Python program for a singly linked list which can perform:
# i) Create the linked list
# ii) Insert element in any position
# iii) Delete the element from any position

class Node:
    def __init__(self, data):
        self.data = data # Store the value
        self.next = None # Pointer to next node

class SinglyLinkedList:
    def __init__(self):
        self.head = None # i) Create the linked list

    # ii) Insert element in any position (Handles Start and After Key)
    def insert_element(self, value, prev_key=None):
        new_node = Node(value)
        # Case: Insert at the beginning or into an empty list
        if prev_key is None or self.head is None:
            new_node.next = self.head
            self.head = new_node
            return
        
        # Case: Insert after a specific position (key)
        temp = self.head
        while temp:
            if temp.data == prev_key:
                new_node.next = temp.next # Link new node to next
                temp.next = new_node # Link current to new node
                return
            temp = temp.next

    # iii) Delete the element from any position
    def delete_element(self, key):
        temp = self.head
        prev = None
        while temp:
            if temp.data == key:
                if prev is None: # Case: Delete head
                    self.head = temp.next
                else: # Case: Delete middle or end
                    prev.next = temp.next
                return
            prev = temp
            temp = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")
        


# ---------------- MAIN PROGRAM ----------------
ll = SinglyLinkedList()
ll.insert_element(10)          # Insert at beginning
ll.insert_element(20)          # Insert at end
ll.insert_element(25, 20)      # Insert after key 20
ll.display()                   # Display list
ll.delete_element(10)         # Delete head
ll.display()                   # Display list
ll.delete_element(25)         # Delete middle
ll.display()                   # Display list


#======================OR=========================


'''
# ---------------- NODE CLASS ----------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ----------- SINGLY LINKED LIST CLASS -----------
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # i) Create the linked list
    def create(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # ii) Insert element at any position
    def insert_at_position(self, value, position):
        new_node = Node(value)

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        count = 1

        while temp and count < position - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Invalid Position")
            return

        new_node.next = temp.next
        temp.next = new_node

    # iii) Delete element from any position
    def delete_at_position(self, position):
        if self.head is None:
            print("Linked List is empty")
            return

        if position == 1:
            self.head = self.head.next
            return

        temp = self.head
        count = 1

        while temp.next and count < position - 1:
            temp = temp.next
            count += 1

        if temp.next is None:
            print("Invalid Position")
            return

        temp.next = temp.next.next

    # Display the linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")


# ---------------- MAIN PROGRAM ----------------
ll = SinglyLinkedList()

# Creating linked list
ll.create(10)
ll.create(20)
ll.create(30)

# Insert at position
ll.insert_at_position(25, 3)

# Delete from position
ll.delete_at_position(2)

# Display list
ll.display()

'''