```python
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # 1: Initialize an array to store the Next Greater Numbers with the same length as the input array, filled with -1.
        result = [-1] * len(nums)
        
        # 2: Use a stack to keep track of the indices of elements for which the Next Greater Number has not been found yet.
        stack = []
        
        # 3: Iterate through the array twice to simulate a circular array.
        for i in range(len(nums) * 2):
            # Since the array is circular, use modulo to wrap around.
            num = nums[i % len(nums)]
            
            # 4: For each element, while the stack is not empty and the current element is greater than the element at the index on the top of the stack:
            while stack and nums[stack[-1]] < num:
                # a. Pop the index from the stack.
                index = stack.pop()
                # b. Update the Next Greater Number for the popped index with the current element.
                result[index] = num
            
            # Only push the index of the first iteration to avoid duplicates.
            if i < len(nums):
                # 5: Push the current index onto the stack.
                stack.append(i)
        
        # 6: Return the array of Next Greater Numbers.
        return result
```