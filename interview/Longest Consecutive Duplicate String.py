class Solution:
    def solve(self, s):
        if len(s) == 0:
            return 0

        lastChar = s[0]
        maxLength = 1
        lenSame = 1
        for idx in range(1, len(s)):
            if s[idx] == lastChar:
                lenSame += 1
            else:
                lastChar = s[idx]
                if lenSame > maxLength:
                    maxLength = lenSame
                lenSame = 1

        return maxLength if maxLength > lenSame else lenSame
    

if __name__ == '__main__':
    s = 'bbbbaaaaa'
    sol = Solution().solve(s)
    print(sol)