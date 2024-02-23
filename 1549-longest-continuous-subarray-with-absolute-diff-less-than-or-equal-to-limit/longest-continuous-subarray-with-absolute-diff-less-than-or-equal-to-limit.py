class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxx, minn = deque(), deque()
        l, n = 0, len(nums)
        ans = 1
        for r in range(n):
            while maxx and maxx[-1] < nums[r]:
                maxx.pop()
            maxx.append(nums[r])

            while minn and minn[-1] > nums[r]:
                minn.pop()
            minn.append(nums[r])

            while maxx[0] - minn[0] > limit:
                if maxx[0] == nums[l]:
                    maxx.popleft()
                if minn[0] == nums[l]:
                    minn.popleft()
                l += 1
            ans = max(ans, r - l + 1)
        return ans
                