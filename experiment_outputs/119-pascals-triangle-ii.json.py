```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 1: Initialize an array to represent the current row with a 1 at the first position.
        row = [1] * (rowIndex + 1)
        
        # 2: Iterate from 1 to k to build each row of Pascal's triangle.
        for i in range(1, rowIndex):
            # 3: For each iteration, update the current row in reverse order using the values from the previous row.
            for j in range(i, 0, -1):
                row[j] += row[j - 1]
        
        # 5: Return the current row as the kth index row of Pascal's triangle.
        return row
```