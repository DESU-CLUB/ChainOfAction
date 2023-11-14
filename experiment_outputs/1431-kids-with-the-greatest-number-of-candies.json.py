```python
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # 1: Determine the maximum number of candies any kid currently has.
        max_candies = max(candies)
        
        # 2: Iterate through each kid in the candies array.
        # 3: For each kid, check if adding extraCandies to their current number of candies would equal or exceed the maximum number found in step 1.
        # 4: Store the result of the check as a boolean value in a new array.
        result = [kid + extraCandies >= max_candies for kid in candies]
        
        # 5: Return the new array containing the boolean values.
        return result
```