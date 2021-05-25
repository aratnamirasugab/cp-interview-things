class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        # each vowels must appear at least once
        res = 0
        listVowels = ['a', 'e', 'i', 'o', 'u']
        idxVow = 0
        idxIterate = 0
        maxTemp = 0

        while idxIterate < len(word):
            # if vowels is at 'u', check, if found else than u, if yes, compare maxTemp, res
            if listVowels[idxVow] == 'u':
                res = max(res, maxTemp)

            # check if current word is lower than current index vowel value, if yes then break
            if listVowels.index(word[idxIterate]) < idxVow : 
            # if found'a' reset res to 1 else 0, reset vowels index to 0
                if word[idxIterate] == 'a':
                    maxTemp = 1
                else:
                    maxTemp = 0
                idxVow = 0
            
            # if same, keep iterating res + 1
            elif listVowels.index(word[idxIterate]) == idxVow:
                maxTemp += 1
            
            # if bigger, check if difference between vowels index
            # if 1 then iterate, res +1, vowels array +1
            # if more than 1 diff in vowels array, break, if found 'a' then reset res to 1, if not reset to 0 and reset index vowels to 0
            elif (listVowels.index(word[idxIterate]) - idxVow) == 1:
                maxTemp += 1
                idxVow += 1
            else:
                if word[idxIterate] == 'a':
                    maxTemp = 1
                else:
                    maxTemp = 0
                idxVow = 0
            
            idxIterate += 1
        
        if listVowels[idxVow] == 'u':
            res = max(res, maxTemp)
            return res
        else:
            return 

        return res
        

if __name__ == '__main__':
    word = "auoeioueiaaioeuieuoaieuaoeuoaiaoueioiaeuiuaeouaoie"
    sol = Solution().longestBeautifulSubstring(word)
    print(sol)
