class Solution(object):
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers) - 1
        
        while i < j :
            if numbers[i] + numbers[j] > target: j -= 1
            elif numbers[i] + numbers[j] < target: i += 1
            else:
                return [i+1, j+1]


Runtime: 44 ms, faster than 84.33% of Python online submissions for Two Sum II - Input array is sorted.
Memory Usage: 13.7 MB, less than 49.40% of Python online submissions for Two Sum II - Input array is sorted.
