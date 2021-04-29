class Solution:
    def defangIPaddr(self, address: str) -> str:

        splitDot = address.split('.')
        res = ""
        for x in splitDot:
            res += x + "[.]"

        return res[0:len(res)-3]
        


if __name__ == '__main__':
    address = "255.100.50.0"
    sol = Solution().defangIPaddr(address)
    print(sol)