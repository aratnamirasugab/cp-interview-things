
# You are given a list of integers nums. Return the number of pairs i < j such that nums[i] = nums[j].

# Constraints

# 0 ≤ n ≤ 100,000 where n is the length of nums
# Example 1
# Input
# nums = [3, 2, 3, 2, 2]
# Output
# 4

class Solution:
    def solve(self, nums):
        dict = {}
        ans = 0
        for item in nums:
            if dict.get(item) == None:
                dict[item] = 1
            else:
                ans += dict.get(item)
                val = dict.get(item)
                val += 1
                dict[item] = val
        
        return ans

# binarysearch.com
# Your code took 56 milliseconds — faster than 50.00% in Python