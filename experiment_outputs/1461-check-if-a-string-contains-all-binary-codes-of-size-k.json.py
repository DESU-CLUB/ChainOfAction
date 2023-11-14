```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # 1: Initialize a set to store unique substrings of length k.
        seen_substrings = set()

        # 2: Iterate over the binary string s to extract all possible substrings of length k.
        for i in range(len(s) - k + 1):
            # 3: Add each substring to the set.
            seen_substrings.add(s[i:i + k])

        # 4: Check if the size of the set is equal to 2^k (the total number of possible binary codes of length k).
        # 5: Return True if the sizes match, otherwise return False.
        return len(seen_substrings) == 2 ** k
```