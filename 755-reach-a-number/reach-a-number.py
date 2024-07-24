class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        k = sm = 1
        while sm < target or (sm - target) % 2 != 0:
            k += 1
            sm += k
        return k
        