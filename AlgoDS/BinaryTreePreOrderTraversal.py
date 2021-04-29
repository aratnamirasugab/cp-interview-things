class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# Preorder traversal
# Root -> Left ->Right
    def PreorderTraversalUsingRecursion(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversalUsingRecursion(root.left)
            res = res + self.PreorderTraversalUsingRecursion(root.right)
        return res

# Preorder traversal
# Data -> Left -> Right
    def PreorderTraversalUsingIterative(self, root):
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.data)
                stack.append(node.right)
                stack.append(node.left)
        return res

# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/992/
root = Node(1)
root.right = Node(2)
root.right.left = Node(3)
print(root.PreorderTraversalUsingIterative(root))
