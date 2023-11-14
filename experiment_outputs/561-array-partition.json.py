```python
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 1: Sort the input array in ascending order.
        nums.sort()
        
        # 2: Initialize a variable to keep track of the sum.
        sum_of_pairs = 0
        
        # 3: Iterate through the array with a step of 2.
        for i in range(0, len(nums), 2):
            # 4: Add the element at the current index to the sum.
            sum_of_pairs += nums[i]
        
        # 5: Return the sum as the final result.
        return sum_of_pairs
```