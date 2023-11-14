```python
class Solution:
    def canWinNim(self, n: int) -> bool:
        # Step 1: Read the input number of stones in the heap (already given as parameter 'n')
        
        # Step 2: Determine if the number of stones is divisible by 4
        is_divisible_by_4 = (n % 4 == 0)
        
        # Step 3: Return true if the number is not divisible by 4, otherwise return false
        return not is_divisible_by_4
```