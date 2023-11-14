```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Step 1: Initialize variables
        max_consecutive = 0
        current_consecutive = 0
        
        # Step 2: Iterate through the binary array
        for num in nums:
            # Step 3: If the current element is 1, increment the counter
            if num == 1:
                current_consecutive += 1
            else:
                # Step 4: If the current element is 0, update the maximum if necessary and reset the counter
                max_consecutive = max(max_consecutive, current_consecutive)
                current_consecutive = 0
        
        # Step 5: After the loop, update the maximum with the counter if necessary
        max_consecutive = max(max_consecutive, current_consecutive)
        
        # Step 6: Return the maximum number of consecutive 1s
        return max_consecutive
```