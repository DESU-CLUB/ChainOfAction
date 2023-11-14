```python
class Solution:
    def numSquares(self, n: int) -> int:
        # 1: Initialize an array to store the minimum number of perfect squares that sum to each number up to n.
        dp = [float('inf')] * (n + 1)
        
        # 2: Populate the array with initial values (e.g., maximum possible count).
        dp[0] = 0
        
        # 3: Loop through the array to fill it with the correct counts for each number.
        for i in range(1, n + 1):
            # 4: For each number, find the minimum count by considering all possible perfect square numbers that could contribute to its sum.
            j = 1
            while j * j <= i:
                # 5: Update the array with the minimum count found for each number.
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        
        # 6: Return the value in the array corresponding to n as the final result.
        return dp[n]
```