class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low = 0
        high = len(s)
        ans = []
        for char in s:
            if char == "I":
                ans.append(low)
                low += 1
            else:
                ans.append(high)
                high -= 1
        if s[-1] == "I" : ans.append(high)
        else: ans.append(low)

        return ans