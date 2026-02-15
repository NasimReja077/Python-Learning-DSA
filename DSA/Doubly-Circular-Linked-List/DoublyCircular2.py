# ---------------- NODE CLASS ----------------
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# ------------- DOUBLY CIRCULAR LINKED LIST CLASS -------------
class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None


    # ---------- INSERT OPERATIONS ----------

    # i) Insert at Beginning
    def insert_beginning(self, value):
        new_node = Node(value)

        if self.head is None:
            # Empty list - node points to itself
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            print(value, "inserted as first node")
            return

        # Find last node
        last = self.head.prev

        # Connect new node
        new_node.next = self.head
        new_node.prev = last
        
        # Update head and last connections
        self.head.prev = new_node
        last.next = new_node
        
        # Update head pointer
        self.head = new_node
        print(value, "inserted at beginning")


    # ii) Insert at End
    def insert_end(self, value):
        new_node = Node(value)

        if self.head is None:
            # Empty list - node points to itself
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            print(value, "inserted as first node")
            return

        # Last node is head.prev (advantage of doubly circular!)
        last = self.head.prev

        # Connect new node
        new_node.next = self.head
        new_node.prev = last
        
        # Update connections
        last.next = new_node
        self.head.prev = new_node
        
        print(value, "inserted at end")


    # iii) Insert after a given value
    def insert_after(self, prev_value, value):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        
        while True:
            if temp.data == prev_value:
                new_node = Node(value)
                
                # Connect new node
                new_node.next = temp.next
                new_node.prev = temp
                
                # Update surrounding nodes
                temp.next.prev = new_node
                temp.next = new_node
                
                print(value, "inserted after", prev_value)
                return

            temp = temp.next
            if temp == self.head:
                break

        print("Value", prev_value, "not found")


    # ---------- DISPLAY / TRAVERSING ----------
    
    def display_forward(self):
        if self.head is None:
            print("Doubly Circular Linked List is empty")
            return

        temp = self.head
        print("Doubly Circular Linked List (Forward):")
        
        while True:
            print(temp.data, end=" ⇄ ")
            temp = temp.next
            if temp == self.head:
                break
        
        print("(back to head)")


    def display_backward(self):
        if self.head is None:
            print("Doubly Circular Linked List is empty")
            return

        # Start from last node
        last = self.head.prev
        temp = last
        
        print("Doubly Circular Linked List (Backward):")
        
        while True:
            print(temp.data, end=" ⇄ ")
            temp = temp.prev
            if temp == last:
                break
        
        print("(back to last)")


    # ---------- SEARCH ----------
    
    def search(self, key):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        position = 1
        
        while True:
            if temp.data == key:
                print(key, "found at position", position)
                return
            
            temp = temp.next
            position += 1
            
            if temp == self.head:
                break

        print(key, "not found in the list")


    # ---------- COUNT NODES ----------
    
    def count_nodes(self):
        if self.head is None:
            print("Total number of nodes: 0")
            return 0

        count = 0
        temp = self.head
        
        while True:
            count += 1
            temp = temp.next
            if temp == self.head:
                break

        print("Total number of nodes:", count)
        return count


    # ---------- DELETE OPERATIONS ----------

    # i) Delete from Beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        # Only one node
        if self.head.next == self.head:
            print(self.head.data, "deleted (only node)")
            self.head = None
            return

        # More than one node
        last = self.head.prev
        deleted_value = self.head.data
        
        # Update connections
        self.head.next.prev = last
        last.next = self.head.next
        
        # Move head
        self.head = self.head.next
        
        print(deleted_value, "deleted from beginning")


    # ii) Delete from End
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        # Only one node
        if self.head.next == self.head:
            print(self.head.data, "deleted (only node)")
            self.head = None
            return

        # More than one node
        last = self.head.prev
        deleted_value = last.data
        
        # Update connections
        last.prev.next = self.head
        self.head.prev = last.prev
        
        print(deleted_value, "deleted from end")
    
    # iii) Delete a given element 
    def delete_element(self, key):
        if self.head is None:
            print("List is empty")
            return
        
        temp = self.head
        
        while True:
            if temp.data == key:
                # Case 1: Only one node
                if temp.next == temp:
                    self.head = None
                    print(key, "deleted (only node)")
                    return

                # Case 2: Deleting head node
                if temp == self.head:
                    last = self.head.prev

                    self.head.next.prev = last
                    last.next = self.head.next
                    self.head = self.head.next

                    print(key, "deleted from beginning")
                    return

                # Case 3: Deleting middle or last node
                temp.prev.next = temp.next
                temp.next.prev = temp.prev

                print(key, "deleted from the list")
                return
            temp = temp.next
            
            if temp == self.head:
                break
            print(key, "not found")
    
# ---------------- MAIN PROGRAM ----------------
dcll = DoublyCircularLinkedList()

print("=" * 60)
print("DOUBLY CIRCULAR LINKED LIST OPERATIONS")
print("=" * 60)

print("\n--- INSERT OPERATIONS ---")
dcll.insert_beginning(10)
dcll.insert_beginning(5)
dcll.insert_end(20)
dcll.insert_end(30)
dcll.insert_after(20, 25)

print("\n--- DISPLAY FORWARD ---")
dcll.display_forward()

print("\n--- DISPLAY BACKWARD ---")
dcll.display_backward()

print("\n--- SEARCH OPERATIONS ---")
dcll.search(25)
dcll.search(100)

print("\n--- COUNT NODES ---")
dcll.count_nodes()

print("\n--- DELETE OPERATIONS ---")
dcll.delete_beginning()
dcll.display_forward()

dcll.delete_end()
dcll.display_forward()

dcll.delete_element(20)
dcll.display_forward()

dcll.count_nodes()

print("\n" + "=" * 60)