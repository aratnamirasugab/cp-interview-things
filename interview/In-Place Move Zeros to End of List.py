class Solution:
    def solve(self, nums):
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return nums
        else:
            for idx, item in enumerate(nums):
                if item == 0:
                    for idxInner, itemInner in enumerate(nums[idx+1:]):
                        print(idxInner)        
                    break
        # return nums

if __name__ == '__main__':
    arr = [0, 1, 0, 2, 3]
    sol = Solution()
    print(sol.solve(arr))