class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""
        for i in range(len(s)):
            odd = self.helper(s, i, i)
            even = self.helper(s, i, i+1)
            res = max(odd, even, res, key=len)
        return res

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        
        return s[l+1:r]

if __name__ == '__main__':
    s = "abbad"
    sol = Solution().longestPalindrome(s) 
    print(sol)

# Runtime: 960 ms, faster than 75.58% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 14.2 MB, less than 93.87% of Python3 online submissions for Longest Palindromic Substring.
