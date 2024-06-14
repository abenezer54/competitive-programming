class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        l, r = 0, 1
        while l + 1e-9 < r:
            mid = (l + r) / 2
            cnt, j, mx = 0, 1, 0
            nm = dm = 0 
            for i in range(n):
                while j < n and arr[i] > arr[j] * mid:
                    j += 1
                cnt += n - j
                
                if j == n:
                    break

                if j < n and mx < arr[i] / arr[j]:
                    mx = arr[i] / arr[j]
                    nm, dm = i, j
                
            if cnt  == k:
                return [arr[nm], arr[dm]]
            elif cnt > k:
                r = mid
            else:
                l = mid
        return []