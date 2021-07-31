class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        if len(intervals) == 1:
            return intervals

        intervals = sorted(intervals)
        
        idx = 1
        while idx < len(intervals):
            if intervals[idx-1][0] > intervals[idx][0] or intervals[idx-1][1] >= intervals[idx][0] or intervals[idx-1][1] >= intervals[idx][1]:
                tempList = []
                for x in intervals[idx-1]:
                    tempList.append(x)

                for x in intervals[idx]:
                    tempList.append(x)

                minVal = min(tempList)
                maxVal = max(tempList)
                intervals.remove(intervals[idx])
                
                intervals[idx-1][0] = minVal
                intervals[idx-1][1] = maxVal
            else:
                idx += 1

        return intervals

        # Runtime: 108 ms, faster than 6.70% of Python online submissions for Merge Intervals.
        # Memory Usage: 15.8 MB, less than 54.46% of Python online submissions for Merge Intervals.

if __name__ == '__main__':
    intervals = [[1,4],[0,0]]
    sol = Solution().merge(intervals)
    print(sol)
