# Your code took 1 millisecond — faster than 99.96% in Python

class Solution:
    def solve(self, n):
        if n is 1:
            return 1

        tempList = []
        while n != 1:
            if n % 2 == 0:
                n = n / 2
                tempList.append(n)
            else:
                n = 3 * n + 1
                tempList.append(n)
        tempList.append(1)
        return len(tempList)
    


if __name__ == '__main__':
    temp = Solution()
    print(temp.solve(11))