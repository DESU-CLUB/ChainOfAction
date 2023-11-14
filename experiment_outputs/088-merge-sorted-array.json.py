```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Step 1: Start from the end of both arrays and the end of the merged array.
        last = m + n - 1
        i, j = m - 1, n - 1
        
        # Step 2: Compare elements from nums1 and nums2 and place the larger one in the correct position of the merged array.
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1
            last -= 1
        
        # Step 3: Continue the process until all elements from nums2 are placed into nums1.
        # Step 4: If there are remaining elements in nums2, move them to the merged array.
        while j >= 0:
            nums1[last] = nums2[j]
            j -= 1
            last -= 1
        
        # No need for Step 5 as the function modifies nums1 in place.
```