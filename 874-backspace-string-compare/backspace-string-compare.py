class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS = []
        for i, char in enumerate(s):
            if stackS and char == "#":
                stackS.pop()
            elif not stackS and char == "#":
                pass
            else:
                stackS.append(char)
 
        stackT = []
        for i, char in enumerate(t):
            if stackT and char == "#":
                stackT.pop()
            elif not stackT and char == "#":
                pass
            else:
                stackT.append(char)
    
        if "".join(stackS) == "".join(stackT):
            return True

        return False
        