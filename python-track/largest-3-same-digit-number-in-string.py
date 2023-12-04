class Solution:
    def largestGoodInteger(self, num: str) -> str:
        left, count, ans, found = 0, defaultdict(int), "000", False
        for right, n in enumerate(num):
            count[n] += 1
            if right > 2:
                count[num[left]] -= 1
                if count[num[left]] == 0:
                    del count[num[left]]
                left += 1
            if right >= 2 and len(count) == 1:
                ans = max(num[left:right+1], ans)
                found = True

        if not found:
            return ""
        return ans
        