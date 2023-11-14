```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Step 1: Check if the integer is negative or ends with 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        # Step 2: Initialize a variable to store the reversed half of the integer
        reversed_half = 0
        
        # Step 3: Loop until the original integer is less than or equal to the reversed integer
        while x > reversed_half:
            # Step 4: Update the reversed integer by appending the last digit of the original integer
            reversed_half = reversed_half * 10 + x % 10
            
            # Step 5: Remove the last digit from the original integer
            x //= 10
        
        # Step 6: Compare the original and reversed integers for equality
        # For odd digit numbers, check if the original is the reversed integer without its last digit
        return x == reversed_half or x == reversed_half // 10
```