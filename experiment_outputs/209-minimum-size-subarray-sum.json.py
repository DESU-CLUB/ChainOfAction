```python
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # 1: Initialize variables for the current sum, start index, and minimal length.
        current_sum = 0
        start_index = 0
        min_length = float('inf')  # Use infinity as initial value for comparison

        # 2: Iterate through the array using two pointers to maintain a sliding window.
        for end_index in range(len(nums)):
            # 3: Expand the window by moving the end pointer and updating the current sum.
            current_sum += nums[end_index]

            # 4: Once the current sum is greater than or equal to s, update the minimal length.
            while current_sum >= s:
                min_length = min(min_length, end_index - start_index + 1)

                # 5: Contract the window by moving the start pointer and updating the current sum.
                current_sum -= nums[start_index]
                start_index += 1

        # 6: Repeat steps 3 to 5 until the end of the array is reached.
        # This is implicitly done by the for loop.

        # 7: Return the minimal length or 0 if no such subarray is found.
        return 0 if min_length == float('inf') else min_length
```