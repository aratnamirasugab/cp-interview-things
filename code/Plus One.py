class Solution(object):
    def plusOne(self, digits):
        tempInteger = int("".join(map(str, digits)))
        tempInteger += 1
        
        tempInteger = list(map(int, str(tempInteger)))
        return tempInteger
        
if __name__ == '__main__':
    arr = [0]
    sol = Solution().plusOne(arr)
    print(sol)

Runtime: 16 ms, faster than 91.51% of Python online submissions for Plus One.
Memory Usage: 13.1 MB, less than 99.29% of Python online submissions for Plus One.
