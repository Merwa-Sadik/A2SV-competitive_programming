# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        room=rooms[0]
        visit=[0]
        while room:
            key=room.pop()
            if key not in visit:
                visit.append(key)
                room+=rooms[key]
        return len(visit)==len(rooms)        
                      


        

        