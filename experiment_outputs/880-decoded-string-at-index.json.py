```python
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        # 1: Initialize variables to keep track of the size of the decoded string.
        size = 0
        
        # 2: Iterate through the encoded string to calculate the size of the decoded string.
        for char in s:
            if char.isdigit():
                size *= int(char)
            else:
                size += 1
        
        # 3: Iterate through the encoded string from the end to the beginning.
        for char in reversed(s):
            # 4: Update K for every character we encounter.
            k %= size
            # 5: If it is a letter and K is 0 or the current size equals K, return the letter.
            if k == 0 and char.isalpha():
                return char
            
            # 6: If it is a digit, update the size of the decoded string by dividing it by the digit.
            if char.isdigit():
                size //= int(char)
            # 7: If it is a letter, decrement the size.
            else:
                size -= 1
```