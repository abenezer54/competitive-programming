class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        N = len(arr)
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)

        ans = 0
        for i in range(N - k + 1):
            if (prefix[i + k] - prefix[i]) / k >= threshold:
                ans += 1
        
        return ans