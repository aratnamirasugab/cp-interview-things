class Solution_one:
    def threeSum(self, nums):
        res = {}
        nums.sort()

        for x in range(len(nums)-2):
            left = x + 1
            right = len(nums) - 1
            while left < right:
                calculate = nums[x] + nums[left] + nums[right]
                if calculate < 0:
                    left += 1
                elif calculate > 0:
                    right -= 1
                else:
                    resTemp = [nums[x], nums[left],nums[right]]
                    strtemp = "".join(map(str, resTemp))
                    if res.get(strtemp) == None:
                        res[strtemp] = resTemp
                    left += 1

        real = list(res.values())
        return real

# Runtime: 5740 ms, faster than 9.18% of Python3 online submissions for 3Sum.
# Memory Usage: 17.4 MB, less than 73.94% of Python3 online submissions for 3Sum.


if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    sol = Solution_one.threeSum(Solution_one, nums)
    print(sol)
