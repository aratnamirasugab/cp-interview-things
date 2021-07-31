class Solution(object):
    # brute force
    def climbStars(self, num):
        """
        :type n: int
        :rtype: int
        """
        return self.climb_Star(0, num)


    def climb_Star(self, idx, num):
        if idx == num:
            return 1
        elif idx > num:
            return 0
        else:
            return self.climb_Star(idx+1, num) + self.climb_Star(idx+2, num)

    #TLE
    ###

    # Dynamic Programming
    def climbStairs_dp(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1

        dp = [None] * (n+1) 
        dp[0] = 1
        dp[1] = 1
        dp[2] = 1
        dp[3] = 2

        i = 4
        while i <= n:
            dp[i] = dp[i-1] + dp[i-2]
            i += 1

        return dp[n]
    # Runtime: 12 ms, faster than 94.19% of Python online submissions for Climbing Stairs.
    # Memory Usage: 13.2 MB, less than 98.39% of Python online submissions for Climbing Stairs.
        
if __name__ == '__main__':
    num = 6
    sol = Solution().climbStairs_dp(num)
    print(sol)
