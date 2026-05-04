class HashTableQuadratic:
    def __init__(self, size=11):           # Prime size is better
        self.size = size
        self.table = [None] * size
        self.deleted = "DELETED"

    def hash_function(self, key):
        return key % self.size

    # INSERT
    def insert(self, key, value):
        index = self.hash_function(key)
        i = 0
        while True:
            probe_index = (index + i * i) % self.size   # Quadratic: i²
            
            if self.table[probe_index] is None or self.table[probe_index] == self.deleted:
                self.table[probe_index] = (key, value)
                return True
            
            if self.table[probe_index][0] == key:       # Update
                self.table[probe_index] = (key, value)
                return True
            
            i += 1
            if i == self.size:                          # Table full
                return False   # or rehash

    # SEARCH
    def search(self, key):
        index = self.hash_function(key)
        i = 0
        while True:
            probe_index = (index + i * i) % self.size
            if self.table[probe_index] is None:
                return None
            if self.table[probe_index] != self.deleted and self.table[probe_index][0] == key:
                return self.table[probe_index][1]
            i += 1
            if i == self.size:
                return None

    # DELETE
    def delete(self, key):
        index = self.hash_function(key)
        i = 0
        while True:
            probe_index = (index + i * i) % self.size
            if self.table[probe_index] is None:
                return False
            if self.table[probe_index] != self.deleted and self.table[probe_index][0] == key:
                self.table[probe_index] = self.deleted
                return True
            i += 1
            if i == self.size:
                return False

    def display(self):
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")
            
            
# Insert Keys: 10, 21, 32, 43, 54, 65

ht = HashTableQuadratic(11)
ht.insert(10, "Ten")
ht.insert(21, "Twenty One")
ht.insert(32, "Thirty Two")
ht.insert(43, "Forty Three")
ht.insert(54, "Fifty Four")
ht.insert(65, "Sixty Five")
ht.display()
print(ht.search(32)) 
ht.delete(21)
ht.display()
print(ht.search(21))
