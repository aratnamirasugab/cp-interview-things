class Solution:
    def createTargetArray(self, nums, index):
        i, res = 0, []
        
        while i < len(index):
            res.insert(index[i], nums[i])
            i += 1
        
        return res



if __name__ == '__main__':
    nums = [0,1,2,3,4]
    index = [0,1,2,2,1]
    sol = Solution().createTargetArray(nums, index)
    print(sol)