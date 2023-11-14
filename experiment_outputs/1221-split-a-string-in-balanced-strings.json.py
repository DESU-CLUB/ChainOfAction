```python
class Solution:
    def balancedStringSplit(self, S: str) -> int:
        # Step 1: Initialize a count of balanced strings and a balance counter.
        balanced_count = 0
        balance = 0
        
        # Step 2: Loop through each character in the string.
        for char in S:
            # Step 3: Update the balance counter for each 'L' and 'R' encountered.
            if char == 'L':
                balance -= 1
            else:  # char == 'R'
                balance += 1
            
            # Step 4: Increment the count of balanced strings when the balance counter is zero.
            if balance == 0:
                balanced_count += 1
        
        # Step 5: Return the count of balanced strings.
        return balanced_count
```