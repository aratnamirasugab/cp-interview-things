class Solution:
    def numIdenticalPairs(self, nums):
        repeat = {}
        ans = 0

        for x in nums:
            if x in repeat:
                ans += repeat[x]
                repeat[x] += 1
            else:
                repeat[x] = 1
        return ans

if __name__ == '__main__':
    nums = [1,2,3]
    sol = Solution().numIdenticalPairs(nums)
    print(sol)

https://leetcode.com/problems/number-of-good-pairs/
Runtime: 32 ms, faster than 76.42% of Python3 online submissions for Number of Good Pairs.
Memory Usage: 14.2 MB, less than 44.57% of Python3 online submissions for Number of Good Pairs.
