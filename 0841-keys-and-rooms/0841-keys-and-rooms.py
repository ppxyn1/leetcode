class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = set()
        queue = deque()    
        queue.append(0)
        seen.add(0)
        print(0)

        while queue:
          room_idx = queue.popleft()
          keys = rooms[room_idx]
          for key in keys:
            if key not in seen:
              queue.append(key)
              seen.add(key)
              print(key)

            
        if len(rooms) == len(seen):
          return True    
        else:
          return False
