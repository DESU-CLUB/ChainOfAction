As per your request, here is the Python code following the identified steps:

```python
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Step 2: Calculate the character frequency of string p
        p_count = Counter(p)
        s_count = Counter()
        
        # Step 3: Initialize a list to store the start indices of anagrams
        result = []
        p_length = len(p)
        
        # Step 4: Iterate over string s with a window of length equal to string p
        for i in range(len(s)):
            # Add one more letter on the right side of the window
            s_count[s[i]] += 1
            
            # Remove one letter from the left side of the window
            if i >= p_length:
                if s_count[s[i - p_length]] == 1:
                    del s_count[s[i - p_length]]
                else:
                    s_count[s[i - p_length]] -= 1
            
            # Step 5 and 6: Compare the window with p's frequency and add to result if it's an anagram
            if s_count == p_count:
                result.append(i - p_length + 1)
        
        # Step 7: Return the list of start indices
        return result
```

Please note that `List[int]` should be imported from the `typing` module if you are using Python version earlier than 3.9. In Python 3.9 and later, you can use the built-in `list` with type hints directly. Here's how you would import it for earlier versions:

```python
from typing import List
```

Make sure to include this import at the beginning of your script if necessary.