class Solution:
    def bestClosingTime(self, customers: str) -> int:
        N = len(customers)
        openPrefix = [0] * (N + 1)
        closePrefix = [0] * (N + 1)
        
        for i, char in enumerate(customers):
            if char == "Y":
                closePrefix[i + 1] = 1
            else:
                openPrefix[i + 1] = 1
    
        for i in range(1, N + 1):
            openPrefix[i] = openPrefix[i - 1] + openPrefix[i]
            closePrefix[i] = closePrefix[i - 1] + closePrefix[i]

        minPenalty = float("inf")
        ans = float("inf")
        for i in range(N + 1):
            penalty = (closePrefix[-1] - closePrefix[i]) + openPrefix[i]
            print(penalty)
            if penalty < minPenalty:
                minPenalty = penalty
                ans = i
        return ans
        
        