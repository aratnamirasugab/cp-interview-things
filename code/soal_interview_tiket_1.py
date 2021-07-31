# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

class Solution:

    def solution(self, A):
        checkFist = self.checkValid(A)

        if checkFist == True:
            return 0

        totalTree = len(A)
        totalWay = 0
        for i in range(totalTree):
            listTemp = list(A)
            listTemp.pop(i)
            check = self.checkValid(listTemp)
            if check == True:
                totalWay += 1

        if totalWay == 0:
            return -1

        return totalWay
        
    def checkValid(self, A):
        result = True
        last = False

        if A[0] < A[1]:
            last = True
        elif A[0] > A[1]:
            last = False
        else:
            return False

        idx = 0
        maxIdx = len(A)-1
        while idx <= maxIdx:
            if A[idx-1] > A[idx] and last == True:
                last = False
            elif A[idx-1] < A[idx] and last == False:    
                last = True
            else:
                result = False
            idx += 1

        return result
        

if __name__ == '__main__':
    A = [1,3,1,2]
    sol = Solution().solution(A)
    print(sol)
    
        