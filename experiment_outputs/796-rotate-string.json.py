```python
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # 1: Check if the lengths of A and B are equal, return false if they are not.
        if len(s) != len(goal):
            return False
        
        # 2: Concatenate A with itself to create a new string AA.
        double_s = s + s
        
        # 3: Check if B is a substring of AA.
        # 4: Return true if B is a substring of AA, otherwise return false.
        return goal in double_s
```