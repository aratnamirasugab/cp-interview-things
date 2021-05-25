# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        resLeft = self.traverse(p)
        resRight = self.traverse(q)
        return resLeft == resRight
        
    def traverse(self, root):
        result = []
        
        if root == None:
            result.append(None)
        
        if root:
            result.append(root.val)
            result = result + self.traverse(root.left)
            result = result + self.traverse(root.right)
            
        return result
        
        
# Runtime: 16 ms
# Memory Usage: 13.4 MB