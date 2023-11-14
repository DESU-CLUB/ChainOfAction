```python
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        # 1: Sort the array in non-increasing order.
        nums.sort(reverse=True)
        
        # 2: Calculate the total sum of the array.
        total_sum = sum(nums)
        
        # 3: Initialize a variable to keep track of the subsequence sum.
        subsequence_sum = 0
        
        # 4: Iterate through the sorted array and add elements to the subsequence until the subsequence sum is greater than the remaining sum.
        subsequence = []
        for num in nums:
            subsequence_sum += num
            subsequence.append(num)
            if subsequence_sum > total_sum - subsequence_sum:
                break
        
        # 5: Return the subsequence.
        return subsequence
```