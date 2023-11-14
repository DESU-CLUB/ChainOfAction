```python
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Step 2: Create a sorted copy of the input array
        sorted_heights = sorted(heights)
        
        # Step 3: Initialize a counter to track the number of students not in the right positions
        count = 0
        
        # Step 4: Iterate through the arrays comparing the original and sorted arrays
        for i in range(len(heights)):
            # Step 5: Increment the counter when a mismatch is found between the two arrays
            if heights[i] != sorted_heights[i]:
                count += 1
        
        # Step 6: Return the counter as the final result
        return count
```