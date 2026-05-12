from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        
        for current_price in prices[1:]:
            # 1. Vendo hipotéticamente hoy, comprando al mínimo visto antes
            max_profit = max(max_profit, current_price - min_price)
            
            # 2. Actualizo el mínimo para los días futuros
            min_price = min(min_price, current_price)
        
        return max_profit