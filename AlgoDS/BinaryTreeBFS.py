class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
    
def BFS_basic(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    res = []
    while queue:
        res.append(queue[0].val)
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    print(res)
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
BFS(root)


        
    