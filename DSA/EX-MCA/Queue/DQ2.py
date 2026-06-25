class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def insertAtEnd(self, value):
        self.items.append(value)

    def insertAtFront(self, value):
        self.items.insert(0, value)

    def deleteAtFront(self):
        if(self.isEmpty()):
            print("Queue is Empty")
        else:
            return self.items.pop(0)

    def deleteAtEnd(self):
        if(self.isEmpty()):
            print("Queue is Empty")
        else:
            return self.items.pop()
       
    def display(self):
         print("Deque Elements:", self.items)
       
dq = Deque()

# Adding elements
dq.insertAtEnd(10)      # State: [10]
dq.insertAtFront(20)    # State: [20, 10]
dq.insertAtEnd(30)      # State: [20, 10, 30]
dq.insertAtEnd(40)      # State: [20, 10, 30, 40]
dq.insertAtFront(50)    # State: [50, 20, 10, 30, 40]

# Removing elements
print(dq.deleteAtEnd())   # Removes 40
print(dq.deleteAtEnd())   # Removes 30
print(dq.deleteAtFront()) # Removes 50
print(dq.deleteAtFront()) # Removes 20
print(dq.deleteAtEnd())   # Removes 10

# Attempting to delete from an empty Deque
dq.deleteAtEnd()
dq.deleteAtFront()

# Displaying Items
dq.display()


dq.insertAtEnd(30)      
dq.insertAtEnd(40) 
dq.insertAtFront(50) 
# Displaying Items
dq.display()
