class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        queue = deque([[-1, 0]])
        ans, cur, n = inf, 0, len(nums)
        for i in range(n):
            cur += nums[i]
            while queue and cur - queue[0][1] >= k:
                ans = min(ans, i - queue.popleft()[0])
            
            while queue and cur <= queue[-1][1]:
                queue.pop()
            queue.append([i, cur])

        if ans == inf:
            return -1
        return ans
        