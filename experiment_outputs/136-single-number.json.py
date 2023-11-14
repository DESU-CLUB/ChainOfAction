```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique_number = 0
        for num in nums:
            unique_number ^= num
        return unique_number
```