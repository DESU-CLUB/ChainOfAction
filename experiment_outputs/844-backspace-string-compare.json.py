As per your request, here is the Python code for the problem using the function head provided:

```python
class Solution:
    def backspaceCompare(self, S, T):
        def build(string):
            result = []
            skip = 0
            for char in reversed(string):
                if char == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    result.append(char)
            return ''.join(result)
        
        return build(S) == build(T)
```

This code defines a helper function `build` which processes a string by simulating the backspace operation. It then compares the processed versions of `S` and `T` to determine if they are equal.