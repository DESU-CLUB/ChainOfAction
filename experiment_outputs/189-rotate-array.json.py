Based on the steps provided, here is the Python code for the `rotate` function:

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start, end = start + 1, end - 1
        
        n = len(nums)
        k %= n  # Step 1: Normalize k by taking k modulo the array's length.
        
        reverse(nums, 0, n - 1)  # Step 2: Reverse the entire array.
        reverse(nums, 0, k - 1)  # Step 3: Reverse the first k elements.
        reverse(nums, k, n - 1)  # Step 4: Reverse the last n-k elements.
```

This code defines a class `Solution` with a method `rotate` that takes a list of integers `nums` and an integer `k`, and rotates the array in place. The `reverse` helper function is used to reverse the elements of the array within a specified range. The steps are followed as outlined, and the code should work correctly to solve the problem as per the given constraints.