Based on the steps provided, here is the Python code for the problem using the provided function head:

```python
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_map = {0: -1}  # Step 1
        max_length = count = 0  # Step 2

        for i, num in enumerate(nums):  # Step 3
            count = count + 1 if num == 1 else count - 1  # Update cumulative count

            if count in count_map:  # Step 4
                max_length = max(max_length, i - count_map[count])  # Step 5
            else:
                count_map[count] = i  # Step 6

        return max_length  # Step 7
```

This code snippet correctly implements the steps you've outlined and should solve the problem as per the given constraints.