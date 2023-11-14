```python
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersections = []
        i, j = 0, 0

        while i < len(firstList) and j < len(secondList):
            start_max = max(firstList[i][0], secondList[j][0])
            end_min = min(firstList[i][1], secondList[j][1])

            if start_max <= end_min:
                intersections.append([start_max, end_min])

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return intersections
```