As per your request, I will provide the Python code based on the steps identified:

```python
import heapq
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # Step 1: Initialize a min-heap data structure.
        min_heap = []
        
        # Step 2: Insert the first element of each row into the min-heap along with its position (row and column).
        for row in range(min(k, len(matrix))):  # Only need to consider up to k rows since kth element can't be beyond kth row
            heapq.heappush(min_heap, (matrix[row][0], row, 0))
        
        # Step 3: Pop elements from the min-heap until you reach the kth element.
        while k > 0:
            element, row, col = heapq.heappop(min_heap)
            k -= 1
            
            # Step 4: Each time you pop an element, insert the next element from the same row into the min-heap if it exists.
            if col + 1 < len(matrix[row]):
                heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))
        
        # Step 5: Return the value of the kth popped element.
        return element
```

This code defines a class `Solution` with a method `kthSmallest` that implements the steps to solve the problem of finding the kth smallest element in a sorted matrix. The min-heap is used to efficiently find the kth smallest element by maintaining a heap of the smallest elements seen so far.