class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count = defaultdict(int)
        for right in range(len(nums)):
            if count[nums[right]] > 0:
                return True 
            count[nums[right]] += 1

            if right >= k:
                count[nums[right - k]] -= 1

        return False