class Solution:
    def shuffle(self, nums, n):
        if n is 1 : return nums
        
        x = 0
        y = n
        ans = []
        while x < n and y < len(nums):
            ans.append(nums[x])
            ans.append(nums[y])
            x += 1
            y += 1

        return ans

if __name__ == '__main__':
    nums = [1,1,2,2]
    n = 2
    sol = Solution().shuffle(nums, n)
    print(sol)
    
https://leetcode.com/problems/shuffle-the-array
Runtime: 52 ms, faster than 96.11% of Python3 online submissions for Shuffle the Array.
Memory Usage: 14.4 MB, less than 78.00% of Python3 online submissions for Shuffle the Array.
