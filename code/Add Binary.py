class Solution(object):
    def addBinary(self, a, b):

        carry = 0
        result = ""
        
        a = list(a)
        b = list(b)

        while a or b or carry:
            if a : carry += int(a.pop())
            if b : carry += int(b.pop())
            result += str(carry%2)
            carry //= 2
        
        return result[::-1]


if __name__ == '__main__':
    a = "11"
    b = "1"
    sol = Solution().addBinary(a, b)
    print(sol)

Runtime: 28 ms, faster than 38.72% of Python online submissions for Add Binary.
Memory Usage: 13.5 MB, less than 80.61% of Python online submissions for Add Binary.
