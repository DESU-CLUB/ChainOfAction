```python
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # 1: Initialize a set to keep track of visited rooms.
        visited = set()

        # 2: Implement a Depth-First Search (DFS) function to traverse rooms.
        def dfs(room):
            # Mark the current room as visited
            visited.add(room)
            # 4: For each visited room, iterate over its keys
            for key in rooms[room]:
                # Visit the corresponding rooms if not already visited
                if key not in visited:
                    dfs(key)

        # 3: Start the traversal from room 0, marking it as visited.
        dfs(0)

        # 5: After traversal, check if the number of visited rooms is equal to the total number of rooms.
        # 6: Return true if all rooms are visited, otherwise return false.
        return len(visited) == len(rooms)
```