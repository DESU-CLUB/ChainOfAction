Here is the Python code that follows the given steps to solve the Last Stone Weight problem:

```python
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Step 1: Create a max-heap to store the stones (Python has min-heap by default, so we negate the values)
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        # Step 2: While more than one stone remains in the heap
        while len(max_heap) > 1:
            # Step 2a: Pop the two heaviest stones from the heap
            stone1 = -heapq.heappop(max_heap)
            stone2 = -heapq.heappop(max_heap)
            
            # Step 2b: If they are not equal, push the difference back into the heap
            if stone1 != stone2:
                heapq.heappush(max_heap, -(stone1 - stone2))
        
        # Step 3: Return the weight of the remaining stone or 0 if the heap is empty
        return -max_heap[0] if max_heap else 0
```

This code defines a class `Solution` with a method `lastStoneWeight` that takes a list of integers representing the stones' weights and returns the weight of the last stone or 0 if there are no stones left. The code uses a max-heap (simulated using a min-heap with negated values) to efficiently find and remove the two heaviest stones until one or no stones remain.