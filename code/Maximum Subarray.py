class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]

        currMax = maxVal = nums[0]
        for x in nums[1:]:
            currMax = max(x, currMax+x)
            maxVal = max(maxVal, currMax)

        return maxVal
    

if __name__ == '__main__':
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    sol = Solution().maxSubArray(arr)
    print(sol) 

# Runtime: 56 ms, faster than 26.80% of Python online submissions for Maximum Subarray.
# Memory Usage: 14.2 MB, less than 71.67% of Python online submissions for Maximum Subarray.