```python
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompressed = []
        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i + 1]
            decompressed.extend([val] * freq)
        return decompressed
```