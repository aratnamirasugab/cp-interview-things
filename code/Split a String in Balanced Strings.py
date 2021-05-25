class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        if s[0] == 'L':
            s[::-1]
        
        left, right = [],[]
        
        i = 0
        while i < len(s):
            if len(left) == len(right) and len(left) != 0:
                res += 1
                left.clear()
                right.clear()
                
            else:
                if s[i] == 'L':left.append('L')
                else: right.append('R')

                if len(left) == len(right) and len(left) != 0:
                    res += 1
                    left.clear()
                    right.clear()
            
            i += 1
        
        return res

if __name__ == '__main__' :
    s = "LLLLRRRR"
    sol = Solution().balancedStringSplit(s)
    print(sol)
