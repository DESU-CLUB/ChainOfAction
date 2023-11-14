```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 1: Initialize an empty list to store the missing elements.
        missing = []
        
        # 2: Create a set from the nums list for O(1) lookups.
        num_set = set(nums)
        
        # 3: Iterate through the range of numbers from 1 to n.
        for number in range(1, len(nums) + 1):
            
            # 4: Check if the number is not in the set.
            if number not in num_set:
                
                # 5: If a number is missing, append it to the list of missing elements.
                missing.append(number)
        
        # 6: Return the list of missing elements after the iteration is complete.
        return missing
```