```python
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # 1: Initialize variables to track the start and end of the subarray.
        start, end = len(nums), 0
        
        # 2: Traverse the array to find the first element that is not in ascending order, mark it as the start.
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                start = min(start, i)
        
        # 3: Traverse the array from the end to find the first element that is not in descending order, mark it as the end.
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                end = max(end, i)
        
        # 4: Find the minimum and maximum values within the identified subarray.
        subarray_min = min(nums[start:end+1], default=float('inf'))
        subarray_max = max(nums[start:end+1], default=float('-inf'))
        
        # 5: Expand the start and end indices to include any numbers outside the subarray that are greater than the minimum or less than the maximum.
        for i in range(start):
            if nums[i] > subarray_min:
                start = i
                break
        
        for i in range(len(nums) - 1, end, -1):
            if nums[i] < subarray_max:
                end = i
                break
        
        # 6: Calculate the length of the subarray from the start and end indices.
        length = end - start + 1
        
        # 7: Return the length of the subarray.
        return length if length > 0 else 0
```