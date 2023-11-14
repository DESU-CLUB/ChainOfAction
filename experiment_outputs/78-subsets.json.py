```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def explore(chosen, remaining, res):
            if not remaining:
                res.append(chosen[:])
                return
            d = remaining.pop(0)
            # choose
            chosen.append(d)
            # explore
            explore(chosen, remaining, res)
            chosen.pop()
            # unchoose
            explore(chosen, remaining, res)
            remaining.insert(0, d)
        
        res = []
        chosen = []
        explore(chosen, nums, res)
        return res
```