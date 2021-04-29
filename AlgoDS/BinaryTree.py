class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def printTree(self):
        if self.left:
            self.left.printTree()
        
        print(self.val)
        
        if self.right:
            self.right.printTree()
    
    def insertNewNode(self, key):
        if self.val:
            if key < self.val:
                if self.left is None:
                    self.left = Node(key)
                else:
                    self.left.insertNewNode(key) 
            elif key > self.val:
                if self.right is None:
                    self.right = Node(key)
                else:
                    self.right.insertNewNode(key)
        else:
            self.val = key

    def findValue(self, key):
        if key < self.val:
            if self.left is None:
                return str(key) + " is not found"
            return self.left.findValue(key)

        elif key > self.right:
            if self.right is None:
                return str(key) + " is not found"
            return self.right.findValue(key)
        else:
            print(self.val + " is found")

    def preOrderTraversal(self, root):
        # DLR
        result = []
        if root:
            result.append(root.val)
            result = result + self.preOrderTraversal(root.left)
            result = result + self.preOrderTraversal(root.right)

        return result

                

if __name__ == '__main__':
    root = Node(1)
    root.right = Node(2)
    root.right.left = Node(3)
    root.preOrderTraversal(root)

