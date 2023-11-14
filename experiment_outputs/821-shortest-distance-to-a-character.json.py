```python
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # 1: Initialize an array to store the shortest distances.
        shortest_distances = [float('inf')] * len(s)
        
        # 2: Traverse the string from left to right, updating the shortest distance to the most recent occurrence of character C.
        prev = float('-inf')
        for i in range(len(s)):
            if s[i] == c:
                prev = i
            shortest_distances[i] = min(shortest_distances[i], i - prev)
        
        # 3: Traverse the string from right to left, updating the shortest distance to the most recent occurrence of character C.
        prev = float('inf')
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                prev = i
            shortest_distances[i] = min(shortest_distances[i], prev - i)
        
        # 4: Return the array of shortest distances.
        return shortest_distances
```