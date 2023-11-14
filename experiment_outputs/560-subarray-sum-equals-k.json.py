As per your request, I will provide the Python code based on the steps identified:

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Step 1: Initialize a counter for the number of subarrays and a cumulative sum variable.
        count, cumulative_sum = 0, 0
        
        # Step 2: Create a hash map to store the frequency of cumulative sums.
        sum_frequency = {0: 1}
        
        # Step 3: Iterate through the array, updating the cumulative sum.
        for num in nums:
            cumulative_sum += num
            
            # Step 4: Check if (cumulative sum - k) exists in the hash map and add its frequency to the counter.
            if (cumulative_sum - k) in sum_frequency:
                count += sum_frequency[cumulative_sum - k]
            
            # Step 5: Update the frequency of the current cumulative sum in the hash map.
            sum_frequency[cumulative_sum] = sum_frequency.get(cumulative_sum, 0) + 1
        
        # Step 6: Return the counter as the final result.
        return count
```

This code defines a `Solution` class with a `subarraySum` method that takes a list of integers `nums` and an integer `k` and returns the total number of continuous subarrays whose sum equals `k`. The method follows the steps you've outlined to solve the problem.