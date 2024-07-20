class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        tot, n = sum(nums), len(nums)
        if tot % k != 0: return False
        target = tot // k

        dp = [-1] * (1 << n) # -1 implying currently not available to make such subset 
        dp[0] = 0 # base case (empty subset has sum = 0)
        for subset in range(1 << n):
            for bit in range(n):
                # check if current bit of subset is set then if the previous sum without using 
                # the current nums[bit] value + nums[bit] less than target.
                if subset & (1 << bit):
                    prev = dp[subset ^ (1 << bit)]# retrieve previous sum without current value
                    if prev != -1 and prev + nums[bit] <= target:
                        dp[subset] = (prev + nums[bit]) % target

        return dp[-1] == 0