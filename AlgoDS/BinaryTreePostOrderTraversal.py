class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def postorderTraversalRecursive(self, root: TreeNode) -> List[int]:
        res = []
        if root:
            res = res + self.postorderTraversal(root.left)
            res = res + self.postorderTraversal(root.right)
            res.append(root.val)
        return res

