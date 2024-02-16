class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        ans = 0
        for key, value in count.items():
            if key:
                ans += ((value // (key + 1)) * (key + 1))
                if value % (key + 1) :
                    ans += key + 1
            else:
                ans += value
        return ans
        