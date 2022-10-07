class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        beg = {}
        dest = {}
        final = 0
        for pas , begin , end in trips:
            beg[begin] = beg.get(begin , 0) + pas
            dest[end] = dest.get(end, 0 ) + pas
            final = max(final , end)
        passengers = 0
        for pos in range(final):
            passengers -= dest.get(pos,0)
            passengers += beg.get(pos,0)
            if passengers > capacity:
                return False
        return True
