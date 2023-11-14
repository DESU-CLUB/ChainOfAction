```python
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # 1: Initialize variables to track the maximum distance and the index of the last occupied seat.
        max_distance = 0
        last_occupied_seat_index = -1
        
        # 2: Iterate through the seats to find the maximum distance from the start to the first occupied seat.
        for i, seat in enumerate(seats):
            if seat == 1:
                if last_occupied_seat_index == -1:
                    max_distance = i
                else:
                    # 3: Continue iterating to find the maximum distance between two occupied seats.
                    max_distance = max(max_distance, (i - last_occupied_seat_index) // 2)
                last_occupied_seat_index = i
        
        # 4: Find the maximum distance from the last occupied seat to the end of the row.
        if seats[-1] == 0:
            max_distance = max(max_distance, len(seats) - 1 - last_occupied_seat_index)
        
        # 5: Return the maximum distance found from steps 2, 3, and 4.
        return max_distance
```