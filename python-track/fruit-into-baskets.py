class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        l, ans, n, = 0, 0, len(fruits)

        for r in range(n):
            basket[fruits[r]] += 1
            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if not basket[fruits[l]]:
                    basket.pop(fruits[l])
                l += 1
            ans = max(ans, r - l + 1)
        return ans
        