class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        N = len(arr)
        if N == k:
            return arr
        m = (N - 1) // 2
        arr.sort()
        median = arr[m]

        ans = []
        for i in range(N):
            if not i == m:
                ans.append([abs(arr[i] - median), arr[i]])   
        ans.sort(key = lambda x:( x[0], x[1]), reverse = True)

        res = []
        for i in range(k):
            res.append(ans[i][1])

        return res