class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        advantage = 0
        t = target
        while maxDoubles and t > 2:
            t //= 2
            advantage += t - 1
            maxDoubles -= 1
        return target - advantage - 1
        