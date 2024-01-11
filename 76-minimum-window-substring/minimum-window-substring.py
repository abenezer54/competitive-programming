class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check(new_dic, t_count):
            for key, val in t_count.items():
                if new_dic[key] < val:
                    return False
            return True

        l, n, flag, possible, minimum_length = 0, len(s), False, [0, 0], float("inf")
        t_count = Counter(t)
        s_count = defaultdict(int)
    
        for r in range(n):
            s_count[s[r]] += 1
            while check(s_count, t_count):
                flag = True
                if r - l + 1 < minimum_length:
                    possible = [l, r]
                    minimum_length = r - l + 1

                s_count[s[l]] -= 1
                if s_count[s[l]] == 0:
                    s_count.pop(s[l])
                l += 1

        if not flag:
            return ''
        return s[possible[0] : possible[1] + 1]
        