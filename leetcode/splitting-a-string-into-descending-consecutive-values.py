class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(start):
            if start == len(s):
                return len(nums) > 1

            for i in range(start, len(s)):
                cur = int(s[start: i + 1])
                if nums and nums[-1] - cur != 1:
                    continue
                nums.append(cur)
                if backtrack(i + 1):
                    return True
                nums.pop()
        nums = []
        return backtrack(0)
        