class Solution:
    def solve(self, n):
        a = list(map(int, str(n)))
        res = 0
        for x in a:
            res += pow(x, len(a))

        return n == res
    


if __name__ == '__main__':
    n = 153
    sol = Solution().solve(n)
    print(sol)