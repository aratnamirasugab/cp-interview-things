class Solution:
    def solve(self, nums):
        dict = {}
        for x in nums:
            if not dict.get(x):
                dict[x] = 1

        return len(dict)



if __name__=='__main__':
    nums = [2, 2, 2, 3, 4, 6, 6]
    answer = Solution()
    # answer.solve(nums)
    print(answer.solve(nums))

# Unique Integers in Sorted List
#Your code took 43 milliseconds — faster than 20.60% in Python
