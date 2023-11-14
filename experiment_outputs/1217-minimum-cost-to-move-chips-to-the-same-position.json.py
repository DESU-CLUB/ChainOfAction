```python
class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        # 1: Count the number of chips at even positions and the number of chips at odd positions.
        even_count = sum(chip % 2 == 0 for chip in chips)
        odd_count = len(chips) - even_count
        
        # 2: Return the smaller of the two counts as the minimum cost.
        return min(even_count, odd_count)
```