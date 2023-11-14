As per your request, here is the Python code based on the steps provided:

```python
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # Step 1: Initialize a counter for the number of valid pairs
        count = 0
        
        # Step 2: Create a frequency array or hash map to store the count of song durations modulo 60
        remainder_count = [0] * 60
        
        # Step 3: Iterate over the list of song durations
        for t in time:
            # Step 4: For each song duration, compute its modulo 60 and update the frequency array or hash map
            remainder = t % 60
            remainder_count[remainder] += 1
        
        # Step 5: For each song duration, find the complementary duration that together with the current duration is divisible by 60, and update the counter based on the frequency array or hash map
        for t in time:
            remainder = t % 60
            complement = (60 - remainder) % 60
            remainder_count[remainder] -= 1  # Exclude the current song from the count
            count += remainder_count[complement]
        
        # Step 6: Return the counter as the final result
        return count
```

This code defines a `Solution` class with a method `numPairsDivisibleBy60` that takes a list of song durations and returns the number of pairs whose total duration is divisible by 60. It uses a frequency array to count the occurrences of each remainder when the song durations are divided by 60, and then it finds complementary durations to form valid pairs.