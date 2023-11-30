class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for i in range(1, len(strs[0]) + 1):
            print(strs[0][:i])
            if all([strs[0][:i] in word[:i] for word in strs]):
                ans = strs[0][:i]
            else:
                break
        return ans