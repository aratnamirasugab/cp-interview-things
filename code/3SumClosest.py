class Solution(object):
    def threeSumClosest(self, nums, target):
        
        nums.sort()
        closest = float('inf')
        for x in range(len(nums)-2):
            pointer_a = x + 1
            pointer_b = len(nums) - 1

            while pointer_a != pointer_b:
                calculate = nums[x] + nums[pointer_a] + nums[pointer_b]
                if calculate < target:
                    pointer_a += 1
                   
                else:
                    pointer_b -= 1
                
                calculateClosest = abs(calculate - target)
                if calculateClosest < closest and calculateClosest is not target:
                    closest = abs(calculate - target)
        
        if closest == float('inf'):
            closest = 0
        return closest

if __name__ == '__main__':
    nums = [0,0,0]
    target = 1
    sol = Solution().threeSumClosest(nums, target)
    print(sol)