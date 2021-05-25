class Solution:
    def runningSum(self, nums):
        total = 0
        arrResult = []

        for item in nums:
            total += item
            arrResult.append(total)

        return arrResult

if __name__ == '__main__':
    arr = [3,1,2,10,1]
    sol = Solution().runningSum(arr)
    print(sol)

Runtime: 28 ms, faster than 57.41% of Python online submissions for Running Sum of 1d Array.
Memory Usage: 13.5 MB, less than 68.95% of Python online submissions for Running Sum of 1d Array.
