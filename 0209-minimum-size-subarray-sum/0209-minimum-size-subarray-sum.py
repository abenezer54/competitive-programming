class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        pre_sum = [0]
        for i in range(len(nums)):
            pre_sum.append(nums[i] + pre_sum[-1])
        # pre_sum.remove(0)
        # print(pre_sum)
        if pre_sum[-1] < target:
            return 0
        # if max(nums)>=target:
        #     return 1
        ans = len(nums)
        l = 0
        r = 1

        while r<len(pre_sum):
            temp=pre_sum[r]-pre_sum[l]
            if temp<target:
                r+=1
            else:
                ans=min(ans,r-l)
                l+=1
        return ans
        