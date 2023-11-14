```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 1: Initialize start and end pointers for binary search.
        start, end = 0, len(nums) - 1
        
        # 2: Perform binary search.
        while start <= end:
            # a. Calculate the middle index.
            mid = (start + end) // 2
            
            # b. Compare the middle element with the target value.
            if nums[mid] == target:
                # c. If the middle element is equal to the target, return the middle index.
                return mid
            elif nums[mid] < target:
                # d. If the target is greater than the middle element, adjust the start pointer.
                start = mid + 1
            else:
                # e. If the target is less than the middle element, adjust the end pointer.
                end = mid - 1
        
        # 3: Return the start pointer as the index where the target would be inserted.
        return start
```