As per your request, here is the Python code following the steps provided:

```python
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Step 1: Define a custom comparison function for sorting the numbers.
        def compare(x, y):
            return 1 if x+y < y+x else -1
        
        # Step 2: Convert all integers in the list to strings.
        str_nums = [str(num) for num in nums]
        
        # Step 3: Sort the list of strings using the custom comparison function.
        str_nums.sort(key=cmp_to_key(compare))
        
        # Step 4: Concatenate the sorted strings into a single string.
        largest_num = ''.join(str_nums)
        
        # Step 5: Return the concatenated string, or "0" if the first character is '0'.
        return '0' if largest_num[0] == '0' else largest_num
```

This code defines a custom comparison function that is used to sort the numbers in such a way that the largest number is formed when they are concatenated. It then converts the numbers to strings, sorts them, concatenates them, and returns the result. If the result starts with a '0', it means all numbers were '0', so it returns '0' instead.