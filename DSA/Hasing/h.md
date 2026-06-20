**Review of Hashing** is the introductory part of **Unit 7 (Hashing)** in your MAKAUT MCAN-201 syllabus. It provides the foundational concepts before diving into **Hash Function**, **Collision Resolution Techniques**, **Separate Chaining**, **Open Addressing** (Linear, Quadratic Probing), **Double Hashing**, **Rehashing**, and **Extendible Hashing**.

### What is Hashing?

**Hashing** is a technique used in data structures that allows **fast storage and retrieval** of data by mapping keys to positions in a data structure called a **Hash Table** (usually an array).

- It uses a **hash function** to compute an index (hash value) from the key.
- The goal is to achieve **average-case time complexity of O(1)** for the three main operations:
  - **Search**
  - **Insert**
  - **Delete**

This is much faster than:
- Linear Search → O(n)
- Binary Search → O(log n)
- Balanced BST (AVL, Red-Black) → O(log n)

### Why Do We Need Hashing? (Motivation / Review from Previous Units)

In previous units you studied:

| Data Structure       | Search Time     | Insert Time     | Delete Time     | Ordered? | Range Query? |
|----------------------|-----------------|-----------------|-----------------|----------|--------------|
| Array / List         | O(n)            | O(n)            | O(n)            | No       | Yes          |
| Sorted Array         | O(log n)        | O(n)            | O(n)            | Yes      | Yes          |
| Singly Linked List   | O(n)            | O(1) (at head)  | O(n)            | No       | No           |
| **Binary Search Tree** (balanced) | **O(log n)** | **O(log n)** | **O(log n)** | Yes | Yes |
| **Hash Table**       | **O(1) avg**    | **O(1) avg**    | **O(1) avg**    | No       | No           |

**Hashing** gives the best **average-case performance** for dictionary operations (key → value mapping) when order and range queries are not required.

### Direct Addressing vs Hashing

This comparison is very important (it appeared in one of your papers as "What is direct addressing?").

- **Direct Addressing**:
  - Keys are used **directly as indices** in an array.
  - Example: If keys are integers from 0 to 999, we can use an array of size 1000.
  - **Advantage**: True O(1) time, no collisions.
  - **Disadvantage**: Requires keys to be small and dense. Wastes huge memory if key range is large (e.g., keys up to 10^9 or strings).

- **Hashing**:
  - Uses a **hash function** `h(key)` to map a large key space into a small array size `m`.
  - `index = h(key) % m`
  - Solves the memory waste problem of direct addressing.
  - Introduces **collisions** (two different keys map to same index).

**Conclusion of Review**: Direct addressing is ideal when possible, but for real-world large/sparse keys (strings, large integers, objects), **hashing** is the practical solution.

### Basic Components of Hashing

1. **Keys** — The data we want to store (integer, string, object, etc.).
2. **Hash Function** — Mathematical function that converts key → integer index (0 to m-1).
3. **Hash Table** — An array of fixed size `m` (buckets/slots).
4. **Collision** — When `h(k1) == h(k2)` but `k1 ≠ k2`.

### How Hashing Works (Simple Example)

Suppose we have a hash table of size **m = 10**.

Hash function: `h(key) = key % 10`

Insert keys: 23, 45, 56, 67, 78

- 23 → 3
- 45 → 5
- 56 → 6
- 67 → 7
- 78 → 8

All good — no collision.

Now insert **88** → `88 % 10 = 8` → **Collision** with 78.

This is where **Collision Resolution Techniques** come in (covered in next topics of the unit).

### Advantages of Hashing

- **Extremely fast average-case performance** — O(1) for insert, search, delete.
- Simple and efficient for implementing **dictionaries** / **maps** / **sets**.
- Good memory utilization compared to direct addressing when keys are sparse.
- Widely used in real-world applications:
  - Symbol tables in compilers
  - Database indexing
  - Caches (Python dict, Java HashMap, etc.)
  - Password storage (though with salting)
  - Checksums and data integrity

### Disadvantages / Limitations of Hashing

- **Collisions** are inevitable (pigeonhole principle).
- **Worst-case time complexity** can degrade to **O(n)** if many collisions occur (poor hash function or high load factor).
- **No ordering** — cannot efficiently do range queries, find min/max, or sorted traversal (unlike BST).
- **Hash function design** is critical — a bad hash function leads to many collisions.
- **Memory overhead** due to empty slots or linked lists (in chaining).
- **Rehashing** may be needed when table becomes too full.

### Load Factor (α)

**Load Factor = (Number of elements stored) / (Size of hash table)**

- Lower load factor → fewer collisions → better performance.
- Usually kept below **0.7** for open addressing.
- Higher load factor → more collisions → performance drops.

When load factor becomes high, we perform **Rehashing** (resize the table and re-insert all elements) — this is an expensive operation but amortized.

### Applications of Hashing (Important for Exam)

- Implementing associative arrays / dictionaries
- Caching (LRU Cache uses hash map)
- Database indexing (hash indexes)
- Cryptography (though cryptographic hash functions like SHA-256 are different — one-way and collision-resistant)
- Detecting duplicates
- Finding anagrams / substrings

### Comparison Summary (Good for 5-mark or part of 15-mark)

- **Hashing vs Array**: Hashing allows search by **key** (not index) in O(1) avg.
- **Hashing vs Linked List**: Much faster search.
- **Hashing vs BST**: Faster on average, but BST maintains order and supports range queries.
- **Hash Table vs Direct Address Table**: Hashing handles large key space efficiently but introduces collisions.

### Key Points to Remember for MAKAUT Exam

- **"Review of Hashing"** mainly expects:
  - Definition of hashing
  - Need / motivation (comparison with other DS)
  - Direct addressing vs Hashing
  - Basic idea of hash function and hash table
  - Concept of collision
  - Advantages and disadvantages
  - Average vs Worst case time complexity

- Always mention **O(1) average case** but **O(n) worst case** due to collisions.

- Draw a simple diagram of hash table + hash function in the answer.

This "Review of Hashing" sets the stage for the rest of the unit. Once you understand this foundation clearly, the topics like **Hash Function** (design goals: fast, uniform distribution, minimize collisions) and **Collision Resolution Techniques** (Separate Chaining vs Open Addressing) become much easier.

Would you like me to explain the next part in depth — **Hash Function** (with examples of different methods like Division, Multiplication, Folding, Mid-square) or directly move to **Collision Resolution Techniques** with diagrams and Python code examples? Let me know!