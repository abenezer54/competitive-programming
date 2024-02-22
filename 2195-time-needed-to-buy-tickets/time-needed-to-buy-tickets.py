class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n, ans = len(tickets), 0
        que = deque([i for i in range(n)])
        
        while True:
            cur = que.popleft()
            ans += 1
            tickets[cur] -= 1
            if tickets[cur]:
                que.append(cur)
            elif cur == k:
                return ans           
 
        