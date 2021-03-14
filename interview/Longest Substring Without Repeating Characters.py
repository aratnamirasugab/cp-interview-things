class Solution():
    def lengthOfLongestSubstring(self, s):

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        if s[0] == ' ':
            return 1

        longestone = 0
        longesttwo = 0

        i = 0
        j = len(s)-1

        dictone = {}
        dicttwo = {}

        while i != len(s) and j > -1:
            "asjrgapa"
            if dictone.get(s[i]) == None:
                dictone[s[i]] = 1
            elif dictone.get(s[i]):
                if longestone < len(dictone):
                    longestone = len(dictone)
                    dictone.clear()
                    dictone[s[i]] = 1
            
            if dicttwo.get(s[j]) == None:
                dicttwo[s[j]] = 1
            elif dicttwo.get(s[j]):
                if longesttwo < len(dicttwo):
                    longesttwo = len(dicttwo)
                    dicttwo.clear()
                    dicttwo[s[j]] = 1
            i += 1
            j -= 1
        
        if longestone < longesttwo:
            longestone = longesttwo

        if len(dictone) < len(dicttwo):
            longestbetweendict = len(dictone)
        else:
            longestbetweendict = len(dicttwo)
        
        if longestone < longestbetweendict:
            longestone = longestbetweendict

        return longestone

if __name__ == '__main__':
    s = "asjrgapa"
    sol = Solution()
    ans = sol.lengthOfLongestSubstring(s)
    print(ans)
        