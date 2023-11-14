```python
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        start, end = 0, len(nums) - 1
        count = 0
        
        while start < end:
            current_sum = nums[start] + nums[end]
            if current_sum == k:
                count += 1
                start += 1
                end -= 1
            elif current_sum < k:
                start += 1
            else:
                end -= 1
        
        return count
```