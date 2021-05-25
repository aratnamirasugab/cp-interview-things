# Given a binary search tree root, and integers lo and hi, return the count of all nodes in root whose values are between [lo, hi] (inclusive).

# Constraints :
# n ≤ 100,000 where n is the number of nodes in root

# Example 1

# Input
# root = [3, [2, null, null], [9, [7, [4, null, null], [8, null, null]], [12, null, null]]]
# lo = 5
# hi = 10

# Output
# 3
# Explanation
# Only 7, 8, 9 are between [5, 10].


# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, lo, hi):
        res = 0
        if root:
            if root.val >= lo and root.val <= hi:
                res += 1
            res = res + self.solve(root.left, lo, hi)
            res = res + self.solve(root.right, lo, hi)
        return res


# binarysearch.com
# Your code took 5 milliseconds — faster than 31.38% in Python


# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, lo, hi):
        if root is None: return 0

        res = 0
        queue = [root]

        while queue:
            node = queue.pop(0)
            if node.val >= lo and node.val <= hi: res += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return res

# Your code took 4 milliseconds — faster than 58.26% in Python