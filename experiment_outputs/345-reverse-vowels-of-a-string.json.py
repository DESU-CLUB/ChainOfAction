```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        # Step 1: Define a function that takes a string as input.
        vowels = "aeiouAEIOU"
        s_list = list(s)
        start, end = 0, len(s) - 1

        # Step 3: While the start pointer is less than the end pointer, iterate.
        while start < end:
            # Step 3a: If the character at the start pointer is a vowel and the character at the end pointer is a vowel, swap them.
            if s_list[start] in vowels and s_list[end] in vowels:
                s_list[start], s_list[end] = s_list[end], s_list[start]
                start += 1
                end -= 1
            # Step 3b: Move the start pointer forward if the current character is not a vowel.
            if s_list[start] not in vowels:
                start += 1
            # Step 3c: Move the end pointer backward if the current character is not a vowel.
            if s_list[end] not in vowels:
                end -= 1

        # Step 4: Convert the characters back to a string if necessary.
        # Step 5: Return the modified string as the result.
        return ''.join(s_list)
```