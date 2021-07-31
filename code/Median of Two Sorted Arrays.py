class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1 = nums1 + nums2
        nums1 = sorted(nums1)

        if len(nums1) % 2 == 0:
            return (float(nums1[len(nums1)/2]) + float(nums1[len(nums1)/2-1])) / 2
        else:
            return float(nums1[len(nums1)/2])
        
if __name__ == '__main__':
    nums1 = []
    nums2 = [1]
    sol = Solution().findMedianSortedArrays(nums1, nums2)
    print(sol)

# Runtime: 76 ms, faster than 58.66% of Python online submissions for Median of Two Sorted Arrays.
# Memory Usage: 13.6 MB, less than 47.85% of Python online submissions for Median of Two Sorted Arrays.