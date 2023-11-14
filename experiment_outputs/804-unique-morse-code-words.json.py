```python
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # 1: Create a mapping of English alphabet letters to Morse code.
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
                      "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
                      "..-","...-",".--","-..-","-.--","--.."]
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        morse_map = {alphabet[i]: morse_code[i] for i in range(26)}
        
        # 2: Define a function to convert a word to its Morse code representation.
        def word_to_morse(word):
            return ''.join(morse_map[char] for char in word)
        
        # 3: Initialize a set to store unique Morse code transformations.
        transformations = set()
        
        # 4: Iterate over the list of words, transforming each to Morse code and adding to the set.
        for word in words:
            transformations.add(word_to_morse(word))
        
        # 5: Return the size of the set containing unique Morse code transformations.
        return len(transformations)
```