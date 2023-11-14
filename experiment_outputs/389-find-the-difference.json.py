```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Step 1: Initialize a data structure to store the frequency of each character in strings s and t.
        count_s = {}
        count_t = {}

        # Step 2: Count the frequency of each character in string s.
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1

        # Step 3: Count the frequency of each character in string t.
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        # Step 4: Compare the frequency of characters in s and t to find the character with one extra count in t.
        for char in count_t:
            if count_t[char] != count_s.get(char, 0):
                # Step 5: Return the character that was added to t.
                return char
```