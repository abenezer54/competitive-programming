class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        arr = []
        for i in range(0, c + 1):
            arr.append(pow(i, 2))
            if pow(i, 2) >= c:
                break
        l = 0
        r = len(arr) - 1
        while l <= r:
            if arr[l] + arr[r] > c:
                r -= 1
            elif arr[l] + arr[r] < c:
                l += 1
            else:
                return True
        return False