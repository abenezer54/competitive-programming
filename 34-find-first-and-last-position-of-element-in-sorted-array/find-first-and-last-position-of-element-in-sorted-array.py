class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l, r, low = 0, n - 1, n

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                low = mid
                r = mid - 1
            else:
                l = mid + 1

        if low == n or nums[low] != target:
            return [-1, -1]
        
        high, l, r = n, low + 1, n - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                high = mid
                r = mid - 1
        
        return [low, high - 1]            
        