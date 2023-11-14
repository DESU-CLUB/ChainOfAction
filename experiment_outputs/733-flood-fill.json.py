```python
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # Step 1: Check if the starting pixel's color is the same as newColor to avoid unnecessary processing.
        originalColor = image[sr][sc]
        if originalColor == newColor:
            return image
        
        # Step 3: Define a recursive function to apply the flood fill.
        def flood_fill(x, y):
            # Step 4: In the recursive function, check if the current pixel is within bounds and has the original color.
            if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]) or image[x][y] != originalColor:
                return
            
            # Step 5: Change the current pixel's color to newColor.
            image[x][y] = newColor
            
            # Step 6: Recursively call the function for the four adjacent pixels (up, down, left, right).
            flood_fill(x + 1, y)
            flood_fill(x - 1, y)
            flood_fill(x, y + 1)
            flood_fill(x, y - 1)
        
        # Step 7: Invoke the recursive function with the starting pixel coordinates.
        flood_fill(sr, sc)
        
        # Step 8: Return the modified image.
        return image
```

Please note that the function head provided in the prompt has been modified to match the correct signature as per the problem statement. The `color` parameter has been renamed to `newColor` for clarity, and the `flood_fill` function has been defined within the `floodFill` method to utilize the `originalColor` and `newColor` variables.