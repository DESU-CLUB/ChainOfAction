As per your request, I will only provide the Python code to solve the problem using the steps previously identified:

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        ways = [0] * (n + 1)
        ways[1] = 1
        ways[2] = 2
        for i in range(3, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]
        return ways[n]
```