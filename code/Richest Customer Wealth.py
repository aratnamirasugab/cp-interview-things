class Solution:
    def maximumWealth(self, nums):
        if len(nums) == 0 : return 0

        maxval = 0
        for x in nums:
            sumVal = sum(x)
            if maxval < sumVal: maxval = sumVal

        return maxval

if __name__ == '__main__':
    accounts = [[2,8,7],[7,1,3],[1,9,5]]
    sol = Solution().maximumWealth(accounts)
    print(sol)

https://leetcode.com/problems/richest-customer-wealth/
Runtime: 52 ms, faster than 74.80% of Python3 online submissions for Richest Customer Wealth.
Memory Usage: 14.1 MB, less than 83.92% of Python3 online submissions for Richest Customer Wealth.