class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for log in logs:
            if log[0] != ".":
                ans += 1
            elif log[0] == '.' and log[1] == '.':
                ans = max(0, ans - 1)
        return ans
        