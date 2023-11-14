```python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Step 1: Calculate the length of the string
        n = len(s)
        
        # Step 2: Loop from 1 to half of the string's length to find potential substrings
        for i in range(1, n // 2 + 1):
            # Step 3: For each length, extract the substring from the start of the string
            substring = s[:i]
            
            # Step 4: Concatenate this substring until it matches the length of the original string
            repeated = substring * (n // i)
            
            # Step 5: Check if the concatenated string equals the original string
            if repeated == s:
                # Step 6: If a match is found, return True
                return True
        
        # Step 7: If no match is found by the end of the loop, return False
        return False
```