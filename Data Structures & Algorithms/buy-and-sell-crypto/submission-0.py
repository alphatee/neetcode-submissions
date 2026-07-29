class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, max_profit = 1000, 0


        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            if prices[i] - buy > max_profit:
                max_profit = prices[i] - buy


        return max_profit if max_profit > 0 else 0