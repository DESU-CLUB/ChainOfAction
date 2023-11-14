As per your request, here is the Python code that follows the steps outlined:

```python
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Step 1: Validate the input arrays to ensure they are not both empty.
        # This step is not needed as per the problem's assumption.

        # Step 2: If one array is empty, find the median of the non-empty array.
        if not nums1:
            return self.median_of_single_array(nums2)
        if not nums2:
            return self.median_of_single_array(nums1)

        # Step 3: Determine the total length of the combined arrays.
        total_length = len(nums1) + len(nums2)

        # Step 4: Calculate the position of the median in the combined array.
        half_length = total_length // 2

        # Ensure nums1 is the smaller array for binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # Step 5: Use a binary search algorithm to find the median by comparing elements of the two arrays.
        left, right = 0, len(nums1) - 1
        while True:
            i = (left + right) // 2  # Partition nums1
            j = half_length - i - 2  # Partition nums2

            nums1_left_max = nums1[i] if i >= 0 else float('-infinity')
            nums1_right_min = nums1[i + 1] if (i + 1) < len(nums1) else float('infinity')
            nums2_left_max = nums2[j] if j >= 0 else float('-infinity')
            nums2_right_min = nums2[j + 1] if (j + 1) < len(nums2) else float('infinity')

            # Check if we have found the correct partition
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # Step 6: Handle the case for even total length by finding the two middle elements and calculating their average.
                if total_length % 2 == 0:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2
                else:
                    return min(nums1_right_min, nums2_right_min)
            elif nums1_left_max > nums2_right_min:
                right = i - 1
            else:
                left = i + 1

    def median_of_single_array(self, nums: List[int]) -> float:
        mid = len(nums) // 2
        if len(nums) % 2 == 0:
            return (nums[mid - 1] + nums[mid]) / 2
        else:
            return nums[mid]
```

This code defines a class `Solution` with a method `findMedianSortedArrays` that implements the binary search algorithm to find the median of two sorted arrays. It also includes a helper method `median_of_single_array` to handle the case where one of the arrays is empty. The binary search is performed on the smaller array to ensure the logarithmic time complexity.