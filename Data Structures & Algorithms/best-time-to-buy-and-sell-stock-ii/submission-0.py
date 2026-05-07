from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        for index in range(1,len(prices)):
            prev_price = prices[index - 1]
            price = prices[index]
            if prev_price < price:
                value = price - prev_price
                total += value
                
        return total