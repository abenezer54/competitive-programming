class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        lookup = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                     '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
                     
        ans, cur = [], []
        def backtrack(index):
            if len(cur) == len(digits):
                ans.append(''.join(cur))
            if index == len(digits):
                return

            for char in lookup[digits[index]]:
                cur.append(char)
                backtrack(index + 1)
                cur.pop()
        backtrack(0)
        return ans
        