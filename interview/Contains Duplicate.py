class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return False
        
        dictTemp = {}
        for item in nums:
            if dictTemp.get(item) == None:
                dictTemp[item] = 1
            else:
                val = dictTemp.get(item)
                val += 1
                dictTemp[item] = val
        
        maxValue = max(dictTemp.values())
        if maxValue == 1:return False
        return True
        

if __name__ == '__main__':
    sol = Solution()
    nums = [1,1,1,3,3,4,3,2,4,2]
    ans = sol.containsDuplicate(nums)
    print(ans)

Runtime: 104 ms, faster than 44.27% of Python online submissions for Contains Duplicate.
Memory Usage: 19.3 MB, less than 55.98% of Python online submissions for Contains Duplicate.
