As per your request, here is the Python code based on the steps provided:

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Step 1: Initialize a hash map to store the value and its latest index.
        value_indices = {}

        # Step 2: Iterate through the array of integers.
        for i, num in enumerate(nums):
            # Step 3: For each element, check if it exists in the hash map and if the current index minus the stored index is less than or equal to k.
            if num in value_indices and i - value_indices[num] <= k:
                # Step 4: If such a pair is found, return true.
                return True
            # Step 5: Update the hash map with the current element's index.
            value_indices[num] = i
        
        # Step 6: If no such pair is found by the end of the iteration, return false.
        return False
```