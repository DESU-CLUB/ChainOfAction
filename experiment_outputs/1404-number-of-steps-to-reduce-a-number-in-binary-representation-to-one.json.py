Here's the Python code based on the steps provided:

```python
class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        while s != "1":
            if s[-1] == "0":
                s = s[:-1]  # Binary division by 2
            else:
                s = self.addBinary(s, "1")  # Binary addition of 1
            steps += 1
        return steps

    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            carry = total // 2
            result = str(total % 2) + result

        return result
```

This code defines a `Solution` class with the `numSteps` method, which takes a binary string `s` and returns the number of steps to reduce it to 1. It also includes a helper method `addBinary` to perform binary addition.