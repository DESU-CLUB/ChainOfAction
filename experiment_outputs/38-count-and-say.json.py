As per your request, here is the Python code for the problem using the provided function head:

```python
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        prev_term = self.countAndSay(n - 1)
        result = ""
        count = 1
        
        for i in range(1, len(prev_term)):
            if prev_term[i] == prev_term[i - 1]:
                count += 1
            else:
                result += str(count) + prev_term[i - 1]
                count = 1
        
        result += str(count) + prev_term[-1]
        
        return result
```

This code uses recursion to generate the previous term and then constructs the current term based on the previous one. It counts consecutive digits and forms the next term accordingly.