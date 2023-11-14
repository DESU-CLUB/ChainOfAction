```python
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # 1: Initialize variables
        max_sum = cur_max = min_sum = cur_min = total = A[0]
        
        # 2: Iterate to calculate max subarray sum (Kadane's algorithm)
        for num in A[1:]:
            cur_max = max(num, cur_max + num)
            max_sum = max(max_sum, cur_max)
        
        # 3: Iterate to calculate min subarray sum (Kadane's algorithm on inverted values)
        for num in A[1:]:
            cur_min = min(num, cur_min + num)
            min_sum = min(min_sum, cur_min)
            total += num
        
        # 4: Calculate the total sum of the array
        # (Already done in step 3)
        
        # 5: Determine the maximum circular subarray sum
        max_circular = total - min_sum
        
        # 6: Handle the edge case where all numbers are negative
        if max_sum < 0:
            return max_sum
        
        # 7: Return the maximum of the max subarray sum and the max circular subarray sum
        return max(max_sum, max_circular)
```