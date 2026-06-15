# ---------------- NODE CLASS ----------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ---------------- SINGLY LINKED LIST ----------------
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at End (Helper function)
    def insert_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Reverse Linked List - Iterative (Best for Exam)
    def reverse(self):
        # If the list is empty or has only one node, already reversed -> do nothing
        if self.head is None or self.head.next is None:
            return

        # Initialize three pointers: prev, current, and next_node
        
        # prev → Points to the previous node (initially None).
        # current → Points to the current node being processed (starts at head).
        # next_node → Temporary pointer to store the next node (to avoid losing the link).

        prev = None
        current = self.head
        next_node = None

        # Iterate through the list and reverse the links
        # Loop continues until current becomes None
        while current:
            next_node = current.next # Before changing anything, we save the address of the next node. # Store next node
            current.next = prev  # Reverse the direction of the link -> 1 3 5 = 5 3 1 > current points backward to prev instead of forward.
            prev = current       # Move prev forward
            current = next_node    # Move current forward

        self.head = prev     # Update head to new first node
        
        
# After the loop ends, prev is pointing to the last node of the original list.
# This last node is now the new head of the reversed list.
# So we update self.head = prev.


    # Display
    def display(self):
        if not self.head:
            print("List is Empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    ll = SinglyLinkedList()
    
    ll.insert_end(10)
    ll.insert_end(20)
    ll.insert_end(30)
    ll.insert_end(40)
    ll.insert_end(50)

    print("Original List:")
    ll.display()

    ll.reverse()

    print("Reversed List:")
    ll.display()
    
