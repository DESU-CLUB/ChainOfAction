Here's the Python code that follows the given steps:

```python
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # Step 1: Initialize a variable to track the minimum sum encountered.
        min_sum = 0
        
        # Step 2: Iterate through the array, updating the running sum and minimum sum.
        running_sum = 0
        for num in nums:
            running_sum += num
            min_sum = min(min_sum, running_sum)
        
        # Step 3: Calculate the minimum start value based on the minimum sum.
        start_value = 1 - min_sum
        
        # Step 4: Return the minimum start value.
        return start_value
```

This code defines a `Solution` class with a `minStartValue` method that takes a list of integers `nums` as input and returns the minimum positive start value such that the step-by-step sum is never less than 1. The method follows the steps provided to calculate the minimum start value.