```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Step 1: Check if the input integer is less than or equal to zero.
        if n <= 0:
            return False
        
        # Step 2: Use bitwise operations to determine if the integer is a power of two.
        # An integer is a power of two if it has exactly one bit set in its binary representation.
        return (n & (n - 1)) == 0
```