class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append("$$")
        cur = chars[0]
        count = 0
        ans = []
        for char in chars:
            if char != cur:
                if count > 1:
                    ans.extend([cur, *list(str(count))])
                else:
                    ans.append(cur)
                count = 1
                cur = char
            else:
                count += 1
        for i in range(len(ans)):
            chars[i] = ans[i]
        chars.pop()
        return len(ans)
        