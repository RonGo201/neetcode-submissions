class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_index = 0

        for i in range(len(prices)):
            if prices[i] < prices[buy_index]:
                buy_index = i
            else:
                profit = prices[i] - prices[buy_index]
                if profit > max_profit:
                    max_profit = profit
        
        return max_profit

            
            