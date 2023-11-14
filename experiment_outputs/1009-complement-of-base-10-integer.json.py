```python
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # Step 1: Convert the integer n to its binary representation
        binary_n = bin(n)[2:]
        
        # Step 2: Flip the bits of the binary representation
        flipped_binary = ''.join('1' if bit == '0' else '0' for bit in binary_n)
        
        # Step 3: Convert the flipped binary representation back to an integer
        complement = int(flipped_binary, 2)
        
        # Step 4: Return the resulting integer
        return complement
```