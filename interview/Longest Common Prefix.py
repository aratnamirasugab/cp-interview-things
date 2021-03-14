#Your code took 8 milliseconds — faster than 92.39% in Python
class Solution:
    def solve(self, words):
        if len(words) == 0:
            return ""

        if len(words) == 1:
            return words

        res = ""
        for i, j in zip(min(words), max(words)):
            if i != j:
                break;

            res += i

        return res



if __name__ == '__main__':
    s = ["bagu", "bagusari", "ba"]
    sol = Solution()
    print(sol.solve(s))

