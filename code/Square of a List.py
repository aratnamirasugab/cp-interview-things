class Solution:
    def solve(self, nums):

        for idx in range(len(nums)):
            nums[idx] *= nums[idx]
        
        return sorted(nums)


if __name__ == '__main__':
    nums = [-9, -2, 0, 2, 3]
    sol = Solution().solve(nums)
    print(sol)
