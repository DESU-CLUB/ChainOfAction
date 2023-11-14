```python
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        # 1: Create a hash map to store each array in pieces with the first element as the key.
        pieces_dict = {p[0]: p for p in pieces}
        
        # 2: Iterate through the arr array.
        i = 0
        while i < len(arr):
            # 3: For each element in arr, check if it exists as a key in the hash map.
            if arr[i] in pieces_dict:
                # 4: If the key exists, retrieve the corresponding array from the hash map.
                piece = pieces_dict[arr[i]]
                # 5: Compare the retrieved array with the subsequent elements in arr.
                for num in piece:
                    if i < len(arr) and arr[i] == num:
                        i += 1
                    else:
                        # 6: If any check fails, return false.
                        return False
            else:
                # 6: If the key does not exist, return false.
                return False
        
        # 7: If the end of arr is reached successfully, return true.
        return True
```