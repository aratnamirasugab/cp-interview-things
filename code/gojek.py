# class Solution(object):
#     def solve(self, x, a, b, i, j):
#         k = j
#         ct = 0
#         while k > i-1:
#             if x[k] <= b and not x[k] <= a:
#                 ct += 1
#             k -= 1
#         return ct

# if __name__ == '__main__':
#     x = [11, 10, 10, 5, 10, 15, 20, 10, 7, 11]
#     sol = Solution().solve(x, 6,7,8,8)
#     print(sol)


class Solution(object):
    def g(self, str):
        i = 0
        new_str = ""
        while i < len(str) - 1:
            new_str += str[i+1]
            i += 1
        return new_str

    def f(self, str):
        if len(str) == 0:
            return ""
        elif len(str) == 1:
            return str
        else:
            return self.f(self.g(str)) + str[0]
        
    def h(self, n, str):
        while n != 1:
            if n % 2 == 0:
                n = n/2
            else:
                n = 3*n + 1

            str = self.f(str)
        return str

    def pow(self, x, y):
        if y == 0:
            return 1
        else:
            return x * self.pow(x, y-1)
    
if __name__ == '__main__':
    sol = Solution().h(pow(2, 1000000000000000), "fruits")
    print(sol)