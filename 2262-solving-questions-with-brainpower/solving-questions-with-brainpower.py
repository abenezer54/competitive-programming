class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            j = i + questions[i][1] + 1
            if j > n: j = n
            dp[i] = max(dp[i + 1], questions[i][0] + dp[j])
        return max(dp)        