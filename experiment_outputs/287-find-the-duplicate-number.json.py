As per your request, here is the Python code that follows the steps provided:

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Step 1: Initialize slow and fast pointers to the beginning of the array.
        slow = nums[0]
        fast = nums[0]
        
        # Step 2: Move the slow pointer by one step and the fast pointer by two steps until they meet.
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Step 3: Reset one pointer to the beginning of the array.
        slow = nums[0]
        
        # Step 4: Move both pointers one step at a time until they meet again.
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        # Step 5 & 6: The meeting point is the duplicate number. Return the duplicate number.
        return slow
```

This code uses Floyd's Tortoise and Hare (Cycle Detection) algorithm to find the duplicate number in the array.