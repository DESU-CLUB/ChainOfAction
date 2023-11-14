```python
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Step 1: Perform a bitwise XOR operation on x and y
        xor_result = x ^ y
        
        # Step 2: Count the number of 1's in the result of the XOR operation
        count = bin(xor_result).count('1')
        
        # Step 3: Return the count as the Hamming distance
        return count
```