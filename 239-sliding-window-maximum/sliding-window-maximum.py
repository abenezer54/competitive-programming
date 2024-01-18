class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        n = len(nums)
        l = 0
        maxx = deque()
        for r in range(n):
            if not maxx:
                maxx.append(nums[r])
            else:
                while maxx and maxx[-1] < nums[r]:
                    maxx.pop()
                maxx.append(nums[r])

            if r + 1 >= k:
                ans.append(maxx[0])
                if maxx and maxx[0] == nums[l]:    
                    maxx.popleft()
                l += 1
                
        return ans          
        