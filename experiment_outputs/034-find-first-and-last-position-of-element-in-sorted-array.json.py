Based on the steps provided, here is the Python code for the problem:

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search_left(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        
        def binary_search_right(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        
        left_index = binary_search_left(nums, target)
        right_index = binary_search_right(nums, target)
        
        # Check if the target is not present in the array
        if left_index > right_index:
            return [-1, -1]
        
        return [left_index, right_index]
```

Please note that the provided references and skills seem to be unrelated to the current problem. The code above follows the steps you've outlined for the specific problem of finding the first and last positions of an element in a sorted array.