# ---------------- NODE CLASS ----------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ------------- SINGLY LINKED LIST CLASS -------------
class SinglyLinkedList:
    def __init__(self):
        self.head = None


    # i) Insert a node at the beginning
    def insert_beginning(self, value):
        # case1: If list is empty, new node becomes head
        if self.head is None:
            self.head = Node(value)
            print(value, "inserted at beginning")
            return

        # case2: If list is not empty, new node points to current head, and then new node becomes head
        new_node = Node(value) # Node(value) mines creating a new node with given value
        new_node.next = self.head # new_node.next = self.head 
        self.head = new_node
        print(value, "inserted at beginning")


    # ii) Insert a node at the end
    def insert_end(self, value):
        new_node = Node(value) # Create a new node with given value

        # case1: If list is empty, new node becomes head
        if self.head is None:
            self.head = new_node # If list is empty, new node becomes head, 
            print(value, "inserted at end")
            return
        
        # case2: If list is not empty, traverse to the last node, and then link new node to it
        temp = self.head # Start from head node 
        while temp.next:
            temp = temp.next # Traverse to the last node, and then link new node to it 
        
        temp.next = new_node # Link the last node to new node, and new node points to None
        print(value, "inserted at end")


    # iii) Insert a node in between (after a given value)
    def insert_after(self, prev_value, value):
        temp = self.head # temp is used to traverse the list

        while temp:
            if temp.data == prev_value: # Found the previous value, temp.data is meaning the data of current node
                new_node = Node(value) # Create a new node with given value
                new_node.next = temp.next # Link new node to the next of current node, new_node.next means the next of new node , new_node.next = temp.next means the next of new node is linked to the next of current node
                temp.next = new_node # Link current node to new node
                print(value, "inserted after", prev_value)
                return
            temp = temp.next # Move to the next node

        print("Value", prev_value, "not found")

    # Insert at any position
    def insert_at_position(self, value, position):
        new_node = Node(value)
        
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            print(value, "inserted at position", position)
            return
        temp = self.head
        for i in range(position - 2):
            if temp is None:
                print("Position", position, "is out of bounds")
                return
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        print(value, "inserted at position", position)
        
     
    # iv) Display / Traversing the list+
    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return

        temp = self.head # Start from head node, temp means current node, so temp = self.head means current node is head node
        print("Linked List:")
        while temp:
            print(temp.data, end=" -> ") #temp.data means the data of current node, end=" -> " means print " -> " after printing the data of current node
            temp = temp.next # Move to the next node
        print("NULL")


    # v) Search an element
    def search(self, key):
        temp = self.head

        while temp:
            if temp.data == key:
                print(key, "found in the linked list")
                return
            temp = temp.next

        print(key, "not found in the linked list")


    # vi) Count number of nodes
    def count_nodes(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        print("Total number of nodes:", count)


    # vii) Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        print(self.head.data, "deleted from beginning") # self.head.data means the data of head node
        self.head = self.head.next


    # viii) Delete from middle (given element)
    def delete_middle(self, key):
        temp = self.head
        prev = None

        while temp:
            if temp.data == key: # Found the key to be deleted
                # Case 1: If the node to be deleted is the head node, update head to next node
                if prev is None:
                    self.head = temp.next #If head node is to be deleted, update head to next node
                else:
                # Case 2: If the node to be deleted is in the middle or end, link previous node to next node, effectively removing current node from the list
                    prev.next = temp.next 
                print(key, "deleted from linked list")
                return
            # Move prev and temp to next nodes
            prev = temp # Move prev to current node
            temp = temp.next 

        print(key, "not found")


    # ix) Delete from end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            print(self.head.data, "deleted from end")
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next

        print(temp.next.data, "deleted from end") # <<< 
        temp.next = None
        
    # x) Delete from any position
    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty")
            return

        if position == 1:
            print(self.head.data, "deleted from position", position)
            self.head = self.head.next
            return

        temp = self.head
        for i in range(position - 2):
            if temp is None or temp.next is None:
                print("Position", position, "is out of bounds")
                return
            temp = temp.next

        print(temp.next.data, "deleted from position", position)
        temp.next = temp.next.next


# ---------------- MAIN PROGRAM ----------------
ll = SinglyLinkedList()

ll.insert_beginning(10)
ll.insert_end(20)
ll.insert_end(30)
ll.insert_after(20, 25)

ll.display()

ll.insert_at_position(6, 2)
ll.display()

ll.search(25)
ll.count_nodes()

ll.delete_beginning()
ll.delete_middle(25)
ll.delete_end()
ll.delete_at_position(2)
ll.display()
# emupedia