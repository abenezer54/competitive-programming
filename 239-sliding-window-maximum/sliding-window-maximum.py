class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que, n, l = deque(), len(nums), 0
        ans = []
        
        for r in range(n):
            while que and que[-1] < nums[r]:
                que.pop()
            que.append(nums[r])

            if r >= k - 1 :
                ans.append(que[0])
                if que and nums[l] == que[0]:
                    que.popleft()
                l += 1

        return ans
        