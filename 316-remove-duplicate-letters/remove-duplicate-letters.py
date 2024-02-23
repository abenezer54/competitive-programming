class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n, stack = len(s), []
        count, checked = Counter(s), set()
        for i in range(n):
            while stack and stack[-1] > s[i] and count[stack[-1]] and s[i] not in checked:
                checked.discard(stack.pop())

            if s[i] not in checked:
                stack.append(s[i])
                checked.add(s[i])

            count[s[i]] -= 1

        return "".join(stack)
        