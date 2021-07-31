class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        prefixSum = [None] * (len(nums) + 1)
        suffixSum = [None] * (len(nums) + 1)

        prefixSum[0] = 1
        suffixSum[len(suffixSum)-1] = 1

        i = 1
        while i < len(prefixSum):
            prefixSum[i] = nums[i-1] * prefixSum[i-1]
            i += 1

        j = len(suffixSum) - 1
        numsPointer = len(nums)-1
        while j > 0:
            suffixSum[j-1] = nums[numsPointer] * suffixSum[j]
            numsPointer -= 1
            j -= 1
        
        for idx, item in enumerate(nums):
            nums[idx] = prefixSum[idx] * suffixSum[idx+1]

        return nums

    # Runtime: 356 ms, faster than 5.07% of Python online submissions for Product of Array Except Self.
    # Memory Usage: 20.9 MB, less than 47.18% of Python online submissions for Product of Array Except Self.
        

if __name__ == '__main__':
    nums = [-1, 1, 0 , -3, -3]
    sol = Solution().productExceptSelf(nums)
    print(sol)


