```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Step 1
        result = [0] * len(temperatures)
        # Step 2
        stack = []
        # Step 3
        for i, temp in enumerate(temperatures):
            # Step 4
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                result[index] = i - index
            # Step 5
            stack.append(i)
        # Step 6
        return result
```