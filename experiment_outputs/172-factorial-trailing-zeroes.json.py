```python
class Solution:
    def trailingZeroes(self, n):
        # Initialize a counter for trailing zeroes
        count = 0
        # Loop to count the factors of 5
        while n > 0:
            n //= 5
            count += n
        # Return the trailing zeroes counter as the final result
        return count
```