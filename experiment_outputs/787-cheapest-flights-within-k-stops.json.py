Here's the Python code that follows the given steps to solve the problem:

```python
from typing import List
from heapq import heappush, heappop

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # Step 1: Construct a graph to represent the cities and flights.
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # Step 2: Initialize a priority queue to perform a modified Dijkstra's algorithm.
        # (cost, city, stops)
        pq = [(0, src, 0)]
        
        # Step 3: Enqueue the starting city with a cost of 0 and 0 stops.
        # This step is already done above while initializing the priority queue.
        
        # Step 4: While the queue is not empty, dequeue the city with the lowest cost.
        while pq:
            cost, city, stops = heappop(pq)
            
            # Step 5: If the dequeued city is the destination, return the cost.
            if city == dst:
                return cost
            
            # Step 6: If the number of stops is within the limit, enqueue neighboring cities with updated costs and stop counts.
            if stops <= K:
                for next_city, price in graph[city]:
                    heappush(pq, (cost + price, next_city, stops + 1))
        
        # Step 7: If the destination is not reached within the stop limit, return -1.
        return -1
```

This code defines a `Solution` class with the `findCheapestPrice` method, which implements the steps to find the cheapest flight price within K stops using a modified Dijkstra's algorithm with a priority queue. The `graph` is represented as an adjacency list, and a priority queue is used to keep track of the cities to visit next, ordered by the current cost to reach them. If the destination is reached within the allowed number of stops, the minimum cost is returned; otherwise, `-1` is returned.