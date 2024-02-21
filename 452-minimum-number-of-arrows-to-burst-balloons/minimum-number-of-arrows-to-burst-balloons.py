class Solution:
    def findMinArrowShots(self, a: List[List[int]]) -> int:
        n = len(a)
        a.sort(key=lambda x:x[0])
        ans = 1
        minn = a[0][1]
        # print(a)
        for i in range(1, n):
            # print(minn)
            if a[i][0] <= a[i - 1][1] and minn >= a[i][0]:
                minn = min(minn, a[i - 1][1])
                continue
            else:
                ans += 1
                minn = a[i][1]
            
        return ans

        