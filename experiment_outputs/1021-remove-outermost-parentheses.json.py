```python
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        counter = 0
        result = ""
        
        for char in S:
            if char == '(':
                if counter > 0:
                    result += char
                counter += 1
            elif char == ')':
                counter -= 1
                if counter > 0:
                    result += char
        
        return result
```