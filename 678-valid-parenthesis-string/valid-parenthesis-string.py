class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        stack = []
        adv = []

        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    if adv:
                        adv.pop()
                    else:
                        return False
            else:
                adv.append(i)
                
        while stack:
            top = stack.pop()
            if adv:
                if top > adv[-1]: return False
                adv.pop()
            else:
                return False
        return True