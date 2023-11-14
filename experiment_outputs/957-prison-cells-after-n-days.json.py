```python
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def nextDay(cells):
            new_cells = [0] * 8  # Step 1
            for i in range(1, 7):
                new_cells[i] = int(cells[i - 1] == cells[i + 1])
            return new_cells
        
        seen_states = {}  # Step 2
        has_cycle = False
        cycle_length = 0
        
        for day in range(N):  # Step 3
            next_cells = nextDay(cells)
            next_cells_str = str(next_cells)
            if next_cells_str in seen_states:
                has_cycle = True
                cycle_length = day - seen_states[next_cells_str]
                break
            else:
                seen_states[next_cells_str] = day
                cells = next_cells
        
        if has_cycle:  # Step 4
            remaining_days = (N - seen_states[next_cells_str]) % cycle_length
            for _ in range(remaining_days):
                cells = nextDay(cells)
        
        return cells  # Step 5
```