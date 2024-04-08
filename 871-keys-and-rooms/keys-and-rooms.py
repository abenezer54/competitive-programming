class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        vis = [0] * n
        vis[0] = 1
        que = deque([0])
        while que:
            node = que.popleft()
            for child in rooms[node]:
                if not vis[child]:
                    que.append(child)
                    vis[child] = 1
        return vis.count(0) == 0
