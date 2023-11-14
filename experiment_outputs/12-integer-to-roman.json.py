```python
class Solution:
    def intToRoman(self, num: int) -> str:
        # 1: Create a list of tuples for Roman numerals and their corresponding integer values, sorted in descending order.
        roman_numerals = [
            ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
            ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
            ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
        ]
        
        # 2: Initialize an empty string for the Roman numeral result.
        result = ""
        
        # 3: Iterate over the list of Roman numeral tuples.
        for roman, value in roman_numerals:
            # 4: While the integer is greater than or equal to the Roman numeral value, append the Roman numeral to the result string and subtract its value from the integer.
            while num >= value:
                result += roman
                num -= value
        
        # 5: Return the result string as the final Roman numeral representation.
        return result
```