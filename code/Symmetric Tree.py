# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.traverse(root, root)
        
    def traverse(self, t1, t2):
        if t1 == None and t2 == None: return True
        if t1 == None or t2 == None: return False
        return t1.val == t2.val and self.traverse(t1.right, t2.left) and self.traverse(t1.left, t2.right)
        
# Runtime: 8 ms, faster than 99.87% of Python online submissions for Symmetric Tree.
# Memory Usage: 13.7 MB, less than 52.22% of Python online submissions for Symmetric Tree.