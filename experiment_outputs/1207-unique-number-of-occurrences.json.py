As per your request, here is the Python code based on the steps provided:

```python
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Step 1: Count the occurrences of each value in the array
        occurrence_count = {}
        for num in arr:
            if num in occurrence_count:
                occurrence_count[num] += 1
            else:
                occurrence_count[num] = 1
        
        # Step 2: Check if all occurrence counts are unique
        unique_counts = set(occurrence_count.values())
        
        # Step 3: Return true if unique, otherwise false
        return len(unique_counts) == len(occurrence_count)
```

This code defines a class `Solution` with a method `uniqueOccurrences` that takes a list of integers `arr` and returns a boolean indicating whether the number of occurrences of each value in the array is unique.