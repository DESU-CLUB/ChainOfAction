As per your request, I will provide the Python code based on the steps identified:

```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 1, num
        
        while low <= high:
            mid = (low + high) // 2
            square = mid * mid
            
            if square == num:
                return True
            elif square < num:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
```

This code defines a class `Solution` with a method `isPerfectSquare` that implements a binary search to determine if a given number is a perfect square without using the built-in `sqrt` function.