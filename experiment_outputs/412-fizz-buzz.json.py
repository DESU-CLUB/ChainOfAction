```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # 1: Initialize an empty list to store the results.
        results = []
        
        # 2: Loop from 1 to n inclusive.
        for i in range(1, n + 1):
            # 3: For each number, check if it is a multiple of both 3 and 5.
            if i % 3 == 0 and i % 5 == 0:
                # 4: If it is, append "FizzBuzz" to the results list.
                results.append("FizzBuzz")
            # 5: If not, check if it is a multiple of 3.
            elif i % 3 == 0:
                # 6: If it is, append "Fizz" to the results list.
                results.append("Fizz")
            # 7: If not, check if it is a multiple of 5.
            elif i % 5 == 0:
                # 8: If it is, append "Buzz" to the results list.
                results.append("Buzz")
            else:
                # 9: If none of the above conditions are met, append the string representation of the number to the results list.
                results.append(str(i))
        
        # 10: Return the results list after the loop ends.
        return results
```