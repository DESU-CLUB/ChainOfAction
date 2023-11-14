```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1: Perform a binary search to determine the index of the smallest element (pivot).
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        
        pivot = start
        
        # Reset start and end for the next binary search
        start, end = 0, len(nums) - 1
        
        # 2: Decide which subarray to search based on the target's relation to the pivot.
        if target >= nums[pivot] and target <= nums[end]:
            start = pivot
        else:
            end = pivot
        
        # 3: Perform a binary search on the chosen subarray to find the target.
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        
        # 4: Return the index of the target, or -1 if not found.
        return -1
```