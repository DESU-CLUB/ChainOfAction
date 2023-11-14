Based on the steps provided, here is the Python code for the `maxProfit` function:

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1: Initialize a variable to store total profit.
        total_profit = 0
        
        # 2: Loop through the array of prices.
        for i in range(1, len(prices)):
            
            # 3: If the current price is less than the next day's price, buy and sell the stock the next day.
            if prices[i] > prices[i - 1]:
                
                # 4: Add the profit from each transaction to the total profit.
                total_profit += prices[i] - prices[i - 1]
        
        # 5: Return the total profit.
        return total_profit
```

Please note that the code assumes that `List` has been imported from `typing` or that the code is being written in a context where `List` is already available. If not, you should include the import statement `from typing import List` at the beginning of your code.