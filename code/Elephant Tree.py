# Given a binary tree root, return the same tree except every node's value is replaced by its original value plus all of the sums of its left and right subtrees.

# Constraints

# n ≤ 100,000 where n is the number of nodes in root
# Example 1
# Input
# Visualize
# root = [2, [1, [0, null, null], null], [4, [3, null, null], null]]
# Output
# Visualize
# [10, [1, [0, null, null], null], [7, [3, null, null], null]]


# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if root is None: return

        queue = [root]

        while queue:
            node = queue.pop(0)
            if node:
                node.val = self.countBottom(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root


    def countBottom(self, root):
        queue = [root]
        res = 0
        while queue:
            node = queue.pop(0)
            if node:
               res += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res 
            
# binarysearch.com
# Your code took 65 milliseconds — faster than 4.46% in Python

