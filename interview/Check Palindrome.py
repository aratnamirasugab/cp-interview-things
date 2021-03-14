# Your code took 1 millisecond — faster than 99.97% in Python
class Solution:
    def solve(self, s):
        if len(s) == 0:
            return True
        
        if len(s) % 2 == 1:
            a = len(s) / 2 - 1
            b = len(s) / 2 + 1
            a = int(a)
            b = int(b)
            while a > -1 and b < len(s):
                if s[a] != s[b]:
                    return False
                a -= 1
                b += 1

        if len(s) % 2 == 0:
            a = len(s) / 2 - 1
            b = len(s) / 2
            a = int(a)
            b = int(b)
            while a > - 1 and b < len(s):
                if s[a] != s[b]:
                    return False
                a -= 1
                b += 1

        return True

if __name__ == '__main__':
    s = "evilolive"
    ini = Solution()
    print(ini.solve(s))
