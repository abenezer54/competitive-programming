class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        #reverse the whole array
        start = 0
        end = len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        #reverse k length elements of the array
        l = 0
        r = k - 1
        while  l < r:
            print(l, r)
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        #reverse the rest elements of the array
        i = k
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1