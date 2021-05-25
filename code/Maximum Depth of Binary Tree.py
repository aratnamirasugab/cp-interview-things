# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root == None:
            return 0
        
        else:
            
            lDepth = self.maxDepth(root.left)
            rDepth = self.maxDepth(root.right)
            
            if lDepth > rDepth:
                return lDepth + 1
            else:
                return rDepth + 1
        


# Runtime: 36 ms, faster than 26.17% of Python online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 16.1 MB, less than 43.94% of Python online submissions for Maximum Depth of Binary Tree.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root == None:
            return 0
        
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))

# Runtime: 36 ms, faster than 26.17% of Python online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 16.1 MB, less than 69.82% of Python online submissions for Maximum Depth of Binary Tree.
