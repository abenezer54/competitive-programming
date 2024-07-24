class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        k = 1
        while (k * (k + 1)) // 2 < target or (((k * (k + 1)) // 2) - target) % 2 != 0:
            k += 1
        return k
        