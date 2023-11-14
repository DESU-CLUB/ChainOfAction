```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        # 1: Initialize variables to keep track of the current jump reach, the farthest reach on the next jump, and the number of jumps.
        jumps = 0
        current_jump_end = 0
        farthest = 0
        
        # 2: Iterate through the array, excluding the last element.
        for i in range(len(nums) - 1):
            # 3: Update the farthest reach on the next jump at each step.
            farthest = max(farthest, i + nums[i])
            
            # 4: If the current index reaches the current jump reach, update the current jump reach to the farthest reach and increment the number of jumps.
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest
        
        # 5: Return the number of jumps after the iteration completes.
        return jumps
```