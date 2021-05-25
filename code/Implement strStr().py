class Solution(object):
    def strStr(self, haystack, needle):
        if len(needle) == 0: return 0

        needleIndex = 0
        same = 0
        indexFound = []
        for idx, item in enumerate(haystack):
            if len(needle) != needleIndex:
                if item == needle[needleIndex]:
                    indexFound.append(idx)
                    same += 1
                    needleIndex += 1
            else:
                if same == len(needle): return indexFound[0]
                if len(indexFound) != 0: indexFound.clear()
                same = 0
                needleIndex += 1

        if same == len(needle): return indexFound[0]
        return -1
        

if __name__ == '__main__':
    sol = Solution()
    haystack = "mississippi"
    needle = "issip"
    print(sol.strStr(haystack, needle))
