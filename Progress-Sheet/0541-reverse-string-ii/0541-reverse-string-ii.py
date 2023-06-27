class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        arr = [char for char in s]
        if len(s) == 1:
            return s
        else:
            for i in range(0, len(arr), 2 * k):
                l = i
                r = min(i + k - 1, len(arr) - 1)  
                while l < r:
                    arr[l], arr[r] = arr[r], arr[l]
                    l += 1
                    r -= 1
            return "".join(arr)
