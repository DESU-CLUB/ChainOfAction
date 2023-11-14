```python
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # 1: Initialize a variable to track the index of the last found 1.
        last_index = -k - 1
        
        # 2: Iterate through the array nums.
        for i, num in enumerate(nums):
            # 3: If a 1 is found, check the distance from the last 1 and update the last found 1's index.
            if num == 1:
                if i - last_index - 1 < k:
                    # 4: If the distance is less than k, return False.
                    return False
                last_index = i
        
        # 5: If the end of the array is reached without finding any 1's closer than k, return True.
        return True
```