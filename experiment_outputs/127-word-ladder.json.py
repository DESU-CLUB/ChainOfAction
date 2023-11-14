```python
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)  # Step 1
        if endWord not in wordSet:  # Step 2
            return 0
        queue = deque([(beginWord, 1)])  # Step 3
        visited = set()  # Step 4
        while queue:  # Step 5
            word, steps = queue.popleft()  # Step 5a
            if word == endWord:
                return steps
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordSet and next_word not in visited:  # Step 5b
                        queue.append((next_word, steps + 1))  # Step 5biii
                        visited.add(next_word)  # Step 5biii
        return 0  # Step 6
```