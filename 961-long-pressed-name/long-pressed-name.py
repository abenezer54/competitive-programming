class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n, m = len(name), len(typed)
        p = 0
        f = False
        prev = None
        for i in range(m):
            if p == n:
                p = n - 1
            if f:              
                if typed[i] == name[p]:
                    
                    f = True
                    prev = name[p]
                    p += 1
                else:
                    if typed[i] != prev:
                        return False
            else:
                if typed[i] == name[p]:
                    f = True
                    prev = name[p]
                    p += 1
                else:
                    return False
        if p < n:
            return False

        return True
        