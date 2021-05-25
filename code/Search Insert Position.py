class Solution(object):
    def searchInsert(self, nums, target):

        indexToAdd = 0
        try:
            found = nums.index(target)
            if found != None:
                return found
        except ValueError:
            for idx, item in enumerate(nums):
                if target < item: 
                    indexToAdd = idx
                    return indexToAdd

            return len(nums)

if __name__ == '__main__':
    arr = [1]
    sol = Solution().searchInsert(arr, 0)
    print(sol)


Runtime: 28 ms, faster than 96.47% of Python online submissions for Search Insert Position.
Memory Usage: 14.3 MB, less than 28.94% of Python online submissions for Search Insert Position.
