class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        if len(candies) == 0 : return []
        
        maxVal = max(candies)
        ans = []
        for x in candies:
            sumVal = x + extraCandies
            
            if sumVal >= maxVal:
                ans.append(True)
            else:
                ans.append(False)
                
        return ans

https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
Runtime: 36 ms, faster than 79.44% of Python3 online submissions for Kids With the Greatest Number of Candies.
Memory Usage: 14.3 MB, less than 54.98% of Python3 online submissions for Kids With the Greatest Number of Candies.
