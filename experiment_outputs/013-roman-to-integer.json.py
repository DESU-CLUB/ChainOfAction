```python
class Solution:
    def romanToInt(self, s: str) -> int:
        # 1: Create a dictionary mapping Roman numerals to integers.
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        # 2: Initialize a variable to store the total value.
        total = 0
        
        # 3: Loop through the Roman numeral string.
        for i in range(len(s)):
            # 4: Compare the current numeral's value with the next one's.
            if i + 1 < len(s) and roman_values[s[i]] < roman_values[s[i + 1]]:
                # 5: Subtract the current numeral's value based on the comparison.
                total -= roman_values[s[i]]
            else:
                # 5: Add the current numeral's value based on the comparison.
                total += roman_values[s[i]]
        
        # 6: Return the total value.
        return total
```