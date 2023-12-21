class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        max_arr = [0] * len(nums)
        max_arr[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > max_arr[i + 1]:
                max_arr[i] = nums[i]
            else:
                max_arr[i] = max_arr[i + 1]

        minn = nums[0]
        for i in range(1, len(nums) - 1):
            if nums[i] > minn and nums[i] < max_arr[i + 1]:
                return True
            minn = min(minn, nums[i])
        return False
        