class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        N = len(arr)
        prefix = [0] * (N + 1)
        for i, num in enumerate(arr):
            prefix[i + 1] = prefix[i] + num

        ans = 0
        for i in range(1, len(prefix)):        
            cur = i - 1
            while cur >= 0:
                ans += prefix[i] - prefix[cur]
                cur -= 2

        return ans