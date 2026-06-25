# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Queue class using Linked List
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Insertion (Enqueue)
    def enqueue(self, value):
        new_node = Node(value)

        # If queue is empty
        if self.rear is None:
            self.front = self.rear = new_node
            print(value, "inserted into queue")
            return

        # Add node at rear
        self.rear.next = new_node
        self.rear = new_node
        print(value, "inserted into queue")

    # Deletion (Dequeue)
    def dequeue(self):
        if self.front is None:
            print("Queue Underflow! Cannot delete.")
            return

        removed_value = self.front.data
        self.front = self.front.next

        # If queue becomes empty
        if self.front is None:
            self.rear = None

        print(removed_value, "deleted from queue")

    # Display operation
    def display(self):
        if self.front is None:
            print("Queue is empty.")
            return

        print("Queue elements (front to rear):")
        temp = self.front
        while temp:
            print(temp.data)
            temp = temp.next


# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()

q.dequeue()
q.display()
