class Node :
    def __init__(self,value):
        self.left = None
        self.right = None
        self.data = value

def preOrder(root):
    if (root != None):
        print(root.data , end= " ")
        preOrder(root.left)
        preOrder(root.right)
        
def InOrder(root):
    if (root != None):
        InOrder(root.left)
        print(root.data , end= " ")
        InOrder(root.right)

def PostOrder(root):
    if (root != None):
        PostOrder(root.left)
        PostOrder(root.right)
        print(root.data , end= " ")

root = Node(1)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(8)

print("Pre-order:", end=" ") 
preOrder(root) # 1 3 2 4 5 8 # Left Root Right

print("\nIn-order:", end=" ")
InOrder(root) # 2 3 4 1 5 8  # Left Right Root

print("\nPost-order:", end=" ")
PostOrder(root) # 2 4 3 8 5 1 # Left Right Root
print()