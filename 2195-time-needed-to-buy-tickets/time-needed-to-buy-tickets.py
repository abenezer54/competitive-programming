class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        que = deque([i for i in range(n)])
        ans = 0
        while tickets[k]:
            tickets[que[0]] -= 1
            rear = que.popleft()
            if tickets[rear] > 0:
                que.append(rear)
            ans += 1
        return ans
        