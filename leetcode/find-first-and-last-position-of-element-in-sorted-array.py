class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = -1, len(nums) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid
        first = r

        if nums and nums[first] == target:
            l, r = first, len(nums) 
            while l + 1 < r:
                mid = (l + r) // 2
                if nums[mid] <= target:
                    l = mid
                else:
                    r = mid
            last = l
            return [first, last]
        else:
            return [-1, -1]
