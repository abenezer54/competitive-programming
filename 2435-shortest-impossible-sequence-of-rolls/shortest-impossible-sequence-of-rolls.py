class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        n = len(rolls)
        count = set()
        group = 0
        for i in range(n):
            count.add(rolls[i])
            if len(count) == k:
                group += 1
                count.clear()
        return group + 1
        