class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        N = len(answerKey)
        Tcount = 0
        Fcount = 0
        l = 0
        res = 0
        for r, ans in enumerate(answerKey):
            if ans == "T":
                Tcount += 1
            else:
                Fcount += 1
            while min(Tcount, Fcount) > k:
                if answerKey[l] == "T":
                    Tcount -= 1
                else:
                    Fcount -= 1
                l += 1
            res = max(res, r - l + 1)

        return res