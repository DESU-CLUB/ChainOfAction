```python
class Solution:
    def removeDuplicates(self, s: str) -> str:
        # 1: Initialize a stack to keep track of characters.
        stack = []
        
        # 2: Iterate over each character in the input string.
        for char in s:
            # 3: For each character, check if the stack is not empty and the top of the stack is equal to the current character.
            if stack and stack[-1] == char:
                # 4: If the top of the stack is equal to the current character, pop the top of the stack.
                stack.pop()
            else:
                # 5: If the top of the stack is not equal to the current character, push the current character onto the stack.
                stack.append(char)
        
        # 6: Convert the stack to a string in the correct order.
        result = ''.join(stack)
        
        # 7: Return the resulting string.
        return result
```