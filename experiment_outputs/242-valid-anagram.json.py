```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: Check if the lengths of both strings s and t are equal.
        if len(s) != len(t):
            return False
        
        # Step 2: Create a frequency map for each character in string s.
        frequency_map = {}
        for char in s:
            frequency_map[char] = frequency_map.get(char, 0) + 1
        
        # Step 3: Decrease the frequency of each character in the map for each character in string t.
        for char in t:
            if char in frequency_map:
                frequency_map[char] -= 1
            else:
                # If the character is not found in the map, it's not an anagram.
                return False
        
        # Step 4: Check if all frequencies in the map are zero.
        for frequency in frequency_map.values():
            if frequency != 0:
                return False
        
        # Step 5: Return true if all frequencies are zero, otherwise return false.
        return True
```