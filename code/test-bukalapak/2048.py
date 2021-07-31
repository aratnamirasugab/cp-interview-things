import random
# from msvcrt import getch

class Solution:
    def solve(self, T, N):
        if N < 0 or N is 0:
            return "Error"

        arr = [ [0] * N for i in range(N)]
        print(arr)
        a = random.randint(0, N*N - 1)
        b = random.randint(0, N*N - 1)

        arr = self.generateRandomValueForArray(arr, N, a)
        arr = self.generateRandomValueForArray(arr, N, b)

        print(arr)
        
        foundValueT = self.findTargetInArray(T, arr, N)

        while foundValueT is False:
            command = input()
            while command[0] is 'a':
                for idx, item in enumerate(arr):
                    arr = self.shiftAndSumValueFromOneDimentionalArray(arr, idx, N)
            
            # while command[0] is 'd':
            #     for idx, item in enumerate(arr):
            #         arr = self.shiftAndSumValueFromOneDimentionalArray(arr[idx], '+')
            
            
            
            foundValueT = self.findTargetInArray(T, arr, N) 
        return arr

    
    def shiftAndSumValueFromOneDimentionalArray(self, arr, idx, N):

        pointerX = N - 1
        pointerY = pointerX - 1
        # counterCombine = 0
        while pointerY > -1:
            if arr[idx][pointerX] == arr[idx][pointerY]:
                arr[idx][pointerY] += arr[idx][pointerX]
                arr[idx][pointerX] = 0
                pointerX -= 1
                pointerY -= 1
                # counterCombine += 1
            elif arr[idx][pointerY] == 0 and arr[idx][pointerX] != 0:
                arr[idx][pointerY] = arr[idx][pointerX]
                arr[idx][pointerX] = 0
                pointerX -= 1
                pointerY -= 1
        
        return arr

    def findTargetInArray(self, T, arr, N):
        i = 0
        j = 0

        while i < N:
            
            j = 0
            while j < N:
                if arr[i][j] == T:
                   return True
                j += 1
            i += 1

        return False
        
    def generateRandomValueForArray(self, arr, N, targetIdx):
        i = 0
        j = 0
        idxRandom = 0

        while i < N:
            
            j = 0
            while j < N:
                if idxRandom == targetIdx:
                    arr[i][j] = 2

                idxRandom += 1
                j += 1
            i += 1

        return arr


if __name__ == '__main__':
    T = 2
    N = 4
    sol = Solution().solve(T, N)
    print(sol)
