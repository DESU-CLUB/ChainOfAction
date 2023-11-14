```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Normalize the string
        normalized_str = ''.join(char.lower() for char in s if char.isalnum())
        
        # Step 2: Initialize two pointers
        left, right = 0, len(normalized_str) - 1
        
        # Step 3: Move pointers towards the center
        while left < right:
            if normalized_str[left] != normalized_str[right]:
                # Step 4: If characters do not match, return false
                return False
            left += 1
            right -= 1
        
        # If all characters match, return true
        return True
```