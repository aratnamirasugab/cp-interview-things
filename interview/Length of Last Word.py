class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.rstrip(' ').split(' ')[-1])


if __name__ == '__main__':
    s = " a "
    sol = Solution().lengthOfLastWord(s)
    print(sol)
        