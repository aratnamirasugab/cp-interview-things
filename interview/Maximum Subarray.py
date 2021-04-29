class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) == 1: return nums[0]

        maxVal = currMax = nums[0]
        for item in nums[1:]:
            currMax = max(item, currMax+item)
            maxVal = max(currMax, maxVal)
        
        return maxVal

if __name__ == '__main__':
    arr = [5,4,-1,7,8]
    sol = Solution().maxSubArray(arr)
    print(sol) 

Runtime: 56 ms, faster than 26.80% of Python online submissions for Maximum Subarray.
Memory Usage: 14.2 MB, less than 71.67% of Python online submissions for Maximum Subarray.