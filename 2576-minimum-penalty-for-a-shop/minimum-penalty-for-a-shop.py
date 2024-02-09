class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        s = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            if customers[i] == "Y":
                s[i] = 1 + s[i + 1]
            else:
                s[i] = s[i + 1]
                
        cur = 0
        minn = float("inf")
        ans = 0
        for i in range(n + 1):      
            penalty = cur + s[i]
            if penalty < minn:
                ans = i
                minn = penalty   
            if i < n and customers[i] == "N":
                cur += 1

        return ans
        