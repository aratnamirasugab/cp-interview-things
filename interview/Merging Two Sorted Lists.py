class Solution:
    def solve(self, a, b):
        i, j, res = 0,0,[]

        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1

        return res + a[i::] + b[j::]
             
        

if __name__ == '__main__':
    a = [5, 10, 15]
    b = [3, 8, 9]
    sol = Solution().solve(a, b)
    print(sol)