```python
class Solution:
    def numberOfSteps(self, num: int) -> int:
        # Step 1: Initialize a step counter to zero.
        steps = 0
        
        # Step 2: Loop until num is zero.
        while num > 0:
            # Step 3: If num is even, divide it by 2, else subtract 1.
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            
            # Step 4: Increment the step counter.
            steps += 1
        
        # Step 5: Return the step counter.
        return steps
```