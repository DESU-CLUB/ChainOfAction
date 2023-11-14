```python
class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str = str(num)  # Step 1
        num_str = num_str.replace('6', '9', 1)  # Steps 2, 3, and 4
        return int(num_str)  # Steps 5 and 6
```