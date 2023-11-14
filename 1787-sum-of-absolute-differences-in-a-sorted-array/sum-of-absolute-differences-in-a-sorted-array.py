class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        N = len(nums) 
        ans = [0] * N
        prefix = [0] * (N + 1)

        for i in range(0, N):
            prefix[i + 1] = prefix[i] + nums[i]
 
        for i, num in enumerate(nums):
            rightSum = prefix[-1] - prefix[i + 1]
            leftSum = prefix[i]

            ans[i] = abs((i * num) - leftSum)  + abs(rightSum - ((N -i -1)*num))

        return ans
        