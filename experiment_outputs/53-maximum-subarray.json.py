```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 1: Initialize variables to track the maximum sum and current sum.
        max_sum = current_sum = nums[0]
        
        # 2: Iterate through the array, updating the current sum and maximum sum as needed.
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        
        # 3: Return the maximum sum after completing the iteration.
        return max_sum
```