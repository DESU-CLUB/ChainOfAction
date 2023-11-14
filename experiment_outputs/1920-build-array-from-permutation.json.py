```python
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # 1: Initialize an empty array ans of the same length as nums.
        ans = [0] * len(nums)
        
        # 2: Iterate over each index i in nums.
        for i in range(len(nums)):
            # 3: Set ans[i] to nums[nums[i]].
            ans[i] = nums[nums[i]]
        
        # 4: Return the array ans.
        return ans
```