class Solution:
    def solve(self, nums):
        if len(nums) % 2 == 1:
            return False
        
        tempDict = {}
        for item in nums:
            if tempDict.get(item) == None:
                tempDict[item] = 1
            else:
                val = tempDict.get(item)
                val += 1
                tempDict[item] = val
        
        values = tempDict.values()
        for val in values:
            if val % 2 == 1:
                return False

        return True

Your code took 88 milliseconds — faster than 15.37% in Python


class Solution:
    def solve(self, nums):
        if len(nums) == 0: return False
        if len(nums) % 2 == 1:
            return False
        
        nums.sort()
        last_char = nums[0]
        count_same = 1
        for idx, item in enumerate(nums[1:]):
            if item == last_char:
                count_same += 1
            else:
                if count_same % 2 == 1:
                    return False
                else:
                    last_char = item
                    count_same = 1

        return True

Your code took 53 milliseconds — faster than 51.34% in Python

