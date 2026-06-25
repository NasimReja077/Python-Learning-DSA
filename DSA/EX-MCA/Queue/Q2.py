class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self, value):
        self.queue.append(value)

    def delete(self):
        if(self.isEmpty()):
            print("Queue is Empty")
        else:
            return self.queue.pop(0)
       
#     def display(self):
#          print("Queue Elements:", self.queue)
          
       
q = Queue()
q.insert(10)
q.insert(20)
q.insert(30)
print(q.delete())
print(q.delete())
print(q.delete())

print(q.delete())

# q.display()