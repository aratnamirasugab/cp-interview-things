# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True
        
        depthLeft = self.maxDepth(root.left)
        depthRight = self.maxDepth(root.right)
        
        diff = abs(depthLeft - depthRight)
        return diff <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def maxDepth(self, root):
        if root == None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# Runtime: 64 ms, faster than 17.80% of Python online submissions for Balanced Binary Tree.
# Memory Usage: 17.7 MB, less than 85.59% of Python online submissions for Balanced Binary Tree.

        
        