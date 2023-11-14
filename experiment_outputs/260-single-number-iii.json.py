```python
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: Initialize a variable to perform XOR on all elements of the array.
        xor = 0
        for num in nums:
            xor ^= num
        
        # Step 2: Find the rightmost set bit in the XOR result.
        rightmost_set_bit = xor & -xor
        
        # Step 3: Initialize two variables to hold the two unique numbers.
        num1, num2 = 0, 0
        
        # Step 4: Partition the array elements into two groups based on the rightmost set bit.
        for num in nums:
            if num & rightmost_set_bit:
                # Step 5: Perform XOR on each group separately to find the two unique numbers.
                num1 ^= num
            else:
                num2 ^= num
        
        # Step 6: Return the two unique numbers as the result.
        return [num1, num2]
```