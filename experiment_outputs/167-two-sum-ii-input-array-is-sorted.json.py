```python
class Solution:
    def two_sum(self, nums, target):
        # 1: Initialize two pointers, one at the start and one at the end of the array.
        left, right = 0, len(nums) - 1
        
        # 2: While the start pointer is less than the end pointer, perform the following:
        while left < right:
            # a. Calculate the sum of the values at the two pointers.
            current_sum = nums[left] + nums[right]
            
            # b. If the sum equals the target, return the indices of the two pointers.
            if current_sum == target:
                return [left + 1, right + 1]  # Convert to 1-based index
            
            # c. If the sum is less than the target, move the start pointer up.
            elif current_sum < target:
                left += 1
            
            # d. If the sum is greater than the target, move the end pointer down.
            else:
                right -= 1
        
        # If no solution is found, this line will not be reached because the problem statement guarantees one solution.
```