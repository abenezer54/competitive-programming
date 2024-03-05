class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, cur = [], []
        def backtrack(opening, closing):
            if opening == 0 and closing == 0:
                ans.append(''.join(cur))
                return 

            if opening and closing:
                for i in range(2):
                    if i & 1:
                        cur.append(')')
                        backtrack(opening, closing - 1)
                        cur.pop()
                    else:
                        cur.append('(')
                        backtrack(opening - 1, closing + 1)
                        cur.pop()
            elif opening:
                cur.append('(')
                backtrack(opening - 1, closing + 1)
                cur.pop()
            else:
                cur.append(')')
                backtrack(opening, closing - 1)
                cur.pop()
        backtrack(n, 0)
        return ans 
        