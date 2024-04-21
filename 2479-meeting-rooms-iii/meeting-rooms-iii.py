class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        ava = list(range(n))
        used = []
        cnt = [0] * n

        for start, end in meetings:

            while used and start >= used[0][0]:
                time, room = heappop(used)
                heappush(ava, room)
            
            if not ava:
                time, room = heappop(used)
                end = time + (end - start)
                heappush(ava, room)
            
            room = heappop(ava)
            cnt[room] += 1
            heappush(used, (end, room))

        return cnt.index(max(cnt))
   