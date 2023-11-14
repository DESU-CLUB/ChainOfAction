```python
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Initialize a deque and a list for maximums
        deq = deque()
        max_window = []

        # Step 2: Populate the deque with the first k elements' indices
        for i in range(k):
            while deq and nums[i] >= nums[deq[-1]]:
                deq.pop()
            deq.append(i)

        # Step 3: Add the maximum element of the first window
        max_window.append(nums[deq[0]])

        # Step 4: Iterate over the array starting from the kth element
        for i in range(k, len(nums)):
            # Step 5: Remove indices that are out of bounds
            while deq and deq[0] <= i - k:
                deq.popleft()
            
            # Step 6: Remove indices that are less than the current element
            while deq and nums[i] >= nums[deq[-1]]:
                deq.pop()
            
            # Step 7: Append the current element's index
            deq.append(i)
            
            # Step 8: Add the front element of the deque to the list of maximums
            max_window.append(nums[deq[0]])

        # Step 9: Return the list of maximums
        return max_window
```