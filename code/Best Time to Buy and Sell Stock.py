class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        highestProfit = 0
        arrPrices = [[0] * len(prices) for i in range(len(prices))]
        
        pointerA = 0
        while pointerA < len(prices):
            pointerB = pointerA
            while pointerB < len(prices):
                calculate = prices[pointerB] - prices[pointerA]
                arrPrices[pointerA][pointerB] = prices[pointerB] - prices[pointerA]
                highestProfit = max(highestProfit, calculate)
                pointerB += 1
            pointerA += 1
            
        return highestProfit
    # TLE -> O(n^2) 0(n+n) 
    # 198/211

    def maxProfit_2(self, prices):
        minprice = float('inf')
        maxprice = 0

        for idx, item in enumerate(prices):
            if item < minprice:
                minprice = item
            elif item - minprice > maxprice:
                maxprice = item-minprice
        return maxprice

    # Runtime: 1124 ms, faster than 6.42% of Python online submissions for Best Time to Buy and Sell Stock.
    # Memory Usage: 22.8 MB, less than 14.95% of Python online submissions for Best Time to Buy and Sell Stock.


            
            
if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    sol = Solution().maxProfit_2(prices)
    print(sol)
