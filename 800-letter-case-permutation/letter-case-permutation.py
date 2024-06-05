class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        #map the indexes with its representing bit
        mp = []
        for i, ch in enumerate(s):
            if ch.isalpha():
                mp.append(i)
        #create a copy of a string as list
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
