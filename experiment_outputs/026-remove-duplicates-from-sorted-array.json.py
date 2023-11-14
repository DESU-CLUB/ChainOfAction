```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 1: Check if the array is empty or has only one element, return its length.
        if len(nums) <= 1:
            return len(nums)
        
        # 2: Initialize two pointers, one for the current element and one for the next non-duplicate element.
        current = 0
        
        # 3: Iterate through the array with the current element pointer.
        for i in range(1, len(nums)):
            # 4: Compare the current element with the next element.
            if nums[current] != nums[i]:
                # 5: If they are different, copy the next element to the position after the next non-duplicate element pointer and increment the next non-duplicate element pointer.
                current += 1
                nums[current] = nums[i]
        
        # 6: Continue the iteration until the end of the array is reached.
        # (This is done within the loop)
        
        # 7: Return the position of the next non-duplicate element pointer as the new length of the array.
        return current + 1
```