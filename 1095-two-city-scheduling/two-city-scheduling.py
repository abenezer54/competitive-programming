class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        costs.sort(key= lambda val : val[1] - val[0])
        ans = 0
        for i in range(n):
            if i < n // 2:
                ans += costs[i][1]
            else:
                ans += costs[i][0]
        return ans
        