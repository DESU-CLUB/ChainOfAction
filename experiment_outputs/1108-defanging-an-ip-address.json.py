```python
class Solution:
    def defangIPaddr(self, address: str) -> str:
        # Replace all occurrences of the period "." with "[.]"
        defanged_address = address.replace('.', '[.]')
        # Return the modified IP address
        return defanged_address
```