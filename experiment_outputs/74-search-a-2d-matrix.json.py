```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        
        # Step 1: Perform a binary search on the rows
        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break  # The target is in the range of the current row
        
        # If we didn't find a row where the target could be, return False
        if not (top <= bottom):
            return False
        
        # Step 2: Perform a binary search on the selected row
        row = (top + bottom) // 2
        left, right = 0, len(matrix[row]) - 1
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True  # The target is found
        
        # Step 3: Return false if the target is not found
        return False
```