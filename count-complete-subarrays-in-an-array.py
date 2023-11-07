class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        left = 0
        ans = 0
        N = len(set(nums))
        current_distinct_numbers = defaultdict(int)
        for right, num in enumerate(nums):
            current_distinct_numbers[num] += 1
            while len(current_distinct_numbers) == N:
                ans += len(nums) - right
                current_distinct_numbers[nums[left]] -= 1
                if current_distinct_numbers[nums[left]] == 0:
                    del current_distinct_numbers[nums[left]]
                left += 1

        return ans