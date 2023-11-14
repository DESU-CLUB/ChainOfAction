```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1: Initialize variables to track the minimum price and maximum profit.
        min_price = float('inf')
        max_profit = 0
        
        # 2: Iterate through the stock prices array.
        for price in prices:
            # 3: Update the minimum price if the current price is lower than the minimum price found so far.
            min_price = min(min_price, price)
            
            # 4: Calculate the profit by subtracting the minimum price from the current price.
            profit = price - min_price
            
            # 5: Update the maximum profit if the calculated profit is higher than the maximum profit found so far.
            max_profit = max(max_profit, profit)
        
        # 6: Return the maximum profit after iterating through all prices.
        return max_profit
```