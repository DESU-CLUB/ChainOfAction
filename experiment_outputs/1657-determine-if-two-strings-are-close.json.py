```python
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Step 1: Check if word1 and word2 have the same length. If not, return false.
        if len(word1) != len(word2):
            return False
        
        # Step 2: Count the frequency of each character in both word1 and word2.
        from collections import Counter
        word1_count = Counter(word1)
        word2_count = Counter(word2)
        
        # Step 3: Compare the sets of unique characters in word1 and word2. If they differ, return false.
        if set(word1_count.keys()) != set(word2_count.keys()):
            return False
        
        # Step 4: Compare the sorted lists of character frequencies in word1 and word2. If they differ, return false.
        if sorted(word1_count.values()) != sorted(word2_count.values()):
            return False
        
        # Step 5: Return true if all checks pass.
        return True
```