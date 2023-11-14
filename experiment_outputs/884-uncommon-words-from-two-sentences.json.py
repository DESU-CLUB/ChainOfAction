```python
from typing import List

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        # Step 1: Split both sentences A and B into words.
        words_A = A.split()
        words_B = B.split()
        
        # Step 2: Count the frequency of each word across both sentences.
        frequency = {}
        for word in words_A + words_B:
            frequency[word] = frequency.get(word, 0) + 1
        
        # Step 3: Identify words with a frequency of exactly one.
        uncommon_words = [word for word, count in frequency.items() if count == 1]
        
        # Step 4: Return the list of identified words.
        return uncommon_words
```