```python
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # Step 1: Start at the top-right corner of the matrix
        m, n = len(grid), len(grid[0])
        row, col = 0, n - 1
        count = 0
        
        # Step 2: While within the bounds of the matrix, move left if the current value is non-negative, down otherwise
        while row < m and col >= 0:
            if grid[row][col] < 0:
                # Step 3: Increment a counter each time a negative value is encountered
                count += (m - row)
                col -= 1
            else:
                row += 1
        
        # Step 4: Return the counter
        return count
```