```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 1: Initialize a 2D array to store the number of ways to reach each cell.
        dp = [[0] * n for _ in range(m)]
        
        # 2: Set the number of ways to reach the cells in the first row and first column to 1.
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        # 3: Iterate through the grid starting from the cell (1,1) to (m-1,n-1).
        for i in range(1, m):
            for j in range(1, n):
                # 4: For each cell, calculate the number of ways to reach it by summing the ways to reach the cell above it and the cell to the left of it.
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        # 5: Return the value in the bottom-right corner of the grid as the number of unique paths.
        return dp[m - 1][n - 1]
```