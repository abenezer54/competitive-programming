class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0 
        for word in zip(*strs):
            for i in range(len(word) - 1):
                if word[i] > word[i + 1]:
                    ans += 1
                    break
        return ans