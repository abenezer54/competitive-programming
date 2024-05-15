class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0]
        mp = {0:1, 1:7, 2:30}
        for i in range(len(days)):
            minn = float('inf')
            for j in range(3):
                idx = bisect_right(days, days[i] - mp[j])
                minn = min(minn, dp[idx] + costs[j])
            dp.append(minn)
        return dp[-1]            
        