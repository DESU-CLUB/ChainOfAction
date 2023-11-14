Here's the Python code based on the steps provided:

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Step 1: Check if the list of house values is empty or has only one house
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # Step 2: Initialize two variables to store the maximum amounts
        rob_previous = 0  # Maximum amount robbed by skipping the previous house
        rob_current = nums[0]  # Maximum amount robbed by robbing the current house
        
        # Step 3: Iterate over the list of house values starting from the second house
        for i in range(1, len(nums)):
            # Step 4: Calculate the new maximum amount that can be robbed
            new_rob = max(rob_current, rob_previous + nums[i])
            
            # Step 5: Update the variables with the new calculated maximums
            rob_previous = rob_current
            rob_current = new_rob
        
        # Step 6: Return the maximum amount that can be robbed without alerting the police
        return rob_current
```

This code defines a class `Solution` with a method `rob` that takes a list of integers `nums` representing the amount of money in each house. It follows the steps to calculate the maximum amount of money that can be robbed without triggering the security systems of adjacent houses.