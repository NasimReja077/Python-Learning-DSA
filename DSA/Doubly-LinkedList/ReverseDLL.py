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

    # Insert at End (Helper Function)
    def insert_end(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node
        new_node.prev = temp

    # Reverse Doubly Linked List - Fixed Version
    def reverse(self):
        if self.head is None or self.head.next is None:
            return

        current = self.head

        while current:
            # Swap next and prev pointers
            next_node = current.next
            current.next = current.prev
            current.prev = next_node
            
            # Move to next node (using the original next)
            current = next_node

        # After loop, head should point to the last node (new first node)
        # We need to find the new head (the node whose prev is None)
        # Since we swapped, we can go back from original head
        self.head = self.head.prev   # Better and cleaner way


    # Display the list
    def display(self):
        if self.head is None:
            print("List is Empty")
            return
        
        temp = self.head
        print("Doubly Linked List: ", end="")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("NULL")


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    dll = DoublyLinkedList()
    
    dll.insert_end(10)
    dll.insert_end(20)
    dll.insert_end(30)
    dll.insert_end(40)
    dll.insert_end(50)

    print("Original List:")
    dll.display()

    dll.reverse()

    print("\nReversed List:")
    dll.display()