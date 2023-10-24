class Solution:
    def minSwaps(self, s: str) -> int:
        stackO = []
        stackC = []
        ans = 0
        for char in s:
            if char == "[":
                stackO.append(char)
            elif char == "]" and not stackO:
                stackC.append(char)
                ans += 1
            else:
                stackO.pop()
        return (ans + 1) // 2