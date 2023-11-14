```python
class Solution:
    def convertToTitle(self, n: int) -> str:
        # 1: Initialize an empty string for the column title.
        column_title = ""
        
        # 2: Loop until the given integer is greater than zero.
        while n > 0:
            # 3: Calculate the modulo of the integer by 26 to find the remainder.
            remainder = (n - 1) % 26
            
            # 4: Convert the remainder to the corresponding alphabet character.
            character = chr(remainder + ord('A'))
            
            # 5: Prepend the character to the column title string.
            column_title = character + column_title
            
            # 6: Update the integer by subtracting the remainder and dividing by 26.
            n = (n - 1) // 26
        
        # 7: Return the column title string after the loop ends.
        return column_title
```