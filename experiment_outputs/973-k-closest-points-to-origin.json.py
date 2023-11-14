```python
from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # Step 1: Calculate the squared distance for each point from the origin.
        distances = [(x**2 + y**2, i) for i, (x, y) in enumerate(points)]
        
        # Step 2: Use a partial sorting algorithm to find the k smallest distances.
        # heapq.nsmallest will get us the k smallest distances along with their original indices.
        k_smallest = heapq.nsmallest(K, distances)
        
        # Step 3: Extract the points corresponding to the k smallest distances.
        # We use the stored indices to get the original points.
        closest_points = [points[i] for (_, i) in k_smallest]
        
        # Step 4: Return the k closest points.
        return closest_points
```

This Python code defines a class `Solution` with a method `kClosest` that takes a list of points and an integer `K` and returns the `K` closest points to the origin. It uses the `heapq` module to efficiently find the `K` smallest distances without fully sorting the entire list.