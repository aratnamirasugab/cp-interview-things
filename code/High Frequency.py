class Solution:
    def solve(self, nums):
        if len(nums) == 0: return 0

        tempDict = {}
        for item in nums:
            if tempDict.get(item) == None:
                tempDict[item] = 1
            else:
                val = tempDict.get(item)
                val += 1
                tempDict[item] = val
            
        return max(tempDict.values())


if __name__ == '__main__':
    sol = Solution()
    arr =  [5, 5, 5, 5, 5, 5, 5]
    ans = sol.solve(arr)
    print(ans)

Your code took 9 milliseconds — faster than 50.21% in Python