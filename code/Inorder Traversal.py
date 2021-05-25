# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        res = []
        if root:
            res = res + self.solve(root.left)
            res.append(root.val)
            res = res + self.solve(root.right)
        return res

binarysearch.com
Your code took 5 milliseconds — faster than 24.07% in Python