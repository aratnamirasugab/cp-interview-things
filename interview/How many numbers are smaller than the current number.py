class Solution:
    def solve(self, nums):
        result = []
        temp = sorted(nums)
        mapping = {}

        for x in range(len(temp)):
            if temp[x] not in mapping:
                mapping[temp[x]] = x

        for x in nums:
            result.append(mapping[x]) 
    
        return result

if __name__ == '__main__':
    nums = [8,1,2,2,3]
    sol = Solution().solve(nums)
    print(sol)

https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
Runtime: 44 ms, faster than 99.26% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
Memory Usage: 14.3 MB, less than 75.91% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.