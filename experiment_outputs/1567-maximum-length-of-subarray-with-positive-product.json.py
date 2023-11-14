As per your request, I will only provide the Python code to solve the problem using the function head you've provided and following the identified steps:

```python
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        max_len = 0
        pos_len = 0
        neg_len = 0
        
        for num in nums:
            if num > 0:
                pos_len += 1
                neg_len = neg_len + 1 if neg_len > 0 else 0
            elif num < 0:
                pos_len, neg_len = neg_len + 1 if neg_len > 0 else 0, pos_len + 1
            else:
                pos_len, neg_len = 0, 0
            
            max_len = max(max_len, pos_len)
        
        return max_len
```

This code snippet is designed to solve the problem as described, using the steps provided.