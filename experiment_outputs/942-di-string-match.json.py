```python
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        # 1: Initialize an empty array A of size N+1 to store the permutation.
        A = []
        
        # 2: Set two pointers, low starting at 0 and high starting at N.
        low, high = 0, len(s)
        
        # 3: Iterate through the string S character by character.
        for char in s:
            # 4: For each 'I' in S, append the value of low to A and increment low.
            if char == 'I':
                A.append(low)
                low += 1
            # 5: For each 'D' in S, append the value of high to A and decrement high.
            elif char == 'D':
                A.append(high)
                high -= 1
        
        # 6: Append the remaining value of low (or high, since they are equal now) to A.
        A.append(low)  # or A.append(high)
        
        # 7: Return the array A as the result.
        return A
```