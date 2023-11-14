```python
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []  # Step 1
        current_number = 1  # Step 2
        for target_number in target:  # Step 3
            while current_number < target_number:  # Step 4
                operations.append("Push")
                operations.append("Pop")
                current_number += 1
            operations.append("Push")  # Step 5
            current_number += 1
        return operations  # Step 6
```