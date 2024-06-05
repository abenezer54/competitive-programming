class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        mp = []
        for i, ch in enumerate(s):
            if ch.isalpha():
                mp.append(i)
        cpy = list(s)
        ans = []
        for num in range(1 << len(mp)):
            for bit in range(len(mp)):
                idx = mp[bit]
                if num & (1 << bit): 
                    cpy[idx] = cpy[idx].upper()
                else:
                    cpy[idx] = cpy[idx].lower()
            ans.append(''.join(cpy))
        return ans
