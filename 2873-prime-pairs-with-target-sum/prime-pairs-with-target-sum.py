class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        def prime_sieve(n):
            is_prime = [True for _ in range(n + 1)]
            is_prime[0] = is_prime[1] = False
            i = 2
            while i * i <= n:
                if is_prime[i]:
                    j = i * i
                    while j <= n:
                        is_prime[j] = False
                        j += i
                i += 1
            return is_prime
        d = prime_sieve(n)
        a = []
        for i in range(len(d)):
            if d[i]:
                a.append(i)

        ans = []
        i, j = 0, len(a) - 1
        while i <= j:
            sm = a[i] + a[j]
            if sm > n:
                j -= 1
            elif sm < n:
                i += 1
            else:
                ans.append([a[i], a[j]])
                i += 1
                j -= 1
        return sorted(ans)