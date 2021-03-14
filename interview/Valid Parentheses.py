class Solution(object):
    def isValid(self, s):
        
        if len(s) == 0 or len(s) == 1: return False

        dictTemp = {'(':')', '{':'}', '[':']'}
        invalidChar = [')', '}', ']']
        stack = []
        stack.append(s[0])
        res = False

        for item in s[1:]:
            if len(stack) != 0:
                lastInStack = stack[-1]
                if lastInStack not in invalidChar:
                    pairStack = dictTemp[lastInStack]
                    if pairStack == item : stack.pop()
                    else: stack.append(item)
            else: stack.append(item)

        if len(stack) == 0 : res = True
        return res 
        
if __name__ == '__main__':
    sol = Solution()
    s = "(){}[]"
    ans = sol.isValid(s)
    print(ans)

Runtime: 16 ms, faster than 88.41% of Python online submissions for Valid Parentheses.
Memory Usage: 13.5 MB, less than 65.46% of Python online submissions for Valid Parentheses.
