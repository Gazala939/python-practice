class Node():
    def __init__(self, data,left = None,right = None):
        self.left = left
        self.right = right
        self.data = data



    def PrintTree(self):
        print(self.data)
        if self.left:
            print("Left:", self.left.data)
        if self.right:
            print("Right:", self.right.data)


# Creating nodes
root = Node(1)
root.left = Node(2)
root.right = Node(3)

# Printing the tree
root.PrintTree()
