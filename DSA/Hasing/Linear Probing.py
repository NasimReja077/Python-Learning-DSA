class HashTableLinearProbing:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size          # None means empty slot
        self.deleted = "DELETED"            # Tombstone for deletion

    def hash_function(self, key):
        return key % self.size

    # INSERT
    def insert(self, key, value):
        index = self.hash_function(key)
        i = 0
        while True:
            current_index = (index + i) % self.size
            
            # If slot is empty or deleted → insert here
            if self.table[current_index] is None or self.table[current_index] == self.deleted:
                self.table[current_index] = (key, value)
                return True
            
            # If key already exists → update
            if self.table[current_index][0] == key:
                self.table[current_index] = (key, value)
                return True
            
            i += 1
            if i == self.size:              # Table is full
                return False   # or trigger rehashing

    # SEARCH
    def search(self, key):
        index = self.hash_function(key)
        i = 0
        while True:
            current_index = (index + i) % self.size
            if self.table[current_index] is None:
                return None                     # Not found
            if self.table[current_index] != self.deleted and self.table[current_index][0] == key:
                return self.table[current_index][1]
            i += 1
            if i == self.size:
                return None

    # DELETE (using tombstone)
    def delete(self, key):
        index = self.hash_function(key)
        i = 0
        while True:
            current_index = (index + i) % self.size
            if self.table[current_index] is None:
                return False
            if self.table[current_index] != self.deleted and self.table[current_index][0] == key:
                self.table[current_index] = self.deleted   # Mark as deleted
                return True
            i += 1
            if i == self.size:
                return False

    def display(self):
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")
            
            
# Example Usage:
ht = HashTableLinearProbing(10)
# Insertion Sequence: 10, 17, 24, 31, 38
ht.insert(10, "One")
ht.insert(17, "Seventeen")
ht.insert(24, "Twenty Four")
ht.insert(31, "Thirty One")
ht.insert(38, "Thirty Eight")
ht.display()
print(ht.search(17))  # Output: Seventeen
ht.delete(17)
ht.display()
print(ht.search(17))  # Output: None