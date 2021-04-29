class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        # ans = 0
        # for x in items:
        #     if ruleKey == "type":
        #         if x[0] == ruleValue:
        #             ans += 1
        #     if ruleKey == "color":
        #         if x[1] == ruleValue:
        #             ans += 1
        #     if ruleKey == "name":
        #         if x[2] == ruleValue:
        #             ans += 1
        # return ans

        # 2nd solution using map
        dict = {'type': 0, 'color': 1, 'name': 2}
        for x in items:
            return sum(1 for x in items if x[dict[ruleKey]] == ruleValue)


if __name__ == '__main__':
    items = [["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"]]
    rk = "name"
    rv = "qqqq"
    sol = Solution().countMatches(items, rk, rv)
    print(sol)

# Runtime: 248 ms, faster than 43.24% of Python3 online submissions for Count Items Matching a Rule.
# Memory Usage: 20.6 MB, less than 21.24% of Python3 online submissions for Count Items Matching a Rule.

Runtime: 236 ms, faster than 85.23% of Python3 online submissions for Count Items Matching a Rule.
Memory Usage: 20.5 MB, less than 64.88% of Python3 online submissions for Count Items Matching a Rule.
