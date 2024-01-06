class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        nums.sort()
        minn = float("inf")
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                cur_sum = nums[l] + nums[r] + nums[i]
                distance = abs(cur_sum - target)

                if distance < minn:
                    minn = distance
                    ans = cur_sum
                    
                if distance == 0:
                    return target
                elif target > cur_sum:
                    l += 1
                else:
                    r -= 1

        return ans