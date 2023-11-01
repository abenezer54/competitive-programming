class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oddIndex = [-1]
        for i, num in enumerate(nums):
            if num % 2 == 1:
                oddIndex.append(i)
        oddIndex.append(len(nums))
        # print(oddIndex)
        ans = 0
        for i in range(1, len(oddIndex) - k):
            ans += (oddIndex[i] - oddIndex[i - 1]) * (oddIndex[i + k ] - oddIndex[i + k - 1])
        
        return ans