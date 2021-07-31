class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        tempDict = {}
        diff = "1"
        for itemStr in strs:
            arrayHolder = [0] * 128
            for ch in itemStr:
                arrayHolder[ord(ch)] += 1

            value = ""
            for item in arrayHolder:
                value += str(item)
            
            if tempDict.get(value) == None:
                tempDict[value] = [itemStr]
            else:
                valueExist = tempDict.get(value)
                check = itemStr in valueExist
                if check is False:
                    tempDict[value+diff] = [itemStr]
                    diff = int(diff) + 1
                    diff = str(diff)
                else:
                    tempDict[value] += [itemStr]
            
        return tempDict.values()
    #unsolved


if __name__ == '__main__':
    strs = ["bdddddddddd","bbbbbbbbbbc"]
    sol = Solution().groupAnagrams(strs)
    print(sol)