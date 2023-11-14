As per your request, here is the Python code based on the steps provided:

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):  # Step 1
            return False
        
        s_to_t = {}  # Step 2
        t_to_s = {}  # Step 2
        
        for char_s, char_t in zip(s, t):  # Step 3
            if (char_s in s_to_t and s_to_t[char_s] != char_t) or \
               (char_t in t_to_s and t_to_s[char_t] != char_s):  # Step 4
                return False  # Step 6
            
            s_to_t[char_s] = char_t  # Step 5
            t_to_s[char_t] = char_s  # Step 5
        
        return True  # Step 7
```

This code follows the steps you've outlined to determine if two strings are isomorphic.