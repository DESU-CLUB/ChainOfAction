Here is the Python code following the steps you've identified:

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Step 1: Create a hash map to store the frequency of each character in the string.
        frequency = {}

        # Step 2: Iterate over the string to populate the hash map with character frequencies.
        for char in s:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

        # Step 3: Iterate over the string again to find the first character with a frequency of 1.
        for index, char in enumerate(s):
            if frequency[char] == 1:
                # Step 4: Return the index of the first non-repeating character.
                return index

        # If no non-repeating character exists, return -1.
        return -1
```

You can use this code to solve the problem on LeetCode by copying it into their code editor and running it against their test cases.