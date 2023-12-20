class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        count = defaultdict(list)
        for i in range(len(nums)):
            if len(count[nums[i]]) > 0:
                for j in range(len(count[nums[i]])):
                    if (count[nums[i]][j] * i) % k == 0:
                        ans += 1
            count[nums[i]].append(i)

        return ans
        