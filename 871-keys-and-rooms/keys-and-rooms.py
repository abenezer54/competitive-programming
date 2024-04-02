class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        vis = [0] * n

        stack = [0]
        vis[0] = 1
        while stack:
            top = stack.pop()
            for child in rooms[top]:
                if not vis[child]:
                    stack.append(child)
                    vis[child] = 1
        return vis.count(0) == 0
