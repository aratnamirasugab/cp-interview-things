class Solution():
    def isAnagram(self, s, t):
        t = sorted(t)
        s = sorted(s)

        return s == t

    # Time complexity O(n log n)
    # Runtime: 64 ms, faster than 13.11% of Python online submissions for Valid Anagram.
    # Memory Usage: 14.7 MB, less than 38.92% of Python online submissions for Valid Anagram.

    def isAnagram_2(self, s, t):

        tempDict = {}

        if len(s) != len(t): return False
        
        for x in s:
            if tempDict.get(x) == None:
                tempDict[x] = 1
            else:
                tempDict[x] += 1
        
        for x in t:
            if tempDict.get(x) != None:
                tempDict[x] -= 1

        maxVal = max(tempDict.values())
        
        if maxVal == 0:
            return True
        else:
            return False

        # Time Complexity O(n) Space is O(n)
        # Runtime: 56 ms, faster than 24.64% of Python online submissions for Valid Anagram.
        # Memory Usage: 14.2 MB, less than 57.81% of Python online submissions for Valid Anagram.



if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    sol = Solution().isAnagram_2(s, t)
    print(sol)
