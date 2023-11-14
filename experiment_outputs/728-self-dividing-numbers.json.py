```python
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        # 1: Initialize an empty list to store self-dividing numbers.
        result = []
        
        # 2: Iterate over the range from the lower bound to the upper bound inclusive.
        for number in range(left, right + 1):
            # 3a: Convert the number to a string to check each digit.
            number_str = str(number)
            # 3b: Ensure the number does not contain the digit zero.
            if '0' in number_str:
                continue
            # 3c: Check if the number is divisible by each of its digits.
            is_self_dividing = True
            for digit in number_str:
                if number % int(digit) != 0:
                    is_self_dividing = False
                    break
            # 4: If a number is self-dividing, add it to the list.
            if is_self_dividing:
                result.append(number)
        
        # 5: Return the list of self-dividing numbers.
        return result
```