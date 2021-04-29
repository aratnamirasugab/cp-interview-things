class Solution:
    def solve(self, s0, s1):
        if len(s0) == 0 or len(s1) == 0:
            return 0

        s0 = s0.lower()
        s1 = s1.lower()

        splitS0 = s0.split(' ')
        splitS1 = s1.split(' ')
        dictS0 = {}
        splitS1 = list(set(splitS1))

        for x in splitS0 : 
            if dictS0.get(x) == None:
                dictS0[x] = 1

        value = 0
        
        for y in splitS1:
            if dictS0.get(y):
                value += 1

        return value
            

if __name__ == '__main__':
    s0 = "hello world hello oyster"
    s1 = "world is your oyster"
    sol = Solution().solve(s0, s1)
    print(sol)
    