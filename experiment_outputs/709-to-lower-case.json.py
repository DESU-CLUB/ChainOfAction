```python
class Solution:
    def toLowerCase(self, str: str) -> str:
        # Define a new string to store the result
        result = ""
        # Iterate over each character in the input string
        for char in str:
            # Check if the character is uppercase
            if 'A' <= char <= 'Z':
                # Convert the character to lowercase and append to result
                result += chr(ord(char) + 32)
            else:
                # Append the character as it is
                result += char
        # Return the result string
        return result
```