Here's the Python code for the problem following the steps you provided:

```python
from heapq import heappush, heappop

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Step 1: Initialize a list to store the count and character for 'a', 'b', and 'c'.
        max_heap = []
        if a: heappush(max_heap, (-a, 'a'))
        if b: heappush(max_heap, (-b, 'b'))
        if c: heappush(max_heap, (-c, 'c'))

        # Step 3: Initialize an empty result string.
        res = []

        # Step 4: While there are characters left to append:
        while max_heap:
            count, char = heappop(max_heap)
            # Step 4a: Append the most frequent character to the result string if it doesn't create a triple.
            if len(res) >= 2 and res[-1] == res[-2] == char:
                if not max_heap:
                    break  # No other character can be used, break the loop
                # Step 4b: Otherwise, append the second most frequent character.
                second_count, second_char = heappop(max_heap)
                res.append(second_char)
                second_count += 1  # Decrease count
                if second_count < 0:  # If there are more of this character, push it back
                    heappush(max_heap, (second_count, second_char))
                heappush(max_heap, (count, char))  # Push the first character back
            else:
                res.append(char)
                count += 1  # Decrease count
                if count < 0:  # If there are more of this character, push it back
                    heappush(max_heap, (count, char))

        # Step 5: Return the result string.
        return ''.join(res)
```

This code uses a max heap to keep track of the characters and their counts, ensuring that no more than two consecutive characters are the same. It builds the result string by appending the most frequent character that doesn't create a triple, or the second most frequent character if necessary.