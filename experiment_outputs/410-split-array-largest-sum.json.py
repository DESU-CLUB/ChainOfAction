To solve the problem in Python using the function head provided, you can follow these steps:

```python
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # Step 1: Define the binary search boundaries
        left, right = max(nums), sum(nums)
        
        # Step 2: Implement the binary search
        while left < right:
            mid = left + (right - left) // 2
            if self.canSplit(nums, m, mid):
                right = mid
            else:
                left = mid + 1
        
        # Step 6: Return the minimum largest sum found by the binary search
        return left
    
    # Helper function to check if the current split is valid
    def canSplit(self, nums: List[int], m: int, max_sum: int) -> bool:
        count = 1
        current_sum = 0
        
        # Step 3: Use a greedy approach to split the array into subarrays
        for num in nums:
            current_sum += num
            if current_sum > max_sum:
                count += 1
                current_sum = num
                # Step 4: Check if the current split is valid with the given m subarrays
                if count > m:
                    return False
        return True
```

This code defines a `Solution` class with the `splitArray` method that takes a list of integers `nums` and an integer `m` as input and returns the minimum largest sum after splitting the array into `m` subarrays. The `canSplit` helper function is used to determine if a given maximum subarray sum is valid for a given number of splits `m`. The binary search is used to find the minimum valid maximum subarray sum.