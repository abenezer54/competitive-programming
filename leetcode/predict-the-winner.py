class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def dfs(player, l, r):
            if l == r:
                return nums[l]       
            left_score = dfs(player + 1, l + 1, r)
            right_score = dfs(player + 1, l, r - 1)

            if not player & 1:
                return max(left_score + nums[l], right_score + nums[r])
            return min(left_score - nums[l], right_score - nums[r])
            
        return dfs(0, 0, len(nums) - 1) >= 0
      