As per your request, I will provide the Python code for the problem using the steps identified:

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1
        triplets = []  # Step 2
        
        for i in range(len(nums)):  # Step 3
            if i > 0 and nums[i] == nums[i - 1]:  # Avoid duplicates for the first element
                continue
            left, right = i + 1, len(nums) - 1  # Step 4
            while left < right:  # Step 5
                total = nums[i] + nums[left] + nums[right]  # Step 5a
                if total < 0:  # Step 5c
                    left += 1
                elif total > 0:  # Step 5d
                    right -= 1
                else:  # Step 5b
                    triplets.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:  # Avoid duplicates for the second element
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:  # Avoid duplicates for the third element
                        right -= 1
                    left += 1
                    right -= 1
        
        return triplets  # Step 6
```

This code follows the steps provided to solve the 3Sum problem.