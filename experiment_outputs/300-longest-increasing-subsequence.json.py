```python
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0

        # Step 1: Initialize an array to store the length of the longest increasing subsequence ending at each index.
        dp = [1] * len(nums)

        # Step 5: Keep track of the overall maximum subsequence length found so far.
        max_length = 1

        # Step 2: Iterate through the input array, comparing each element with the previous elements.
        for i in range(1, len(nums)):
            # Step 3: For each element, determine the maximum subsequence length from the previous elements that can be extended.
            for j in range(i):
                if nums[i] > nums[j]:
                    # Step 4: Update the array with the new maximum subsequence length for the current element.
                    dp[i] = max(dp[i], dp[j] + 1)
            # Update the overall maximum subsequence length if necessary.
            max_length = max(max_length, dp[i])

        # Step 6: Return the overall maximum subsequence length as the final result.
        return max_length
```