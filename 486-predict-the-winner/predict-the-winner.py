class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        l, r = 0, len(nums) - 1
        def find(player, l, r):
            if l == r:
                if player == 0:
                    return [nums[l], 0]
                return [0, nums[l]]
            if player == 0:
                left = find(1 - player, l + 1, r)
                right = find(1 - player, l, r - 1)

                if left[0] + nums[l] > right[0] + nums[r]:
                    left[0] += nums[l]
                    return left
                else:
                    right[0] += nums[r]
                    return right
            else:
                left = find(1 - player, l + 1, r)
                right = find(1 - player, l, r - 1)

                if left[1] + nums[l] > right[1] + nums[r]:
                    left[1] += nums[l]
                    return left
                else:
                    right[1] += nums[r]
                    return right
        score = find(0, l, r)
        if score[0] >= score[1]:
            return True
        return False