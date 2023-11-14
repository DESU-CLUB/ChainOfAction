```python
class Solution:
    def countSegments(self, s: str) -> int:
        # 1: Initialize a counter for segments.
        segment_count = 0
        
        # 2: Iterate over the string character by character.
        for i in range(len(s)):
            # 3: Check for the beginning of a segment (non-space following a space or start of the string).
            if (i == 0 or s[i-1] == ' ') and s[i] != ' ':
                # 4: Increment the counter each time a new segment is detected.
                segment_count += 1
        
        # 5: Return the segment counter as the final result.
        return segment_count
```