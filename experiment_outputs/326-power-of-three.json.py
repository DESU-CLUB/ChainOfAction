```python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Step 1: Check if the input integer is less than or equal to zero.
        if n <= 0:
            return False
        
        # Step 2: Calculate the logarithm of the integer base 3.
        # Step 3: Check if the result of the logarithm is an integer.
        # The largest power of 3 value that integer can hold is 3^19 = 1162261467 for 32-bit signed integer
        # If n is a power of three, it must divide 3^19 without a remainder.
        return 1162261467 % n == 0
```