```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 1: Initialize a counter for tracking element occurrences.
        counts = {}

        # 2: Iterate through the array, counting occurrences of each element.
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1

            # 3: If an element's count exceeds ⌊ n/2 ⌋, return that element as the majority element.
            if counts[num] > len(nums) // 2:
                return num
```