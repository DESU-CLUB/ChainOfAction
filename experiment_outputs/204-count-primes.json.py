```python
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        # Initialize a list to mark non-prime numbers
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        
        # Sieve of Eratosthenes
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False
        
        # Count prime numbers
        return sum(is_prime)
```