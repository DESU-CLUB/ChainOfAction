As per your request, I will only provide the Python code without any additional explanation. Here is the code based on the steps provided:

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Step 1: Initialize variables
        max_product = min_product = result = nums[0]
        
        # Step 2: Iterate through the array
        for i in range(1, len(nums)):
            num = nums[i]
            if num < 0:
                max_product, min_product = min_product, max_product
            
            # Update the maximum and minimum product
            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)
            
            # Step 3: Update the result
            result = max(result, max_product)
        
        # Step 4: Return the result
        return result
```