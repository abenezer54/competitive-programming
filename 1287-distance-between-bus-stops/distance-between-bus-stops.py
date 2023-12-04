class Solution:
    def distanceBetweenBusStops(self, ds: List[int], s: int, dest: int) -> int:
        if len(ds) == 1:
            return 0
        prefix = [0]
        for d in ds:
            prefix.append(prefix[-1] + d)
        minn = min(s, dest)
        maxx = max(s, dest)
        sum1 = prefix[maxx] - prefix[minn]
        sum2 = prefix[-1] - sum1
        return min(sum1, sum2)
        