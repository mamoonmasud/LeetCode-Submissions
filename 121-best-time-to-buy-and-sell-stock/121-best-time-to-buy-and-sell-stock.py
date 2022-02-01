class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         x_min = prices[0]
#         max_profit = 0
#         profit = 0
#         for s_price in prices:
#             x_min = min(x_min, s_price)
#             profit = s_price - x_min
#             max_profit = max(max_profit, profit)
            
#         return max_profit
    
    
        x_min = prices[0]
        
        max_profit = 0
        
        profit = 0
        for x in prices:
            x_min = min(x, x_min)
            profit = x - x_min
            max_profit = max(profit, max_profit)
            
        return max_profit
        