class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = ""
        pointerA = 0
        pointerB = 0
        
        while pointerA < len(word1) and pointerB < len(word2):
            res += word1[pointerA]
            res += word2[pointerB]
            pointerA += 1
            pointerB += 1
            
        while pointerA < len(word1):
            res += word1[pointerA]
            pointerA += 1
            
        while pointerB < len(word2):
            res += word2[pointerB]
            pointerB += 1
            
        return res
        
# Runtime: 40 ms, faster than 22.58% of Python online submissions for Merge Strings Alternately.
# Memory Usage: 13.6 MB, less than 7.80% of Python online submissions for Merge Strings Alternately.
