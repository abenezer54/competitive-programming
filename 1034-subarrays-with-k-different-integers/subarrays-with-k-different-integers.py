class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:          
        def lessOrEqual(a, k):
            l, ans, count, cur, n = 0, 0, 0, defaultdict(int), len(a)
            for r in range(n):
                cur[a[r]] += 1
                count += 1
                while len(cur) > k:
                    cur[a[l]] -= 1
                    if not cur[a[l]]:
                        cur.pop(a[l])
                    count -= 1
                    l += 1
                ans += count
                
            return ans

        return lessOrEqual(nums, k) - lessOrEqual(nums, k - 1)