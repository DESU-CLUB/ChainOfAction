```python
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # 1: Initialize a list to represent the circle of friends.
        friends = list(range(1, n + 1))
        
        # 2: Simulate the game using a loop to eliminate friends.
        index = 0
        while len(friends) > 1:
            # 3: Calculate the index of the next friend to be eliminated in each iteration.
            index = (index + k - 1) % len(friends)
            
            # 4: Remove the friend from the circle.
            friends.pop(index)
        
        # 5: Continue the loop until only one friend remains.
        # 6: Return the remaining friend as the winner.
        return friends[0]
```