class Solution:
    def solve(self, s):

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return "1" + s[0]

        length = 1
        i = 1
        j = len(s)
        
        ans = ""
        ch = s[0]
        while i < j:
            if ch == s[i]:
                length += 1
            else:
                strLen = str(length)
                ans += strLen + ch
                ch = s[i]
                length = 1

            i += 1

        if length != 0:
            strLen = str(length)
            ans += strLen + ch
        return ans

Your code took 3 milliseconds — faster than 89.78% in Python

