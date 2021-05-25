class Solution:
    def firstUniqChar(self, s: str) -> int:
        tempMap = {}
        for x in s:
            if tempMap.get(x) == None:
                tempMap[x] = 1
            else:
                tempMap[x] += 1
        
        for idx, item in enumerate(s):
            if tempMap.get(item) == 1:
                return idx
        return -1

if __name__== '__main__':
    s = "aabb"
    sol = Solution().firstUniqChar(s)
    print(sol)