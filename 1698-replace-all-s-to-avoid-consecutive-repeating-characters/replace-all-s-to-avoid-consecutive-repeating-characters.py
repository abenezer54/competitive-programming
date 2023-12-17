class Solution:
    def modifyString(self, s: str) -> str:
        if len(s) ==  1:
            if s == "?":
                return "s"
            else:
                return s
        s = list(s)
        for i in range(len(s)):
            if i == 0:   
                if s[i] == "?":        
                    if s[i + 1] == "z":
                        print("u")
                        s[i] = "a"
                    else:
                        s[i] = "z"
            elif i == len(s) - 1:
                if s[i] == "?":
                    if s[i - 1] == "z":
                        s[i] = "a"
                    else:
                        s[i] = "z"
            else:
                if s[i] == "?":
                    for ch in ["a", "b", "c"]:
                        if ch != s[i - 1] and ch != s[i + 1]:
                            s[i] = ch
                            
        return "".join(s)