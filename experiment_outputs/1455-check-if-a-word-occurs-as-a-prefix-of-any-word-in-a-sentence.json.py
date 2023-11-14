```python
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()  # Step 1
        for index, word in enumerate(words):  # Step 2
            if word.startswith(searchWord):  # Step 3
                return index + 1  # Step 4
        return -1  # Step 5
```