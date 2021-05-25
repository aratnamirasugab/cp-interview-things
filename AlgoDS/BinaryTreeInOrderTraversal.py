class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def InOrderTraversalRecursion(self, root):
        res = []
        if root:
            res = res + self.InOrderTraversalRecursion(root.left)
            res.append(root.data)
            res = res + self.InOrderTraversalRecursion(root.right)
        return res

    def inorderTraversalIterative(self, root):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
        return res

root = Node(1)
root.right = Node(2)
root.right.left = Node(3)
print(root.InOrderTraversalRecursion(root))