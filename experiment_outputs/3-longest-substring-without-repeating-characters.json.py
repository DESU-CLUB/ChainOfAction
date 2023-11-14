Based on the steps provided, here is the Python code for the `lengthOfLongestSubstring` function:

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Step 1: Initialize two pointers and a variable for the maximum length.
        start = 0
        max_length = 0
        
        # Step 2: Create a hash map to store the last index of each character.
        last_seen = {}
        
        # Step 3: Iterate over the string with one pointer.
        for end in range(len(s)):
            # Step 4: Update the second pointer based on the last seen index of the current character.
            if s[end] in last_seen and last_seen[s[end]] >= start:
                start = last_seen[s[end]] + 1
            
            # Step 5: Update the hash map with the current character's index.
            last_seen[s[end]] = end
            
            # Step 6: Calculate the length of the current substring and update the maximum length if it's larger.
            max_length = max(max_length, end - start + 1)
        
        # Step 7: Return the maximum length after completing the iteration.
        return max_length
```

You can use this code to solve the problem on LeetCode by copying it into their code editor and running it against their test cases.