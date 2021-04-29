class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        import math

        i, j, res = 0,0, []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        res += nums1[i::] + nums2[j::]
        if len(res) % 2 == 0:
            idxFront = int(len(res)/2)
            idxBack = idxFront - 1
            idx = (res[idxFront] + res[idxBack]) / 2
            print(idx)
            return float(idx)
        else:
            idx = len(res)/2
            return res[int(math.floor(idx))]
        
if __name__ == '__main__':
    nums1 = [1,2]
    nums2 = [3,4]
    sol = Solution().findMedianSortedArrays(nums1, nums2)
    print(sol)