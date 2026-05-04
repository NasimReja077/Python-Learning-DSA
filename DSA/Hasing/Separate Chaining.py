class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size          # Array of head pointers

    def hash_function(self, key):
        return key % self.size

    # Insert Operation
    def insert(self, key, value):
        index = self.hash_function(key)
        new_node = Node(key, value)
        
        # If list is empty at that index
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            # Collision: traverse to end and append
            current = self.table[index]
            while current.next is not None:
                current = current.next
            current.next = new_node

    # Search Operation
    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    # Delete Operation
    def delete(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        
        while current is not None:
            if current.key == key:
                if prev is None:                    # First node
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        return False

    # Display Hash Table
    def display(self):
        for i in range(self.size):
            print(f"Index {i}: ", end="")
            current = self.table[i]
            while current:
                print(f"({current.key}, {current.value}) → ", end="")
                current = current.next
            print("None")
            
          
          
# Example Usage
if __name__ == "__main__":
     ht = HashTable()
     ht.insert(1, "One")
     ht.insert(11, "Eleven")
     ht.insert(21, "Twenty One")
     ht.display()
     print(ht.search(11))  # Output: Eleven
     ht.delete(11)
     ht.display()
     print(ht.search(11))  # Output: None
     