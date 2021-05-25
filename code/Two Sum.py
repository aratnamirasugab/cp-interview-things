class Solution(object):
    def twoSum(self, nums, target):
        dictTemp = {}
        
        for idx, item in enumerate(nums):
            dictTemp[item] = idx
                
        for idx, item in enumerate(nums):
            pair = target-item
            if dictTemp.get(pair) != None and idx != dictTemp.get(pair):
                return [idx, dictTemp[pair]]


if __name__ == '__main__':
    arr = [3,3]
    target = 6
    sol = Solution().twoSum(arr, target)
    print(sol)

Runtime: 32 ms, faster than 76.91% of Python online submissions for Two Sum.
Memory Usage: 13.5 MB, less than 52.31% of Python online submissions for Two Sum.

    