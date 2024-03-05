class Solution:
    def decodeString(self, s: str) -> str:       
        def dfs(s,p):
            ans = ""
            i, num = p, 0
            while i < len(s):
                if s[i].isdigit():           
                    num = (num * 10) + (ord(s[i]) - 48)
                elif s[i] == "[":
                    local, pos = dfs(s, i + 1)
                    ans += local * num
                    i = pos
                    num = 0
                elif s[i] == "]":
                    return ans, i
                else:
                    ans += s[i]
                i += 1
            return ans, i
        
        return dfs(s, 0)[0]
	