class Solution:
    def romanToInt(self, s):

        tempMap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        if len(s) == 1: return tempMap[s[0]]

        lastchar = s[len(s)-1]
        result = tempMap[s[len(s)-1]]

        i = len(s)-2
        while i > -1 :
            if tempMap[s[i]] < tempMap[lastchar]:
                result -= tempMap[s[i]]
            else:
                result += tempMap[s[i]]
                
            lastchar = s[i]
            i -= 1

        return result

if __name__ == '__main__':
    s = "IX"
    sol = Solution().romanToInt(s)
    print(sol)

# Runtime: 28 ms, faster than 94.18% of Python online submissions for Roman to Integer.
# Memory Usage: 13.5 MB, less than 57.85% of Python online submissions for Roman to Integer.