```python
class Solution:
    def findComplement(self, num: int) -> int:
        # Step 1: Convert the given integer to its binary representation
        binary_rep = bin(num)[2:]
        
        # Step 2: Flip the bits of the binary representation
        flipped_binary = ''.join('1' if bit == '0' else '0' for bit in binary_rep)
        
        # Step 3: Convert the flipped binary representation back to an integer
        complement = int(flipped_binary, 2)
        
        # Step 4: Return the resulting integer as the complement number
        return complement
```