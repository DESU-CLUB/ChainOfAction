```python
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop_index = 0
        
        for push_val in pushed:
            stack.append(push_val)
            while stack and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1
        
        return not stack
```