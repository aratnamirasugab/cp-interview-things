class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        dp = [None] * (n+2)
        dp[0] = 0
        dp[1] = 1
        
        if n < 2:
            return dp[n]
        else:
            i = 2
            while i <= n:
                dp[i] = dp[i-1] + dp[i-2]
                i += 1
        return dp[n]

if __name__ == '__main__':
    n = 4
    sol = Solution().fib(n)
    print(sol)

# Runtime: 16 ms, faster than 78.78% of Python online submissions for Fibonacci Number.
# Memory Usage: 13.5 MB, less than 31.18% of Python online submissions for Fibonacci Number.