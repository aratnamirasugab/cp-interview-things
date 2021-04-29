#Your code took 208 milliseconds — faster than 1.64% in Python
class Solution:
    def solve(self, s0, s1):
        if len(s0) != len(s1):
            return False
        if len(s0) == 0 or len(s1) == 0:
            return False
        
        dictone = {}
        dicttwo = {}

        for idx, item in enumerate(s0):
            if dictone.get(item) == None:
                dictone[item] = 1
            elif dictone.get(s0[idx]):
                val = dictone.get(item)
                dictone[item] = val + 1
            
            if dicttwo.get(s1[idx]) == None:
                dicttwo[s1[idx]] = 1
            elif dicttwo.get(s1[idx]):
                val = dicttwo.get(s1[idx])
                dicttwo[s1[idx]] = val + 1

        if dictone == dicttwo:
            return True
        else:
            return False

# faster than 1.xx % all code

class Solution:
    def solve(self, s0, s1):
        if len(s0) != len(s1) : return False
        dict = {}
        for i in s1:
            if dict.get(i) == None:
                dict[i] = 1
            else:
                dict[i] += 1

        for i in s0:
            if dict.get(i) == None: return False
            else:
                dict[i] -= 1
                if dict.get(i) == 0: dict.pop(i)

        return True

# faster than 30% all code

if __name__ == '__main__':
    s0 = 'silent'
    s1 = 'listen'
    sol = Solution()
    print(sol.solve(s0,s1))


# solution 2 -- faster than 94% python submission
# https://www.guru99.com/python-counter-collections-example.html
class Solution:
    def solve(self, s0, s1):
        return Counter(s0) == Counter(s1)