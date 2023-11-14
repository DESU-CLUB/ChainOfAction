Based on the steps provided, here is the Python code for the `kthFactor` function:

```python
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # Step 1: Initialize a counter for the number of factors found.
        counter = 0
        
        # Step 2: Loop from 1 to the square root of n to find factors.
        for i in range(1, int(n**0.5) + 1):
            # Step 3: For each factor found, increment the counter and check if it is the kth factor.
            if n % i == 0:
                counter += 1
                # Step 4: If the counter reaches k, return the current factor.
                if counter == k:
                    return i
        
        # Step 5: After the loop, adjust k for symmetric factors if n is a perfect square.
        if (int(n**0.5))**2 == n:
            k += 1  # Adjust k to skip the perfect square's duplicate factor
        
        # Step 6: Loop backwards from the largest factor found to n/2 to find the kth factor from the end.
        for i in range(int(n**0.5), 0, -1):
            if n % i == 0:
                counter += 1
                # Step 7: If the adjusted kth factor is found, return it.
                if counter == k:
                    return n // i
        
        # Step 8: If no kth factor is found, return -1.
        return -1
```

Please note that the code above follows the steps you provided, but there is a slight modification in Step 5 to correctly handle the case when `n` is a perfect square. The adjustment to `k` is necessary to avoid counting the square root twice when looking for factors greater than the square root of `n`.