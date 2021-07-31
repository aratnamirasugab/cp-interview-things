# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

class Solution:
    def solution(self, N):
        # write your code in Python 3.6
        negative = False
        if N < 0 :
            negative = True

            N = N * -1
    
        digit_string = str(N)
        digit_int = map(int, digit_string)
        listToCheck = list(digit_int)

        if negative == True:
            listToCheck.insert(0, 5)
        else:
            indexLowest = 0
            for idx, item in enumerate(listToCheck):

                if item < 5:
                    indexLowest = idx
                    pass

            listToCheck.insert(indexLowest, 5)

        
        strings = [str(x) for x in listToCheck]
        a_string = "".join(strings)
        result = int(a_string)     

        if negative == True:
            return result * -1
        return result  


if __name__ == '__main__':
    A = 0
    sol = Solution().solution(A)
    print(sol)
    