#Your code took 8 milliseconds — faster than 92.39% in Python
class Solution:
    def solve(self, words):
        l = list(zip(*words))
        print(l)
        prefix = ""
        for x in l:
            res = set(x)
            if len(res) == 1:
                prefix += x[0]
            else:
                break

        return prefix
       


if __name__ == '__main__':
    s = ["flower","flow","flight"]
    sol = Solution().solve(s)
    print(sol)

