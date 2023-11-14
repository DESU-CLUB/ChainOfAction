```python
class Solution:
    def maxPower(self, s: str) -> int:
        max_power = 1
        current_power = 1
        previous_char = s[0]

        for i in range(1, len(s)):
            if s[i] == previous_char:
                current_power += 1
                max_power = max(max_power, current_power)
            else:
                previous_char = s[i]
                current_power = 1

        return max_power
```