class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        look = {arr[i]:i for i in range(len(arr))}
        peak = max(arr)
        idx = look[peak]
        if idx == 0 or idx == len(arr) - 1:
            return False
        for i in range(len(arr)):
            if i < idx:
                if arr[i] >= arr[i + 1]:
                    return False
            if i > idx:
                if arr[i] >= arr[i - 1]:
                    return False

        return True
        