```python
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # Step 1: Create a frequency map to count occurrences of each number in nums.
        freq = collections.Counter(nums)
        
        # Step 2: Identify the maximum value in nums to determine the range of possible values.
        max_num = max(nums)
        
        # Step 3: Initialize an array to store the maximum points that can be earned up to each value.
        earn = [0] * (max_num + 1)
        
        # Step 4: Populate the earn array with points from the frequency map.
        for num in freq:
            earn[num] = num * freq[num]
        
        # Step 5: Iterate through the range of possible values, calculating the maximum points for each value.
        for i in range(2, max_num + 1):
            earn[i] = max(earn[i-1], earn[i-2] + earn[i])
        
        # Step 6: Return the maximum points that can be earned for the maximum value in nums.
        return earn[max_num]
```