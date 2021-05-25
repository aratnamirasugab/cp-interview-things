# class Solution:
#     def rotate(self, nums, k):
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         holder = []
#         i = 0 
#         while i < k:
#             holder.append(nums.pop())
#             nums.insert(0, holder.pop())
#             i += 1
#         return nums

# Runtime: 3148 ms, faster than 5.08% of Python3 online submissions for Rotate Array.
# Memory Usage: 25.6 MB, less than 21.71% of Python3 online submissions for Rotate Array

# class Solution:
#     def rotate(self, nums, k):
#         a = [0] * len(nums)
#         for i in range(len(nums)):
#             a[(i+k)%len(nums)] = nums[i] #recycle

#         for i in range(len(nums)):
#             nums[i] = a[i]

# Runtime: 240 ms, faster than 11.29% of Python3 online submissions for Rotate Array.
# Memory Usage: 25.6 MB, less than 30.08% of Python3 online submissions for Rotate Array.


if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7] 
    k = 3
    sol = Solution().rotate(nums, k)  
    print(nums)