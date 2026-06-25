class ThreadedNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.leftThread = False   # True if left points to predecessor (thread)
        self.rightThread = False  # True if right points to successor (thread)


def inorderThreadedTraversal(root):
    if not root:
        return
    
    current = root
    
    # Step 1: Go to the leftmost node
    while current and not current.leftThread:
        current = current.left
    
    # Step 2: Traverse using threads
    while current:
        print(current.data, end=" ")   # Visit node
        
        if current.rightThread:
            # Direct successor via thread
            current = current.right
        else:
            # Go to right child and then leftmost
            current = current.right
            while current and not current.leftThread:
                current = current.left


# Example Usage (for testing)
if __name__ == "__main__":
    # Create a sample threaded tree (manually for demonstration)
    root = ThreadedNode(50)
    root.left = ThreadedNode(30)
    root.right = ThreadedNode(70)
    root.left.left = ThreadedNode(20)
    root.left.right = ThreadedNode(40)
    root.right.left = ThreadedNode(60)
    root.right.right = ThreadedNode(80)
    
    # Set threads (simplified for example)
    root.left.left.rightThread = True
    root.left.left.right = root.left          # 20 -> 30
    root.left.rightThread = True
    root.left.right = root                    # 40 -> 50
    # ... (In real code, threads are set during construction)
    
    print("Inorder Traversal:")
    inorderThreadedTraversal(root)
    
    
    
'''
Algorithm Inorder_Threaded_Traversal(root):

    Step 1: If root is NULL, return

    Step 2: Initialize current = root

    Step 3: Go to the leftmost node
           while (current != NULL and current.leftThread == False):
               current = current.left

    Step 4: Repeat until current becomes NULL:
           a. Visit / Print current.data
           b. If current.rightThread == True:
                  current = current.right          // Follow thread to successor
              Else:
                  current = current.right
                  // Go to leftmost node in the right subtree
                  while (current != NULL and current.leftThread == False):
                      current = current.left
'''
