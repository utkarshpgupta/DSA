# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        n = len(prices)
        profit = 0
        while r < len(prices):
            if prices[l]<prices[r]:
                profit = max(profit, prices[r]-prices[l])
            else:
                l = r
            r += 1
        
        return profit 