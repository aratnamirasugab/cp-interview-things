class Solution(object):
    def findDisappearedNumbers(self, nums):
        setNums = set(nums)
        ansArr = []
        i = 1
        j = len(nums) + 1
        while i < j:
            if i not in setNums:
                ansArr.append(i)    
            i += 1
        return ansArr
        

if __name__ == '__main__':
    arr = [1,1]
    sol = Solution()
    ans = sol.findDisappearedNumbers(arr)
    print(ans)

Runtime: 324 ms, faster than 94.74% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 23.9 MB, less than 33.97% of Python3 online submissions for Find All Numbers Disappeared in an Array.