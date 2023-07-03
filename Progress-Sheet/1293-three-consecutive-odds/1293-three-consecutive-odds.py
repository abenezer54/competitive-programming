class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        p1 = 0
        p2 = 1
        p3 = 2
        if len(arr) < 3:
            return False
        else:
            while p3 < len(arr):
                if arr[p1] % 2 != 0 and arr[p2] % 2 != 0 and arr[p3] % 2 != 0:
                    return True
                else:
                    p1 += 1
                    p2 += 1
                    p3 += 1
            return False
                