# Definition for a binary tree node.
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    
    def sortedArrayToBST(self, nums):
        if not nums:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root

    def inorderPrint(self, root):
        res = []
        if root:
            res += self.inorderPrint(root.left)
            res.append(root.val)
            res += self.inorderPrint(root.right)

        return res


if __name__ == '__main__':
    nums = [-10,-3,0,5,9]
    sol = Solution().sortedArrayToBST(nums)
    prt = Solution().inorderPrint(sol)
    print(prt)


# Runtime: 52 ms, faster than 45.06% of Python online submissions for Convert Sorted Array to Binary Search Tree.
# Memory Usage: 16.3 MB, less than 15.88% of Python online submissions for Convert Sorted Array to Binary Search Tree.
        
        
        
        
        