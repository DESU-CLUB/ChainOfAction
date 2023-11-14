```python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # 1: Initialize a variable to store the cumulative sum.
        cumulative_sum = 0
        
        # 2: Iterate over the array, updating the cumulative sum with the current element.
        for i in range(len(nums)):
            cumulative_sum += nums[i]
            
            # 3: Replace the current element with the cumulative sum.
            nums[i] = cumulative_sum
        
        # 4: Return the updated array.
        return nums
```