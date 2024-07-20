class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[] for _ in range(n + 1)]
        dp[-1].append([])
        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
            
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n + 1):
                cur = s[i:j]
                if isPalindrome(i, j - 1):
                    for val in dp[j]:
                        dp[i].append([cur] + val)
        return dp[0]
