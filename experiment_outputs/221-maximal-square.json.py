```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 1: Initialize a variable to store the maximum size of a square found.
        max_square_length = 0
        
        # 2: Create a 2D array to store the size of the largest square ending at each position.
        if matrix:
            rows, cols = len(matrix), len(matrix[0])
            dp = [[0] * cols for _ in range(rows)]
            
            # 3: Loop through each cell in the matrix.
            for i in range(rows):
                for j in range(cols):
                    # 4: Update the 2D array with the size of the square if the cell is '1'.
                    if matrix[i][j] == '1':
                        if i == 0 or j == 0:  # If it's the first row or first column
                            dp[i][j] = 1
                        else:  # If it's not the first row or column
                            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                        # 5: Update the maximum size variable if a larger square is found.
                        max_square_length = max(max_square_length, dp[i][j])
        
        # 6: Calculate the area of the largest square using the maximum size.
        max_square_area = max_square_length ** 2
        
        # 7: Return the area.
        return max_square_area
```