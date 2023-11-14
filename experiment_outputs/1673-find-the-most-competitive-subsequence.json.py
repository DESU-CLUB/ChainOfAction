```python
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []  # Step 1
        num_skips_allowed = len(nums) - k  # Additional step to calculate allowed skips

        for num in nums:  # Step 2
            while stack and num < stack[-1] and num_skips_allowed > 0:  # Step 2 (continued)
                stack.pop()
                num_skips_allowed -= 1
            stack.append(num)

        # Step 3 is implicitly covered in Step 2 by limiting the number of skips

        return stack[:k]  # Steps 4 and 5
```