class Node():
    def __init__(self,data,left=None,right=None):
        self.left = left
        self.right = right
        self.data = data

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.data,end = " ")
        if self.right:
            self.right.inorder_traversal()


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)

root.inorder_traversal()

