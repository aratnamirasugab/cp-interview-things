# # class Solution:
# #     def lengthOfLongestSubstring(self, s: str) -> int:

# #         forward = self.check(s)
# #         backward = self.check(s[::-1])

# #         res = max(forward, backward)

# #         return res
       

# #     def check(self, s:str) -> int:
# #         l = [0] * 128
# #         res = ""
# #         strTemp = ""
# #         lastInput = ""
# #         for x in s:

# #             if l[ord(x)] == 0:
# #                 l[ord(x)] += 1
# #                 strTemp += x
                
# #             else:
# #                 l = [0] * 128
# #                 l[ord(x)] += 1
# #                 strTemp = x
# #                 if lastInput[0] != x: 
# #                     l[ord(lastInput[0])] += 1
# #                     strTemp += lastInput[0]
                    
# #             lastInput = ""
# #             lastInput += x

# #             res = max(res, strTemp, key=len)

# #         return len(res)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
            
        tempdict = {}
        max_length = 0

        a_pointer = 0
        b_pointer = 0
        
        while b_pointer < len(s):
            if tempdict.get(s[b_pointer]) == None:
                tempdict[s[b_pointer]] = 1
                b_pointer += 1
                max_length = max(max_length, len(tempdict))
            else:
                tempdict.pop(s[a_pointer])
                a_pointer += 1
        return max_length

if __name__ == '__main__':
    s = "anviaj"
    sol = Solution().lengthOfLongestSubstring(s)
    print(sol)
    
# Runtime: 72 ms, faster than 44.37% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.3 MB, less than 79.48% of Python3 online submissions for Longest Substring Without Repeating Characters.