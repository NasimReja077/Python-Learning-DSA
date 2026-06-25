
ALGORITHM: InsertNode(data)

Input:  data to be inserted
Output: Updated binary tree (complete as possible)

Step 1: Create a new node
        newNode (N) ← Node(data)

Step 2: If tree is empty (root == NULL):
        root ← newNode
        Return

Step 3: Create an empty Queue Q
        Enqueue root into Q

Step 4: Insert root into queue


Step 5: While Q is not empty:
        temp ← Dequeue() from Q // delete front node from queue

        // Try to insert as Left Child first
        IF temp.left == NULL:
            temp.left ← newNode
            Return

        ELSE:
            Enqueue temp.left into Q

        // Then try to insert as Right Child
        IF temp.right == NULL:
            temp.right ← newNode
            Return

        ELSE:
            Enqueue temp.right into Q // insert temp.right into queue



🔹 2. Algorithm: Inorder Traversal
ALGORITHM: InOrder(node)
Step 1: If node is not None:
        InOrder(node.left)          // Visit Left // Traverse left subtree
        Print node.data             // Visit Root // Visit node (print data)
        InOrder(node.right)         // Visit Right // Traverse right subtree

🔹 3. Algorithm: Preorder Traversal
ALGORITHM: PreOrder(node)
Step 1: If node is not None:
        Print node.data             // Visit Root // Visit node (print data)
        PreOrder(node.left)         // Visit Left // Traverse left subtree
        PreOrder(node.right)        // Visit Right // Traverse right subtree


🔹 4. Algorithm: Postorder Traversal
ALGORITHM: PostOrder(node)
Step 1: If node is not None:
        PostOrder(node.left)        // Visit Left //  Traverse left subtree
        PostOrder(node.right)       // Visit Right // Traverse right subtree
        Print node.data             // Visit Root // Visit node (print data)


🔹 5. Algorithm: Level Order Traversal
ALGORITHM: LevelOrderTraversal()

Step 1: If root is None:
        Print "Tree is empty"
        Return

Step 2: Create an empty queue
        Enqueue root

Step 3: While queue is not empty:
        temp ← Dequeue front node
        Print temp.data

        If temp.left is not None:
            Enqueue temp.left // insert temp.left into queue
          
        If temp.right is not None:
            Enqueue temp.right // insert temp.right into queue


🔹 6. ALGORITHM: Display Tree Structure

ALGORITHM: Display()

Step 1: If root is None:
        Print "Tree is empty"
        Return

Step 2: Create an empty queue
        Enqueue root

Step 3: While queue is not empty:
        temp ← Dequeue
        left  ← temp.left.data  if temp.left else "NULL"
        right ← temp.right.data if temp.right else "NULL"
        Print temp.data → L: left  R: right

        If temp.left  ≠ None: Enqueue temp.left
        If temp.right ≠ None: Enqueue temp.right
