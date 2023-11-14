```python
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # 1: Initialize a variable to store the column number.
        column_number = 0
        
        # 2: Iterate over each character in the input string from right to left.
        for i, char in enumerate(reversed(columnTitle)):
            # 3: Convert each character to its corresponding number value.
            number = ord(char) - ord('A') + 1
            
            # 4: Update the column number using the positional value and the character's number value.
            column_number += number * (26 ** i)
        
        # 5: Return the final column number.
        return column_number
```