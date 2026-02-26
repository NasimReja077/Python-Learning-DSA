class DisjointSet:
    def __init__(self, n):
        # Initially, every element is its own parent (its own set)
        self.parent = [i for i in range(n)]
        # Rank is used to keep the tree flat
        self.rank = [0] * n

    def find(self, i):
        # Path Compression: 
        # Directly attach the node to the root to speed up future lookups
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        # Find the roots of the sets containing i and j
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # Union by Rank: Attach the smaller tree under the taller tree
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1
            return True # Successfully joined
        return False # They were already in the same set
   
    def connected(self, i, j):
          # Check if i and j are in the same set
          return self.find(i) == self.find(j)
    def print_sets(self):
          print("Parent array:", self.parent)
          print("Rank array :", self.rank)
          
          
ds = DisjointSet(7)

print(ds.union(0,1))   # True
print(ds.union(1,2))   # True
print(ds.union(3,4))   # True
print(ds.union(0,2))   # False (already connected)
print(ds.union(4,5))   # True
print(ds.union(5,6))   # True
print(ds.union(2,6))   # True – connects two components

print("Parents:", ds.parent)
# You should see most nodes pointing directly to one of the roots




'''
# Assuming the DisjointSet class you provided is above this line

# 1. Initialize a Disjoint Set with 5 elements (0, 1, 2, 3, 4)
ds = DisjointSet(5)

# 2. Connect elements
print(f"Union(0, 1): {ds.union(0, 1)}") # True: 0 and 1 are now joined
print(f"Union(2, 3): {ds.union(2, 3)}") # True: 2 and 3 are now joined
print(f"Union(1, 2): {ds.union(1, 2)}") # True: 0, 1, 2, and 3 are now all connected

# 3. Check connectivity
# Since 0 is connected to 1, and 1 is connected to 2... 0 is connected to 3.
if ds.find(0) == ds.find(3):
    print("0 and 3 are in the same set") # This will print
else:
    print("0 and 3 are NOT in the same set")

# 4. Check an unconnected element
print(f"Is 4 connected to 0? {ds.find(4) == ds.find(0)}") # False

# 5. Redundant Union
print(f"Union(0, 3): {ds.union(0, 3)}") # False: Already in the same set

'''