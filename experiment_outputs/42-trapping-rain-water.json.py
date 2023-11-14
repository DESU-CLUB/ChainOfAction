```python
class Solution:
    def trap(self, height):
        # 1: Initialize variables to store the total amount of trapped water, and the current left and right maximum heights.
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        total_water = 0

        # 3: Iterate through the height array using a while loop until the left pointer is less than the right pointer.
        while left < right:
            # 4: If the height at the left pointer is less than the height at the right pointer:
            if height[left] < height[right]:
                # 4a: Check if the current height is greater than the current left maximum height.
                if height[left] >= left_max:
                    # 4b: Update the left maximum height if necessary.
                    left_max = height[left]
                else:
                    # 4c: Add the difference between the left maximum height and the current height to the total trapped water.
                    total_water += left_max - height[left]
                # 4d: Move the left pointer to the right.
                left += 1
            # 5: Else:
            else:
                # 5a: Check if the current height is greater than the current right maximum height.
                if height[right] >= right_max:
                    # 5b: Update the right maximum height if necessary.
                    right_max = height[right]
                else:
                    # 5c: Add the difference between the right maximum height and the current height to the total trapped water.
                    total_water += right_max - height[right]
                # 5d: Move the right pointer to the left.
                right -= 1

        # 6: Return the total amount of trapped water.
        return total_water
```