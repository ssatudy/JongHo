class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp_p = prices[-1]
        profit = 0
        for i in range(len(prices)-2, -1, -1):  
            if temp_p < prices[i]:  
                temp_p = prices[i]
            else:  
                if temp_p - prices[i] > profit:  
                    profit = temp_p-prices[i]
        return profit