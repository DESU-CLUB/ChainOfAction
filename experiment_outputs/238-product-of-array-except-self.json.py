```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1: Initialize an output array with the same length as the input array.
        output = [1] * len(nums)
        
        # 2: Create a variable to store the cumulative product from the left.
        left_product = 1
        
        # 3: Iterate over the input array from left to right, updating the output array with the cumulative product.
        for i in range(len(nums)):
            output[i] = left_product
            left_product *= nums[i]
        
        # 4: Reset the cumulative product variable for the right side.
        right_product = 1
        
        # 5: Iterate over the input array from right to left, updating the output array by multiplying the cumulative product from the right.
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
        
        # 6: Return the output array.
        return output
```